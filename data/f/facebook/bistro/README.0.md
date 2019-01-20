= Worker state transitions =

A scheduler talks to multiple workers, each identified by a shard ID -- a
string which logically identifies a worker so as to allow smooth failovers
(and per-worker customization).  The scheduler tracks each worker's state
according to the diagram below.  Each worker also models its own state, with
the same timeouts.  A worker will not run tasks unless it's HEALTHY, and
will commit suicide upon MUST_DIE.

NEW -> UNHEALTHY -> MUST_DIE (lost / suicide requested)
           ^
           |
           v
        HEALTHY

When a worker becomes MUST_DIE on the scheduler, its "running" and "unsure
if running" tasks are forgotten, and a suicide request is sent.  The
identifying information is retained, so that if the worker, due to network
partitions or bugs, comes back, it gets a suicide request ASAP.

A worker is truly forgotten when another connects with the same shard ID.  A
worker can be replaced when it is not HEALTHY, but by default, it can be
replaced only when it is MUST_DIE (see --allow_bump_unhealthy_worker).  As
above, the worker is sent a suicide request, its "running" and "unsure if
running" tasks are forgotten.  But this time, the scheduler retains no
memory of its identity, as it is overwritten by the new worker.

One can construct a pathological situation when a displaced or lost worker
comes back to life, and successfully re-associates with the scheduler.  For
example, there is a network partition, a new worker with the same shard ID
is spawned, then the partition resolves, the old worker reconnects, and we
discover its tasks were running all along.  This cannot be prevented, so the
remediation is that one of the workers ends up getting a suicide request
(see RemoteWorker::processHeartbeat).

Aside from the above pathology, a running worker instance cannot return to
the NEW state, nor can it leave the MUST_DIE state.

= Scheduler startup and initial wait =

On startup, the scheduler does not know the set of available workers, and
does not know what tasks are already running.  It simply waits for workers
to connect, and polls them for running tasks.  Eventually, enough time
passes that it can conclude that any workers that were up, and separated by
a network partition, would have had to commit suicide by now.  At that
point, the list of already-connected workers is known to be complete.

In setups where the "time to lose a worker" is long (e.g. to protect 
fragile, long-running tasks in HPC-like settings), this initial wait
can be inconveniently long. 

See remote/README.worker_set_consensus for a description of Bistro's current
solution to this problem.  The 'worker set consensus' mechanism drastically
shortens this initial wait in the common case by having each workers record
a hash of the most recently seen set of workers.

= Core calls =

The core calls of the scheduler-worker protocol maintain the
scheduler-worker association, worker health information, and running tasks
for both the scheduler and the worker.  They also update the scheduler-only
list of "unsure if running" tasks.

Of these, "running tasks" is the most fragile and important state in the
system, maintained with a lot of care to mitigate the usual distributed-RPC
issues.  The block comments of the core calls have the details, but in a
nutshell, a task is running:
 - From the worker's point of view -- from the receipt of runTask, until
   updateStatus succeeds completely.
 - From the scheduler's point of view -- from before runTask is sent, until
   the worker is lost or until an updateStatus is received (either a normal
   "task ended", or a "was not running" in response to a
   notifyIfTasksNotRunning query).
A scheduler will only runTask with a given invocationID once.

Worker to scheduler (in scheduler.thrift):
 - processHeartbeat: Associate with a scheduler, maintain health. 
 - updateStatus: Comes in two varieties -- (i) "task ended", when the
   task just stopped running, and (ii) "was not running" in reply to
   notifyIfTasksNotRunning.  The worker retries sending the update until it
   succeeds.  For "task ended", the worker only stops considering a task
   "running" once the updateStatus succeeds.

Scheduler to worker (below):
 - getRunningTasks: After a new worker associates with the scheduler, and
   before the scheduler runs any tasks, discover the tasks that the were
   already running on the worker.
 - runTask: The scheduler marks the task as running, then tells the worker
   to start it too.
 - notifyIfTasksNotRunning: If runTask fails in such a way that the
   scheduler is unsure if the worker started it, this call asks the worker
   for an updateStatus for the tasks that are not running.  The scheduler
   retries this call until it succeeds, or until the task are found to be
   not running through updateStatus or worker loss.  Once this call succeds,
   the scheduler treats the tasks as "running" until further notice.

After the initial getRunningTasks, the scheduler & worker only synchronize
their lists of running tasks through the iterative updates of runTask and
updateStatus (helped by rare notifyIfTasksNotRunning calls when the
scheduler might have gotten out of sync).

Therefore, the protocol embodied by the above calls has to be 100% robust,
or the scheduler & worker's states will drift apart.  The docblocks of the
individual calls are a great place to address five of of the six the
standard distributed-RPC issues:
 - failure: Both on the sender and the receiver
 - partial failure: Failed on the sender but succeeded on the receiver
 - delay: Call received much later than expected, including self-ordering
 - replay: Can the call be received twice? What happens if it does?
 - identity: Calls from the wrong process (i.e. authentication)
However, the sixth issue of multi-call ordering is better covered in a
central place because pairwise interactions are hard to pin to a single
call's docblock.

For the 5 calls, pairwise interactions have to be considered both on from
the scheduler's and worker's perspective.  That means we ought to discuss a
total of (5 * 4 / 2) * 2 = 20 interactions.  Some will be implicit.

= processHeartbeat interactions (8/20 so far) =

== Health state ==

When a worker sends its first processHeartbeat to a new scheduler, its
health state is NEW on both sides.  On the scheduler, it leaves the NEW
state immediately after getRunningTasks succeeds.  The worker leaves the NEW
state upon receiving a response its first processHeartbeat that the
scheduler receives *after* getRunningTasks succeeds.

processHeartbeat barely interacts with the other core calls during normal
operation.  Rather, it is is the main call that maintains health state. 
Healthchecks' runTask and updateStatus also have an impact on healh, but
their ordering with respect to processHeartbeat does not matter.  Even
transient delays, failures, and partial failures in health-related calls can
only cause minor health state discrepancies between the worker and the
scheduler.  These last until the next successful heartbeat & healthcheck
exchange.  Such discrepancies are not dangerous, because new tasks can only
start if both the scheduler & worker believe the worker is healthy, while a
worker will become lost if either side marks it MUST_DIE.

== Task-related state ==

Only when workers switch schedulers, or schedulers switch workers, does
processHeartbeat modify state that is relevant to the other calls.

When a worker associates with a new scheduler, the worker resets the
notifyIfTasksNotRunning sequence number.  Since the worker validates the
scheduler ID in the two calls using the sequence number (runTask and
notifyIfTasksNotRunning), this state change is safe.

When a new worker replaces the old, the scheduler:
 - discards old running tasks
 - discards old "unsure if running" tasks
 - resets the notifyIfTasksNotRunning sequence number
This is safe, since the scheduler will not send any requests to the old
worker aside from requestSuicide, and will not accept old updateStatus since
the worker ID won't match.  In the unlikely event that it accepts another
processHeartbeat from the old worker, the worker would be treated as new.

Poetic aside: If the scheduler loses a worker (marking it MUST_DIE), but it
is not replaced, and the worker for some reason survives the requestSuicide,
and does not itself enter MUST_DIE, it is theoretically possible that a
much-delayed runTask would cause a task to start on this worker.  Once the
task finishes, the scheduler would still accept its updateStatus, so not
much harm is done.  This is also not a big issue because sane health
timeouts make such a scenario exceedingly unlikely.

= notifyIfTasksNotRunning interactions (14/20 so far) =

All interactions with processHeartbeat were discussed above.

This call does not interact with getRunningTasks in any way, because the
latter is only called for workers the NEW state, while
notifyIfTasksNotRunning may only be called after a runTask, which is never
used in the NEW state.  Now, let's check the remaining 2 calls.

This call does not modify "running tasks" state, and only inspects it on the
worker.  In terms of state changes, it increments its own per-worker
sequence number (on both scheduler & worker), and updates the scheduler's
"unsure if running" task list.  It also causes the worker to call
updateStatus(was not running) for the tasks that are not running at the time
this call was received.

On the worker, notifyIfTasksNotRunning simultaneously locks state_, to
update the sequence number, and runningTasks_, to inspect it.

== Interactions on the worker ==

- With runTask: On the worker, a mutex protects runningTasks_, so
  notifyIfTasksNotRunning and runTask are strictly ordered, and the
  updateStatus(was not running) is always issued truthfully.  But, there is
  a catch -- once a worker claims that a task "was not running", it must
  reject any attempts to later start the same task (as might happen if a
  runTask hits networks delays).  By starting such a task, the worker would
  retroactively make itself a liar.

  To spare the worker from having to store all its past "was not running"
  tasks, the worker and the scheduler track a "notifyIfTasksNotRunning
  sequence number".  It prevents the worker from executing runTasks that
  were sent *before* the most recently received notifyIfTasksNotRunning. 
  The exact evolution of this state is documented in the comment for
  runTask.

 - With updateStatus: (i) There are no interactions with updateStatus(was
   not running); (ii) updateStatus(task ended) locks the runningTasks_
   mutex, so the "running->not running" transition is strictly ordered with
   respect to to notifyIfTasksNotRunning.  If the matching updateStatus runs
   earlier than notifyIfTasksNotRunning, the worker will issue a _redundant_
   updateStatus(was not running).  This is not a problem because the
   scheduler handles it correctly (see the updateStatus docblock).  If the
   matching updateStatus runs later, then notifyIfTasksNotRunning will see a
   running task, and issue no additional updateStatus.

== Interactions on the scheduler == 

notifyIfTasksNotRunning on the scheduler does not access runningTasks_, so
any inter-call interactions can only concern the "unsure if running" tasks
list, or the notifyIfTasksNotRunning sequence number.

 - With runTask: Obviously, notifyIfTasksNotRunning can only query task
   invocations after their runTask call failed, and appended them to "unsure
   if running" list.  This list is protected by the workers_ mutex, so those
   accesses are safe.

   runTask, by design, sends the current notifyIfTasksNotRunning sequence
   number, while notifyIfTasksNotRunning increments it and then sends it. 
   This number is protected by the workers_ mutex, so those accesses are
   safely ordered.  The invariant that must be honored is that the sequence
   number sent with notifyIfTasksNotRunning be greater than that of any of
   the failed runTasks' sequence numbers.  This is trivially true, since
   notifyIfTasksNotRunning increments the sequence number
   *after* it has the list of tasks to query.

 - With updateStatus: Whenever the scheduler receives a valid
   updateStatus (either "was not running" or "task ended"), it locks the
   workers_ mutex and removes the task from the "unsure if running" list. 
   This might happen after the task list for notifyIfTasksNotRunning is
   composed, in which case the query will include some tasks that the
   scheduler actually knows not to be running.  This is fine, since any
   consequent updateStatus(was not running) calls will be ignored -- see the
   updateStatus docblock.

   The scheduler's updateStatus does not interact with the
   notifyIfTasksNotRunning sequence number.

== Aside: Tracking the "unsure if running" state ==

The scheduler sends notifyIfTasksNotRunning queries about tasks in the
"unsure if running" list.  Since this list is scheduler-only (not
distributed), and is protected by a mutex, keeping it correct is pretty
straighforward:
 - runTask may add to the list.
 - A successful notifyIfTasksNotRunning removes from the list, taking care
   only to remove the tasks & invocation IDs it queried.
 - Worker loss clears the list.
 - updateStatus removes the updated item from the list.
So long as this list is non-empty, the scheduler periodically calls
notifyIfTasksNotRunning to try to clear it out.

= runTask interactions (18/20 so far) =

All interactions with processHeartbeat and notifyIfTasksNotRunning were
discussed above.

The scheduler cannot call runTask until after getRunningTasks succeeds.  The
worker will not accept runTask until it leaves the NEW state (i.e.  after it
knows that the scheduler's getRunningTasks succeeded).  So, these two calls
do not interact.

This leaves just the interactions with updateStatus:

 - On the worker: (i) updateStatus(was not running); (ii)
   updateStatus(task ended)

 - On the worker, the updateStatus(task ended) for a particular task
   invocation can obviously only be sent after its runTask was received.  As
   for updateStatus(was not running), it might be sent if a
   notifyIfTasksNotRunning arrives before the runTask, in which case the
   runTask will be rejected (see notifyIfTasksNotRunning's interactions on
   the worker).  notifyIfTasksNotRunning checks task invocation IDs, while
   runTask prohibits even two tasks with the same task ID.  Thus, no
   cross-task interactions are possible.

 - On the scheduler: For a given task invocation, these are intrinsically
   ordered -- the scheduler can only receive updateStatus (of either kind)
   after sending the corresponding runTask.  Interactions between different
   invocations can't happen, since updateStatus checks the ID.

= updateStatus interactions (20/20 so far) =

All interactions with processHeartbeat, notifyIfTasksNotRunning, and runTask
were discussed above.  The interactions between updateStatus(was not
running) and updateStatus(task ended) are described in the updateStatus
docblock.  That leaves only getRunningTasks:

- The worker makes updateStatus calls completely indepentently of
  getRunningTasks, so it may send updates while still in NEW state.

- The scheduler rejects updates from a worker in NEW state, so no
  updateStatus changes will be received until after getRunningTasks is
  received and processed.  Otherwise, the two calls could race to modify the
  running tasks state.

= Non-core calls =

The following calls do not interact with any of the scheduler or worker
state above, so they can be excluded from the interaction analysis:

 - getJobLogsByID: Return log lines for the UI.
 - killTask: Kill a specific running task instance, but do not change the
   worker's or scheduler's internal state -- instead, the task's death will
   be registered just as if it had quit on its own.
 - requestSuicide: The scheduler sends this if it decides that the worker
   should not be running (e.g.  another has replaced it, or it has been
   unhealthy too long and became lost).  The worker quits immediately, from
   a system perspective, this is equivalent to the worker crashing.
== READ THIS FIRST ==

This was written before Bistro got its CGroup-based termination support, so
this is much less critical now, since an appropriately configured Bistro
worker can reliably reap its children without external help.  

Post-Bistro-CGroups, one possible improvement would be to write a
`fry_taskreaper` to reap tasks even when `bistro_worker` is gone by:
 - Adding AsyncCGroupReaper support (killing self last -- do use
   `cgroup.procs`, do **not** use `cgroup.tasks`), and
 - Adding a TERM-wait-KILL option upon receipt of only SIGTERM.

When used in such a setup, Bistro would set its PARENT_DEATH_SIGNAL to
SIGTERM (or similar), and would use TERM-only killing, thereby delegating
all KILL authority to `fry_taskreaper`.

== Bistro signal handling ==

Imagine a Bistro worker starting tasks, which in turn start some of their
own subprocesses.  It is important to carefully handle termination signals
in this pyramid, for two reasons:

 - To avoid orphaning tasks: Any user code that keeps running when Bistro 
   is not aware of it is a liability. It ruins our resource tracking, and is
   very likely to cause Bistro to start a second copy of the same task --
   which might even cause data corruption.

 - If a person wants to manually end a task, pkill & kill should work as 
   expected.

This note explores the design space, and gives the rationale for the current
defaults.


== Design for least surprise ==

There are many signal-handling behaviors possible. This design aims to
satisfy the following high-level constraints:

1) Terminating the parent should terminate all descendants.  In other words,
terminating any process in the hierarchy should not leave orphans.

 * When a Bistro scheduler or worker exits, so should all its tasks.
 * SIGKILL should trigger as much descendant cleanup as feasible, via
   PARENT_DEATH_SIGNAL.

2) SIGKILLing a process should trigger a best effort to terminate all its
descendants.

3) Interactive behavior in a terminal should be as expected. Ctrl-Z and
Ctrl-C should work.

Unfortunately, is not possible to adhere to these perfectly, so we just do
our best.  The defaults below are meant to be a good compromise when CGroups
are disabled (otherwise, there's not much to worry about).


== Bistro scheduler / worker choices ==

a) PARENT_DEATH_SIGNAL for tasks:

 - None: Let children run if the parent is killed.
 - TERM: If (b) is Yes, this enables the child to do a careful cleanup of
   its own children.  Can leak the child if it has poor signal handling.
 - KILL: **Default**, because (b) defaults to No, making it impossible for
   to forward the SIGTERM to all descendands without CGroups support.  Great
   when tasks do not spawn other subprocesses, or when they properly set
   their descendants' PARENT_DEATH_SIGNAL (otherwise, descendants *will* get
   orphaned due to this KILL).

b) Make each child a process group leader? 

 - No: **Default**, to make Ctrl-C and Ctrl-Z work as expected in an
   interactive setting.  Specifically:
    - With a process group per task, Bistro tasks will continue running
      even if you Ctrl-Z the worker. Surprising, but not terrible.
    - The worker will carefully reap its tasks when terminating due to
      SIGTERM/INT/QUIT, so no problems here.
    - When used with Local Runner, Ctrl-C or other signals *will* leak
      the tasks on exit. Once we fix this, it would be best to default to
      "all tasks are process group leaders"
 - Yes: Great in non-interactive environments, since this lets Bistro
   terminate multi-process tasks pretty well even without CGroup support.

c) What signals should "killTask" send? (see the "kill_subprocess" config)

 - TERM: **Default** Gives the child a chance to clean up, and return some
   status.  Safest without CGroups, since broken tasks might fail to quit,
   rather than quit, and leak their descendants.   
 - TERM, wait some seconds, then KILL: Risks leaking descendants, see KILL. 
 - KILL: Faster when no cleanup is needed. WARNING: without CGroups and
   without PARENT_DEATH_SIGNAL settings on all descendant subprocesses, this
   will result in the task's subprocesses being orphaned.

d) Destination for the "killTask" signals:

 - Only the child process: **Default**, because (b) defaults to No. 
 - The child process's group: If (b) is Yes, lets us soft-kill all
   descendants of a task, giving them a chance to clean up.  

e) SIGTERM/SIGQUIT/SIGINT handler:

 - Bistro worker has one, and reaps all its tasks.
 - TODO: Bistro scheduler + local runner needs to reuse this logic, but
   currently does not. Once this happens, update (b)'s default.
For a brief foreword, see "Scheduler startup and initial wait" in
if/README.worker_protocol.


= Why is the initial wait necessary? =

A reliable task scheduler:
 - *Never* starts a second copy of a task that is already running.
 - Eventually retries tasks that were running on a worker that died.

This requires distinguishing between tasks that are "probably running" and
those "certainly not running", and some kind of timeout mechanism to
identify tasks that stopped running without notice (e.g. due to a kernel
crash).

Typically, remote task schedulers use of persistent store, like a database
or ZooKeeper, as the source of truth for what tasks are running, and to
store the "last heard from" value for timeouts.  This has a few
disadvantages:
 - The overall QPS of the system becomes bottlenecked by your storage
   latency, which can be challenging to keep low.
 - The system becomes more complex to operate and deploy, since storage
   services are notoriously labor-intensive to keep up and responsive.
 - The possibility of 3-way conflicts between scheduler, DB, and the workers
   themselves, creates more failure modes, and substantial code complexity
   to mitigate them.

Bistro takes an approach with fewer moving parts and bottlenecks: its
workers are the sole source of truth about the currently running tasks.  See
if/README.worker_protocol for the protocol details, but in a nutshell:
 - A scheduler associates with new workers by accepting their heartbeats.
 - It then polls them for running tasks to populate its in-RAM model
   of what tasks are running.
 - The scheduler's model errs on the side of assuming that a task is running
   until proven otherwise.
 - The worker-scheduler protocol keeps the scheduler's models up to date.
 - The worker & scheduler both use the same state machine for worker
   health, ensuring that network-partitioned workers kills their tasks
   just as the scheduler decides they would be lost.

At startup, the scheduler does not know the set of workers, nor their
running tasks.  It is imperative to find the running tasks *before* starting
new tasks, since we would otherwise certainly start duplicates of
already-running tasks.  So, the scheduler must wait for workers to connect.
In the simplest implementation, the wait is just as long as it would take
for a healthy, but network-partitioned worker to commit suicide.  That is
sure to prevent double-starting tasks, but makes it inconvenient to use a
large timeout for "worker becomes lost" -- each scheduler restart leads to a
long downtime.

Why not just give the scheduler a full list of workers at startup? Manually
curating one is too laborious with big deployments.  Automatically
maintaining one is tricky, since one has to watch a worker's health status
using Bistro's state machine, and remove workers that exceed their timeout.
In effect, the automatic curator would still have to wait the same amount of
time whenever a worker goes AWOL, and it would be another moving part in the
system.  This additional complexity is not clearly better than starting with
an unknown set of workers.


= How to shorten the initial wait? =

One can sacrifice reliability to manually shorten the initial wait via
--CAUTION_startup_wait_for_workers.  This will mean that each scheduler
restart exposes you to a risk of double-starting tasks.  Network partitions
are not all that rare in production systems (Facebook has had plenty).  So,
basically, this is a bad idea if you care about reliability.  And if you do
not, why not just make your "--lose_unhealthy_worker_after" and other
timeouts shorter?

Instead of the Faustian bargain of using an unsafe intitial wait, Bistro
has a mechanism to shorten the initial wait in the common case. Imagine
that your scheduler restarts when:
 - All workers are healthy / responsive.
 - Workers are neither being removed nor added.

In this steady-state scenario, there is a simple fix:
 - Each worker stores a hash of the entire worker set, regularly
   updated by the scheduler.
 - When the workers reconnect, the scheduler can check whether all
   the workers agree on the same worker set, and exit initial wait
   the moment that this worker set is reached.

This is why each worker heartbeat carries the WorkerSetID it currently
knows, to which the scheduler responds with its latest WorkerSetID.


= What makes a worker set consensus robust? =

While the fix above sounds simple, our ultimate goal is to have workers'
WorkerSetIDs be set up in such a way that if the scheduler restarts, and
workers connect to the new scheduler at some arbitrary speed, and in an
arbitrary order, it will never be the case that the scheduler detects a
worker consensus before *all* workers that might be running tasks have
connected.

Such guaranteed robustness takes a bit of extra care.

== It can be unsafe to start running tasks before enough consensus emerges ==

Here is a simple example that shows why tasks must not be run before enough
consensus exists:

- Start with one unhealthy worker w1 whose WorkerSetID is itself.
- A second worker w2 connects. A choice is forced -- either:
 (a) Wait for the unhealthy w1 to add w2 to its WorkerSetID.
 (b) Immediately start running tasks on w2.

Choosing (b) is unsafe:
 * A task starts on w2.
 * The scheduler restarts.
 * w1, still unaware of w2, is first to reconnect to the scheduler.
 * The scheduler instantly achieves consensus, and starts duplicate tasks on
   the formerly unhealthy w1.

The problem is that w1's WorkerSetID is enough for a spurious consensus,
while w2 has running tasks.  We cannot prevent the spurious consensus -- a
consensus set of workers can become transiently unhealthy, and new workers
can connect in the meanwhile.  However, we **can** avoid starting new tasks
until the spurious consensus disappears.

Bistro achieves this via `consensusPermitsWorkerToBecomeHealthy()`, a pure
function that examines a newly added worker, and decides whether it's safe
to start running tasks on it.  Once a worker `hasBeenHealthy_`, this
function's output is no longer used.  In effect, this adds an extra state to
Bistro's state diagram, located between NEW and HEALTHY, but it was easier
to implement the hysteresis as an extra boolean.

This initial state of "UNHEALTHY due to lack of consensus" has an extra
wrinkle: workers will NOT become MUST_DIE solely due to lack of consensus.
This is important when we have a high turnover of workers -- any incoming or
departing worker delays consensus, so without blocking MUST_DIE here, it is
possible to reach a pathological steady state where workers are lost because
they have no consensus, thus preventing other workers from reaching
consensus.  See also "Future: dealing with high worker turnover" below.

The simplest implementation of `consensusPermitsWorkerToBecomeHealthy()`
would be to always wait for all non-MUST_DIE workers (healthy or not) to add
a new worker to their WorkerSetID **before** running tasks on the new
worker.  Unfortunately, this means that any time you have unhealthy workers,
you will be unable to use additional workers until the unhealthy ones are
lost.  This is very inconvenient -- such a "consensus" cure for long initial
waits would be just as bad as the disease.

Instead, Bistro only waits for as long as there are workers, which do not --
either directly, or through other workers in their WorkerSetID -- require
the newly added workers to achieve consensus.  In other words, instead of
asking each worker's WorkerSetID to include the new worker, we take the
transitive closure through all available WorkerSetIDs.  This precludes the
existence of worker set that can achieve consensus on scheduler restart, but
that does **not** include the new worker.  In a setup with many workers,
this mechanism requires far fewer WorkerSetIDs to actually contain the new
worker.  Instead of waiting for O(# workers) WorkerSetIDs to include the new
worker, we generically only need to wait for 1 WorkerSetID update before it
is safe to run tasks on a new worker.

For the careful reader: yes, Bistro's mechanism is equivalent to "wait for
w1" in the contrived scenario above.  Its strength lies in that it works
very well when there are many workers, while "wait for all workers" works
terribly.

A naive implementation of the "transitive closure of WorkerSetIDs" idea
would store for every worker the set of workers it requires.  With N
workers, this would lead to O(N^2) memory usage and O(N^2) update duration.
These are not appealing at Bistro's scale.  However, there is a smarter
implementation.


= Efficiently maintaining a robust worker set consensus =

The rest of this README is dedicated to the nitty-gritty details of Bistro's
implementation of the above idea, but does not add much conceptual depth.
Read on if you are:
 - seeking to understand the corner cases, and what can go wrong,
 - modifying the relevant RemoteWorkers code.

== Why are UNHEALTHY workers required for initial-wait-ending consensus? ==

The downside of including UNHEALTHY workers is clear: if a `w` becomes
UNHEALTHY, and the scheduler restarts, the scheduler will incur the maximum
initial wait unless the worker comes back sooner.

However, it is unsafe to exclude such workers, for the same reason -- the
network partition may be transient, the UNHEALTHY workers may actually be
running tasks, and if the scheduler exits initial wait before those workers
reconnect, it can easily start second copies of those tasks.

There is no simple way to wiggle out of this scenario. Not waiting for
UNHEALTHY workers to get lost **and** not double-starting tasks would
require a secondary way of learning about what workers were running which
tasks -- either a DB, or consensus storage among the workers themselves.
Bistro avoids the complexity, and accepts the occasional startup delay.

== Why must UNHEALTHY workers indirectly require new workers? =

This section reiterates the point of the above "It can be unsafe to start
running tasks before enough consensus emerges" in slightly different words.

We insist that all non-MUST_DIE workers indirectly require `w` before
allowing tasks to be run on `w`.  Why is that?

The downside is that we can end waiting for UNHEALTHY workers to get lost
before we can start tasks on new workers.  Unfortunately, failing to wait is
unsafe.

The following scenario demonstrates what goes wrong if we do not require
UNHEALTHY workers to participate in the consensus -- we will end up
double-starting tasks:
  - The scheduler is empty.
  - w1 connects
  - w1's WorkerSetID becomes "just itself"
  - w1 stops sending heartbeats
  - scheduler leaves initial wait
  - w2 connects, becomes healthy
  - scheduler starts task T on w2 -- **we did not wait for w1 to learn of w2**
  - scheduler restarts
  - ex-unhealthy w1 sends a heartbeat, registering a WorkerSetID of {w1}.
  - scheduler detects consensus and exits initial wait
  - scheduler starts task T on w1 (UH-OH, double-start!)
  - w2 connects, *kaboom*

We don't *have* to require NEW workers to be part of the consensus. For
the scheduler to start tasks, while having a NEW worker, the worker must
have first connected after the scheduler exited initial wait -- it's
pretty safe to assume that such a NEW worker has an empty WorkerSetID and
thus could not trigger the initial WorkerSetID consensus.  However, there
is no harm in including NEW workers, so we do.

== How can Bistro's consensus mechanism fail? ==

Excluding UNHEALTHY workers from the consensus is not the only thing that
can cause problems, but it is the only one we can do something about.  Here
are the other cases to consider:

MUST_DIE worker: it would be pretty pathological, though not impossible, for
such a worker to both be alive *and* have a dangerous WorkerSetID.  For
example, in the scenario above, w1 might have become MUST_DIE due to a w1a
connecting with the same shard ID **and** the suicide request might have
gotten lost.  However, we have to take this chance, since otherwise losing a
worker will prevent worker set consensus from working on the next scheduler
restart.  The good news is that this particular scenario can be prevented by
**not** using --allow_bump_unhealthy_worker, which would guarantee that w1
would suicide due to its own timeout.

Unknown worker: in some macabre circumstances (e.g. multiple rapid scheduler
restarts), we can end up with a worker like w1 above, which is unknown to
the scheduler *and* has a WorkerSetID e.g.  equal to {w1}.  If this worker
is first to connect to a just-started scheduler, it **will** exit initial
wait, and **will** double-start tasks.

== Tracking which workers require each other to achieve consensus ==

Remember our goal: never to achieve a consensus on startup, which excludes
any workers that might already be running tasks.  We achieve it by only
starting to run tasks on a worker `w` when (a) `w` requires every
non-MUST_DIE worker, and (b) `w` is **indirectly** required by every other
non-MUST_DIE worker.

Definition: `w` indirectly requires `wN` if there is a chain such that `w`
requires `w1`, which requires ..., which requires `wN`.

We could further relax the above condition (and thus start running tasks
sooner), since any worker that indirectly requires a `MUST_DIE` worker
cannot participate in any kind of consensus.  Clearly, `w` does not have to
wait to be required by any such workers.  However, computing or maintaining
whether a given worker indirectly requires a MUST_DIE worker is
unnecessarily complex.  To implement it efficiently, one would likely
forward-and-back-propagate additional types of updates through the graph of
"w1 requires w2".  Bistro neglects this optimization, and compromises on
starting to some tasks a bit later than necessary by waiting for `w` to be
indirectly required even by workers that also indirectly require MUST_DIE
workers.

== Efficiently maintaining `indirectWorkerSetID_` ==

Conceptually, the scheduler has a graph of workers, whose directed edges
indicate that one worker's workerSetID includes the other worker.  The size
of the edge set is quadratic in the number of workers.  Fortunately, we do
not have to explicitly store the edges or even iterate over them.

Every relevant WorkerSetID originates from this scheduler, and since
RemoteWorkers is synchronized, we have a linear view of history: w1 was
added, w2 was added, w1 was lost, etc.  Every associated worker's set can be
uniquely identified by a single version number.  So, that's what we do.

For each worker, we iteratively maintain a lower bound on the set of workers
that it indirectly requires in `indirectWorkerSetID_`.  This is an
ever-increasing version pointing into the worker set history.  Its update
strategy is a simple form of label propagation -- note that it may require
multiple passes to converge:

- Initially, it is not set. This means "worker requires unknown other
  workers" -- unsafe for consensus!

- Resets to `workerSetID_` any time that version is newer than ours.

- On every `RemoteWorkers::updateState`, updates to the highest-versioned
  `indirectWorkerSetID_` of all of the current set's workers.

  Note that some of the workers may be MUST_DIE -- either MUST_DIE because
  they timed out and were lost, or because they were bumped (possibly with
  the unsafe flag of --allow_bump_unhealthy_worker), or both.  For the ones
  that were not bumped, we will use (and update) their
  `indirectWorkerSetID_` as if they were not MUST_DIE.  It must be safe to
  either use or not use these (since we can neither "unpropagate" through
  workers that became MUST_DIE after we propagated through them, nor can we
  propagate through bumped ones) -- see ** below.  The decision to propagate
  trades off a little more computation for the occasional chance to start
  running on new workers sooner.

  To do this propagation, we must use the history to materialize each
  version as an actual worker set, and consider all the workers in the set
  -- we can do so efficiently by sorting the RemoteWorkers by their version,
  and maintaining a sorted set of versions as we iterate through history.

- Run this algorithm every `updateState`, so that `indirectWorkerSetID_`
  eventually captures all the workers that the current worker indirectly
  requires.

== Why is it okay to always pick the highest version when propagating? ==

Let's say we're trying to find the transitive closure of indirectly required
workers for `w`.  Each propagation will pick the highest `workerSetID_`
version among the workers in its `indirectWorkerSetID_`.  This new will
contain some newly-added workers, but they all have the property that `w`
cannot be part of an initial-wait-ending consensus without those workers.

So the added workers cause no problems. On the other hand, using a higher
version will also forget that `w` indirectly requires some workers that
became MUST_DIE after its current version of `indirectWorkerSetID_` (and,
recursively, all of their requirements).  As a result, `w`'s
`indirectWorkerSetID_` value ends up conservative -- a new worker `w` may be
blocked from running tasks while waiting for worker `w_older` to indirectly
require it, even though `w_older` indirectly requires some MUST_DIE workers
(and thus is irrelevant for the purposes of consensus safety).

**This subsection also explains why either choice is safe: to propagate, or
not to propagate worker sets through MUST_DIE workers.


= Future: dealing with high worker turnover =

If new workers connect, or existing workers are lost, with a high enough
frequency, the existing workers will NEVER reach consensus.  This is a bit
of an adversarial case, but there is a fairly simple trigger -- a small pool
of workers which connect, become unhealthy, and then lost.

The required number of misbehaving workers to trigger a pathology can be
estimated as N = (time to lose a worker) / (time to establish consensus).
If we have many more than N crash-looping workers, and their restarts are
spread uniformly through time, then consensus will never emerge.

With the current scheduler & worker defaults, this N is approximately:
 (60 + 60 + 500 + 2*5) / (2 * 15) = 21

Here is an idea for counteracting this. Suppose we haven't reached consensus
after some number K of "new worker" (but not "updated", and probably not
'lost') WorkerSetID changes.  Then, we temporarily queue up any incoming
"new worker" updates to the consensus state, and establish a slightly stale
consensus.  In the worst case, where we gradually lose all workers just
before achieving consensus, the time to reach consensus is bounded by
(number of workers) * (time to reach consensus). In practice, this should
converge pretty fast.

Then, we replay the batched queue of "new worker" updates and reset the
counter of "updates without consensus" to K.

Aside: I **think** that it's not a good idea to also queue "lost" updates,
since doing that could block consensus from emerging.  It's also harder,
since a lost RemoteWorker can get replaced, complicating our bookkeeping.

This idea is a definite improvement in that it gives guaranteed convergence.
The minor complication is that the current "new worker" callback is
synchronous, and enabling it to be queued up would require some care.  The
resulting RemoteWorker would, for all intents and purposes, appear as any
other "never been healthy, blocked by consensus" worker.  The only
difference is that it would not be included in any consensus calculations.
If such a worker is lost, or its WorkerSetID state updated, we have to take
care not to touch the consensus state either, and instead just update the
queue.
= Bistro Cron =

== Usage ==

```
#include <boost/date_time/local_time/local_time_types.hpp>
#include <folly/dynamic.h>
#include "bistro/bistro/cron/CrontabItem.h"
boost::local_time::time_zone_ptr tz;  // null for "system tz", or a boost tz
auto cron_pattern = CrontabItem::fromDynamic(
  dynamic::object  // At 10am and 8pm every Tuesday (can also parseJson here)
    ("day_of_week", "Tue")
    ("hour", {10, 20})
    ("minute", 0)
    ("dst_fixes", {"skip", "repeat_use_only_early"})
  tz
);
// Can throw runtime_error if the pattern is malformed.
folly::Optional<time_t> maybe_time = cron_pattern->findFirstMatch(input_time);
if (maybe_time.hasValue()) {
  std::cout << "Next event at " maybe_time.value() << std::endl;
} else {
  std::cout << "No more events" << std::endl;
}
```

== Overview ==

This C++11 cron library has three layers:

=== Timezone handling using either boost::date_time or POSIX ===

This is important because some applications really need boost's explicit,
reentrant timezone support, while others are happy to use the system
timezone (by passing a null timezone pointer).

=== Stateless cron ===

Given a cron-style pattern (e.g. "at 5pm every Tuesday"), and an input_time,
compute the first time >= input_time that matches the pattern.

It improves on traditional crons in several ways:

* The default configuration format is folly::dynamic / JSON, which makes for
  readable and extensible configurations.  Since you don't need a manual to
  understand the schedule, user errors should be less frequent.
  
* It supports "epoch", a simple "run every X seconds" mode unavailable in
  traditional cron.  Combined with a monotonic clock, this is perfect for
  periodic maintenance tasks -- this style of cron is completely immune to
  daylight savings and other date-time disruptions.

* Since Daylight Savings Time transitions are a common source of cron-related
  errors, you are required to specify "dst_fixes" in non-"epoch" cron
  patterns.  This is a list containing (a) either "skip" or "unskip" for
  events that would be skipped when DST moves the clock forward, and (b) one
  of "repeat_use_both", "repeat_use_only_early", or "repeat_use_only_late"
  to handle events that would be repeated due to DST rewinding the clock.
  
* Combining "day_of_week" and "day_of_month" is deliberately unsupported. 
  In traditional crons, this behaves as "either Tuesday or the 15th of the
  month", which breaks the usual rule of "selectors compose via AND". 
  The principle of least surprise demands that this misfeature be removed. 
  If you need this "either-or" behavior, simply create two CrontabItems.

The library is easy to extend, so if you need to have it parse traditional
crontab lines, send us a patch.

=== Stateful cron [not implemented, design below] ===

Stateless cron cannot detect timezone changes, system time changes. It also
cannot gracefully handle events that are late due to your process being
suspended, or the system experiencing very heavy load.  Keeping a bit of
state, and using a monotonic clock, it's possible to address all these
issues in a single wrapper on top of stateless cron.  See 'Stateful cron
design' for a detailed "how to build this".  A patch would be most welcome!

== Concepts and features ==

=== Crontab items and selectors ===

A CrontabItem represents a sequence of recurring events, a pattern of
timestamps.  It is configured with a JSON object (or folly::dynamic).

If the object contains the key "epoch", no other keys are allowed. Such an
item typically represents an event occurring every N seconds in POSIX time
(timezone is never used).  Here are the possible variations:

```
{"epoch": {"period": 300}}  // Every 5 minutes, :00, :05, ... :55
// Every 5 minutes starting at 00:01, Mar 13, 2011 PST (:01, :06, ... :56).
{"epoch": {"period": 300, "start": 1300003260}}
// Every 5 minutes ending on 00:00, Mar 13, 2011 PST (starting in 1970 UTC).
{"epoch": {"period": 300, "end": 1300003260}}
{"epoch": 2700}  // Once, at 16:45 on Dec 31 1969, PST
{"epoch": [2700, 5400]}  // Twice, at 16:45 and 17:30 on Dec 31 1969, PST
```

What follows after "epoch" is a CrontabSelector. As illustrated above,
selectors can be a range with a stride, a single value, or a list of values. 
In a range, "start", "end", and "period" are all optional.  The defaults
are to start with the minimum value (0 for epoch), end at the maximum value
(system-dependent for epoch), and have a period of 1.
  
If "epoch" is not present in a crontab item, the item is assumed to use the
traditional cron semantics. In this case, you are /required/ to specify a 
"minute" selector -- e.g. this item fires every minute:

```
{"minute": {"period": 1}}
```
 
Additionally, you can use "hour", "day_of_week", "day_of_month", "month",
and "year" selectors to further restrict your event. All selectors in an 
item must match for the item to match (they are combined with logical AND).
Some essential details:

* "minute" is between 0 and 59.

* "hour" is between 0 and 23, 13 meaning 1pm.

* "day_of_week" is between 1 (Sunday) and 7 (Saturday) regardless of your
  locale. You can use case-insensitive English day abbreviations with 3+
  letters, e.g.  "Mon", "Tues", "thu", "SUNDAY".

* "day_of_month" can only be used when "day_of_week" is missing. Allowed 
  values are from 1 to 31, though {"day": 30, "minute": 0} will obviously
  always skip February.

* "month" is between 1 and 12, or you can use case-insensitive
  English abbreviations with 3+ letters, e.g. "JAN" or "sEpTe".

* "year" tops out at 9999 because of a boost::date_time limitation.
 
If you specify something nonsensical like the 30th of February,
findFirstMatch() will inspect up to 50 years before giving up and throwing. 
We fail loudly instead of returning "no matches" because this can only
happen due to user error.

CrontabItem parsing can also throw, responding to more straightforward
configuration errors (bad key names, our-of-range values, etc).
 
=== DST Fixes ===

Why is the "dst_fixes" field mandatory for traditional CrontabItems? Due to
Daylight Savings Time transitions, local time is not monotonic:

* 1:30am happened twice on Nov 3, 2013 in the US Pacific timezone -- at UTC
  timestamps 1383467400 and 1383471000.  That's because the local clock was
  set back 1 hour at POSIX time 1383469200.
  
* 2:30am never happened on Mar 10, 2013 in the US Pacific timezone, because
  the local clock was set forward one hour at POSIX time 1362909600.

This causes all problems for users of traditional crons. The author of the
schedule doesn't think about the twice-a-year eventuality, and their
critical daily event ends up running twice in the winter, or not running at
all in the spring.

Vixie cron implements a nice heuristic depending on the frequency of the
job, which reduces the odds of this problem occurring.  Search for "Daylight
Savings" here: http://unixhelp.ed.ac.uk/CGI/man-cgi?crond.  One could add a
thin wrapper on top of "dst_fixes" to replicate this heuristic (send a
patch).

However, I think it's better to have the schedule author think about DST
upfront -- otherwise, they can still be surprised that some days have 23
hours, and some have 25.

That is why "dst_fixes" is required. Its usage is pretty simple: you provide
a list of two strings, e.g.:

```
"dst_fixes": ["unskip", "repeat_use_only_early"]
```

One of the strings says how to handle events whose local time labels would
be skipped by DST moving the clock forward. The options are:

* "skip" -- the event does not fire

* "unskip" -- the event that would be skipped fires 1 second before DST sets
  the clock forward.  Notice that normal events fire on the minute (e.g. 
  2:31:00), but this one happens on the 59th second in countries where DST
  transitions fall on the minute.  You shouldn't rely on this behavior.

The other string must specify how to handle events whose local time label is
repeated by DST moving the clock backwards. The options are:

* "repeat_use_both" -- the event fires twice, once before, and once after
  the clock gets set back.

* "repeat_use_only_early" -- the event fires once, only before the clock
  gets set back.

* "repeat_use_only_late" -- the event fires once, only after the clock gets
  set back.
  
DST fixes are specified per-item because, e.g. "skip" makes a lot of sense
for frequent events, but "unskip" is appropriate for daily events. 
Similarly, "repeat_use_both" is good for frequent events, while daily events
are best served by one of the other two options.

== Caveats and worries ==

=== Timezone rule changes after program start ===

Even if your system is always in the same timezone, and never has large time
shifts, the government can still change the rules.  So, if you're writing a
long-running program, take care to keep the timezone information current. 
This has bitten people in the past:
  http://brian.moonspot.net/2007/03/14/vixie-cron-and-the-new-us-dst/

==== How to keep timezone info fresh ===

* Maybe you don't need to track the local time? Then, you have two options
  that beat dealing with timezone rules.  Option 1: use the "epoch"
  selector.  Your events will fire at different local times depending on
  whether you are in or out of DST, but they will be predictable and
  correct.  Option 2: you can get the same effect, but with human-readable
  crontab items, by forcing a timezone with a fixed offset from UTC, e.g.
  
```  
boost::local_time::time_zone_ptr(
   new boost::local_time::posix_time_zone("MST-07")
)
```

* If you use the system timezone: do whatever it takes to get your libc
  to re-read its timezone DB (potentially even restarting the program).

* If you use boost::date_time: automatically downloading and reading the
  freshest version of the DB.  Send a patch if you write any code to make
  this easier.

* Write some code to parse the Linux timezone DB and feed it into 
  boost::date_time. Then, reread that DB periodically. This has the
  advantage of letting your system package manager keep the timezone
  information current, while getting all the predictability and reentrancy
  benefits of boost::date_time.  If you do this, send a patch.

=== Year 2038 ===

If you want your code to keep working past 2038, you should assert that the
time_t type is 64-bit.

=== Boost "posix" timezone names are nonstandard ===

There are at least two major ways in which boost::date_time's
posix_time_zone does not conform to the POSIX timezone parsing spec:

1) The sign on the timezone's offset relative to UTC is flipped. 
POSIX GMT-5 is Boost GMT+5 and vice versa: 
  https://svn.boost.org/trac/boost/ticket/3336
  https://svn.boost.org/trac/boost/ticket/4545

2) Also, POSIX specifies the DST offset relative to UTC, whereas Boost has
it relative to the standard zone.

For example, both of these compute "Sun Nov 1 01:59:59 EDT 1992" followed by
"Sun Nov 1 01:00:00 EST 1992":

  export TZ="EST+5EDT+4,M3.2.0,M11.1.0"; date -d@720597599; date -d@720597600

  #include <boost/date_time/local_time/local_time.hpp>
  #include <boost/date_time/posix_time/posix_time.hpp>
  int main(int argc, char **argv) {
    for (time_t t : {720597599, 720597600}) {
      std::cout << boost::local_time::local_date_time(
        boost::posix_time::from_time_t(t),
        boost::local_time::time_zone_ptr(
          new boost::local_time::posix_time_zone("EST-5EDT1,M3.2.0,M11.1.0")
        )
      ) << std::endl;
    }
  }

==== How to help ====

Write an adapter that converts POSIX TZ strings to boost TZ names to
eliminate this confusion.  Contribute it to boost, and/or send us a patch.

=== System timezone behavior is dangerous ===

(You should probably specify a boost timezone if at all practical.)

The system timezone (used when the time_zone_ptr is null) can change
arbitrarily at any time (or at least the standard is vague on the subject),
and it can definitely be changed mid-computation by other threads.  This
could trigger some of the assertions in StandardCrontabItem, causing your
program to crash, or -- worse yet -- schedule stuff at the wrong time.

==== How to use the system timezone safely ===

* Use boost::date_time timezones if practical.

* Only call timezone-sensitive functions from a single thread.

* Audit cron library code for places of particular vulnerability to system
  timezone changes (e.g.  the various searches), and see they can be
  improved.  Patches are welcome.

=== System timezone behavior may not be portable ===

If you use a null time_zone_ptr, you are calling localtime_r() and mktime(). 
This is akin to playing Russian Roulette with your C library implementation. 
The standards for those functions are pretty vague.

For example, this library assumes that mktime() & localtime_r() use time_t
to store seconds since the UTC epoch.  This is a safe assumption on systems
I know about, but not part of the standard.

Thread-safey is also not clearly promised in the standard. Glibc has a mutex
in tzset, so it's probably fairly robust.  Regarding clang, Mac OS library
documentation also mentions thread-safety, but not in a clear way.

All that said, these functions are very old and very fundamental, so they
probably work okay on major platforms.


== Possible improvements ==

This list could be much longer and more detailed -- if you get interested in
helping with one or more of those things, email us, and we'll provide more
context.

* In the cron code that does not touch boost timezones, it would be possible
  to replace ptime with a TimeLabel class (akin to struct tm).  In addition
  to cleaning up the semantics, this would enable boost::date_time to be an
  _optional_ dependency, which might be nice for some people. 
  
* Add some "iterated" selector types. For example, "iter_month" could let us
  represent "every 5th month", or "iter_day_of_week" would let you do "every
  other Tuesday", or "iter_day" could help with "every 3 days".  Practically
  speaking, most of these can be addressed pretty well by using "epoch".  If
  you were to implement these new selectors, they should let you specify the
  starting / ending month / day in a human-readable way.  That would be a
  nice usability improvement.

* A different selector type could help with representing some holidays. E.g. 
  to encode "First Tuesday of November", we would also need a
  "weekday_of_the_month" selector.  See boost::gregorian week_iterator and
  nth_day_of_the_week_in_month.
  
* It would be trivial to add a "seconds" selector, but there are some
  complications.  First, the client would have to call findFirstMatch at
  least once per second -- at which point, performance tuning of this code
  may be meaningful.  Secondly, you will start to be affected by time
  discontinuities due to NTP clock adjustments, and leap seconds.  If you
  need really frequent events, the better option is probably to use a
  monotonic clock with "epoch", and not to worry about hitting precise
  places on the local clock.

* Some countries (e.g. Japan and Israel) use a non-Gregorian calendar. It's
  possible to support this using boost::locale, but see "P.S.  Why
  boost::date_time?" for some context first.  You are welcome to add support
  for non-Gregorian calendars (just add new subclasses of CrontabItem), but
  we will be skeptical of patches that add mandatory heavy external
  dependencies.  So, if you have to depend on ICU, you will have to make
  your new CrontabItem a compile-time option -- most folks will not use it.

== Stateful cron design ==

=== Goals and overview ===

Cron is intended to fire events on a precise schedule, as close as possible
to the requested time.  Stateless cron already handles the complication of
Daylight Savings Time.  However, system time changes, timezone changes, and
process suspension / system load can all impact cron's ability to fire
events correctly.  These three exigencies cannot be detected without keeping
state.  They also require additional policy tools to enable schedule authors
to react appropriately.

Stateful cron will be a robust wrapper around stateless cron. It should let
schedule authors gracefully recover from these three disruptions:

* System time changes: big (e.g. manually move the clock by 1 hour, 3 hours,
  1 year) or small (NTP adjusts the clock by seconds or minutes).

* Timezone changes: when the machine moves from Shanghai to Hawaii, stateful
  cron should notice and do the right thing.  This should ideally also cover
  DST rule changes -- so if your current timezone changes its DST shift from
  +1h to +2h, stateful cron should help your service cope.

* Stopping / resuming the cron process: this is similar to the system time
  jumping forward, unless the system clock got set back while we were
  stopped.

When the local time jumps forward, some events will look like they are "in
the past" without having had a chance to fire.  When time jumps backward,
some events will be eligible to fire twice.  There is no universally correct
handling for these.
 
If an event consumer relies on a fixed number of seconds passing between two
events, a "local time" cron library cannot do anything to help -- even the
easy case of daylight savings creates anomalous local-time days having 25
hours and 23 hours.  Clients requiring strict periods between events
should prefer to use the "epoch" crontab selector to escape timezone
changes, and a monotonic clock to escape system time changes.  In such a
setup, stateless cron would be enough -- also, implementing either "skip" or
"unskip" policies for events missed due to process suspension is so easy
that it requires no library support.

For everybody else, stateful cron can provide various policies akin to
"dst_fixes", which specify how to respond to time and timezone changes.

=== Basic requirements for stateful cron ===

Stateful cron needs to have access to the system clock, to a timezone, and
to a monotonic clock (so that we can reliably detect time changes).  The
clocks should be provided via callbacks or templates (for testability),
while timezone setting differs substantially between "system" and "boost" --
more below.

In order to fire events on-schedule, the stateful cron code should run
frequently (e.g.  every minute for normal cron, or every second, if you are
using epoch cron with a 1-second period).

If, due to heavy system load, or process suspension, a long time passes
between two runs of the stateful cron code, it should have an output queue
or iterator interface to allow the emission of more than one event.  We'll
later discuss when it makes sense to skip some events.

A reasonable semantics for the output events would be "emit all events up to
and including the current system time, modulo any policies for mitigating
timezone shifts, time shifts, and process suspensions".

For many applications, running cron in a separate thread, and feeding events
into a thread-safe queue would be a good solution. This should probably be 
an optional feature provided by the library.

=== Timezone changes ===

==== What is a timezone change? ====

A timezone change is when the system is manually transferred to a different
timezone, or when a system's timezone rules are modified in a way that
affects the present moment.  This specifically does not include Daylight
Savings Time changes, since those are already handled by stateless cron.

The way that a timezone change comes about will depend on whether you are
using the system timezone or a boost::date_time zone.

Using the system timezone, any other thread of the process could potentially
trigger a timezone change -- something to be carefully avoided, since
changing the timezone in the middle of a cron computation has undefined
results (including potentially triggering assertions and throwing).  For the
remainder of this section, we assumethat you are calling tzset() in a safe
way periodically, in order to stay on top of the current timezone rules. 
The stateful cron implementation should include some implementation of "keep
the TZ info current", assuming this can be done in a robust way.

Using a boost::date_time timezone, the cron library would actually have to
explicitly accept a timezone change.  So, stateful Cron must provide a
setTimezone() method, which may receive a new time_zone_ptr at any time. 
This is good, because then stateful cron has control of all requisite
locking, and the TZ change will never be effected mid-computation.

==== Detecting a timezone change ====

So, now imagine: the timezone rules just changed. How does one detect this,
and/or separate it from "the system time has changed"?

The best signal would be that the GMT offset of the current timezone, at the
current time, has changed between two invocations of the stateful cron code. 
There are confounding issues:

* With the system timezone, we can only query the current timezone, not our
  previous run's timezone.

* Normal DST transitions also change the DST offset, so we are looking for
  "unexpected" changes to the GMT offset.

* If I manually move the system time across a DST transition, it will also
  change the GMT offset.

In both cases, therefore, we are not looking for a change in GMT offset
between "now" and "the previous time we looked".  Rather, we should remember
the timestamp and GMT offset of the previous time we looked, and recompute
the offset using our current timezone.  If it hasn't changed, we conclude
that we're in the same timezone as before.  This heuristic is imperfect,
since it ignores the GMT offset of the present moment.  Unfortunately, when
using the systme timezone, there is no way of querying the GMT offset of
"now" with "our previous run's timezone".  So, this retrospective heuristic
is probably the best we can do -- better suggestions are welcome.

==== Responding to a timezone change ====

Timezone changes are administrative events that change the definition of
"local time".  They do not affect "epoch" crontab items at all (code test:
isTimezoneDependent() returns false).  For "standard" crontab items, the
easiest strategy is to forget the past and to work with the new timezone. 
This is equivalent to DST fixes of "skip", "repeat_use_both".

One might potentially introduce "unskip" and "repeat_use_only_early", for
the cases where the timezone change moves local time a few hours forward or
back.  Implementing "repeat_use_only_late" is impossible, since unlike DST
transitions, we have no way of anticipating the timezone change.  Therefore,
I'll just call the second heuristic "do_not_repeat".

The complication is that schedule authors might want different behaviors
depending on the size of the timezone change.  If I have a daily event, and
I move local time back by 3 hours, it seems bad to repeat the event.  So,
one would want "do_not_repeat" for that case.  But, for the same daily event
and a timezone shift of 18 hours back, you might as well repeat the event.

Therefore, the policy tool should probably be "unskip if the the shift is
less than X seconds", and "do not repeat if the shift is less than Y
seconds".  Since X and Y depend mostly on the frequency of the event, you
might use the same number for both.  So, a reasonable policy tool is:

```
"max_shift_seconds_for_unskip_and_do_not_repeat": 7200,
```

If local time moves forward less than 2 hours, we will fire all events that
would have happened in that time immediately after the shift (in contrast
with "dst_fixes" whose "unskip" fires just before the shift).  Conversely,
if local time moves back less than 2 hours, we will not re-run events
falling on the local times that got repeated.

Much like "dst_fixes", this policy should be specified per-crontab item, and
should be mandatory (see the reasons in the 'DST Fixes' section).

Naturally, this section only applies to timezone-sensitive crontab items, so
that the "epoch" selector ought not to track the GMT offset.

=== Process suspensions or system load ===

Imagine that you have an event that fires every 5-10 minutes (e.g. in some
complex pattern).  If your process blocks for 30 seconds, and an event was
supposed to fire in that period, we should fire the event as soon as the
process unblocks.  The same goes if the process is suspended for 2 minutes. 
However, with a 4- or 15- minute suspension, it becomes more reasonable to
just skip the event(s) that we missed.

So, the setting we developed for timezone changes would also apply here. 
For the described scenario, setting

```
"max_shift_seconds_for_unskip_and_do_not_repeat": 150,
```

would be a good choice. We catch up on stale events that are less than 2.5
minutes old, but skip anything older than that.

The implementation is also pretty easy. Stateful cron remembers the last
system timestamp that it had processed, and when it gets run again, it tries
to catch up to the new system timestamp.  Events that are too old simply get
discarded. 

There's the small complication of how this interacts with system time
changes.  If the process is suspended for 1 hour, during which the system
time is set back 1 hour, then stateful cron would see the monotonic clock
jump forward 1 hour, but no other changes.  In this case, the "time between
runs" A and the "system time change" B cancel out, and we should proceed as
if nothing happened.  This shows you must look at (B - A) when reacting to
system time changes, and that you need to carefully test interactions
between different disruptions.

This section applies both to timezone-sensitive and timezone-insensitive
items.  Of course, for timezone-sensitive ones, we must also track the local
time changes.  You should think about, and test scenarios similar to this
one: your process is suspended for A seconds, during which the local time
moves by B seconds, while the system time moves by C seconds.  The
arithmetic won't be too hard, but you must take care.

=== System time changes ===

To detect system time changes, simply compare (system_clock -
prev_system_clock) with (monotonic_clock - prev_monotonic_clock).  The
difference is the system time change.

It should come as no surprise that the same policy tool of
"max_shift_seconds_for_unskip_and_do_not_repeat" would do the trick here.

Implementation-wise, you should be sure to test that system time changes of
a few seconds are effectively ignored by your code (this is important since
NTP can trigger frequent small-scale time adjustments).  This should not
require special logic -- it should just be a consequence of
"max_shift_seconds_for_unskip_and_do_not_repeat" being set much higher. 
Another good test case is that of a frequent event (whose
"max_shift_seconds..." is appropriately low) seeing the system time change
by a year.  A good implementation should handle this quickly (without
iterating through a million events), and should only send the most recent
"max_shift_seconds..." worth of events to the client.

Like process suspensions, this affects all crontab item types. Also, as
mentioned before, carefully test interactions with process suspension, and
timezone changes.

=== A design modification ===

Instead of exposing a "max_shift_seconds..." policy, a lower-level stateful
cron API coudl just export events that are labelled "skipped" or "already
fired", with a "shift_seconds" field, letting the user trivially implement
the "max_shift_seconds...".  This is a nice and extensible implementation
choice, but I think that even then, you should provide the
"max_shift_seconds..." wrapper on top.

== P.S. Why boost::date_time? ==

POSIX date-time functions are simple to use, but are rife with practical
issues: implementations vary, standards-compliance varies, and thread-safety
varies.  In particular, you cannot reliably use them to query arbitrary
timezones.  Yes, some hackery with tzset() and environment variables can be
attempted, but that is too fragile a path for a library to take.

There are three major open-source C++ libraries that attempt to bring some
uniformity to date-time handling: ICU, boost::locale (partly based on ICU),
and boost::date_time. The latter won by elimination.

* ICU is huge and hard to use. It's much too heavy for a cron library.

* boost::locale has perhaps the nices API of the bunch, but the library is
  of questionable maturity, e.g. https://svn.boost.org/trac/boost/ticket/9584
  The documentation is scant, and does not precisely define the behavior.
  It's therefore not obvious that thought has been put into covering edge 
  cases properly, which means that we can't count on the library for
  mission-critical tasks. Last, but not least, some important features
  are only available when boost::locale is linked against ICU, increasing
  the dependency weight dramatically.
  
* boost::date_time has been around for much longer than boost::locale (at
  least 2001 vs 2011).  As a consequence, its API is not as modern and
  clean, but it has precise, detailed documentation, and there is evidence
  that edge cases are covered.  It also has issues (see the section 'Boost
  "posix" timezone names are nonstandard'), but these are reasonable
  deviations from a standard, rather than crazy/incorrect behaviors.

As a bonus, using boost::date_time instead of the system timezone makes it
easier to add new features -- e.g.  an "nth day-of-the-week in the month"
selector (see 'Possible improvements' for others).
  
N.B. None of the three libraries is able to read the Linux system timezone
database, which is really annoying, since one is forced to put work into
keeping the timezone rules current.  See 'How to keep timezone info fresh'
for some ideas.
Does your web UI need to query a lot of servers at once? Multi-curl
dispatches a lot of concurrent self-curls against your web server as a crude
form of multi-threading.

The library abstracts away all the hard work. All you need to do is:
  1) Extend BistroBaseMultiCurlController.
  2) Add an endpoint for your controller to PhabricatorApplicationBistro.
  3) Extend BistroBaseMultiCurlClient, with the class constant
     CURL_ENDPOINT_PREFIX pointing at your endpoint.

Note that multi-curl has substantial performance overhead (see the TODO in
the base controller), so when your query parallelism is too low (under
PREF_HOSTPORTS_PER_CURL), the library does the queries serially in the main
request, with no self-curl.
# Test-driving the Bistro UI


## Security: words to the wise

**IMPORTANT:** The "test-drive" Docker-based scripts provided for the UI and
for the back-end are emphatically **NOT** appropriate for production use.

I am paranoid, but If I were you, I would run them in a VM with highly
restricted access to the Internet:
 
 - No inbound connections,
 - Allow outgoing connections only to Github, to the Docker repo hosing the
   Ubuntu image, and to the Ubuntu package-management servers.

Upon completing the setup below, you would fire up a browser inside the VM
to play with the UI.

Some specific security issues with these demos include:

 - Everything runs as `root` -- don't kid yourself, Linux kernel isolation
   used by Docker is not perfect, so this is `root` on the host VM too.
 - Docker's security model -- more in `build/fbcode_builder/README.docker`.
 - Lack of code hash / signature verification on the Github code.
 - Lack of production hardening on the Phabricator set-up.
 - Lack of production hardening on the Bistro back-end setup.
 - Default MySQL password in containers.
 - `bistro.get-state-hostname-suffix` is set to '', instead of a safe value.

The above list is definitely not complete.


## Start the backend first

First, you'll want a running back-end. The quickest way to get one is:
 - Use `build/fbcode_builder/README.md` to quickly build the binaries,
 - Follow `bistro/scripts/docker_toy/README.md` to start a toy deployment.

Once that's ready, let's bring up a second Docker image with a web server
hosting the Bistro UI on port 80.


## Docker build

Run this

  ./docker_build.sh &> docker_build.log ; tail docker_build.log


## Start the Bistro UI in a Docker container

Start an interactive session in the UI image you just built:

  docker run --rm -it --expose 80 $(docker images -q | head -n1) /bin/bash
  service mysql start
  service apache2 start


## Connect to the Bistro UI from outside the container

To connect, your browser will need to send a request to the container's IP
address with `phabdocker.example.com` in the `Host` header.  The easiest way
is to add an appropriate line to `/etc/hosts` via the command below.  If you
already have a browser extension that lets you set the `Host` header for
IPs, use that instead.

  sudo apt-get install jq  # If not already installed.
  (
    echo "# Phabricator docker image virtual host"
    echo "$(docker inspect $(docker ps -q | head -n1) | 
              jq -r .[0].NetworkSettings.IPAddress) phabdocker.example.com"
  ) | sudo tee -a /etc/hosts

*Reminder:* clean up your `/etc/hosts` once you're done test-driving Bistro.

Now, you can go to `http://phabdocker.example.com` in your browser. Phabricator
will ask you to register an admin account. Enter some fake data to continue.

After account setup:
 - Go to `http://phabdocker.example.com/bistro`
 - Click the "Hostport List" radio button next to "Host:port Source"
 - Enter `BACKEND_CONTAINER_IP:31415` into "Host:port Data".
 - Click "View Jobs". 
 - The next page will have colored bars representing groups of tasks. 
   Click on one of the colored areas, then click on a task links in the
   revealed panel to see the task's logs.


## Toy example caveats

- Read `Security: word to the wise` at the top of this file!

- Your Docker-based UI will be in UTC. Change the container's timezone if
  that's annoying.

- The in-container Phabricator install has a lot of set-up issues. This is a
  minimal example, for production use you would want to address them.


## Docker disk usage tip: finding images unused by the latest build

If you are building a lot of Docker containers, they tend to eat up disk
quickly.  This command will list image IDs that are **NOT** in use by your
latest build:

  sort <(docker images -qa) <(
    grep '^ ---> [0-9a-f]\+$' docker_build.log | cut -f 3- -d\  | sed p
  ) | uniq -u

Upon checking the output, you can wrap the command with `docker rmi $(...)`
to delete the images.
# Building using `fbcode_builder`

Continuous integration builds are powered by `fbcode_builder`, a tiny tool
shared by several Facebook projects.  Its files are in `./fbcode_builder`
(on Github) or in `fbcode/opensource/fbcode_builder` (inside Facebook's
repo).

Start with the READMEs in the `fbcode_builder` directory.

`./fbcode_builder_config.py` contains the project-specific configuration.
## Debugging Docker builds

To debug a a build failure, start up a shell inside the just-failed image as
follows:

```
docker ps -a | head  # Grab the container ID
docker commit CONTAINER_ID  # Grab the SHA string
docker run -it SHA_STRING /bin/bash
# Debug as usual, e.g. `./run-cmake.sh Debug`, `make`, `apt-get install gdb`
```

## A note on Docker security

While the Dockerfile generated above is quite simple, you must be aware that
using Docker to run arbitrary code can present significant security risks:

 - Code signature validation is off by default (as of 2016), exposing you to
   man-in-the-middle malicious code injection.

 - You implicitly trust the world -- a Dockerfile cannot annotate that
   you trust the image `debian:8.6` because you trust a particular
   certificate -- rather, you trust the name, and that it will never be
   hijacked.

 - Sandboxing in the Linux kernel is not perfect, and the builds run code as
   root.  Any compromised code can likely escalate to the host system.

Specifically, you must be very careful only to add trusted OS images to the
build flow.

Consider setting this variable before running any Docker container -- this
will validate a signature on the base image before running code from it:

```
export DOCKER_CONTENT_TRUST=1
```

Note that unless you go through the extra steps of notarizing the resulting
images, you will have to disable trust to enter intermediate images, e.g.

```
DOCKER_CONTENT_TRUST= docker run -it YOUR_IMAGE_ID /bin/bash
```
# Easy builds for Facebook projects

This is a Python 2.6+ library designed to simplify continuous-integration
(and other builds) of Facebook projects.

For external Travis builds, the entry point is `travis_docker_build.sh`.


## Using Docker to reproduce a CI build

If you are debugging or enhancing a CI build, you will want to do so from
host or virtual machine that can run a reasonably modern version of Docker:

``` sh
./make_docker_context.py --help  # See available options for OS & compiler
# Tiny wrapper that starts a Travis-like build with compile caching:
os_image=ubuntu:16.04 \
  gcc_version=5 \
  make_parallelism=2 \
  travis_cache_dir=~/travis_ccache \
    ./travis_docker_build.sh &> build_at_$(date +'%Y%m%d_%H%M%S').log
```

**IMPORTANT**: Read `fbcode_builder/README.docker` before diving in!

Setting `travis_cache_dir` turns on [ccache](https://ccache.samba.org/),
saving a fresh copy of `ccache.tgz` after every build.  This will invalidate
Docker's layer cache, foring it to rebuild starting right after OS package
setup, but the builds will be fast because all the compiles will be cached.
To iterate without invalidating the Docker layer cache, just `cd
/tmp/docker-context-*` and interact with the `Dockerfile` normally.  Note
that the `docker-context-*` dirs preserve a copy of `ccache.tgz` as they
first used it.


# What to read next

The *.py files are fairly well-documented. You might want to peruse them
in this order:
 - shell_quoting.py
 - fbcode_builder.py
 - docker_builder.py
 - make_docker_context.py

As far as runs on Travis go, the control flow is:
 - .travis.yml calls
 - travis_docker_build.sh calls
 - docker_build_with_ccache.sh

This library also has an (unpublished) component targeting Facebook's
internal continuous-integration platform using the same build-step DSL.


# Contributing

Please follow the ambient style (or PEP-8), and keep the code Python 2.6
compatible -- since `fbcode_builder`'s only dependency is Docker, we want to
allow building projects on even fairly ancient base systems.   We also wish
to be compatible with Python 3, and would appreciate it if you kept that
in mind while making changes also.
