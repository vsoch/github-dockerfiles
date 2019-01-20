<section class="dex_guide"><h1 class="dex_title">Wangle</h1><section class="dex_document"><h1></h1><p class="dex_introduction">C++ networking library</p><p>Wangle is a library that makes it easy to build protocols, application clients, and application servers.</p>

<p>It&#039;s like Netty + Finagle smooshed together, but in C++</p>

## Building and Installing

The main dependencies are:
* The folly library from https://github.com/facebook/folly/. 
* Cmake
* OpenSSL, at least version 1.0.2+, preferably with TLS extension support.

Once folly is installed, run the following inside the wangle directory to build, test, and install wangle:
```
cmake .
make
ctest
sudo make install
```

## Tutorial

There is a tutorial [here](tutorial.md) that explains the basics of Wangle and shows how to build an echo server/client.

## Examples

See the examples/ directory for some example Wangle servers and clients

## License
Wangle is Apache 2.0-licensed.

## Contributing
See the CONTRIBUTING file for how to help out.

## Documentation

<p>Wangle interfaces are asynchronous.  Interfaces are currently based on <a href="https://github.com/facebook/folly/tree/master/folly/futures">Futures</a>, but we&#039;re also exploring how to support fibers</p>

<h2 id="client-server-abstractio">Client / Server abstraction <a href="#client-server-abstractio" class="headerLink">#</a></h2>

<p>You&#039;re probably familiar with Java&#039;s Netty, or Python&#039;s twisted, or similar libraries.</p>

<p>It is built on top of folly/async/io, so it&#039;s one level up the stack from that (or similar abstractions like boost::asio)</p>

<p>ServerBootstrap - easily manage creation of threadpools and pipelines</p>

<p>ClientBootstrap - the same for clients</p>

<p>Pipeline - set up a series of handlers that modify your socket data</p>

<h2 id="request-response-abstrac">Request / Response abstraction <a href="#request-response-abstrac" class="headerLink">#</a></h2>

<p>This is roughly equivalent to the <a href="https://twitter.github.io/finagle/" target="_blank">Finagle</a> library.</p>

<p>Aims to provide easy testing, load balancing, client pooling, retry logic, etc.  for any request/response type service - i.e. thrift, http, etc.</p>

<p>Service - a matched interface between client/server.  A server will implement this interface, and a client will call in to it.  These are protocol-specific</p>

<p>ServiceFilter - a generic filter on a service. Examples: stats, request timeouts, rate limiting</p>

<p>ServiceFactory - A factory that creates client connections.  Any protocol specific setup code goes here</p>

<p>ServiceFactoryFilter - Generic filters that control how connections are created.  Client examples: load balancing, pooling,  idle timeouts, markdowns, etc.</p></section><section class="dex_document"><h1>ServerBootstrap</h1><p class="dex_introduction">Easily create a new server</p><p>ServerBootstrap does the work to set up one or multiple acceptor threads, and one or multiple sets of IO threads.  The thread pools can be the same.  SO_REUSEPORT is automatically supported for multiple accept threads. tcp is most common, although udp is also supported.</p>

<h2 id="methods">Methods <a href="#methods" class="headerLink">#</a></h2>

<p><strong>childPipeline(PipelineFactory&lt;Pipeline&gt;)</strong></p>

<p>Sets the pipeline factory for each new connection.  One pipeline per connection will be created.</p>

<p><strong>group(IOThreadPoolExecutor accept, IOThreadPoolExecutor io)</strong></p>

<p>Sets the thread pools for accept and io thread pools.  If more than one thread is in the accept group, SO_REUSEPORT is used.  Defaults to a single accept thread, and one io thread per core.</p>

<p><strong>bind(SocketAddress),bind(port)</strong></p>

<p>Binds to a port. Automatically starts to accept after bind.</p>

<p><strong>stop()</strong></p>

<p>Stops listening on all sockets.</p>

<p><strong>join()</strong></p>

<p>Joins all threadpools - all current reads and writes will be completed before this method returns.</p>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> however that both accept and io thread pools will be stopped using this method, so the thread pools can&#039;t be shared, or care must be taken using shared pools during shutdown.</div>

<p><strong>waitForStop()</strong></p>

<p>Waits for stop() to be called from another thread.</p>

<h2 id="other-methods">Other methods <a href="#other-methods" class="headerLink">#</a></h2>

<p><strong>channelFactory(ServerSocketFactory)</strong></p>

<p>Sets up the type of server.  Defaults to TCP AsyncServerSocket, but AsyncUDPServerSocket is also supported to receive udp messages.  In practice, ServerBootstrap is only useful for udp if you need to multiplex the messages across many threads, or have TCP connections going on at the same time, etc.  Simple usages of AsyncUDPSocket probably don&#039;t need the complexity of ServerBootstrap.</p>

<p><strong>pipeline(PipelineFactory&lt;AcceptPipeline&gt;)</strong></p>

<p>This pipeline method is used to get the accepted socket (or udp message) *before* it has been handed off to an IO thread.  This can be used to steer the accept thread to a particular thread, or for logging.</p>

<p>See also AcceptRoutingHandler and RoutingDataHandler for additional help in reading data off of the accepted socket <strong>before</strong> it gets attached to an IO thread.  These can be used to hash incoming sockets to specific threads.</p>

<p><strong>childHandler(AcceptorFactory)</strong></p>

<p>Previously facebook had lots of code that used AcceptorFactories instead of Pipelines, this is a method to support this code and be backwards compatible.  The AcceptorFactory is responsible for creating acceptors, setting up pipelines, setting up AsyncSocket read callbacks, etc.</p>

<h2 id="examples">Examples <a href="#examples" class="headerLink">#</a></h2>

<p>A simple example:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">ServerBootstrap</span><span class="o">&lt;</span><span class="no">TelnetPipeline</span><span class="o">&gt;</span> <span class="no">server</span><span class="o">;</span>                                                                                                      
<span class="no">server</span><span class="o">.</span><span class="nf" data-symbol-name="childPipeline">childPipeline</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="make_shared">make_shared</span><span class="o">&lt;</span><span class="no">TelnetPipelineFactory</span><span class="o">&gt;());</span>                                                                             
<span class="no">server</span><span class="o">.</span><span class="nf" data-symbol-name="bind">bind</span><span class="o">(</span><span class="no">FLAGS_port</span><span class="o">);</span>                                                                                                                     
<span class="no">server</span><span class="o">.</span><span class="nf" data-symbol-name="waitForStop">waitForStop</span><span class="o">();</span></pre></div></section><section class="dex_document"><h1>ClientBootstrap</h1><p class="dex_introduction">Create clients easily</p><p>ClientBootstrap is a thin wrapper around AsyncSocket that provides a future interface to the connect callback, and a Pipeline interface to the read callback.</p>

<h2 id="methods">Methods <a href="#methods" class="headerLink">#</a></h2>

<p><strong>group(IOThreadPoolExecutor)</strong></p>

<p>Sets the thread or group of threads where the IO will take place.  Callbacks are also made on this thread.</p>

<p><strong>bind(port)</strong></p>

<p>Optionally bind to a specific port</p>

<p><strong>Future&lt;Pipeline*&gt; connect(SocketAddress)</strong></p>

<p>Connect to the selected address.  When the future is complete, the initialized pipeline will be returned.</p>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> future.cancel() can be called to cancel an outstanding connection attempt.</div>

<p><strong>pipelineFactory(PipelineFactory&lt;Pipeline&gt;)</strong></p>

<p>Set the pipeline factory to use after a connection is successful.</p>

<h2 id="example">Example <a href="#example" class="headerLink">#</a></h2>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">ClientBootstrap</span><span class="o">&lt;</span><span class="no">TelnetPipeline</span><span class="o">&gt;</span> <span class="no">client</span><span class="o">;</span>
<span class="no">client</span><span class="o">.</span><span class="nf" data-symbol-name="group">group</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="make_shared">make_shared</span><span class="o">&lt;</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="wangle">wangle</span><span class="o">::</span><span class="na" data-symbol-name="IOThreadPoolExecutor">IOThreadPoolExecutor</span><span class="o">&gt;(</span><span class="mi">1</span><span class="o">));</span>
<span class="no">client</span><span class="o">.</span><span class="nf" data-symbol-name="pipelineFactory">pipelineFactory</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="make_shared">make_shared</span><span class="o">&lt;</span><span class="no">TelnetPipelineFactory</span><span class="o">&gt;());</span>
<span class="c">// synchronously wait for the connect to finish</span>
<span class="no">auto</span> <span class="no">pipeline</span> <span class="o">=</span> <span class="no">client</span><span class="o">.</span><span class="nf" data-symbol-name="connect">connect</span><span class="o">(</span><span class="nf" data-symbol-name="SocketAddress">SocketAddress</span><span class="o">(</span><span class="no">FLAGS_host</span><span class="o">,</span><span class="no">FLAGS_port</span><span class="o">)).</span><span class="nf" data-symbol-name="get">get</span><span class="o">();</span>

<span class="c">// close the pipeline when finished</span>
<span class="no">pipeline</span><span class="o">-&gt;</span><span class="na" data-symbol-name="close">close</span><span class="o">();</span></pre></div></section><section class="dex_document"><h1>Pipeline</h1><p class="dex_introduction">Send your socket data through a series of tubes</p><p>A Pipeline is a series of Handlers that intercept inbound or outbound events, giving full control over how events are handled.  Handlers can be added dynamically to the pipeline.</p>

<p>When events are called, a Context* object is passed to the Handler - this means state can be stored in the context object, and a single instantiation of any individual Handler can be used for the entire program.</p>

<p>Netty&#039;s documentation: <a href="http://netty.io/4.0/api/io/netty/channel/ChannelPipeline.html" target="_blank">ChannelHandler</a></p>

<p>Usually, the bottom of the Pipeline is a wangle::AsyncSocketHandler to read/write to a socket, but this isn&#039;t a requirement.</p>

<p>A pipeline is templated on the input and output types:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">EventBase</span> <span class="no">base_</span><span class="o">;</span>
<span class="no">Pipeline</span><span class="o">&lt;</span><span class="no">IOBufQueue</span><span class="o">&amp;,</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="unique_ptr">unique_ptr</span><span class="o">&lt;</span><span class="no">IOBuf</span><span class="o">&gt;&gt;</span> <span class="no">pipeline</span><span class="o">;</span>
<span class="no">pipeline</span><span class="o">.</span><span class="nf" data-symbol-name="addBack">addBack</span><span class="o">(</span><span class="nf" data-symbol-name="AsyncSocketHandler">AsyncSocketHandler</span><span class="o">(</span><span class="nc" data-symbol-name="AsyncSocket">AsyncSocket</span><span class="o">::</span><span class="nf" data-symbol-context="AsyncSocket" data-symbol-name="newSocket">newSocket</span><span class="o">(</span><span class="no">eventBase</span><span class="o">)));</span></pre></div>

<p>The above creates a pipeline and adds a single AsyncSocket handler, that will push read events through the pipeline when the socket gets bytes.  Let&#039;s try handling some socket events:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="k">class</span> <span class="no">MyHandler</span> <span class="o">:</span> <span class="k">public</span> <span class="no">InboundHandler</span><span class="o">&lt;</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="IOBufQueue">IOBufQueue</span><span class="o">&amp;&gt;</span> <span class="o">&#123;</span>
 <span class="k">public</span><span class="o">:</span>

  <span class="no">void</span> <span class="nf" data-symbol-name="read">read</span><span class="o">(</span><span class="no">Context</span><span class="o">*</span> <span class="no">ctx</span><span class="o">,</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="IOBufQueue">IOBufQueue</span><span class="o">&amp;</span> <span class="no">q</span><span class="o">)</span> <span class="no">override</span> <span class="o">&#123;</span>
    <span class="no">IOBufQueue</span> <span class="no">data</span><span class="o">;</span>   
    <span class="k">if</span> <span class="o">(</span><span class="no">q</span><span class="o">.</span><span class="nf" data-symbol-name="chainLength">chainLength</span><span class="o">()</span> <span class="o">&gt;=</span> <span class="mi">4</span><span class="o">)</span> <span class="o">&#123;</span>
       <span class="no">data</span><span class="o">.</span><span class="nf" data-symbol-name="append">append</span><span class="o">(</span><span class="no">q</span><span class="o">.</span><span class="nf" data-symbol-name="split">split</span><span class="o">(</span><span class="mi">4</span><span class="o">));</span>
       <span class="no">ctx</span><span class="o">-&gt;</span><span class="na" data-symbol-name="fireRead">fireRead</span><span class="o">(</span><span class="no">data</span><span class="o">);</span>
    <span class="o">&#125;</span> 
  <span class="o">&#125;</span>
<span class="o">&#125;;</span></pre></div>

<p>This handler only handles read (inbound) data, so we can inherit from InboundHandler, and ignore the outbound type (so the ordering of inbound/outbound handlers in your pipeline doesn&#039;t matter).   It checks if there are at least 4 bytes of data available, and if so, passes them on to the next handler.  If there aren&#039;t yet four bytes of data available, it does nothing, and waits for more data.</p>

<p>We can add this handler to our pipeline like so:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="nx">pipeline</span><span class="k">.</span><span data-symbol-name="addBack" class="nf">addBack</span><span class="k">(</span><span data-symbol-name="MyHandler" class="nf">MyHandler</span><span class="k">(</span><span class="k">)</span><span class="k">)</span><span class="k">;</span></pre></div>

<p>and remove it just as easily:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">pipeline</span><span class="o">.</span><span class="no">remove</span><span class="o">&lt;</span><span class="no">MyHandler</span><span class="o">&gt;();</span></pre></div>

<h3 id="staticpipeline">StaticPipeline <a href="#staticpipeline" class="headerLink">#</a></h3>

<p>Instantiating all these handlers and pipelines can hit the allocator pretty hard.  There are two ways to try to do fewer allocations.  StaticPipeline allows *all* the handlers, and the pipeline, to be instantiated all in the same memory block, so we only hit the allocator once.</p>

<p>The other option is to allocate the handlers once at startup, and reuse them in many pipelines.  This means all state has to be saved in the HandlerContext object instead of the Handler itself, since each handler can be in multiple pipelines.  There is one context per pipeline to get around this limitation.</p></section><section class="dex_document"><h1>Built-in handlers</h1><p class="dex_introduction">The stuff that comes with the box</p><h2 id="byte-to-byte-handlers">Byte to byte handlers <a href="#byte-to-byte-handlers" class="headerLink">#</a></h2>

<h3 id="asyncsockethandler">AsyncSocketHandler <a href="#asyncsockethandler" class="headerLink">#</a></h3>

<p>This is almost always the first handler in the pipeline for clients and servers - it connects an AsyncSocket to the pipeline.  Having it as a handler is nice, because mocking it out for tests becomes trivial.</p>

<h3 id="outputbufferinghandler">OutputBufferingHandler <a href="#outputbufferinghandler" class="headerLink">#</a></h3>

<p>Output is buffered and only sent once per event loop.  This logic is exactly what is in ThriftServer, and very similar to what exists in proxygen - it can improve throughput for small writes by up to 300%.</p>

<h3 id="eventbasehandler">EventBaseHandler <a href="#eventbasehandler" class="headerLink">#</a></h3>

<p>Putting this right after an AsyncSocketHandler means that writes can happen from any thread, and eventBase-&gt;runInEventBaseThread() will automatically be called to put them in the correct thread.  It doesn&#039;t intrinsically make the pipeline thread-safe though, writes from different threads may be interleaved, other handler stages must be only used from one thread or be thread safe, etc.</p>

<p>In addition, reads are still always called on the eventBase thread.</p>

<h2 id="codecs">Codecs <a href="#codecs" class="headerLink">#</a></h2>

<h3 id="fixedlengthframedecoder">FixedLengthFrameDecoder <a href="#fixedlengthframedecoder" class="headerLink">#</a></h3>

<p>A decoder that splits received IOBufs by a fixed number of bytes.  Used for fixed-length protocols</p>

<h3 id="lengthfieldprepender">LengthFieldPrepender <a href="#lengthfieldprepender" class="headerLink">#</a></h3>

<p>Prepends a fixed-length field length.  Field length is configurable.</p>

<h3 id="lengthfieldbasedframedec">LengthFieldBasedFrameDecoder <a href="#lengthfieldbasedframedec" class="headerLink">#</a></h3>

<p>The receiving portion of LengthFieldPrepender - decodes based on a fixed frame length, with optional header/tailer data sections.</p>

<h3 id="linebasedframedecoder">LineBasedFrameDecoder <a href="#linebasedframedecoder" class="headerLink">#</a></h3>

<p>Decodes by line (with optional ending detection types), to be used for text-based protocols</p>

<h3 id="stringcodec">StringCodec <a href="#stringcodec" class="headerLink">#</a></h3>

<p>Converts from IOBufs to std::strings and back for text-based protocols.  Must be used after one of the above frame decoders</p></section><section class="dex_document"><h1>Services</h1><p class="dex_introduction">How to add a new protocol</p><p><a href="https://twitter.github.io/finagle/guide/ServicesAndFilters.html" target="_blank">Finagle&#039;s documentation</a> on Services is highly recommended</p>

<h2 id="services">Services <a href="#services" class="headerLink">#</a></h2>

<p>A Pipeline was read() and write() methods - it streams bytes in one or both directions.  write() returns a future, but the future is set when the bytes are successfully written.   Using pipeline there is no easy way to match up requests and responses for RPC.</p>

<p>A Service is an RPC abstraction - Both clients and servers implement the interface.   Servers implement it by handling the request.  Clients implement it by sending the request to the server to complete.</p>

<p>A Dispatcher is the adapter between the Pipeline and Service that matches up the requests and responses.  There are several built in Dispatchers, however if you are doing anything advanced, you may need to write your own.</p>

<p>Because both clients and servers implement the same interface, mocking either clients or servers is trivially easy.</p>

<h2 id="servicefilters">ServiceFilters <a href="#servicefilters" class="headerLink">#</a></h2>

<p>ServiceFilters provide a way to wrap filters around every request and response.  Things like logging, timeouts, retrying requests, etc. can be implemented as ServiceFilters.</p>

<p>Existing ServiceFilters include:</p>

<ul>
<li>CloseOnReleaseFilter - rejects requests after connection is closed.  Often used in conjunction with</li>
<li>ExpiringFilter - idle timeout and max connection time (usually used for clients)</li>
<li>TimeoutFilter - request timeout time.  Usually used on servers.  Clients can use future.within to specify timeouts individually.</li>
<li>ExecutorFilter - move requests to a different executor.</li>
</ul>

<h2 id="servicefactories">ServiceFactories <a href="#servicefactories" class="headerLink">#</a></h2>

<p>For some services, a Factory can help instantiate clients.   In Finagle, these are frequently provided for easy use with specific protocols, i.e. http, memcache, etc.</p>

<h2 id="servicefactoryfilters">ServiceFactoryFilters <a href="#servicefactoryfilters" class="headerLink">#</a></h2>

<p>ServiceFactoryFilters provide filters for getting clients.  These include most connection-oriented things, like connection pooling, selection, dispatch, load balancing, etc.</p>

<p>Existing ServiceFactoryFilters:</p>

<ul>
<li></li>
<li></li>
</ul></section>
# RPC client/server example
---------------------------

Similar to the telnet example, this provides examples of using a
Pipeline and Server/Client bootstrap libraries.  In addition, it
provides examples of:

* Custom codec for serialization
* Service interface, to match up requests with replies.  Various
  versions of this are in the comments
* ServiceFilters, for timeouts, logging, etc.
Codecs are modeled after netty's codecs:

https://github.com/netty/netty/tree/master/codec/src/main/java/io/netty/handler/codec

Most of the changes are due to differing memory allocation strategies.
Rx is a pattern for "functional reactive programming" that started at
Microsoft in C#, and has been reimplemented in various languages, notably
RxJava for JVM languages.

It is basically the plural of Futures (a la Wangle).

```
                    singular              |            plural
        +---------------------------------+-----------------------------------
  sync  |  Foo getData()                  |  std::vector<Foo> getData()
  async |  wangle::Future<Foo> getData()  |  wangle::Observable<Foo> getData()
```

For more on Rx, I recommend these resources:

Netflix blog post (RxJava): http://techblog.netflix.com/2013/02/rxjava-netflix-api.html
Introduction to Rx eBook (C#): http://www.introtorx.com/content/v1.0.10621.0/01_WhyRx.html
The RxJava wiki: https://github.com/Netflix/RxJava/wiki
Netflix QCon presentation: http://www.infoq.com/presentations/netflix-functional-rx
https://rx.codeplex.com/

I haven't even tried to support move-only data in this version. I'm on the
fence about the usage of shared_ptr. Subject is underdeveloped. A whole rich
set of operations is obviously missing. I haven't decided how to handle
subscriptions (and therefore cancellation), but I'm pretty sure C#'s
"Disposable" is thoroughly un-C++ (opposite of RAII). So for now subscribe
returns nothing at all and you can't cancel anything ever. The whole thing is
probably riddled with lifetime corner case bugs that will come out like a
swarm of angry bees as soon as someone tries an infinite sequence, or tries to
partially observe a long sequence. I'm pretty sure subscribeOn has a bug that
I haven't tracked down yet.

DEPRECATED:
This was an experimental exploration. There are better, more robust, and (most
importantly) supported C++ implementations, notably
[rxcpp](https://rxcpp.codeplex.com/). Use that instead. You really shouldn't
use this one. It's unsupported and incomplete. Honest.
Folly: Facebook Open-source Library
-----------------------------------

[![Build Status](https://travis-ci.org/facebook/folly.svg?branch=master)](https://travis-ci.org/facebook/folly)

### What is `folly`?

Folly (acronymed loosely after Facebook Open Source Library) is a
library of C++11 components designed with practicality and efficiency
in mind. **Folly contains a variety of core library components used extensively
at Facebook**. In particular, it's often a dependency of Facebook's other
open source C++ efforts and place where those projects can share code.

It complements (as opposed to competing against) offerings
such as Boost and of course `std`. In fact, we embark on defining our
own component only when something we need is either not available, or
does not meet the needed performance profile. We endeavor to remove
things from folly if or when `std` or Boost obsoletes them.

Performance concerns permeate much of Folly, sometimes leading to
designs that are more idiosyncratic than they would otherwise be (see
e.g. `PackedSyncPtr.h`, `SmallLocks.h`). Good performance at large
scale is a unifying theme in all of Folly.

### Logical Design

Folly is a collection of relatively independent components, some as
simple as a few symbols. There is no restriction on internal
dependencies, meaning that a given folly module may use any other
folly components.

All symbols are defined in the top-level namespace `folly`, except of
course macros. Macro names are ALL_UPPERCASE and should be prefixed
with `FOLLY_`. Namespace `folly` defines other internal namespaces
such as `internal` or `detail`. User code should not depend on symbols
in those namespaces.

Folly has an `experimental` directory as well. This designation connotes
primarily that we feel the API may change heavily over time. This code,
typically, is still in heavy use and is well tested.

### Physical Design

At the top level Folly uses the classic "stuttering" scheme
`folly/folly` used by Boost and others. The first directory serves as
an installation root of the library (with possible versioning a la
`folly-1.0/`), and the second is to distinguish the library when
including files, e.g. `#include <folly/FBString.h>`.

The directory structure is flat (mimicking the namespace structure),
i.e. we don't have an elaborate directory hierarchy (it is possible
this will change in future versions). The subdirectory `experimental`
contains files that are used inside folly and possibly at Facebook but
not considered stable enough for client use. Your code should not use
files in `folly/experimental` lest it may break when you update Folly.

The `folly/folly/test` subdirectory includes the unittests for all
components, usually named `ComponentXyzTest.cpp` for each
`ComponentXyz.*`. The `folly/folly/docs` directory contains
documentation.

### What's in it?

Because of folly's fairly flat structure, the best way to see what's in it
is to look at the headers in [top level `folly/` directory](https://github.com/facebook/folly/tree/master/folly). You can also
check the [`docs` folder](folly/docs) for documentation, starting with the
[overview](folly/docs/Overview.md).

Folly is published on Github at https://github.com/facebook/folly

### Build Notes

#### Dependencies

folly requires gcc 4.9+ and a version of boost compiled with C++14 support.

googletest is required to build and run folly's tests.  You can download
it from https://github.com/google/googletest/archive/release-1.8.0.tar.gz
The following commands can be used to download and install it:

```
wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz && \
tar zxf release-1.8.0.tar.gz && \
rm -f release-1.8.0.tar.gz && \
cd googletest-release-1.8.0 && \
cmake configure . && \
make && \
make install
```

#### Finding dependencies in non-default locations

If you have boost, gtest, or other dependencies installed in a non-default
location, you can use the `CMAKE_INCLUDE_PATH` and `CMAKE_LIBRARY_PATH`
variables to make CMAKE look also look for header files and libraries in
non-standard locations.  For example, to also search the directories
`/alt/include/path1` and `/alt/include/path2` for header files and the
directories `/alt/lib/path1` and `/alt/lib/path2` for libraries, you can invoke
`cmake configure` as follows:

```
cmake configure \
  -DCMAKE_INCLUDE_PATH=/alt/include/path1:/alt/include/path2 \
  -DCMAKE_LIBRARY_PATH=/alt/lib/path1:/alt/lib/path2
```

#### Ubuntu 16.04 LTS

The following packages are required (feel free to cut and paste the apt-get
command below):

```
sudo apt-get install \
    g++ \
    cmake \
    libboost-all-dev \
    libevent-dev \
    libdouble-conversion-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libiberty-dev \
    liblz4-dev \
    liblzma-dev \
    libsnappy-dev \
    make \
    zlib1g-dev \
    binutils-dev \
    libjemalloc-dev \
    libssl-dev \
    pkg-config
```

If advanced debugging functionality is required

```
sudo apt-get install \
    libunwind8-dev \
    libelf-dev \
    libdwarf-dev
```

In the folly directory, run:
```
  mkdir _build && cd _build
  cmake configure ..
  make -j $(nproc)
  make install
```

#### OS X (Homebrew)

folly is available as a Formula and releases may be built via `brew install folly`.

You may also use `folly/build/bootstrap-osx-homebrew.sh` to build against `master`:

```
  cd folly
  ./build/bootstrap-osx-homebrew.sh
```

#### OS X (MacPorts)

Install the required packages from MacPorts:

```
  sudo port install \
    autoconf \
    automake \
    boost \
    gflags \
    git \
    google-glog \
    libevent \
    libtool \
    lz4 \
    lzma \
    scons \
    snappy \
    zlib
```

Download and install double-conversion:

```
  git clone https://github.com/google/double-conversion.git
  cd double-conversion
  cmake -DBUILD_SHARED_LIBS=ON .
  make
  sudo make install
```

Download and install folly with the parameters listed below:

```
  git clone https://github.com/facebook/folly.git
  cd folly/folly
  autoreconf -ivf
  ./configure CPPFLAGS="-I/opt/local/include" LDFLAGS="-L/opt/local/lib"
  make
  sudo make install
```

#### Windows (Vcpkg)

folly is available in [Vcpkg](https://github.com/Microsoft/vcpkg#vcpkg) and releases may be built via `vcpkg install folly:x64-windows`.

You may also use `vcpkg install folly:x64-windows --head` to build against `master`.

#### Other Linux distributions

- double-conversion (https://github.com/google/double-conversion)

  Download and build double-conversion.
  You may need to tell cmake where to find it.

  [double-conversion/] `ln -s src double-conversion`

  [folly/] `mkdir build && cd build`
  [folly/build/] `cmake configure "-DCMAKE_INCLUDE_PATH=$DOUBLE_CONVERSION_HOME/include" "-DCMAKE_LIBRARY_PATH=$DOUBLE_CONVERSION_HOME/lib" ..`

  [folly/build/] `make`

- additional platform specific dependencies:

  Fedora 21 64-bit
    - gcc
    - gcc-c++
    - cmake
    - automake
    - boost-devel
    - libtool
    - lz4-devel
    - lzma-devel
    - snappy-devel
    - zlib-devel
    - glog-devel
    - gflags-devel
    - scons
    - double-conversion-devel
    - openssl-devel
    - libevent-devel

  Optional
    - libdwarf-dev
    - libelf-dev
    - libunwind8-dev
This directory contains `fbcode_builder` configuration and scripts.
Note that the `folly/build` subdirectory also contains some additional build
scripts for other platforms.

## Building using `fbcode_builder`

`fbcode_builder` is a small tool shared by several Facebook projects to help
drive continuous integration builds for our open source repositories.  Its
files are in `folly/fbcode_builder` (on Github) or in
`fbcode/opensource/fbcode_builder` (inside Facebook's repo).

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
allow building projects on even fairly ancient base systems.
<!-- This file is generated from internal wiki guide by folly/facebook/fibers-update-readme.sh. -->
<section class="dex_guide"><h1 class="dex_title">folly::fibers</h1><section class="dex_document"><h1></h1><p class="dex_introduction">folly::fibers is an async C++ framework, which uses fibers for parallelism.</p><h2 id="overview">Overview <a href="#overview" class="headerLink">#</a></h2>

<p>Fibers (or coroutines) are lightweight application threads. Multiple fibers can be running on top of a single system thread. Unlike system threads, all the context switching between fibers is happening explicitly. Because of this every such context switch is very fast (~200 million of fiber context switches can be made per second on a single CPU core).</p>

<p>folly::fibers implements a task manager (FiberManager), which executes scheduled tasks on fibers. It also provides some fiber-compatible synchronization primitives.</p>

<h2 id="basic-example">Basic example <a href="#basic-example" class="headerLink">#</a></h2>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">...</span>
<span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="EventBase">EventBase</span> <span class="no">evb</span><span class="o">;</span>
<span class="no">auto</span><span class="o">&amp;</span> <span class="no">fiberManager</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="getFiberManager">getFiberManager</span><span class="o">(</span><span class="no">evb</span><span class="o">);</span>
<span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Baton">Baton</span> <span class="no">baton</span><span class="o">;</span>

<span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="cout">cout</span> <span class="o">&lt;&lt;</span> <span class="s2">&quot;Task 1: start&quot;</span> <span class="o">&lt;&lt;</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="endl">endl</span><span class="o">;</span>
  <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="wait">wait</span><span class="o">();</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="cout">cout</span> <span class="o">&lt;&lt;</span> <span class="s2">&quot;Task 1: after baton.wait()&quot;</span> <span class="o">&lt;&lt;</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="endl">endl</span><span class="o">;</span> 
<span class="o">&#125;);</span>

<span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="cout">cout</span> <span class="o">&lt;&lt;</span> <span class="s2">&quot;Task 2: start&quot;</span> <span class="o">&lt;&lt;</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="endl">endl</span><span class="o">;</span>
  <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="post">post</span><span class="o">();</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="cout">cout</span> <span class="o">&lt;&lt;</span> <span class="s2">&quot;Task 2: after baton.post()&quot;</span> <span class="o">&lt;&lt;</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="endl">endl</span><span class="o">;</span> 
<span class="o">&#125;);</span>

<span class="no">evb</span><span class="o">.</span><span class="nf" data-symbol-name="loop">loop</span><span class="o">();</span>
<span class="o">...</span></pre></div>

<p>This would print:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">Task</span> <span class="mi">1</span><span class="o">:</span> <span class="no">start</span>
<span class="no">Task</span> <span class="mi">2</span><span class="o">:</span> <span class="no">start</span>
<span class="no">Task</span> <span class="mi">2</span><span class="o">:</span> <span class="no">after</span> <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="post">post</span><span class="o">()</span>
<span class="no">Task</span> <span class="mi">1</span><span class="o">:</span> <span class="no">after</span> <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="wait">wait</span><span class="o">()</span></pre></div>

<p>It&#039;s very important to note that both tasks in this example were executed on the same system thread. Task 1 was suspended by <tt>baton.wait()</tt> call. Task 2 then started and called <tt>baton.post()</tt>, resuming Task 1.</p>

<h2 id="features">Features <a href="#features" class="headerLink">#</a></h2>

<ul>
<li>Fibers creation and scheduling is performed by FiberManager</li>
<li>Integration with any event-management system (e.g. EventBase)</li>
<li>Low-level synchronization primitives (Baton) as well as higher-level primitives built on top of them (await, collectN, mutexes, ... )</li>
<li>Synchronization primitives have timeout support</li>
<li>Built-in mechanisms for fiber stack-overflow detection</li>
<li>Optional fiber-local data (i.e. equivalent of thread locals)</li>
</ul>

<h2 id="non-features">Non-features <a href="#non-features" class="headerLink">#</a></h2>

<ul>
<li>Individual fibers scheduling can&#039;t be directly controlled by application</li>
<li>FiberManager is not thread-safe (we recommend to keep one FiberManager per thread). Application is responsible for managing its own threads and distributing load between them</li>
<li>We don&#039;t support automatic stack size adjustments. Each fiber has a stack of fixed size.</li>
</ul>

<h2 id="why-would-i-not-want-to">Why would I not want to use fibers ? <a href="#why-would-i-not-want-to" class="headerLink">#</a></h2>

<p>The only real downside to using fibers is the need to keep a pre-allocated stack for every fiber being run. That either makes you application use a lot of memory (if you have many concurrent tasks and each of them uses large stacks) or creates a risk of stack overflow bugs (if you try to reduce the stack size).</p>

<p>We believe these problems can be addressed (and we provide some tooling for that), as fibers library is used in many critical applications at Facebook (mcrouter, TAO, Service Router). However, it&#039;s important to be aware of the risks and be ready to deal with stack issues if you decide to use fibers library in your application.</p>

<h2 id="what-are-the-alternative">What are the alternatives ? <a href="#what-are-the-alternative" class="headerLink">#</a></h2>

<ul>
<li><a href="https://github.com/facebook/folly/blob/master/folly/futures/" target="_blank">Futures</a> library works great for asynchronous high-level application code. Yet code written using fibers library is generally much simpler and much more efficient (you are not paying the penalty of heap allocation).</li>
<li>You can always keep writing your asynchronous code using traditional callback approach. Such code quickly becomes hard to manage and is error-prone. Even though callback approach seems to allow you writing the most efficient code, inefficiency still comes from heap allocations (<tt>std::function</tt>s used for callbacks, context objects to be passed between callbacks etc.)</li>
</ul></section><section class="dex_document"><h1>Quick guide</h1><p class="dex_introduction"></p><p>Let&#039;s take a look at this basic example:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">...</span>
<span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="EventBase">EventBase</span> <span class="no">evb</span><span class="o">;</span>
<span class="no">auto</span><span class="o">&amp;</span> <span class="no">fiberManager</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="getFiberManager">getFiberManager</span><span class="o">(</span><span class="no">evb</span><span class="o">);</span>
<span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Baton">Baton</span> <span class="no">baton</span><span class="o">;</span>

<span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="cout">cout</span> <span class="o">&lt;&lt;</span> <span class="s2">&quot;Task: start&quot;</span> <span class="o">&lt;&lt;</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="endl">endl</span><span class="o">;</span>
  <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="wait">wait</span><span class="o">();</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="cout">cout</span> <span class="o">&lt;&lt;</span> <span class="s2">&quot;Task: after baton.wait()&quot;</span> <span class="o">&lt;&lt;</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="endl">endl</span><span class="o">;</span> 
<span class="o">&#125;);</span>

<span class="no">evb</span><span class="o">.</span><span class="nf" data-symbol-name="loop">loop</span><span class="o">();</span>

<span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="post">post</span><span class="o">();</span>
<span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="cout">cout</span> <span class="o">&lt;&lt;</span> <span class="s2">&quot;Baton posted&quot;</span> <span class="o">&lt;&lt;</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="endl">endl</span><span class="o">;</span>

<span class="no">evb</span><span class="o">.</span><span class="nf" data-symbol-name="loop">loop</span><span class="o">();</span>

<span class="o">...</span></pre></div>

<p>This would print:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">Task</span><span class="o">:</span> <span class="no">start</span>
<span class="no">Baton</span> <span class="no">posted</span>
<span class="no">Task</span><span class="o">:</span> <span class="no">after</span> <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="wait">wait</span><span class="o">()</span></pre></div>

<p>What makes fiber-task different from any other task run on e.g. an <tt>folly::EventBase</tt> is the ability to suspend such task, without blocking the system thread. So how do you suspend a fiber-task ?</p>

<h3 id="fibers-baton">fibers::Baton <a href="#fibers-baton" class="headerLink">#</a></h3>

<p><tt>fibers::Baton</tt> is the core synchronization primitive which is used to suspend a fiber-task and notify when the task may be resumed. <tt>fibers::Baton</tt> supports two basic operations: <tt>wait()</tt> and <tt>post()</tt>. Calling <tt>wait()</tt> on a Baton will suspend current fiber-task until <tt>post()</tt> is called on the same Baton.</p>

<p>Please refer to <a href="https://github.com/facebook/folly/blob/master/folly/fibers/Baton.h" target="_blank">Baton</a> for more detailed documentation.</p>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> <tt>fibers::Baton</tt> is the only native synchronization primitive of folly::fibers library. All other synchronization primitives provided by folly::fibers are built on top of <tt>fibers::Baton</tt>.</div>

<h3 id="integrating-with-other-a">Integrating with other asynchronous APIs (callbacks) <a href="#integrating-with-other-a" class="headerLink">#</a></h3>

<p>Let&#039;s say we have some existing library which provides a classic callback-style asynchronous API.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">void</span> <span class="nf" data-symbol-name="asyncCall">asyncCall</span><span class="o">(</span><span class="no">Request</span> <span class="no">request</span><span class="o">,</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="Function">Function</span><span class="o">&lt;</span><span class="nf" data-symbol-name="void">void</span><span class="o">(</span><span class="no">Response</span><span class="o">)&gt;</span> <span class="no">cb</span><span class="o">);</span></pre></div>

<p>If we use folly::fibers we can just make an async call from a fiber-task and wait until callback is run:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="no">Response</span> <span class="no">response</span><span class="o">;</span>
  <span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-context="fibers" data-symbol-name="Baton">Baton</span> <span class="no">baton</span><span class="o">;</span>
  
  <span class="nf" data-symbol-name="asyncCall">asyncCall</span><span class="o">(</span><span class="no">request</span><span class="o">,</span> <span class="o">[&amp;](</span><span class="no">Response</span> <span class="no">r</span><span class="o">)</span> <span class="no">mutable</span> <span class="o">&#123;</span>
     <span class="no">response</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">r</span><span class="o">);</span>
     <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="post">post</span><span class="o">();</span>
  <span class="o">&#125;);</span>
  <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="wait">wait</span><span class="o">();</span>

  <span class="c">// Now response holds response returned by the async call</span>
  <span class="o">...</span>
<span class="o">&#125;</span></pre></div>

<p>Using <tt>fibers::Baton</tt> directly is generally error-prone. To make the task above simpler, folly::fibers provide <tt>fibers::await</tt> function.</p>

<p>With <tt>fibers::await</tt>, the code above transforms into:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="no">auto</span> <span class="no">response</span> <span class="o">=</span> <span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="nf" data-symbol-context="fibers" data-symbol-name="await">await</span><span class="o">([&amp;](</span><span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-context="fibers" data-symbol-name="Promise">Promise</span><span class="o">&lt;</span><span class="no">Response</span><span class="o">&gt;</span> <span class="no">promise</span><span class="o">)</span> <span class="o">&#123;</span>
    <span class="nf" data-symbol-name="asyncCall">asyncCall</span><span class="o">(</span><span class="no">request</span><span class="o">,</span> <span class="o">[</span><span class="no">promise</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">promise</span><span class="o">)](</span><span class="no">Response</span> <span class="no">r</span><span class="o">)</span> <span class="no">mutable</span> <span class="o">&#123;</span>
      <span class="no">promise</span><span class="o">.</span><span class="nf" data-symbol-name="setValue">setValue</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">r</span><span class="o">));</span>
    <span class="o">&#125;);</span>
  <span class="o">&#125;);</span>

  <span class="c">// Now response holds response returned by the async call</span>
  <span class="o">...</span>
<span class="o">&#125;</span></pre></div>

<p>Callback passed to <tt>fibers::await</tt> is executed immediately and then fiber-task is suspended until <tt>fibers::Promise</tt> is fulfilled. When <tt>fibers::Promise</tt> is fulfilled with a value or exception, fiber-task will be resumed and &#039;fibers::await&#039; returns that value (or throws an exception, if exception was used to fulfill the <tt>Promise</tt>).</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="k">try</span> <span class="o">&#123;</span>
    <span class="no">auto</span> <span class="no">response</span> <span class="o">=</span> <span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="nf" data-symbol-context="fibers" data-symbol-name="await">await</span><span class="o">([&amp;](</span><span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-context="fibers" data-symbol-name="Promise">Promise</span><span class="o">&lt;</span><span class="no">Response</span><span class="o">&gt;</span> <span class="no">promise</span><span class="o">)</span> <span class="o">&#123;</span>
      <span class="nf" data-symbol-name="asyncCall">asyncCall</span><span class="o">(</span><span class="no">request</span><span class="o">,</span> <span class="o">[</span><span class="no">promise</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">promise</span><span class="o">)](</span><span class="no">Response</span> <span class="no">r</span><span class="o">)</span> <span class="no">mutable</span> <span class="o">&#123;</span>
        <span class="no">promise</span><span class="o">.</span><span class="nf" data-symbol-name="setException">setException</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="runtime_error">runtime_error</span><span class="o">(</span><span class="s2">&quot;Await will re-throw me&quot;</span><span class="o">));</span>
      <span class="o">&#125;);</span>
    <span class="o">&#125;);</span>
    <span class="nf" data-symbol-name="assert">assert</span><span class="o">(</span><span class="kc">false</span><span class="o">);</span> <span class="c">// We should never get here</span>
  <span class="o">&#125;</span> <span class="k">catch</span> <span class="o">(</span><span class="nc" data-symbol-name="const">const</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-name="exception">exception</span><span class="o">&amp;</span> <span class="no">e</span><span class="o">)</span> <span class="o">&#123;</span>
    <span class="nf" data-symbol-name="assert">assert</span><span class="o">(</span><span class="no">e</span><span class="o">.</span><span class="nf" data-symbol-name="what">what</span><span class="o">()</span> <span class="o">==</span> <span class="s2">&quot;Await will re-throw me&quot;</span><span class="o">);</span>
  <span class="o">&#125;</span>
  <span class="o">...</span>
<span class="o">&#125;</span></pre></div>

<p>If <tt>fibers::Promise</tt> is not fulfilled, <tt>fibers::await</tt> will throw a <tt>std::logic_error</tt>.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="k">try</span> <span class="o">&#123;</span>
    <span class="no">auto</span> <span class="no">response</span> <span class="o">=</span> <span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="nf" data-symbol-context="fibers" data-symbol-name="await">await</span><span class="o">([&amp;](</span><span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-context="fibers" data-symbol-name="Promise">Promise</span><span class="o">&lt;</span><span class="no">Response</span><span class="o">&gt;</span> <span class="no">promise</span><span class="o">)</span> <span class="o">&#123;</span>
      <span class="c">// We forget about the promise</span>
    <span class="o">&#125;);</span>
    <span class="nf" data-symbol-name="assert">assert</span><span class="o">(</span><span class="kc">false</span><span class="o">);</span> <span class="c">// We should never get here</span>
  <span class="o">&#125;</span> <span class="k">catch</span> <span class="o">(</span><span class="nc" data-symbol-name="const">const</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-name="logic_error">logic_error</span><span class="o">&amp;</span> <span class="no">e</span><span class="o">)</span> <span class="o">&#123;</span>
    <span class="o">...</span>
  <span class="o">&#125;</span>
  <span class="o">...</span>
<span class="o">&#125;</span></pre></div>

<p>Please refer to <a href="https://github.com/facebook/folly/blob/master/folly/fibers/Promise.h" target="_blank">await</a> for more detailed documentation.</p>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> most of your code written with folly::fibers, won&#039;t be using <tt>fibers::Baton</tt> or <tt>fibers::await</tt>. These primitives should only be used to integrate with other asynchronous API which are not fibers-compatible.</div>

<h3 id="integrating-with-other-a-1">Integrating with other asynchronous APIs (folly::Future) <a href="#integrating-with-other-a-1" class="headerLink">#</a></h3>

<p>Let&#039;s say we have some existing library which provides a Future-based asynchronous API.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="Future">Future</span><span class="o">&lt;</span><span class="no">Response</span><span class="o">&gt;</span> <span class="nf" data-symbol-name="asyncCallFuture">asyncCallFuture</span><span class="o">(</span><span class="no">Request</span> <span class="no">request</span><span class="o">);</span></pre></div>

<p>The good news are, <tt>folly::Future</tt> is already fibers-compatible. You can simply write:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="no">auto</span> <span class="no">response</span> <span class="o">=</span> <span class="nf" data-symbol-name="asyncCallFuture">asyncCallFuture</span><span class="o">(</span><span class="no">request</span><span class="o">).</span><span class="nf" data-symbol-name="get">get</span><span class="o">();</span>
  
  <span class="c">// Now response holds response returned by the async call</span>
  <span class="o">...</span>
<span class="o">&#125;</span></pre></div>

<p>Calling <tt>get()</tt> on a <tt>folly::Future</tt> object will only suspend the calling fiber-task. It won&#039;t block the system thread, letting it process other tasks.</p>

<h2 id="writing-code-with-folly">Writing code with folly::fibers <a href="#writing-code-with-folly" class="headerLink">#</a></h2>

<h3 id="building-fibers-compatib">Building fibers-compatible API <a href="#building-fibers-compatib" class="headerLink">#</a></h3>

<p>Following the explanations above we may wrap an existing asynchronous API in a function:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">Response</span> <span class="nf" data-symbol-name="fiberCall">fiberCall</span><span class="o">(</span><span class="no">Request</span> <span class="no">request</span><span class="o">)</span> <span class="o">&#123;</span>
  <span class="k">return</span> <span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="nf" data-symbol-context="fibers" data-symbol-name="await">await</span><span class="o">([&amp;](</span><span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-context="fibers" data-symbol-name="Promise">Promise</span><span class="o">&lt;</span><span class="no">Response</span><span class="o">&gt;</span> <span class="no">promise</span><span class="o">)</span> <span class="o">&#123;</span>
    <span class="nf" data-symbol-name="asyncCall">asyncCall</span><span class="o">(</span><span class="no">request</span><span class="o">,</span> <span class="o">[</span><span class="no">promise</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">promise</span><span class="o">)](</span><span class="no">Response</span> <span class="no">r</span><span class="o">)</span> <span class="no">mutable</span> <span class="o">&#123;</span>
      <span class="no">promise</span><span class="o">.</span><span class="nf" data-symbol-name="setValue">setValue</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">r</span><span class="o">));</span>
    <span class="o">&#125;);</span>
  <span class="o">&#125;);</span>
<span class="o">&#125;</span></pre></div>

<p>We can then call it from a fiber-task:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="no">auto</span> <span class="no">response</span> <span class="o">=</span> <span class="nf" data-symbol-name="fiberCall">fiberCall</span><span class="o">(</span><span class="no">request</span><span class="o">);</span>
  <span class="o">...</span>
<span class="o">&#125;);</span></pre></div>

<p>But what happens if we just call <tt>fiberCall</tt> not from within a fiber-task, but directly from a system thread ? Here another important feature of <tt>fibers::Baton</tt> (and thus all other folly::fibers synchronization primitives built on top of it) comes into play. Calling <tt>wait()</tt> on a <tt>fibers::Baton</tt> within a system thread context just blocks the thread until <tt>post()</tt> is called on the same <tt>folly::Baton</tt>.</p>

<p>What this means is that you no longer need to write separate code for synchronous and asynchronous APIs. If you use only folly::fibers synchronization primitives for all blocking calls inside of your synchronous function, it automatically becomes asynchronous when run inside a fiber-task.</p>

<h3 id="passing-by-reference">Passing by reference <a href="#passing-by-reference" class="headerLink">#</a></h3>

<p>Classic asynchronous APIs (same applies to folly::Future-based APIs) generally rely on copying/moving-in input arguments and often require you to copy/move in some context variables into the callback. E.g.:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">...</span>
<span class="no">Context</span> <span class="no">context</span><span class="o">;</span>
 
<span class="nf" data-symbol-name="asyncCall">asyncCall</span><span class="o">(</span><span class="no">request</span><span class="o">,</span> <span class="o">[</span><span class="no">request</span><span class="o">,</span> <span class="no">context</span><span class="o">](</span><span class="no">Response</span> <span class="no">response</span><span class="o">)</span> <span class="no">mutable</span> <span class="o">&#123;</span>
  <span class="nf" data-symbol-name="doSomething">doSomething</span><span class="o">(</span><span class="no">request</span><span class="o">,</span> <span class="no">response</span><span class="o">,</span> <span class="no">context</span><span class="o">);</span>
<span class="o">&#125;);</span>
<span class="o">...</span></pre></div>

<p>Fibers-compatible APIs look more like synchronous APIs, so you can actually pass input arguments by reference and you don&#039;t have to think about passing context at all. E.g.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="no">Context</span> <span class="no">context</span><span class="o">;</span>

  <span class="no">auto</span> <span class="no">response</span> <span class="o">=</span> <span class="nf" data-symbol-name="fiberCall">fiberCall</span><span class="o">(</span><span class="no">request</span><span class="o">);</span>
 
  <span class="nf" data-symbol-name="doSomething">doSomething</span><span class="o">(</span><span class="no">request</span><span class="o">,</span> <span class="no">response</span><span class="o">,</span> <span class="no">context</span><span class="o">);</span>
  <span class="o">...</span>
<span class="o">&#125;);</span></pre></div>

<p>Same logic applies to <tt>fibers::await</tt>. Since <tt>fibers::await</tt> call blocks until promise is fulfilled, it&#039;s safe to pass everything by reference.</p>

<h3 id="limited-stack-space">Limited stack space <a href="#limited-stack-space" class="headerLink">#</a></h3>

<p>So should you just run all the code inside a fiber-task ? No exactly.</p>

<p>Similarly to system threads, every fiber-task has some stack space assigned to it. Stack usage goes up with the number of nested function calls and objects allocated on the stack. folly::fibers implementation only supports fiber-tasks with fixed stack size. If you want to have many fiber-tasks running concurrently - you need to reduce the amount of stack assigned to each fiber-task, otherwise you may run out of memory.</p>

<div class="remarkup-important"><span class="remarkup-note-word">IMPORTANT:</span> If a fiber-task runs out of stack space (e.g. calls a function which does a lot of stack allocations) you program will fail.</div>

<p>However if you know that some function never suspends a fiber-task, you can use <tt>fibers::runInMainContext</tt> to safely call it from a fiber-task, without any risk of running out of stack space of the fiber-task.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">Result</span> <span class="nf" data-symbol-name="useALotOfStack">useALotOfStack</span><span class="o">()</span> <span class="o">&#123;</span>
  <span class="no">char</span> <span class="no">buffer</span><span class="o">[</span><span class="mi">1024</span><span class="o">*</span><span class="mi">1024</span><span class="o">];</span>
  <span class="o">...</span>
<span class="o">&#125;</span>

<span class="o">...</span>
<span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="no">auto</span> <span class="no">result</span> <span class="o">=</span> <span class="nc" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="nf" data-symbol-context="fibers" data-symbol-name="runInMainContext">runInMainContext</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
    <span class="k">return</span> <span class="nf" data-symbol-name="useALotOfStack">useALotOfStack</span><span class="o">();</span>
  <span class="o">&#125;);</span>
  <span class="o">...</span>
<span class="o">&#125;);</span>
<span class="o">...</span></pre></div>

<p><tt>fibers::runInMainContext</tt> will switch to the stack of the system thread (main context), run the functor passed to it and then switch back to the fiber-task stack.</p>

<div class="remarkup-important"><span class="remarkup-note-word">IMPORTANT:</span> Make sure you don&#039;t do any blocking calls on main context though. It will suspend the whole system thread, not just the fiber-task which was running.</div>

<p>Remember that it&#039;s fine to use <tt>fibers::runInMainContext</tt> in general purpose functions (those which may be called both from fiber-task and non from fiber-task). When called in non-fiber-task context <tt>fibers::runInMainContext</tt> would simply execute passed functor right away.</p>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> Besides <tt>fibers::runInMainContext</tt> some other functions in folly::fibers are also executing some of the passed functors on the main context. E.g. functor passes to <tt>fibers::await</tt> is executed on main context, finally-functor passed to <tt>FiberManager::addTaskFinally</tt> is also executed on main context etc. Relying on this can help you avoid extra <tt>fibers::runInMainContext</tt> calls (and avoid extra context switches).</div>

<h3 id="using-locks">Using locks <a href="#using-locks" class="headerLink">#</a></h3>

<p>Consider the following example:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">...</span>
<span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="EventBase">EventBase</span> <span class="no">evb</span><span class="o">;</span>
<span class="no">auto</span><span class="o">&amp;</span> <span class="no">fiberManager</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="getFiberManager">getFiberManager</span><span class="o">(</span><span class="no">evb</span><span class="o">);</span>
<span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="mutex">mutex</span> <span class="no">lock</span><span class="o">;</span>
<span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Baton">Baton</span> <span class="no">baton</span><span class="o">;</span>

<span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="lock_guard">lock_guard</span><span class="o">&lt;</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="mutex">mutex</span><span class="o">&gt;</span> <span class="nf" data-symbol-name="lg">lg</span><span class="o">(</span><span class="no">lock</span><span class="o">);</span>
  <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="wait">wait</span><span class="o">();</span>
<span class="o">&#125;);</span>

<span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
  <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="lock_guard">lock_guard</span><span class="o">&lt;</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="mutex">mutex</span><span class="o">&gt;</span> <span class="nf" data-symbol-name="lg">lg</span><span class="o">(</span><span class="no">lock</span><span class="o">);</span>
<span class="o">&#125;);</span>

<span class="no">evb</span><span class="o">.</span><span class="nf" data-symbol-name="loop">loop</span><span class="o">();</span>
<span class="c">// We won&#039;t get here :(</span>
<span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="post">post</span><span class="o">();</span>
<span class="o">...</span></pre></div>

<p>First fiber-task will grab a lock and then suspend waiting on a <tt>fibers::Baton</tt>. Then second fiber-task will be run and it will try to grab a lock. Unlike system threads, fiber-task can be only suspended explicitly, so the whole system thread will be blocked waiting on the lock, and we end up with a dead-lock.</p>

<p>There&#039;re generally two ways we can solve this problem. Ideally we would re-design the program to never not hold any locks when fiber-task is suspended. However if we are absolutely sure we need that lock - folly::fibers library provides some fiber-task-aware lock implementations (e.g. 
<a href="https://github.com/facebook/folly/blob/master/folly/fibers/TimedMutex.h" target="_blank">TimedMutex</a>).</p></section><section class="dex_document"><h1>APIs</h1><p class="dex_introduction"></p><h2 id="fibers-baton">fibers::Baton <a href="#fibers-baton" class="headerLink">#</a></h2>

<p>All of the features of folly::fibers library are actually built on top a single synchronization primitive called Baton. <tt>fibers::Baton</tt> is a fiber-specific version of <tt>folly::Baton</tt>. It only  supports two basic operations: <tt>wait()</tt> and <tt>post()</tt>. Whenever <tt>wait()</tt> is called on the Baton, the current thread or fiber-task is suspended, until <tt>post()</tt> is called on the same Baton. <tt>wait()</tt> does not suspend the thread or fiber-task if <tt>post()</tt> was already called on the Baton. Please refer to <a href="https://github.com/facebook/folly/blob/master/folly/fibers/Baton.h" target="_blank">Baton</a> for more detailed documentation.</p>

<p>Baton is thread-safe, so <tt>wait()</tt> and <tt>post()</tt> can be (and should be :) ) called from different threads or fiber-tasks.</p>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> Because Baton transparently works both on threads and fiber-tasks, any synchronization primitive built using it would have the same property. This means that any library with a synchronous API, which uses only <tt>fibers::Baton</tt> for synchronization, becomes asynchronous when used in fiber context.</div>

<h3 id="timed-wait">timed_wait() <a href="#timed-wait" class="headerLink">#</a></h3>

<p><tt>fibers::Baton</tt> also supports wait with timeout.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([=]()</span> <span class="o">&#123;</span>
  <span class="no">auto</span> <span class="no">baton</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="make_shared">make_shared</span><span class="o">&lt;</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Baton">Baton</span><span class="o">&gt;();</span>
  <span class="no">auto</span> <span class="no">result</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="make_shared">make_shared</span><span class="o">&lt;</span><span class="no">Result</span><span class="o">&gt;();</span>

  <span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([=]()</span> <span class="o">&#123;</span>
    <span class="o">*</span><span class="no">result</span> <span class="o">=</span> <span class="nf" data-symbol-name="sendRequest">sendRequest</span><span class="o">(...);</span>
    <span class="no">baton</span><span class="o">-&gt;</span><span class="na" data-symbol-name="post">post</span><span class="o">();</span>
  <span class="o">&#125;);</span>

  <span class="no">bool</span> <span class="no">success</span> <span class="o">=</span> <span class="no">baton</span><span class="o">.</span><span class="nf" data-symbol-name="timed_wait">timed_wait</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="chrono">chrono</span><span class="o">::</span><span class="na" data-symbol-name="milliseconds">milliseconds</span><span class="o">&#123;</span><span class="mi">10</span><span class="o">&#125;);</span>
  <span class="k">if</span> <span class="o">(</span><span class="no">success</span><span class="o">)</span> <span class="o">&#123;</span>
    <span class="c">// request successful</span>
    <span class="o">...</span>
  <span class="o">&#125;</span> <span class="k">else</span> <span class="o">&#123;</span>
    <span class="c">// handle timeout</span>
    <span class="o">...</span>
  <span class="o">&#125;</span>
<span class="o">&#125;);</span></pre></div>

<div class="remarkup-important"><span class="remarkup-note-word">IMPORTANT:</span> unlike <tt>wait()</tt> when using <tt>timed_wait()</tt> API it&#039;s generally not safe to pass <tt>fibers::Baton</tt> by reference. You have to make sure that task, which fulfills the Baton is either cancelled in case of timeout, or have shared ownership for the Baton.</div>

<h2 id="task-creation">Task creation <a href="#task-creation" class="headerLink">#</a></h2>

<h3 id="addtask-addtaskremote">addTask() / addTaskRemote() <a href="#addtask-addtaskremote" class="headerLink">#</a></h3>

<p>As you could see from previous examples, the easiest way to create a new fiber-task is to call <tt>addTask()</tt>:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
<span class="o">&#125;);</span></pre></div>

<p>It is important to remember that <tt>addTask()</tt> is not thread-safe. I.e. it can only be safely called from the the thread, which is running the <tt>folly::FiberManager</tt> loop.</p>

<p>If you need to create a fiber-task from a different thread, you have to use <tt>addTaskRemote()</tt>:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="EventBase">EventBase</span> <span class="no">evb</span><span class="o">;</span>
<span class="no">auto</span><span class="o">&amp;</span> <span class="no">fiberManager</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="getFiberManager">getFiberManager</span><span class="o">(</span><span class="no">evb</span><span class="o">);</span>

<span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="thread">thread</span> <span class="nf" data-symbol-name="t">t</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
  <span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTaskRemote">addTaskRemote</span><span class="o">([]()</span> <span class="o">&#123;</span>
    <span class="o">...</span>
  <span class="o">&#125;);</span>
<span class="o">&#125;);</span>

<span class="no">evb</span><span class="o">.</span><span class="nf" data-symbol-name="loopForever">loopForever</span><span class="o">();</span></pre></div>

<h3 id="addtaskfinally">addTaskFinally() <a href="#addtaskfinally" class="headerLink">#</a></h3>

<p><tt>addTaskFinally()</tt> is useful when you need to run some code on the main context in the end of a fiber-task.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTaskFinally">addTaskFinally</span><span class="o">(</span>
  <span class="o">[=]()</span> <span class="o">&#123;</span>
    <span class="o">...</span>
    <span class="k">return</span> <span class="no">result</span><span class="o">;</span>
  <span class="o">&#125;,</span>
  <span class="o">[=](</span><span class="no">Result</span><span class="o">&amp;&amp;</span> <span class="no">result</span><span class="o">)</span> <span class="o">&#123;</span>
    <span class="nf" data-symbol-name="callUserCallbacks">callUserCallbacks</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">result</span><span class="o">),</span> <span class="o">...)</span>
  <span class="o">&#125;</span>
<span class="o">);</span></pre></div>

<p>Of course you could achieve the same by calling <tt>fibers::runInMainContext()</tt>, but <tt>addTaskFinally()</tt> reduces the number of fiber context switches:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([=]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
  <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="runInMainContext">runInMainContext</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
    <span class="c">// Switched to main context</span>
    <span class="nf" data-symbol-name="callUserCallbacks">callUserCallbacks</span><span class="o">(</span><span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="nf" data-symbol-context="std" data-symbol-name="move">move</span><span class="o">(</span><span class="no">result</span><span class="o">),</span> <span class="o">...)</span>
  <span class="o">&#125;</span>
  <span class="c">// Switched back to fiber context</span>

  <span class="c">// On fiber context we realize there&#039;s no more work to be done.</span>
  <span class="c">// Fiber-task is complete, switching back to main context.</span>
<span class="o">&#125;);</span></pre></div>

<p></p>

<h3 id="addtaskfuture-addtaskrem">addTaskFuture() / addTaskRemoteFuture() <a href="#addtaskfuture-addtaskrem" class="headerLink">#</a></h3>

<p><tt>addTask()</tt> and <tt>addTaskRemote()</tt> are creating detached fiber-tasks. If you need to know when fiber-task is complete and/or have some return value for it -  <tt>addTaskFuture()</tt> / <tt>addTaskRemoteFuture()</tt> can be used.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="EventBase">EventBase</span> <span class="no">evb</span><span class="o">;</span>
<span class="no">auto</span><span class="o">&amp;</span> <span class="no">fiberManager</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="getFiberManager">getFiberManager</span><span class="o">(</span><span class="no">evb</span><span class="o">);</span>

<span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="thread">thread</span> <span class="nf" data-symbol-name="t">t</span><span class="o">([&amp;]()</span> <span class="o">&#123;</span>
  <span class="no">auto</span> <span class="no">future1</span> <span class="o">=</span> <span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTaskRemoteFuture">addTaskRemoteFuture</span><span class="o">([]()</span> <span class="o">&#123;</span>
    <span class="o">...</span>
  <span class="o">&#125;);</span>
  <span class="no">auto</span> <span class="no">future2</span> <span class="o">=</span> <span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTaskRemoteFuture">addTaskRemoteFuture</span><span class="o">([]()</span> <span class="o">&#123;</span>
    <span class="o">...</span>
  <span class="o">&#125;);</span> 

  <span class="no">auto</span> <span class="no">result1</span> <span class="o">=</span> <span class="no">future1</span><span class="o">.</span><span class="nf" data-symbol-name="get">get</span><span class="o">();</span>
  <span class="no">auto</span> <span class="no">result2</span> <span class="o">=</span> <span class="no">future2</span><span class="o">.</span><span class="nf" data-symbol-name="get">get</span><span class="o">();</span>
  <span class="o">...</span>
<span class="o">&#125;);</span>

<span class="no">evb</span><span class="o">.</span><span class="nf" data-symbol-name="loopForever">loopForever</span><span class="o">();</span></pre></div>

<h2 id="other-synchronization-pr">Other synchronization primitives <a href="#other-synchronization-pr" class="headerLink">#</a></h2>

<p>All the listed synchronization primitives are built using <tt>fiber::Baton</tt>. Please check their source code for detailed documentation.</p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/Promise.h" target="_blank">await</a></p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/WhenN.h" target="_blank">collectN</a></p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/WhenN.h" target="_blank">collectAll</a></p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/WhenN.h" target="_blank">collectAny</a></p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/ForEach.h" target="_blank">forEach</a></p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/AddTasks.h" target="_blank">addTasks</a></p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/TimedMutex.h" target="_blank">TimedMutex</a></p>

<p><a href="https://github.com/facebook/folly/blob/master/folly/fibers/TimedMutex.h" target="_blank">TimedRWMutex</a></p></section><section class="dex_document"><h1>Fiber stacks</h1><p class="dex_introduction"></p><p>Similarly to system threads, every fiber-task has some stack space assigned to it. Stack usage goes up with the number of nested function calls and objects allocated on the stack. folly::fibers implementation only supports fiber-tasks with fixed stack size. If you want to have many fiber-tasks running concurrently - you need to reduce the amount of stack assigned to each fiber-task, otherwise you may run out of memory.</p>

<h3 id="selecting-stack-size">Selecting stack size <a href="#selecting-stack-size" class="headerLink">#</a></h3>

<p>Stack size used for every fiber-task is part of FiberManager configuration. But how do you pick the right stack size ?</p>

<p>First of all you need to figure out the maximum number of concurrent fiber-tasks your application may have. E.g. if you are writing a Thrift-service you will probably have a single fiber-task for every request in-fly (but remember that e.g. <tt>fibers::collectAll</tt> and some other synchronization primitives may create extra fiber-tasks). It&#039;s very important to get that number first, because if you will at most need 100 concurrent fiber-tasks, even 1MB stacks will result in at most 100MB used for fiber stacks. On the other hand if you need to have 100,000 concurrent fiber-tasks, even 16KB stacks will result in 1.6GB peak memory usage just for fiber stacks.</p>

<p>folly::fibers also supports recording stack usage (it can be enabled via <tt>recordStackEvery</tt> option of <tt>FiberManager</tt>). When enabled, the stack of each fiber-task will be filled with magic values. Later linear search can be performed to find the boundary of unused stack space.</p>

<h3 id="stack-overflow-detection">Stack overflow detection <a href="#stack-overflow-detection" class="headerLink">#</a></h3>

<p>By default every fiber-task stack is allocated with a special guard page next to it (this can be controlled via <tt>useGuardPages</tt> option of <tt>FiberManager</tt>). If a stack overflow happens - this guard page will be accessed, which will result in immediate segmentation fault.</p>

<div class="remarkup-important"><span class="remarkup-note-word">IMPORTANT:</span> disabling guard page protection may result in unnoticed stack overflows. Those will inevitably cause memory corruptions, which are usually very hard to debug.</div></section><section class="dex_document"><h1>Event Loops</h1><p class="dex_introduction"></p><p>folly::fibers library doesn&#039;t implement it&#039;s own event system. Instead it allows <tt>fibers::FiberManager</tt> to work with any other event system by implementing <tt>fibers::LoopController</tt> interface.</p>

<h2 id="folly-eventbase-integrat">folly::EventBase integration <a href="#folly-eventbase-integrat" class="headerLink">#</a></h2>

<p>The easiest way to create a <tt>fibers::FiberManager</tt> attached to a <tt>folly::EventBase</tt> is by using <tt>fibers::getFiberManager</tt> function:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="EventBase">EventBase</span> <span class="no">evb</span><span class="o">;</span>
<span class="no">auto</span><span class="o">&amp;</span> <span class="no">fiberManager</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="getFiberManager">getFiberManager</span><span class="o">(</span><span class="no">evb</span><span class="o">);</span>

<span class="no">fiberManager</span><span class="o">.</span><span class="nf" data-symbol-name="addTask">addTask</span><span class="o">([]()</span> <span class="o">&#123;</span>
  <span class="o">...</span>
<span class="o">&#125;);</span>

<span class="no">evb</span><span class="o">.</span><span class="nf" data-symbol-name="loop">loop</span><span class="o">();</span></pre></div>

<p>Such <tt>fibers::FiberManager</tt> will be automatically destroyed, when <tt>folly::EventBase</tt> is destroyed.</p>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> folly::fibers doesn&#039;t support killing fiber-tasks in-flight (for similar reasons you can&#039;t kill a thread). If <tt>fibers::FiberManager</tt> has any outstanding fiber-tasks, when <tt>folly::EventBase</tt> is being destroyed, it will keep running the event loop until all those tasks are finished.</div></section><section class="dex_document"><h1>GDB integration</h1><p class="dex_introduction"></p><p>folly::fibers provides some GDB extensions which can be very useful for debugging. To load them simply run the following in GDB console:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">fbload</span> <span class="no">folly_fibers</span></pre></div>

<h3 id="find-all-fibermanagers">Find all FiberManagers <a href="#find-all-fibermanagers" class="headerLink">#</a></h3>

<p>You can use <tt>$get_fiber_manager_map_evb()</tt> and <tt>$get_fiber_manager_map_vevb()</tt> to get <tt>folly::EventBase</tt> =&gt; <tt>fibers::FiberManager</tt> and <tt>folly::VirtualEventBase</tt> =&gt; <tt>fibers::FiberManager</tt> mappings respectively:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">fbload</span> <span class="nf" data-symbol-name="stl">stl</span>
<span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">p</span> <span class="nv">$get_fiber_manager_map_evb</span><span class="o">()</span>
$<span class="mi">2</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="unordered_map">unordered_map</span> <span class="no">with</span> <span class="mi">2</span> <span class="no">elements</span> <span class="o">=</span> <span class="o">&#123;</span>
  <span class="o">[</span><span class="mh">0x7fffffffda80</span><span class="o">]</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="unique_ptr">unique_ptr</span><span class="o">&lt;</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="FiberManager">FiberManager</span><span class="o">&gt;</span> <span class="no">containing</span> <span class="mh">0x7ffff5c22a00</span><span class="o">,</span>
  <span class="o">[</span><span class="mh">0x7fffffffd850</span><span class="o">]</span> <span class="o">=</span> <span class="nc" data-symbol-name="std">std</span><span class="o">::</span><span class="na" data-symbol-context="std" data-symbol-name="unique_ptr">unique_ptr</span><span class="o">&lt;</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="FiberManager">FiberManager</span><span class="o">&gt;</span> <span class="no">containing</span> <span class="mh">0x7ffff5c22800</span>
<span class="o">&#125;</span></pre></div>

<p>This will only list <tt>fibers::FiberManager</tt>s created using <tt>fibers::getFiberManager()</tt> function.</p>

<h3 id="printing-a-fibermanager">Printing a FiberManager <a href="#printing-a-fibermanager" class="headerLink">#</a></h3>

<p>Given a pointer to a <tt>fibers::FiberManager</tt> you can get a list of all its active fibers:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">p</span> <span class="o">*((</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="FiberManager">FiberManager</span><span class="o">*)</span><span class="mh">0x7ffff5c22800</span><span class="o">)</span>
$<span class="mi">4</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="FiberManager">FiberManager</span> <span class="o">=</span> <span class="o">&#123;</span>
  <span class="mh">0x7ffff5d23380</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Fiber">Fiber</span> <span class="o">=</span> <span class="o">&#123;</span>
    <span class="no">state</span> <span class="o">=</span> <span class="no">Awaiting</span> <span class="no">immediate</span><span class="o">,</span>
    <span class="no">backtrace</span> <span class="no">available</span> <span class="o">=</span> <span class="kc">true</span>
  <span class="o">&#125;</span>
<span class="o">&#125;</span></pre></div>

<p><tt>fiber-print-limit</tt> command can be used to change the maximum number of fibers printed for a <tt>fibers::FiberManager</tt> (default value is 100).</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">fiber</span><span class="o">-</span><span class="no">print</span><span class="o">-</span><span class="no">limit</span> <span class="mi">10</span>
<span class="k">New</span> <span class="nc" data-symbol-name="fiber">fiber</span> <span class="no">limit</span> <span class="k">for</span> <span class="no">FiberManager</span> <span class="no">printer</span> <span class="no">set</span> <span class="no">to</span> <span class="mi">10</span></pre></div>

<h3 id="printing-a-fiber-task">Printing a fiber-task <a href="#printing-a-fiber-task" class="headerLink">#</a></h3>

<p>Given a pointer to a <tt>fibers::Fiber</tt>, which is running some fiber-task, you can get its current state:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">p</span> <span class="o">*((</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Fiber">Fiber</span><span class="o">*)</span><span class="mh">0x7ffff5d23380</span><span class="o">)</span>
$<span class="mi">5</span> <span class="o">=</span> <span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Fiber">Fiber</span> <span class="o">=</span> <span class="o">&#123;</span>
  <span class="no">state</span> <span class="o">=</span> <span class="no">Awaiting</span> <span class="no">immediate</span><span class="o">,</span>
  <span class="no">backtrace</span> <span class="no">available</span> <span class="o">=</span> <span class="kc">true</span>
<span class="o">&#125;</span></pre></div>

<h3 id="activating-a-fiber-task">Activating a fiber-task <a href="#activating-a-fiber-task" class="headerLink">#</a></h3>

<p>Every <tt>fibers::Fiber</tt>, which is suspended (and so has its backtrace available), can be activated. To activate a fiber-task you can either use <tt>fiber</tt> GDB command, passing a <tt>fibers::Fiber</tt> pointer to it:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">fiber</span> <span class="mh">0x7ffff5d23380</span>
<span class="no">Fiber</span> <span class="mi">140737317581696</span> <span class="no">activated</span><span class="o">.</span> <span class="no">You</span> <span class="no">can</span> <span class="no">call</span> <span class="s1">&#039;bt&#039;</span> <span class="no">now</span><span class="o">.</span></pre></div>

<p>or simply call <tt>activate()</tt> on a <tt>fibers::Fiber</tt> object:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="nf" data-symbol-name="p">p</span> <span class="o">((</span><span class="nc" data-symbol-name="folly">folly</span><span class="o">::</span><span class="na" data-symbol-context="folly" data-symbol-name="fibers">fibers</span><span class="o">::</span><span class="na" data-symbol-name="Fiber">Fiber</span><span class="o">*)</span><span class="mh">0x7ffff5d23380</span><span class="o">)-&gt;</span><span class="na" data-symbol-name="activate">activate</span><span class="o">()</span>
$<span class="mi">6</span> <span class="o">=</span> <span class="s2">&quot;Fiber 0x7ffff5d23380 activated. You can call &#039;bt&#039; now.&quot;</span></pre></div>

<p>Once fiber-task is activated you can explore its stack using <tt>bt</tt> and <tt>frame</tt> commands, just like a regular thread.</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">bt</span>
<span class="c">#1  0x00000000005497e9 in folly::fibers::FiberImpl::deactivate() (this=0x7ffff5d233a0)</span>
    <span class="no">at</span> <span class="no">buck</span><span class="o">-</span><span class="no">out</span><span class="o">/</span><span class="no">dbg</span><span class="o">/</span><span class="no">gen</span><span class="o">/</span><span class="no">folly</span><span class="o">/</span><span class="no">fibers</span><span class="o">/</span><span class="no">fibers_core</span><span class="c">#default,headers/folly/fibers/BoostContextCompatibility.h:105</span>
<span class="c">#2  0x000000000054996d in folly::fibers::FiberManager::deactivateFiber(folly::fibers::Fiber*) (this=0x7ffff5c22800, fiber=0x7ffff5d23380)</span>
    <span class="no">at</span> <span class="no">buck</span><span class="o">-</span><span class="no">out</span><span class="o">/</span><span class="no">dbg</span><span class="o">/</span><span class="no">gen</span><span class="o">/</span><span class="no">folly</span><span class="o">/</span><span class="no">fibers</span><span class="o">/</span><span class="no">fibers_core</span><span class="c">#default,headers/folly/fibers/FiberManagerInternal-inl.h:103</span>
<span class="c">#3  0x0000000000548b91 in folly::fibers::Fiber::&lt;lambda()&gt;::operator()(void) (__closure=0x7ffff59ffb20) at folly/fibers/Fiber.cpp:175</span>
<span class="c">#4  0x0000000000548d78 in folly::fibers::Fiber::preempt(folly::fibers::Fiber::State) (this=0x7ffff5d23380, state=folly::fibers::Fiber::AWAITING_IMMEDIATE)</span>
    <span class="no">at</span> <span class="no">folly</span><span class="o">/</span><span class="no">fibers</span><span class="o">/</span><span class="no">Fiber</span><span class="o">.</span><span class="no">cpp</span><span class="o">:</span><span class="mi">185</span>
<span class="c">#5  0x000000000043bcc6 in folly::fibers::FiberManager::runInMainContext&lt;FiberManager_nestedFiberManagers_Test::TestBody()::&lt;lambda()&gt;::&lt;lambda()&gt; &gt;(&lt;unknown type in /mnt/fio0/andrii/fbsource/fbcode/buck-out/dbg/gen/folly/fibers/test/fibers_test, CU 0x31b, DIE 0x111bdb&gt;) (this=0x7ffff5c22800, func=&lt;unknown type in   /mnt/fio0/andrii/fbsource/fbcode/buck-out/dbg/gen/folly/fibers/test/fibers_test, CU 0x31b, DIE 0x111bdb&gt;)</span>
    <span class="no">at</span> <span class="no">buck</span><span class="o">-</span><span class="no">out</span><span class="o">/</span><span class="no">dbg</span><span class="o">/</span><span class="no">gen</span><span class="o">/</span><span class="no">folly</span><span class="o">/</span><span class="no">fibers</span><span class="o">/</span><span class="no">fibers_core</span><span class="c">#default,headers/folly/fibers/FiberManagerInternal-inl.h:459</span>
<span class="c">#6  0x00000000004300f3 in folly::fibers::runInMainContext&lt;FiberManager_nestedFiberManagers_Test::TestBody()::&lt;lambda()&gt;::&lt;lambda()&gt; &gt;(&lt;unknown type in /mnt/fio0/andrii/fbsource/fbcode/buck-out/dbg/gen/folly/fibers/test/fibers_test, CU 0x31b, DIE 0xf7caa&gt;) (func=&lt;unknown type in   /mnt/fio0/andrii/fbsource/fbcode/buck-out/dbg/gen/folly/fibers/test/fibers_test, CU 0x31b, DIE 0xf7caa&gt;)</span>
    <span class="no">at</span> <span class="no">buck</span><span class="o">-</span><span class="no">out</span><span class="o">/</span><span class="no">dbg</span><span class="o">/</span><span class="no">gen</span><span class="o">/</span><span class="no">folly</span><span class="o">/</span><span class="no">fibers</span><span class="o">/</span><span class="no">fibers_core</span><span class="c">#default,headers/folly/fibers/FiberManagerInternal.h:551</span>
<span class="c">#7  0x0000000000422101 in FiberManager_nestedFiberManagers_Test::&lt;lambda()&gt;::operator()(void) const (__closure=0x7ffff5d23450)</span>
    <span class="no">at</span> <span class="no">folly</span><span class="o">/</span><span class="no">fibers</span><span class="o">/</span><span class="no">test</span><span class="o">/</span><span class="no">FibersTest</span><span class="o">.</span><span class="no">cpp</span><span class="o">:</span><span class="mi">1537</span>
<span class="o">...</span></pre></div>

<p>To deactivate previously activated fiber-task and switch back to the stack of current thread simply use <tt>fiber-deactivate</tt> GDB command:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="o">(</span><span class="no">gdb</span><span class="o">)</span> <span class="no">fiber</span><span class="o">-</span><span class="no">deactivate</span>
<span class="no">Fiber</span> <span class="no">de</span><span class="o">-</span><span class="no">activated</span><span class="o">.</span></pre></div>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> For running (i.e. not suspended) fiber-task, you can simply switch to the system thread which owns it and use regular GDB commands for debugging.</div></section></section><!-- This file is generated from the Dex guide by fbcode/folly/facebook/futures-update-readme.sh. -->
<section class="dex_guide"><h1 class="dex_title">Futures</h1><section class="dex_document"><h1></h1><p class="dex_introduction">Futures is a framework for expressing asynchronous code in C++ using the Promise/Future pattern.</p><h2 id="overview">Overview <a href="#overview" class="headerLink">#</a></h2>

<p>Folly Futures is an async C++ framework inspired by <a href="https://twitter.github.io/finagle/guide/Futures.html" target="_blank">Twitter&#039;s Futures</a> implementation in Scala (see also <a href="https://github.com/twitter/util/blob/master/util-core/src/main/scala/com/twitter/util/Future.scala" target="_blank">Future.scala</a>, <a href="https://github.com/twitter/util/blob/master/util-core/src/main/scala/com/twitter/util/Promise.scala" target="_blank">Promise.scala</a>, and friends), and loosely builds upon the existing but anemic Futures code found in the C++11 standard (<a href="http://en.cppreference.com/w/cpp/thread/future" target="_blank">std::future</a>) and <a href="http://www.boost.org/doc/libs/1_53_0/doc/html/thread/synchronization.html#thread.synchronization.futures" target="_blank">boost::future</a> (especially &gt;= 1.53.0). 
Although inspired by the C++11 std::future interface, it is not a drop-in replacement because some ideas don&#039;t translate well enough to maintain API compatibility.</p>

<p>The primary difference from std::future is that you can attach callbacks to Futures (with <tt>then()</tt>), which enables sequential and parallel composition of Futures for cleaner asynchronous code.</p>

<h2 id="brief-synopsis">Brief Synopsis <a href="#brief-synopsis" class="headerLink">#</a></h2>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="cp">#</span><span class="cp">include</span><span class=""> </span><span class="cpf">&lt;folly/futures/Future.h&gt;</span><span class="cp">
</span><span class="k">using</span><span class=""> </span><span class="k">namespace</span><span class=""> </span><span class="n">folly</span><span class="p">;</span><span class="">
</span><span class="k">using</span><span class=""> </span><span class="k">namespace</span><span class=""> </span><span class="n">std</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="kt">void</span><span class=""> </span><span class="nf">foo</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">x</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// do something with x
</span><span class="">  </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="s">&quot;</span><span class="s">foo(</span><span class="s">&quot;</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">x</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="s">&quot;</span><span class="s">)</span><span class="s">&quot;</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">endl</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="">
</span><span class="">
</span><span class="c1">// ...
</span><span class="">
</span><span class="">  </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="s">&quot;</span><span class="s">making Promise</span><span class="s">&quot;</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">endl</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="n">f</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">foo</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="s">&quot;</span><span class="s">Future chain made</span><span class="s">&quot;</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">endl</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// ... now perhaps in another event callback
</span><span class="">
</span><span class="">  </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="s">&quot;</span><span class="s">fulfilling Promise</span><span class="s">&quot;</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">endl</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="n">p</span><span class="p">.</span><span class="n">setValue</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="s">&quot;</span><span class="s">Promise fulfilled</span><span class="s">&quot;</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">endl</span><span class="p">;</span><span class="">
</span></pre></div>

<p>This would print:</p>

<div class="remarkup-code-block" data-code-lang="php"><pre class="remarkup-code"><span class="no">making</span> <span class="no">Promise</span>
<span class="no">Future</span> <span class="no">chain</span> <span class="no">made</span>
<span class="no">fulfilling</span> <span class="no">Promise</span>
<span class="nf" data-symbol-name="foo">foo</span><span class="o">(</span><span class="mi">42</span><span class="o">)</span>
<span class="no">Promise</span> <span class="no">fulfilled</span></pre></div>

<h3 id="blog-post">Blog Post <a href="#blog-post" class="headerLink">#</a></h3>

<p>In addition to this document, there is <a href="https://code.facebook.com/posts/1661982097368498/futures-for-c-11-at-facebook/" target="_blank">a blog post on code.facebook.com (June 2015)</a>.</p></section><section class="dex_document"><h1>Brief Guide</h1><p class="dex_introduction"></p><p>This brief guide covers the basics. For a more in-depth coverage skip to the appropriate section.</p>

<p>Let&#039;s begin with an example using an imaginary simplified Memcache client interface:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">using</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">string</span><span class="p">;</span><span class="">
</span><span class="k">class</span><span class=""> </span><span class="nc">MemcacheClient</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class=""> </span><span class="k">public</span><span class="o">:</span><span class="">
</span><span class="">  </span><span class="k">struct</span><span class=""> </span><span class="n">GetReply</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="k">enum</span><span class=""> </span><span class="k">class</span><span class=""> </span><span class="nc">Result</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">      </span><span class="n">FOUND</span><span class="p">,</span><span class="">
</span><span class="">      </span><span class="n">NOT_FOUND</span><span class="p">,</span><span class="">
</span><span class="">      </span><span class="n">SERVER_ERROR</span><span class="p">,</span><span class="">
</span><span class="">    </span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="">    </span><span class="n">Result</span><span class=""> </span><span class="n">result</span><span class="p">;</span><span class="">
</span><span class="">    </span><span class="c1">// The value when result is FOUND,
</span><span class="">    </span><span class="c1">// The error message when result is SERVER_ERROR or CLIENT_ERROR
</span><span class="">    </span><span class="c1">// undefined otherwise
</span><span class="">    </span><span class="n">string</span><span class=""> </span><span class="n">value</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="n">GetReply</span><span class=""> </span><span class="nf">get</span><span class="p">(</span><span class="n">string</span><span class=""> </span><span class="n">key</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span></pre></div>

<p>This API is synchronous, i.e. when you call <tt>get()</tt> you have to wait for the result. This is very simple, but unfortunately it is also very easy to write very slow code using synchronous APIs.</p>

<p>Now, consider this traditional asynchronous signature for <tt>get()</tt>:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="kt">int</span><span class=""> </span><span class="nf">get</span><span class="p">(</span><span class="n">string</span><span class=""> </span><span class="n">key</span><span class="p">,</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">function</span><span class="o">&lt;</span><span class="kt">void</span><span class="p">(</span><span class="n">GetReply</span><span class="p">)</span><span class="o">&gt;</span><span class=""> </span><span class="n">callback</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>When you call <tt>get()</tt>, your asynchronous operation begins and when it finishes your callback will be called with the result. Very performant code can be written with an API like this, but for nontrivial applications the code devolves into a special kind of spaghetti code affectionately referred to as &quot;callback hell&quot;.</p>

<p>The Future-based API looks like this:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="n">GetReply</span><span class="o">&gt;</span><span class=""> </span><span class="n">get</span><span class="p">(</span><span class="n">string</span><span class=""> </span><span class="n">key</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>A <tt>Future&lt;GetReply&gt;</tt> is a placeholder for the <tt>GetReply</tt> that we will eventually get. A Future usually starts life out &quot;unfulfilled&quot;, or incomplete, i.e.:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">fut</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="nb">false</span><span class="">
</span><span class="n">fut</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="">  </span><span class="c1">// will throw an exception because the Future is not ready
</span></pre></div>

<p>At some point in the future, the Future will have been fulfilled, and we can access its value.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">fut</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="nb">true</span><span class="">
</span><span class="n">GetReply</span><span class="o">&amp;</span><span class=""> </span><span class="n">reply</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">fut</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Futures support exceptions. If something exceptional happened, your Future may represent an exception instead of a value. In that case:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">fut</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="nb">true</span><span class="">
</span><span class="n">fut</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="c1">// will rethrow the exception
</span></pre></div>

<p>Just what is exceptional depends on the API. In our example we have chosen not to raise exceptions for <tt>SERVER_ERROR</tt>, but represent this explicitly in the <tt>GetReply</tt> object. On the other hand, an astute Memcache veteran would notice that we left <tt>CLIENT_ERROR</tt> out of <tt>GetReply::Result</tt>, and perhaps a <tt>CLIENT_ERROR</tt> would have been raised as an exception, because <tt>CLIENT_ERROR</tt> means there&#039;s a bug in the library and this would be truly exceptional. These decisions are judgement calls by the API designer. The important thing is that exceptional conditions (including and especially spurious exceptions that nobody expects) get captured and can be handled higher up the &quot;stack&quot;.</p>

<p>So far we have described a way to initiate an asynchronous operation via an API that returns a Future, and then sometime later after it is fulfilled, we get its value. This is slightly more useful than a synchronous API, but it&#039;s not yet ideal. There are two more very important pieces to the puzzle.</p>

<p>First, we can aggregate Futures, to define a new Future that completes after some or all of the aggregated Futures complete. Consider two examples: fetching a batch of requests and waiting for all of them, and fetching a group of requests and waiting for only one of them.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">vector</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">GetReply</span><span class="o">&gt;</span><span class="o">&gt;</span><span class=""> </span><span class="n">futs</span><span class="p">;</span><span class="">
</span><span class="k">for</span><span class=""> </span><span class="p">(</span><span class="k">auto</span><span class="o">&amp;</span><span class=""> </span><span class="nl">key</span><span class=""> </span><span class="p">:</span><span class=""> </span><span class="n">keys</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="n">futs</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">mc</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="">
</span><span class="k">auto</span><span class=""> </span><span class="n">all</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">collectAll</span><span class="p">(</span><span class="n">futs</span><span class="p">.</span><span class="n">begin</span><span class="p">(</span><span class="p">)</span><span class="p">,</span><span class=""> </span><span class="n">futs</span><span class="p">.</span><span class="n">end</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">GetReply</span><span class="o">&gt;</span><span class="o">&gt;</span><span class=""> </span><span class="n">futs</span><span class="p">;</span><span class="">
</span><span class="k">for</span><span class=""> </span><span class="p">(</span><span class="k">auto</span><span class="o">&amp;</span><span class=""> </span><span class="nl">key</span><span class=""> </span><span class="p">:</span><span class=""> </span><span class="n">keys</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="n">futs</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">mc</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="">
</span><span class="k">auto</span><span class=""> </span><span class="n">any</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">collectAny</span><span class="p">(</span><span class="n">futs</span><span class="p">.</span><span class="n">begin</span><span class="p">(</span><span class="p">)</span><span class="p">,</span><span class=""> </span><span class="n">futs</span><span class="p">.</span><span class="n">end</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p><tt>all</tt> and <tt>any</tt> are Futures (for the exact type and usage see the header files). They will be complete when all/one of futs are complete, respectively. (There is also <tt>collectN()</tt> for when you need some.)</p>

<p>Second, we can attach callbacks to a Future, and chain them together monadically. An example will clarify:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="n">GetReply</span><span class="o">&gt;</span><span class=""> </span><span class="n">fut1</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">mc</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="s">&quot;</span><span class="s">foo</span><span class="s">&quot;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">string</span><span class="o">&gt;</span><span class=""> </span><span class="n">fut2</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">fut1</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="">
</span><span class="">  </span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">GetReply</span><span class=""> </span><span class="n">reply</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="k">if</span><span class=""> </span><span class="p">(</span><span class="n">reply</span><span class="p">.</span><span class="n">result</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="n">MemcacheClient</span><span class="o">:</span><span class="o">:</span><span class="n">GetReply</span><span class="o">:</span><span class="o">:</span><span class="n">Result</span><span class="o">:</span><span class="o">:</span><span class="n">FOUND</span><span class="p">)</span><span class="">
</span><span class="">      </span><span class="k">return</span><span class=""> </span><span class="n">reply</span><span class="p">.</span><span class="n">value</span><span class="p">;</span><span class="">
</span><span class="">    </span><span class="k">throw</span><span class=""> </span><span class="nf">SomeException</span><span class="p">(</span><span class="s">&quot;</span><span class="s">No value</span><span class="s">&quot;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">Unit</span><span class="o">&gt;</span><span class=""> </span><span class="n">fut3</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">fut2</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">string</span><span class=""> </span><span class="n">str</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">str</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">endl</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">exception</span><span class=""> </span><span class="k">const</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="n">cerr</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">e</span><span class="p">.</span><span class="n">what</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">endl</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>That example is a little contrived but the idea is that you can transform a result from one type to another, potentially in a chain, and unhandled errors propagate. Of course, the intermediate variables are optional.</p>

<p>Using then to add callbacks is idiomatic. It brings all the code into one place, which avoids callback hell.</p>

<p>Up to this point we have skirted around the matter of waiting for Futures. You may never need to wait for a Future, because your code is event-driven and all follow-up action happens in a then-block. But if want to have a batch workflow, where you initiate a batch of asynchronous operations and then wait for them all to finish at a synchronization point, then you will want to wait for a Future. Futures have a blocking method called <tt>wait()</tt> that does exactly that and optionally takes a timeout.</p>

<p>Futures are partially threadsafe. A Promise or Future can migrate between threads as long as there&#039;s a full memory barrier of some sort. <tt>Future::then</tt> and <tt>Promise::setValue</tt> (and all variants that boil down to those two calls) can be called from different threads. <strong>But</strong>, be warned that you might be surprised about which thread your callback executes on. Let&#039;s consider an example.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// Thread A
</span><span class="n">Promise</span><span class="o">&lt;</span><span class="n">Unit</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Thread B
</span><span class="n">f</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">z</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Thread A
</span><span class="n">p</span><span class="p">.</span><span class="n">setValue</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>This is legal and technically threadsafe. However, it is important to realize that you do not know in which thread <tt>x</tt>, <tt>y</tt>, and/or <tt>z</tt> will execute. Maybe they will execute in Thread A when <tt>p.setValue()</tt> is called. Or, maybe they will execute in Thread B when <tt>f.then</tt> is called. Or, maybe <tt>x</tt> will execute in Thread A, but <tt>y</tt> and/or <tt>z</tt> will execute in Thread B. There&#039;s a race between <tt>setValue</tt> and <tt>then</tt>&#x2014;whichever runs last will execute the callback. The only guarantee is that one of them will run the callback.</p>

<p>Naturally, you will want some control over which thread executes callbacks. We have a few mechanisms to help.</p>

<p>The first and most useful is <tt>via</tt>, which passes execution through an <tt>Executor</tt>, which usually has the effect of running the callback in a new thread.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">aFuture</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">via</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y1</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y2</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">via</span><span class="p">(</span><span class="n">e2</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">z</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p><tt>x</tt> will execute in the current thread. <tt>y1</tt> and <tt>y2</tt> will execute in the thread on the other side of <tt>e1</tt>, and <tt>z</tt> will execute in the thread on the other side of <tt>e2</tt>. If after <tt>z</tt> you want to get back to the current thread, you need to get there via an executor. Another way to express this is using an overload of <tt>then</tt> that takes an Executor:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">aFuture</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">e1</span><span class="p">,</span><span class=""> </span><span class="n">y1</span><span class="p">,</span><span class=""> </span><span class="n">y2</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">e2</span><span class="p">,</span><span class=""> </span><span class="n">z</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Either way, there is no ambiguity about which thread will execute <tt>y1</tt>, <tt>y2</tt>, or <tt>z</tt>.</p>

<p>You can still have a race after <tt>via</tt> if you break it into multiple statements, e.g. in this counterexample:</p>

<div class="remarkup-code-block remarkup-counterexample" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">f</span><span class="p">.</span><span class="n">via</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y1</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y2</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="c1">// nothing racy here
</span><span class="n">f2</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y3</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="c1">// racy
</span></pre></div>

<h2 id="you-make-me-promises-pro">You make me Promises, Promises <a href="#you-make-me-promises-pro" class="headerLink">#</a></h2>

<p>If you are wrapping an asynchronous operation, or providing an asynchronous API to users, then you will want to make <tt>Promise</tt>s. Every Future has a corresponding Promise (except Futures that spring into existence already completed, with <tt>makeFuture()</tt>). Promises are simple: you make one, you extract the Future, and you fulfill it with a value or an exception. Example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">f</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="nb">false</span><span class="">
</span><span class="">
</span><span class="n">p</span><span class="p">.</span><span class="n">setValue</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">f</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="nb">true</span><span class="">
</span><span class="n">f</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="mi">42</span><span class="">
</span></pre></div>

<p>and an exception example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">f</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="nb">false</span><span class="">
</span><span class="">
</span><span class="n">p</span><span class="p">.</span><span class="n">setException</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">Fail</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">f</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="nb">true</span><span class="">
</span><span class="n">f</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="c1">// throws the exception
</span></pre></div>

<p>It&#039;s good practice to use setWith which takes a function and automatically captures exceptions, e.g.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="n">p</span><span class="p">.</span><span class="n">setWith</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">try</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// do stuff that may throw
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="mi">42</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class=""> </span><span class="k">catch</span><span class=""> </span><span class="p">(</span><span class="n">MySpecialException</span><span class=""> </span><span class="k">const</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// handle it
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="mi">7</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="">  </span><span class="c1">// Any exceptions that we didn&#039;t catch, will be caught for us
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div></section><section class="dex_document"><h1>More Details</h1><p class="dex_introduction"></p><p>Let&#039;s look at a contrived and synchronous example of Futures.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// ...
</span><span class="n">p</span><span class="p">.</span><span class="n">setValue</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="c1">// or setException(...)
</span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">f</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="c1">// prints 42
</span></pre></div>

<p>First, we create a <a href="https://github.com/facebook/folly/blob/master/folly/futures/Promise.h" target="_blank">Promise</a> object of type <tt>int</tt>. This object is exactly what it sounds like&#x2014;a pledge to provide an <tt>int</tt> (or an exception) at some point in the future.</p>

<p>Next, we extract a <a href="https://github.com/facebook/folly/blob/master/folly/futures/Future.h" target="_blank">Future</a> object from that promise. You can think of futures as handles on promises - they provide a way to access that <tt>int</tt> when the promise is fulfilled.</p>

<p>Later, when the promise is fulfilled via <tt>setValue()</tt> or <tt>setException()</tt>, that <tt>int</tt> is accessible via the future&#039;s <tt>value()</tt> method. That method will throw if the future contains an exception.</p>

<h2 id="setting-callbacks-with-t">Setting callbacks with then() <a href="#setting-callbacks-with-t" class="headerLink">#</a></h2>

<p>Ok, great, so now you&#039;re wondering what these are actually useful for. Let&#039;s consider another way to follow up on the result of a <tt>Future</tt> once its corresponding <tt>Promise</tt> is fulfilled&#x2014;callbacks! Here&#039;s a snippet that is functionally equivalent to the one above:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">f</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">i</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">p</span><span class="p">.</span><span class="n">setValue</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>That <tt>then()</tt> method on futures is the real bread and butter of Futures code. It allows you to provide a callback which will be executed when that <tt>Future</tt> is complete. Note that while we fulfill the promise after setting the callback here, those operations could be swapped. Setting a callback on an already completed future executes the callback immediately.</p>

<p>In this case, the callback takes a value directly. If the Future contained an exception, the callback will be passed over and the exception will be propagated to the resultant Future - more on that in a second. Your callback may also take a <a href="https://github.com/facebook/folly/blob/master/folly/Try.h" target="_blank">Try</a>, which encapsulates either an exception or a value of its templated type.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">f</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="k">const</span><span class="o">&amp;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="n">cout</span><span class=""> </span><span class="o">&lt;</span><span class="o">&lt;</span><span class=""> </span><span class="n">t</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> Do not use Try unless you are actually going to do exception handling in your callback. It is much cleaner and often more performant to take the value directly when you can. If you want to do exception handling, there still might be better options than Try. See <a href="#error-handling">Error Handling</a>.</div>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> When passing a callback to <tt>then</tt>, the future stores a copy of it until the callback has been executed. If, for example, you pass a lambda function that captures a shared pointer, the future will keep the referenced object alive only until the callback has been executed.</div>

<p>The real power of <tt>then()</tt> is that it <em>returns a <tt>Future</tt> of the type that the callback returns</em> and can therefore be chained and nested with ease. Let&#039;s consider another example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="n">string</span><span class="o">&gt;</span><span class=""> </span><span class="n">f2</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">f</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">return</span><span class=""> </span><span class="n">folly</span><span class="o">:</span><span class="o">:</span><span class="n">to</span><span class="o">&lt;</span><span class="n">string</span><span class="o">&gt;</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">f2</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">string</span><span class=""> </span><span class="n">s</span><span class="p">)</span><span class="p">&#123;</span><span class=""> </span><span class="cm">/* ... */</span><span class=""> </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Here, we convert that <tt>int</tt> to a <tt>string</tt> in the callback and return the result, which results in a <tt>Future&lt;string&gt;</tt> that we can set further callbacks on. I&#039;ve created a named variable <tt>f2</tt> to demonstrate types but don&#039;t hesitate to chain futures directly:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">finalFuture</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">getSomeFuture</span><span class="p">(</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>That&#039;s all great, but this code is still synchronous. These constructs truly become useful when you start to chain, nest, and compose asynchronous operations. Let&#039;s say you instead have some <em>remote</em> service that converts your integers to strings for you, and that you also have a client with Future interfaces (i.e. interfaces that return Futures). Now let&#039;s leverage the fact that <tt>then()</tt> also allows you to return <tt>Future&lt;T&gt;</tt> from inside your callbacks as well as just <tt>T</tt>:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="n">string</span><span class="o">&gt;</span><span class=""> </span><span class="n">f2</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">f</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">return</span><span class=""> </span><span class="n">getClient</span><span class="p">(</span><span class="p">)</span><span class="o">-</span><span class="o">&gt;</span><span class="n">future_intToString</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="c1">// returns Future&lt;string&gt;
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">f2</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="n">string</span><span class="o">&gt;</span><span class=""> </span><span class="k">const</span><span class="o">&amp;</span><span class=""> </span><span class="n">s</span><span class="p">)</span><span class="p">&#123;</span><span class=""> </span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class=""> </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>In general, your code will be cleaner if you return <tt>T</tt> from your callbacks and only switch to returning <tt>Future&lt;T&gt;</tt> when necessary (i.e. when there is a nested call to a future-returning function).</p>

<h2 id="futures-promises-and-mov">Futures, Promises, and move semantics <a href="#futures-promises-and-mov" class="headerLink">#</a></h2>

<p><tt>Futures</tt> and <tt>Promises</tt> are movable but non-copyable. This preserves the invariant of a one-to-one mapping between a Promise and a Future and as a side effect encourages performant code. There is a piece of heap-allocated shared state underlying each promise-future pair&#x2014;keep this in mind as a bare minimum performance cost.</p>

<h2 id="synchronously-creating-a">Synchronously creating and completing futures <a href="#synchronously-creating-a" class="headerLink">#</a></h2>

<p>Synchronously entering and exiting the futures paradigm can be useful, especially in tests, so the following utilities are available:</p>

<ul>
<li>Create already-completed futures with <tt>makeFuture&lt;T&gt;()</tt>, which takes a <tt>T&amp;&amp;</tt> (or an exception, more info <a href="#error-handling">here</a>). If you pass <tt>T&amp;&amp;</tt> the type is inferred and you don&#039;t have to specify it.</li>
<li>Extract a future&#039;s <tt>T</tt> value with <tt>Future&lt;T&gt;::get()</tt>. This method is blocking, so make sure that either your future is already completed or that another thread will complete the future while the calling thread blocks. <tt>get()</tt> can also take a timeout&#x2014;see <a href="#timeouts-and-related-features">Timeouts</a>.</li>
<li>Perform a blocking wait on a Future with <tt>Future&lt;T&gt;::wait()</tt>. This is just like <tt>get()</tt> but it instead of extracting the value or throwing the exception, <tt>wait()</tt> returns a new Future with the result of the input Future. Like <tt>get()</tt>, <tt>wait()</tt> can also take a timeout&#x2014;see <a href="#timeouts-and-related-features">Timeouts</a>.</li>
<li><tt>getVia()</tt> and <tt>waitVia()</tt>, which are like <tt>get()</tt> and <tt>wait()</tt> except that they drive some Executor (say, an <tt>EventBase</tt>) until the Future is complete. See <a href="#testing">Testing</a> for more.</li>
</ul>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> <tt>makeFuture()</tt>, <tt>get()</tt>, <tt>wait()</tt>, and friends are especially handy in tests and are documented further in the <a href="#testing">Testing</a> article.</div>

<h2 id="overloads-of-then">Overloads of then() <a href="#overloads-of-then" class="headerLink">#</a></h2>

<p>Above are demonstrations of variants of <tt>then()</tt> whose callbacks</p>

<ul>
<li>return <tt>Future&lt;T&gt;</tt> or <tt>T</tt></li>
<li>take <tt>T const&amp;</tt> or <tt>Try&lt;T&gt; const&amp;</tt> (also possible are <tt>T</tt>, <tt>Try&lt;T&gt;</tt>, <tt>T&amp;&amp;</tt>, and <tt>Try&lt;T&gt;&amp;&amp;</tt>)</li>
</ul>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> The preferred pattern is&#x2014;when possible&#x2014;to use value semantics (take a <tt>T</tt> or <tt>Try&lt;T&gt;</tt>). If your type is expensive to copy or can&#039;t be copied, take a reference. (e.g. <tt>T const&amp;</tt> or <tt>Try&lt;T&gt; const&amp;</tt>) If you need move semantics, an lvalue reference or rvalue reference is the same in this situation. Use whichever you stylistically prefer.</div>

<p>The flexibility doesn&#039;t end there. There are also overloads so that you can bind global functions, member functions, and static member functions to <tt>then()</tt>:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="kt">void</span><span class=""> </span><span class="nf">globalFunction</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="k">const</span><span class="o">&amp;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="k">struct</span><span class=""> </span><span class="n">Foo</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="kt">void</span><span class=""> </span><span class="n">memberMethod</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="k">const</span><span class="o">&amp;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="k">static</span><span class=""> </span><span class="kt">void</span><span class=""> </span><span class="nf">staticMemberMethod</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="k">const</span><span class="o">&amp;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span><span class="n">Foo</span><span class=""> </span><span class="n">foo</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// bind global function
</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">globalFunction</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// bind member method
</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="o">&amp;</span><span class="n">Foo</span><span class="o">:</span><span class="o">:</span><span class="n">memberMethod</span><span class="p">,</span><span class=""> </span><span class="o">&amp;</span><span class="n">foo</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// bind static member method
</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="o">&amp;</span><span class="n">Foo</span><span class="o">:</span><span class="o">:</span><span class="n">staticMemberMethod</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="a-note-on-promises">A note on Promises <a href="#a-note-on-promises" class="headerLink">#</a></h2>

<p>Generally speaking, the majority of your futures-based code will deal with <tt>Futures</tt> alone and not <tt>Promises</tt>&#x2014;calling <tt>Future</tt>-returning interfaces, composing callbacks on them, and eventually returning another <tt>Future</tt>. <tt>Promises</tt> are most useful when you&#039;re wrapping some lower level asynchronous interface so that you can return a <tt>Future</tt>:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="kt">void</span><span class=""> </span><span class="nf">fooOldFashioned</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">arg</span><span class="p">,</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">function</span><span class="o">&lt;</span><span class="kt">int</span><span class="p">(</span><span class="kt">int</span><span class="p">)</span><span class="o">&gt;</span><span class=""> </span><span class="n">callback</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">arg</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">auto</span><span class=""> </span><span class="n">promise</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">make_shared</span><span class="o">&lt;</span><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="n">fooOldFashioned</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span><span class=""> </span><span class="p">[</span><span class="n">promise</span><span class="p">]</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">result</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="n">promise</span><span class="o">-</span><span class="o">&gt;</span><span class="n">setValue</span><span class="p">(</span><span class="n">result</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="k">return</span><span class=""> </span><span class="n">promise</span><span class="o">-</span><span class="o">&gt;</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="">
</span></pre></div>

<p>Though not a hard-and-fast rule, using promises heavily in your code might indicate</p>

<ul>
<li>an opportunity for a cleaner futures-based version</li>
<li>a missing abstraction in our library. See <a href="#compositional-building-blocks">Compositional Building Blocks</a>, <a href="#timeouts-and-related-features">Timeouts</a>, <a href="#interrupts-and-cancellations">Interrupts</a>, etc. Let us know if you think this is the case.</li>
</ul>

<h2 id="sharedpromise">SharedPromise <a href="#sharedpromise" class="headerLink">#</a></h2>

<p><a href="https://github.com/facebook/folly/blob/master/folly/futures/SharedPromise.h" target="_blank">SharedPromise</a> provides the same interface as Promise, but you can extract multiple Futures from it, i.e. you can call <tt>getFuture()</tt> as many times as you&#039;d like. When the SharedPromise is fulfilled, all of the Futures will be called back. Calls to getFuture() after the SharedPromise is fulfilled return a completed Future. If you find yourself constructing collections of Promises and fulfilling them simultaneously with the same value, consider this utility instead. Likewise, if you find yourself in need of setting multiple callbacks on the same Future (which is indefinitely unsupported), consider refactoring to use SharedPromise to &quot;split&quot; the Future.</p></section><section class="dex_document"><h1>Error Handling</h1><p class="dex_introduction">Asynchronous code can't employ try/catch exception handling universally, so Futures provides facilities to make error handling as easy and natural as possible. Here's an overview.</p><h2 id="throwing-exceptions">Throwing Exceptions <a href="#throwing-exceptions" class="headerLink">#</a></h2>

<p>There are several ways to introduce exceptions into your Futures flow. First, <tt>makeFuture&lt;T&gt;()</tt> and <tt>Promise&lt;T&gt;::setException()</tt> can create a failed future from any <tt>std::exception</tt>, from a <tt>folly::exception_wrapper</tt>, or from an <tt>std::exception_ptr</tt> (deprecated):</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">oh no!</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">folly</span><span class="o">:</span><span class="o">:</span><span class="n">make_exception_wrapper</span><span class="o">&lt;</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="o">&gt;</span><span class="p">(</span><span class="s">&quot;</span><span class="s">oh no!</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">current_exception</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">p1</span><span class="p">,</span><span class=""> </span><span class="n">p2</span><span class="p">,</span><span class=""> </span><span class="n">p3</span><span class="p">;</span><span class="">
</span><span class="n">p1</span><span class="p">.</span><span class="n">setException</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">oh no!</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">p2</span><span class="p">.</span><span class="n">setException</span><span class="p">(</span><span class="n">folly</span><span class="o">:</span><span class="o">:</span><span class="n">make_exception_wrapper</span><span class="o">&lt;</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="o">&gt;</span><span class="p">(</span><span class="s">&quot;</span><span class="s">oh no!</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">p3</span><span class="p">.</span><span class="n">setException</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">current_exception</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span></pre></div>

<p>In general, any time you pass a function to a method that returns a <tt>Future</tt> or fulfills a <tt>Promise</tt>, you can rest assured that any thrown exceptions (including non-<tt>std::exceptions</tt>) will be caught and stored. For instance,</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">makeFuture</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">throw</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">ugh</span><span class="s">&quot;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>is perfectly valid code. The exception will be caught and stored in the resultant <tt>Future</tt>.</p>

<p>Methods that behave this way include</p>

<ul>
<li><tt>Future&lt;T&gt;::then()</tt> and all its variants</li>
<li><tt>Future&lt;T&gt;::onError()</tt>: more on this below</li>
<li><tt>makeFutureTry()</tt>: takes a function, executes it, and creates a Future with the result or any thrown exception</li>
<li><tt>Promise&lt;T&gt;::setWith()</tt>: similar to <tt>makeFutureTry</tt> except it fulfills a Promise instead of creating a completed Future</li>
</ul>

<h2 id="catching-exceptions">Catching Exceptions <a href="#catching-exceptions" class="headerLink">#</a></h2>

<p>There are also several ways to handle exceptions in Futures code.</p>

<h3 id="using-try">Using Try <a href="#using-try" class="headerLink">#</a></h3>

<p>First, there&#039;s the <tt>Try</tt> abstraction which multiplexes values and exceptions so they can be handled simultaneously in a <tt>then()</tt> callback:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">ugh</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">try</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="k">auto</span><span class=""> </span><span class="n">i</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">t</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="c1">// will rethrow
</span><span class="">    </span><span class="c1">// handle success
</span><span class="">  </span><span class="p">&#125;</span><span class=""> </span><span class="k">catch</span><span class=""> </span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">exception</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// handle failure
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Try is also integrated with exception_wrapper
</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">ugh</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">if</span><span class=""> </span><span class="p">(</span><span class="n">t</span><span class="p">.</span><span class="n">hasException</span><span class="o">&lt;</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">exception</span><span class="o">&gt;</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// this is enough if we only care whether the given exception is present
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">ugh</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// we can also extract and handle the exception object
</span><span class="">  </span><span class="c1">// TODO(jsedgwick) infer exception type from the type of the function
</span><span class="">  </span><span class="kt">bool</span><span class=""> </span><span class="n">caught</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">t</span><span class="p">.</span><span class="n">withException</span><span class="o">&lt;</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">exception</span><span class="o">&gt;</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">exception</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// do something with e
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span></pre></div>

<p>Unfortunately, <tt>Try</tt> encourages both intertwining success and error logic as well as excessive rethrowing. Thankfully, there&#039;s another option.</p>

<h3 id="using-onerror">Using onError() <a href="#using-onerror" class="headerLink">#</a></h3>

<p><tt>Future&lt;T&gt;::onError()</tt> allows you to have individual exception handlers as separate callbacks. The parameter you specify for your callback is exactly what <tt>onError()</tt> will try to catch. The callback will be passed over if the future doesn&#039;t contain that exception, otherwise, it will be executed and the T or Future&lt;T&gt; that it returns will become the resultant Future instead.</p>

<div class="remarkup-warning"><span class="remarkup-note-word">WARNING:</span> Chaining together multiple calls to onError will NOT necessarily behave in the same way as multiple catch &#123;&#125; blocks after a try. Namely, if you throw an exception in one call to onError, the next onError will catch it.</div>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">intGenerator</span><span class="p">(</span><span class="p">)</span><span class=""> </span><span class="c1">// returns a Future&lt;int&gt;, which might contain an exception
</span><span class="">  </span><span class="c1">// This is a good opportunity to use the plain value (no Try)
</span><span class="">  </span><span class="c1">// variant of then()
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class=""> 
    </span><span class="k">return</span><span class=""> </span><span class="mi">10</span><span class=""> </span><span class="o">*</span><span class=""> </span><span class="n">i</span><span class="p">;</span><span class=""> </span><span class="c1">// maybe we throw here instead
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// ... runtime_error handling ...
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="o">-</span><span class="mi">1</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">exception</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// ... all other exception handling ...
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="o">-</span><span class="mi">2</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>You can also use <tt>onError()</tt> directly with <tt>exception_wrapper</tt>. One use case for this variant is if you want to handle non-<tt>std::exception</tt> exceptions.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">makeFuture</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">throw</span><span class=""> </span><span class="mi">42</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">exception_wrapper</span><span class=""> </span><span class="n">ew</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// ...
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="ensure">ensure() <a href="#ensure" class="headerLink">#</a></h2>

<p><tt>Future&lt;T&gt;::ensure(F func)</tt> is similar to the <tt>finally</tt> block in languages like Java. That is, it takes a void function and will execute regardless of whether the Future contains a value or an exception. The resultant Future will contain the exception/value of the original Future, unless the function provided to ensure throws, in which case that exception will be caught and propagated instead. For instance:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">fd</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">open</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">makeFuture</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="n">fd</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// do some stuff with the file descriptor
</span><span class="">  </span><span class="c1">// maybe we throw, maybe we don&#039;t
</span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="p">.</span><span class="n">ensure</span><span class="p">(</span><span class="p">[</span><span class="n">fd</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// either way, let&#039;s release that fd
</span><span class="">  </span><span class="n">close</span><span class="p">(</span><span class="n">fd</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// f now contains the result of the then() callback, unless the ensure()
</span><span class="c1">// callback threw, in which case f will contain that exception
</span></pre></div>

<h2 id="performant-exception-han">Performant Exception Handling <a href="#performant-exception-han" class="headerLink">#</a></h2>

<p>Under the hood, the Futures use <tt>folly::exception_wrapper</tt> to store exceptions in a way that minimizes costly rethrows. However, the effectiveness of this mechanism depends on whether exceptions are supplied in a way that enables our library (and <tt>exception_wrapper</tt>) to maintain type information about your exception. Practically speaking, this means constructing exceptional futures directly instead of throwing. For instance:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// This version will throw the exception twice
</span><span class="n">makeFuture</span><span class="p">(</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="k">throw</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">ugh</span><span class="s">&quot;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// ...
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// This version won&#039;t throw at all!
</span><span class="n">makeFuture</span><span class="p">(</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// This will properly wrap the exception
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="n">Unit</span><span class="o">&gt;</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">ugh</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// ...
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Likewise, using <tt>onError</tt> instead of throwing via <tt>Try</tt> will often reduce rethrows. If you want to use <tt>Try</tt>, look at <tt>Try&lt;T&gt;::hasException()</tt> and <tt>Try&lt;T&gt;::withException()</tt> for ways to inspect and handle exceptions without rethrows.</p>

<p>Be wary of premature optimization, and err towards clean code over minimizing rethrows unless you&#039;re sure you need the performance. That said, we will continue to strive to make the cleanest option the most performant one as well.</p></section><section class="dex_document"><h1>Compositional Building Blocks</h1><p class="dex_introduction">Sometimes chaining and nesting with then() is not enough. Here are some utilities for composing futures.</p><div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> For maximum flexibility, many of the helpers documented below take start and end iterators on a collection. All such functions have overloads that take just the collection by reference and automatically operate on the <tt>begin()</tt> and <tt>end()</tt> iterators. You will almost always want to take advantage of this sugar. For instance, <tt>collect(futures.begin(), futures.end())</tt> can be written as simply  <tt>collect(futures)</tt>.</div>

<h2 id="collectall">collectAll() <a href="#collectall" class="headerLink">#</a></h2>

<p><tt>collectAll()</tt> takes an iterable collection of <tt>Future&lt;T&gt;</tt>s (or start and end iterators on such a collection) and returns a <tt>Future&lt;std::vector&lt;Try&lt;T&gt;&gt;&gt;</tt> that will complete once all of the input futures complete. The resultant Future&#039;s vector will contain the results of each in the same order in which they were passed. Errors in any component Future will not cause early termination. Input Futures are moved in and are no longer valid. For example, we could fan out and fan in a bunch of RPCs like so:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span><span class=""> </span><span class="n">someRPC</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span><span class="o">&gt;</span><span class=""> </span><span class="n">fs</span><span class="p">;</span><span class="">
</span><span class="k">for</span><span class=""> </span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="mi">0</span><span class="p">;</span><span class=""> </span><span class="n">i</span><span class=""> </span><span class="o">&lt;</span><span class=""> </span><span class="mi">10</span><span class="p">;</span><span class=""> </span><span class="n">i</span><span class="o">+</span><span class="o">+</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="n">fs</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">someRPC</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="">
</span><span class="">
</span><span class="n">collectAll</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">Try</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="o">&amp;</span><span class=""> </span><span class="n">tries</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">for</span><span class=""> </span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="k">auto</span><span class="o">&amp;</span><span class=""> </span><span class="nl">t</span><span class=""> </span><span class="p">:</span><span class=""> </span><span class="n">tries</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// handle each response
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> Just as with any then() callback, you could take a Try instead and it would compile. But you shouldn&#039;t, because the only way the outer Future can fail is if there&#039;s a bug in our library. Save yourself some typing and skip the Try. This advice also applies to all of the compositional operations below whose Future types contain inner Trys (i.e. everything except for <tt>collect()</tt> and <tt>map()</tt>).</div>

<h2 id="collectall-variadic">collectAll() variadic <a href="#collectall-variadic" class="headerLink">#</a></h2>

<p>There is also a variadically templated flavor of <tt>collectAll()</tt> that allows you to mix and match different types of Futures. It returns a <tt>Future&lt;std::tuple&lt;Try&lt;T1&gt;, Try&lt;T2&gt;, ...&gt;&gt;</tt>. For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">f1</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">string</span><span class="o">&gt;</span><span class=""> </span><span class="n">f2</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">;</span><span class="">
</span><span class="n">collectAll</span><span class="p">(</span><span class="n">f1</span><span class="p">,</span><span class=""> </span><span class="n">f2</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">tuple</span><span class="o">&lt;</span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">,</span><span class=""> </span><span class="n">Try</span><span class="o">&lt;</span><span class="n">string</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="o">&amp;</span><span class=""> </span><span class="n">tup</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">get</span><span class="o">&lt;</span><span class="mi">0</span><span class="o">&gt;</span><span class="p">(</span><span class="n">tup</span><span class="p">)</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="n">string</span><span class=""> </span><span class="n">s</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">get</span><span class="o">&lt;</span><span class="mi">1</span><span class="o">&gt;</span><span class="p">(</span><span class="n">tup</span><span class="p">)</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="c1">// ...
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="collect">collect() <a href="#collect" class="headerLink">#</a></h2>

<p><tt>collect()</tt> is similar to <tt>collectAll()</tt>, but will terminate early if an exception is raised by any of the input Futures. Therefore, the returned Future is of type <tt>std::vector&lt;T&gt;</tt>. Like <tt>collectAll()</tt>, input Futures are moved in and are no longer valid, and the resulting Future&#039;s vector will contain the results of each input Future in the same order they were passed in (if all are successful). For instance:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">collect</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span><span class="o">&amp;</span><span class=""> </span><span class="n">vals</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">for</span><span class=""> </span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="k">auto</span><span class="o">&amp;</span><span class=""> </span><span class="nl">val</span><span class=""> </span><span class="p">:</span><span class=""> </span><span class="n">vals</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// handle each response
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">exception</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// drat, one of them failed
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Or using a Try:
</span><span class="n">collect</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">Try</span><span class="o">&lt;</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="o">&amp;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class=""> </span><span class="c1">// ...
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="collect-variadic">collect() variadic <a href="#collect-variadic" class="headerLink">#</a></h2>

<p>There is also a variadically templated flavor of <tt>collect()</tt> that allows you to mix and match different types of Futures. It returns a <tt>Future&lt;std::tuple&lt;T1, T2, ...&gt;&gt;</tt>.</p>

<h2 id="collectn">collectN() <a href="#collectn" class="headerLink">#</a></h2>

<p><tt>collectN</tt>, like <tt>collectAll()</tt>, takes a collection of Futures, or a pair of iterators thereof, but it also takes a <tt>size_t</tt> N and will complete once N of the input futures are complete. It returns a <tt>Future&lt;std::vector&lt;std::pair&lt;size_t, Try&lt;T&gt;&gt;&gt;&gt;</tt>. Each pair holds the index of the corresponding Future in the original collection as well as its result, though the pairs themselves will be in arbitrary order. Like <tt>collectAll()</tt>, <tt>collectN()</tt> moves in the input Futures, so your copies are no longer valid. If multiple input futures complete &quot;simultaneously&quot; or are already completed, winners are chosen but the choice is undefined.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// Wait for 5 of the input futures to complete
</span><span class="n">collectN</span><span class="p">(</span><span class="n">fs</span><span class="p">,</span><span class=""> </span><span class="mi">5</span><span class="p">,</span><span class="">
</span><span class="">  </span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">pair</span><span class="o">&lt;</span><span class="kt">size_t</span><span class="p">,</span><span class=""> </span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="o">&amp;</span><span class=""> </span><span class="n">tries</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// there will be 5 pairs
</span><span class="">    </span><span class="k">for</span><span class=""> </span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="k">auto</span><span class="o">&amp;</span><span class=""> </span><span class="nl">pair</span><span class=""> </span><span class="p">:</span><span class=""> </span><span class="n">tries</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">      </span><span class="kt">size_t</span><span class=""> </span><span class="n">index</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">pair</span><span class="p">.</span><span class="n">first</span><span class="p">;</span><span class="">
</span><span class="">      </span><span class="kt">int</span><span class=""> </span><span class="n">result</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">pair</span><span class="p">.</span><span class="n">second</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">      </span><span class="c1">// ...
</span><span class="">    </span><span class="p">&#125;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="collectany">collectAny() <a href="#collectany" class="headerLink">#</a></h2>

<p><tt>collectAny()</tt> also takes a collection of Futures (or a pair of iterators thereof), but it completes as soon as any of the input Futures completes. It returns a <tt>Future&lt;std::pair&lt;size_t, Try&lt;T&gt;&gt;&gt;</tt> which holds the index of the first completed Future along with its result. The input futures are moved in, so your copies are no longer valid. If multiple input futures complete &quot;simultaneously&quot; or are already completed, a winner is chosen but the choice is undefined. For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">collectAny</span><span class="p">(</span><span class="n">fs</span><span class="p">,</span><span class=""> </span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">pair</span><span class="o">&lt;</span><span class="kt">size_t</span><span class="p">,</span><span class=""> </span><span class="n">Try</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="o">&amp;</span><span class=""> </span><span class="n">p</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="kt">size_t</span><span class=""> </span><span class="n">index</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">first</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="kt">int</span><span class=""> </span><span class="n">result</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">second</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="c1">// ...
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="map">map() <a href="#map" class="headerLink">#</a></h2>

<p><tt>map()</tt> is the Futures equivalent of the higher order function <a href="http://en.wikipedia.org/wiki/Map_%28higher-order_function%29" target="_blank">map</a>. It takes a collection of <tt>Future&lt;A&gt;</tt> (or a pair of iterators thereof) and a function that can be passed to Future&lt;A&gt;::then(), and in turn calls then() with the function on each input Future. It returns a vector of the resultant Futures in the order they were passed in. This is simple sugar for:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">A</span><span class="o">&gt;</span><span class="o">&gt;</span><span class=""> </span><span class="n">fs</span><span class="p">;</span><span class="">
</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">B</span><span class="o">&gt;</span><span class="o">&gt;</span><span class=""> </span><span class="n">fs2</span><span class="p">;</span><span class="">
</span><span class="k">for</span><span class=""> </span><span class="p">(</span><span class="k">auto</span><span class=""> </span><span class="n">it</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">fs</span><span class="p">.</span><span class="n">begin</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="n">it</span><span class=""> </span><span class="o">&lt;</span><span class=""> </span><span class="n">fs</span><span class="p">.</span><span class="n">end</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="n">it</span><span class="o">+</span><span class="o">+</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="n">fs2</span><span class="p">.</span><span class="n">push_back</span><span class="p">(</span><span class="n">it</span><span class="o">-</span><span class="o">&gt;</span><span class="n">then</span><span class="p">(</span><span class="n">func</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="">
</span></pre></div>

<p>For instance, say you have some expensive RPC that fetches an <tt>int</tt> and you&#039;d like to do expensive processing on each of many calls to this RPC. <tt>collect()</tt> or <tt>collectAll()</tt> might not be wise since they wait for all the results to be ready, while you&#039;d rather process the integers as they arrive. You could use <tt>map()</tt> in this scenario:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">fs2</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">map</span><span class="p">(</span><span class="n">fs</span><span class="p">,</span><span class=""> </span><span class="n">expensiveProcessingFunc</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// You probably now want to wait for all of these to complete. Call
</span><span class="c1">// collect() or collectAll() on fs2 to obtain such a Future.
</span></pre></div>

<h2 id="reduce">reduce() <a href="#reduce" class="headerLink">#</a></h2>

<p><tt>reduce()</tt> is the Futures equivalent of the higher order function <a href="http://en.wikipedia.org/wiki/Fold_%28higher-order_function%29" target="_blank">fold</a> (foldl, specifically). It takes a collection of <tt>Future&lt;A&gt;</tt> (or a pair of iterators thereof), an initial value of type <tt>B</tt>, and a function taking two arguments - the reduced value of type <tt>B</tt> and the next result from the collection of <tt>Future&lt;A&gt;</tt>. The function must return either <tt>B</tt> or <tt>Future&lt;B&gt;</tt>. <tt>reduce()</tt>, in turn, returns a <tt>Future&lt;B&gt;</tt>. The function will be applied to the initial value and the result of the first Future, and then to the result of that initial application and the result of the second Future, and so on until the whole collection of Futures has been reduced or an unhandled exception is hit.</p>

<p>The second argument to the reducing function can be either <tt>A</tt> or <tt>Try&lt;A&gt;</tt>, depending on whether you want to handle exceptions from the input Futures. If there is an exception in an input Future and you don&#039;t take a <tt>Try</tt>, the reduce operation will short circuit with that exception. Any exception thrown in the reducing function will similarly short circuit the whole operation.</p>

<p>For instance, if you have a collection of <tt>Future&lt;int&gt;</tt> and you want a <tt>Future&lt;bool&gt;</tt> that contains true if and only if all the input <tt>ints</tt> are equal to zero, you might write:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">reduce</span><span class="p">(</span><span class="n">fs</span><span class="p">,</span><span class=""> </span><span class="nb">true</span><span class="p">,</span><span class=""> </span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">bool</span><span class=""> </span><span class="n">b</span><span class="p">,</span><span class=""> </span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// You could also return a Future&lt;bool&gt; if you needed to
</span><span class="">  </span><span class="k">return</span><span class=""> </span><span class="n">b</span><span class=""> </span><span class="o">&amp;</span><span class="o">&amp;</span><span class=""> </span><span class="p">(</span><span class="n">i</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="mi">0</span><span class="p">)</span><span class="p">;</span><span class=""> 
</span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">bool</span><span class=""> </span><span class="n">result</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// result is true if all inputs were zero
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// You could use onError or Try here in case one of your input Futures
</span><span class="c1">// contained an exception or if your reducing function threw an exception 
</span></pre></div>

<p>To demonstrate the exception handling case, suppose you have a collection of <tt>Future&lt;T&gt;</tt> and you want a <tt>Future&lt;bool&gt;</tt> that contains true if all the input Futures are non-exceptional:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">reduce</span><span class="p">(</span><span class="n">fs</span><span class="p">,</span><span class=""> </span><span class="nb">true</span><span class="p">,</span><span class=""> </span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">bool</span><span class=""> </span><span class="n">b</span><span class="p">,</span><span class=""> </span><span class="n">Try</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span><span class=""> </span><span class="n">t</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">return</span><span class=""> </span><span class="n">b</span><span class=""> </span><span class="o">&amp;</span><span class="o">&amp;</span><span class=""> </span><span class="n">t</span><span class="p">.</span><span class="n">hasValue</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">bool</span><span class=""> </span><span class="n">result</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// result is true if all inputs were non-exceptional
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>And finally one example where we&#039;re not reducing to a <tt>bool</tt> - here&#039;s how you might calculate the sum of a collection of <tt>Future&lt;int&gt;</tt>:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">reduce</span><span class="p">(</span><span class="n">fs</span><span class="p">,</span><span class=""> </span><span class="mi">0</span><span class="p">,</span><span class=""> </span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">a</span><span class="p">,</span><span class=""> </span><span class="kt">int</span><span class=""> </span><span class="n">b</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">return</span><span class=""> </span><span class="n">a</span><span class=""> </span><span class="o">+</span><span class=""> </span><span class="n">b</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">sum</span><span class="p">)</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// ...
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>See the <tt>reduce()</tt> tests in <a href="https://github.com/facebook/folly/blob/master/folly/futures/test/FutureTest.cpp" target="_blank">the Future tests</a> for a more complete catalog of possibilities.</p>

<h2 id="unorderedreduce">unorderedReduce() <a href="#unorderedreduce" class="headerLink">#</a></h2>

<p>Like <tt>reduce()</tt>, but consumes Futures in the collection as soon as they become ready. Use this if your function doesn&#039;t depend on the order of the Futures in the input collection. See the <a href="https://github.com/facebook/folly/blob/master/folly/futures/test/FutureTest.cpp#L1810" target="_blank">tests</a> for examples.</p>

<h2 id="window">window() <a href="#window" class="headerLink">#</a></h2>

<p><tt>window()</tt> is a sliding window implementation for Futures. It takes a collection of <tt>T</tt> (or a pair of iterators thereof), a function taking a <tt>T&amp;&amp;</tt> and returning a <tt>Future&lt;S&gt;</tt>, and a window size <tt>n</tt>. <tt>window()</tt> will create up to <tt>n</tt> Futures at a time using the function. As Futures complete, new Futures are created until the collection is exhausted.</p>

<p>It ensures that at any given time, no more than <tt>n</tt> Futures are being processed.</p>

<p>Combine with <tt>collectAll</tt>, <tt>reduce</tt> or <tt>unorderedReduce</tt>. See the <a href="https://github.com/facebook/folly/blob/master/folly/futures/test/WindowTest.cpp" target="_blank">tests</a> for examples.</p>

<h2 id="other-possibilities">Other Possibilities <a href="#other-possibilities" class="headerLink">#</a></h2>

<p>There are a number of other possibilities for composing multiple Futures which we&#039;ll probably get around to at some point. If any of these seem like they would come in handy, let us know or better yet submit a diff:</p>

<ul>
<li><tt>filter()</tt></li>
<li>&lt;your suggestion here&gt;</li>
</ul></section><section class="dex_document"><h1>Multithreading and via()</h1><p class="dex_introduction">What to know and what to watch out for when using futures in a multithreaded environment, and how to control your threading model.</p><h2 id="futures-are-thread-safe">Futures are thread safe... with a catch. <a href="#futures-are-thread-safe" class="headerLink">#</a></h2>

<p>The core mutating operations on Futures and Promises are thread safe, insofar as they will throw exceptions if misused (usually, this means being called more than once, including simultaneous calls from different threads). For example, <tt>then()</tt>, <tt>onError()</tt> and other methods that set callbacks on Futures will throw exceptions if called twice. The same goes for fulfilling Promises via <tt>setValue()</tt> and <tt>setException()</tt>.</p>

<p>So what&#039;s the catch? Let&#039;s look at the following example of multithreaded Futures code:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// Thread A
</span><span class="n">Promise</span><span class="o">&lt;</span><span class="n">Unit</span><span class="o">&gt;</span><span class=""> </span><span class="n">p</span><span class="p">;</span><span class="">
</span><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="p">.</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Thread B
</span><span class="n">f</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Thread A
</span><span class="n">p</span><span class="p">.</span><span class="n">setValue</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>In which thread are x and y executed? Unfortunately, it depends. There is a race between setting the callbacks and fulfilling the promise. If setting the callbacks wins, they will be executed in thread A when the Promise is fulfilled. If setting the value wins, they will be executed in thread B as soon as they are set. If <tt>setValue()</tt> sneaks in at just the right time between the two <tt>then()</tt> calls, then x will be executed in thread A and y will be executed in thread B. You could imagine that this nondeterminism might become unwieldy or downright unacceptable. Thankfully, there&#039;s a mechanism to resolve this race and give you fine-grained control over your execution model.</p>

<h2 id="via-to-the-rescue">via() to the rescue <a href="#via-to-the-rescue" class="headerLink">#</a></h2>

<p>Futures have a method called <tt>via()</tt> which takes an <a href="https://github.com/facebook/folly/blob/master/folly/Executor.h#L27" target="_blank">Executor</a>. Executor is a simple interface that requires only the existence of an <tt>add(std::function&lt;void()&gt; func)</tt> method which must be thread safe and must execute the provided function somehow, though not necessarily immediately. <tt>via()</tt> guarantees that a callback set on the Future will be executed on the given Executor. For instance:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">makeFutureWith</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">via</span><span class="p">(</span><span class="n">exe1</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">y</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">via</span><span class="p">(</span><span class="n">exe2</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">z</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>In this example, <tt>y</tt> will be executed on <tt>exe1</tt>, and <tt>z</tt> will be executed on <tt>exe2</tt>. This is a fairly powerful abstraction. It not only solves the above race, but gives you clear, concise, and self-documenting control over your execution model. One common pattern is having different executors for different types of work (e.g. an IO-bound pool spinning on event bases doing your network IO and a CPU-bound thread pool for expensive work) and switching between them with <tt>via()</tt>.</p>

<p>There is also a static function <tt>via()</tt> that creates a completed <tt>Future&lt;Unit&gt;</tt> that is already set up to call back on the provided Executor, and <tt>via(Executor&amp;,Func)</tt> returns a Future for executing a function via an executor.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">via</span><span class="p">(</span><span class="n">exe</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">a</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">via</span><span class="p">(</span><span class="n">exe</span><span class="p">,</span><span class=""> </span><span class="n">a</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">b</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="or-pass-an-executor-to-t">Or, pass an Executor to <tt>then()</tt> <a href="#or-pass-an-executor-to-t" class="headerLink">#</a></h2>

<p>An alternative to <tt>via()</tt> is to pass an Executor as the first parameter to <tt>then()</tt>, which causes the callback to be executed via that Executor. Unlike <tt>via()</tt> the Executor is not sticky, it only applies for this callback. See the docblock for more details and caveats.</p>

<h2 id="executor-implementations">Executor implementations <a href="#executor-implementations" class="headerLink">#</a></h2>

<p><tt>via()</tt> wouldn&#039;t be of much use without practical implementations around. We have a handful, and here&#039;s a (possibly incomplete) list.</p>

<ul>
<li><a href="https://github.com/facebook/folly/blob/master/folly/executors/ThreadPoolExecutor.h" target="_blank">ThreadPoolExecutor</a> is an abstract thread pool implementation that supports resizing, custom thread factories, pool and per-task stats, NUMA awareness, user-defined task expiration, and Codel task expiration. It and its subclasses are under active development. It currently has two implementations:<ul>
<li><a href="https://github.com/facebook/folly/blob/master/folly/executors/CPUThreadPoolExecutor.h" target="_blank">CPUThreadPoolExecutor</a> is a general purpose thread pool. In addition to the above features, it also supports task priorities.</li>
<li><a href="https://github.com/facebook/folly/blob/master/folly/executors/IOThreadPoolExecutor.h" target="_blank">IOThreadPoolExecutor</a> is similar to CPUThreadPoolExecutor, but each thread spins on an EventBase (accessible to callbacks via <a href="https://github.com/facebook/folly/blob/master/folly/io/async/EventBaseManager.h" target="_blank">EventBaseManager</a>)</li>
</ul></li>
<li>folly&#039;s <a href="https://github.com/facebook/folly/blob/master/folly/io/async/EventBase.h" target="_blank">EventBase</a> is an Executor and executes work as a callback in the event loop</li>
<li><a href="https://github.com/facebook/folly/blob/master/folly/futures/ManualExecutor.h" target="_blank">ManualExecutor</a> only executes work when manually cranked. This is useful for testing.</li>
<li><a href="https://github.com/facebook/folly/blob/master/folly/futures/InlineExecutor.h" target="_blank">InlineExecutor</a> executes work immediately inline</li>
<li><a href="https://github.com/facebook/folly/blob/master/folly/futures/QueuedImmediateExecutor.h" target="_blank">QueuedImmediateExecutor</a> is similar to InlineExecutor, but work added during callback execution will be queued instead of immediately executed</li>
<li><a href="https://github.com/facebook/folly/blob/master/folly/executors/ScheduledExecutor.h" target="_blank">ScheduledExecutor</a> is a subinterface of Executor that supports scheduled (i.e. delayed) execution. There aren&#039;t many implementations yet, see <a class="remarkup-task" href="#" target="_blank">T5924392</a></li>
<li>Thrift&#039;s <a href="https://github.com/facebook/fbthrift/blob/master/thrift/lib/cpp/concurrency/ThreadManager.h" target="_blank">ThreadManager</a> is an Executor but we aim to deprecate it in favor of the aforementioned CPUThreadPoolExecutor</li>
<li><a href="https://github.com/facebook/folly/blob/master/folly/executors/FutureExecutor.h" target="_blank">FutureExecutor</a> wraps another Executor and provides <tt>Future&lt;T&gt; addFuture(F func)</tt> which returns a Future representing the result of func. This is equivalent to <tt>futures::async(executor, func)</tt> and the latter should probably be preferred.</li>
</ul></section><section class="dex_document"><h1>Timeouts and related features</h1><p class="dex_introduction">Futures provide a number of timing-related features. Here's an overview.</p><h2 id="timing-implementation">Timing implementation <a href="#timing-implementation" class="headerLink">#</a></h2>

<h3 id="timing-resolution">Timing resolution <a href="#timing-resolution" class="headerLink">#</a></h3>

<p>The functions and methods documented below all take a <tt>Duration</tt>, <a href="https://github.com/facebook/folly/blob/master/folly/futures/detail/Types.h" target="_blank">which is an alias for <tt>std::chrono::milliseconds</tt></a>. Why not allow more granularity? Simply put, we can&#039;t guarantee sub-millisecond resolution and we don&#039;t want to lie to you.</p>

<p>Do not use the <tt>Duration</tt> type directly, that defeats the point of using a <tt>std::chrono::duration</tt> type. Rather, use the appropriate <tt>std::chrono::duration</tt>, e.g. <tt>std::chrono::seconds</tt> or <tt>std::chrono::milliseconds</tt>.</p>

<h3 id="the-timekeeper-interface">The TimeKeeper interface <a href="#the-timekeeper-interface" class="headerLink">#</a></h3>

<p>Most timing-related methods also optionally take a <a href="https://github.com/facebook/folly/blob/master/folly/futures/Timekeeper.h#L44" target="_blank"><tt>TimeKeeper</tt></a>. Implement that interface if you&#039;d like control over how Futures timing works under the hood. If you don&#039;t provide a <tt>TimeKeeper</tt>, a default singleton will be lazily created and employed. The <a href="https://github.com/facebook/folly/blob/master/folly/futures/detail/ThreadWheelTimekeeper.h" target="_blank">default implementation</a> uses a folly::HHWheelTimer in a dedicated EventBase thread to manage timeouts.</p>

<h2 id="within">within() <a href="#within" class="headerLink">#</a></h2>

<p><tt>Future&lt;T&gt;::within()</tt> returns a new Future that will complete with the provided exception (by default, a TimedOut exception) if it does not complete within the specified duration. For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">using</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">chrono</span><span class="o">:</span><span class="o">:</span><span class="n">milliseconds</span><span class="p">;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// f will complete with a TimedOut exception if the Future returned by foo()
</span><span class="c1">// does not complete within 500 ms
</span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">within</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">500</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Same deal, but a timeout will trigger the provided exception instead
</span><span class="n">f2</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">within</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">500</span><span class="p">)</span><span class="p">,</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">you took too long!</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="ontimeout">onTimeout() <a href="#ontimeout" class="headerLink">#</a></h2>

<p><tt>Future&lt;T&gt;::onTimeout()</tt> lets you simultaneously set up a timeout and a timeout handler. For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">onTimeout</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">500</span><span class="p">)</span><span class="p">,</span><span class=""> </span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// You must maintain the resultant future&#039;s type
</span><span class="">    </span><span class="c1">// ... handle timeout ...
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="o">-</span><span class="mi">1</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>The astute reader might notice that this is effectively syntactic sugar for</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">within</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">500</span><span class="p">)</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="k">const</span><span class=""> </span><span class="n">TimedOut</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// handle timeout
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="o">-</span><span class="mi">1</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="get-and-wait-with-timeou">get() and wait() with timeouts <a href="#get-and-wait-with-timeou" class="headerLink">#</a></h2>

<p><tt>get()</tt> and <tt>wait()</tt>, which are detailed in the <a href="#testing">Testing</a> article, optionally take timeouts:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// Will throw TimedOut if the Future doesn&#039;t complete within one second of
</span><span class="c1">// the get() call
</span><span class="kt">int</span><span class=""> </span><span class="n">result</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">1000</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// If the Future doesn&#039;t complete within one second, f will remain
</span><span class="c1">// incomplete. That is, if a timeout occurs, it&#039;s as if wait() was
</span><span class="c1">// never called.
</span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">wait</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">1000</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="delayed">delayed() <a href="#delayed" class="headerLink">#</a></h2>

<p><tt>Future&lt;T&gt;::delayed()</tt> returns a new Future whose completion is delayed for at least the specified duration. For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">makeFuture</span><span class="p">(</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">delayed</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">1000</span><span class="p">)</span><span class="p">)</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// This will be executed when the original Future has completed or when
</span><span class="">    </span><span class="c1">// 1000ms has elapsed, whichever comes last.
</span><span class="">  </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="futures-sleep">futures::sleep() <a href="#futures-sleep" class="headerLink">#</a></h2>

<p><tt>sleep()</tt> returns a <tt>Future&lt;Unit&gt;</tt> that will complete after the specified duration. For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">futures</span><span class="o">:</span><span class="o">:</span><span class="n">sleep</span><span class="p">(</span><span class="n">milliseconds</span><span class="p">(</span><span class="mi">1000</span><span class="p">)</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// This will be executed after 1000ms
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div></section><section class="dex_document"><h1>Interrupts and Cancellations</h1><p class="dex_introduction">Interrupts are a mechanism for Future holders to send a signal to Promise holders. Here's how to use them.</p><p>Let&#039;s say that your Futures code kicks off some long, expensive operation in another thread. A short while later, something comes up that obviates the need for the result of that operation. Are those resources gone forever? Not necessarily. Enter interrupts.</p>

<p>Interrupts allow Future holders to send signals in the form of exceptions to Promise holders, who are free to handle the interrupt as they please (or not at all). For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">p</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">make_shared</span><span class="o">&lt;</span><span class="n">Promise</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="o">&gt;</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">p</span><span class="o">-</span><span class="o">&gt;</span><span class="n">setInterruptHandler</span><span class="p">(</span><span class="p">[</span><span class="n">weakPromise</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">folly</span><span class="o">:</span><span class="o">:</span><span class="n">to_weak_ptr</span><span class="p">(</span><span class="n">p</span><span class="p">)</span><span class="p">]</span><span class="p">(</span><span class="">
</span><span class="">    </span><span class="k">const</span><span class=""> </span><span class="n">exception_wrapper</span><span class="o">&amp;</span><span class=""> </span><span class="n">e</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="k">auto</span><span class=""> </span><span class="n">promise</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">weakPromise</span><span class="p">.</span><span class="n">lock</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="c1">// Handle the interrupt. For instance, we could just fulfill the Promise
</span><span class="">  </span><span class="c1">// with the given exception:
</span><span class="">  </span><span class="k">if</span><span class=""> </span><span class="p">(</span><span class="n">promise</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="n">promise</span><span class="o">-</span><span class="o">&gt;</span><span class="n">setException</span><span class="p">(</span><span class="n">e</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="c1">// Or maybe we want the Future to complete with some special value
</span><span class="">  </span><span class="k">if</span><span class=""> </span><span class="p">(</span><span class="n">promise</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="n">promise</span><span class="o">-</span><span class="o">&gt;</span><span class="n">setValue</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="c1">// Or maybe we don&#039;t want to do anything at all! Including not setting
</span><span class="">  </span><span class="c1">// this handler in the first place.
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">p</span><span class="o">-</span><span class="o">&gt;</span><span class="n">getFuture</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// The Future holder can now send an interrupt whenever it wants via raise().
</span><span class="c1">// If the interrupt beats out the fulfillment of the Promise *and* there is
</span><span class="c1">// an interrupt handler set on the Promise, that handler will be called with
</span><span class="c1">// the provided exception
</span><span class="n">f</span><span class="p">.</span><span class="n">raise</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">runtime_error</span><span class="p">(</span><span class="s">&quot;</span><span class="s">Something went awry! Abort!</span><span class="s">&quot;</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// cancel() is syntactic sugar for raise(FutureCancellation())
</span><span class="n">f</span><span class="p">.</span><span class="n">cancel</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Going forward, we&#039;d like to integrate interrupts with major Future interface provides as a way to cancel RPCs and the like, but that&#039;s not in place yet. This is a bleeding edge feature&#x2014;please let us know your use cases so that we can iterate!</p></section><section class="dex_document"><h1>Testing</h1><p class="dex_introduction">Testing futures-based code does not have to be a pain. Here are some tips and idiomatic approaches.</p><h2 id="extracting-values-synchr">Extracting values synchronously <a href="#extracting-values-synchr" class="headerLink">#</a></h2>

<div class="remarkup-note"><span class="remarkup-note-word">NOTE:</span> The tests in this article are written using the <a href="https://code.google.com/p/googletest/wiki/Primer" target="_blank">gtest</a> framework.</div>

<p>Let&#039;s say we want to test the following interface:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Future</span><span class="o">&lt;</span><span class="kt">bool</span><span class="o">&gt;</span><span class=""> </span><span class="n">isPrime</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">n</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>We could make a couple of calls and set expectations on the resultant futures via <tt>value()</tt>:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">EXPECT_TRUE</span><span class="p">(</span><span class="n">isPrime</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">EXPECT_FALSE</span><span class="p">(</span><span class="n">isPrime</span><span class="p">(</span><span class="mi">8</span><span class="p">)</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>But what if <tt>isPrime()</tt> is asynchronous (e.g. makes an async call to another service that computes primeness)? It&#039;s now likely that you&#039;ll call <tt>value()</tt> before the Future is complete, which will throw a <a href="https://github.com/facebook/folly/blob/master/folly/futures/FutureException.h#L66" target="_blank"><tt>FutureNotReady</tt></a> exception.</p>

<p>A naive approach is to spin until the Future is complete:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// Spin until ready. Gross. Don&#039;t do this.
</span><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">isPrime</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="k">while</span><span class=""> </span><span class="p">(</span><span class="o">!</span><span class="n">f</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="p">&#125;</span><span class="">
</span><span class="n">EXPECT_TRUE</span><span class="p">(</span><span class="n">f</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Thankfully, we have some better options in the form of <tt>Future&lt;T&gt;::get()</tt> and <tt>Future&lt;T&gt;::wait()</tt>.</p>

<h3 id="get">get() <a href="#get" class="headerLink">#</a></h3>

<p><tt>T Future&lt;T&gt;::get()</tt> blocks until the Future is complete and either returns a moved out copy of the value or throws any contained exception. You can use it like so.</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">EXPECT_TRUE</span><span class="p">(</span><span class="n">isPrime</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Keep in mind that some other thread had better complete the Future, because the thread that calls <tt>get()</tt> will block. Also, <tt>get()</tt> optionally takes a timeout after which its throws a TimedOut exception. See the <a href="#timeouts-and-related-features">Timeouts</a> article for more information.</p>

<h3 id="wait">wait() <a href="#wait" class="headerLink">#</a></h3>

<p><tt>Future&lt;T&gt; Future&lt;T&gt;::wait()</tt> is similar to <tt>get()</tt> in that it blocks until the Future is complete. However, instead of returning a value or throwing an exception, it returns a new completed Future with the result of the original Future. One use case is when you&#039;d rather not have the throwing behavior of <tt>get()</tt> so that you can check for exceptions separately without a try/catch. For example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">isPrime</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span><span class="p">.</span><span class="n">wait</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">EXPECT_FALSE</span><span class="p">(</span><span class="n">f</span><span class="p">.</span><span class="n">getTry</span><span class="p">(</span><span class="p">)</span><span class="p">.</span><span class="n">hasException</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">EXPECT_TRUE</span><span class="p">(</span><span class="n">f</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Like <tt>get()</tt>, <tt>wait()</tt> optionally takes a timeout. Again, see the <a href="#timeouts-and-related-features">Timeouts</a> article.</p>

<h3 id="getvia-and-waitvia">getVia() and waitVia() <a href="#getvia-and-waitvia" class="headerLink">#</a></h3>

<p><tt>T Future&lt;T&gt;::getVia(DrivableExecutor*)</tt> and <tt>Future&lt;T&gt; Future&lt;T&gt;::waitVia(DrivableExecutor*)</tt> have the same semantics as <tt>get()</tt> and <tt>wait()</tt> except that they drive some Executor until the Future is complete. <a href="https://github.com/facebook/folly/blob/master/folly/executors/DrivableExecutor.h" target="_blank"><tt>DrivableExecutor</tt></a> is a simple subinterface of <tt>Executor</tt> that requires the presence of a method <tt>drive()</tt> which can somehow make progress on the Executor&#039;s work. Two commonly helpful implementations are <a href="https://github.com/facebook/folly/blob/master/folly/io/async/EventBase.h" target="_blank"><tt>EventBase</tt></a> (where <tt>drive()</tt> loops on the EventBase) and <a href="https://github.com/facebook/folly/blob/master/folly/futures/ManualExecutor.h" target="_blank"><tt>ManualExecutor</tt></a>. These are simple but useful sugar for the following common pattern:</p>

<p>Given this:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">doAsyncWorkOnEventBase</span><span class="p">(</span><span class="o">&amp;</span><span class="n">eventBase</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Don&#039;t do this:</p>

<div class="remarkup-code-block remarkup-counterexample" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">while</span><span class=""> </span><span class="p">(</span><span class="o">!</span><span class="n">f</span><span class="p">.</span><span class="n">isReady</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="n">eb</span><span class="p">.</span><span class="n">loop</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="">
</span></pre></div>

<p>Do one of these instead:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">val</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">f</span><span class="p">.</span><span class="n">getVia</span><span class="p">(</span><span class="o">&amp;</span><span class="n">eventBase</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// or
</span><span class="n">f</span><span class="p">.</span><span class="n">waitVia</span><span class="p">(</span><span class="o">&amp;</span><span class="n">eb</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">Value</span><span class=""> </span><span class="n">val</span><span class="p">)</span><span class="p">&#123;</span><span class=""> </span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class=""> </span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="using-gmock">Using gmock <a href="#using-gmock" class="headerLink">#</a></h2>

<p><a href="https://code.google.com/p/googlemock/" target="_blank">Google Mock</a> is a powerful mocking framework for writing and using C++ mock classes. Unfortunately, Gmock requires that the parameters and return types of mocked functions and methods are copyable. You&#039;re likely to hit this issue when mocking Futures code because Futures (and, less importantly, Promises) are noncopyable, and many of your interfaces will return Futures and some will even be passed Futures.</p>

<p>The canonical approach to mocking interfaces that involve noncopyable objects is to override your interface with a dummy method that simply calls a mock method that has had the noncopyable components stripped or replaced. For Futures, this usually means returning/passing contained values directly and synchronously, which shouldn&#039;t be a problem since your mocks won&#039;t actually be asynchronous. Here is a very contrived but demonstrative example:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// The async interface we want to mock
</span><span class="k">class</span><span class=""> </span><span class="nc">AsyncClient</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class=""> </span><span class="k">public</span><span class="o">:</span><span class="">
</span><span class="">  </span><span class="k">virtual</span><span class=""> </span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// The mock implementation
</span><span class="k">class</span><span class=""> </span><span class="nc">MockAsyncClient</span><span class=""> </span><span class="o">:</span><span class=""> </span><span class="k">public</span><span class=""> </span><span class="n">AsyncClient</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class=""> </span><span class="k">public</span><span class="o">:</span><span class="">
</span><span class="">  </span><span class="c1">// Declare a mock method foo_ that takes an int and returns an int
</span><span class="">  </span><span class="n">MOCK_METHOD1</span><span class="p">(</span><span class="n">foo_</span><span class="p">,</span><span class=""> </span><span class="kt">int</span><span class="p">(</span><span class="kt">int</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="c1">// Plug the mock into an override of the interface
</span><span class="">  </span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class=""> </span><span class="k">override</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// Lift the result back into a Future before returning
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class="p">(</span><span class="n">foo_</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Let&#039;s say that we&#039;re testing a class MyProxy that simply forwards foo()
</span><span class="c1">// calls to AsyncClient and returns the result
</span><span class="k">class</span><span class=""> </span><span class="nc">MyProxy</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class=""> </span><span class="k">public</span><span class="o">:</span><span class="">
</span><span class="">  </span><span class="n">Future</span><span class="o">&lt;</span><span class="kt">int</span><span class="o">&gt;</span><span class=""> </span><span class="n">foo</span><span class="p">(</span><span class="kt">int</span><span class=""> </span><span class="n">i</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="k">return</span><span class=""> </span><span class="n">client</span><span class="o">-</span><span class="o">&gt;</span><span class="n">foo</span><span class="p">(</span><span class="n">i</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">  </span><span class="p">&#125;</span><span class="">
</span><span class="">  </span><span class="kt">void</span><span class=""> </span><span class="n">setClient</span><span class="p">(</span><span class="n">AsyncClient</span><span class="o">*</span><span class=""> </span><span class="n">client</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class=""> </span><span class="k">private</span><span class="o">:</span><span class="">
</span><span class="">  </span><span class="n">AsyncClient</span><span class="o">*</span><span class=""> </span><span class="n">client</span><span class="p">;</span><span class="">
</span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// Now, in our testing code
</span><span class="n">MyProxy</span><span class=""> </span><span class="n">proxy</span><span class="p">;</span><span class="">
</span><span class="n">MockAsyncClient</span><span class=""> </span><span class="n">mockClient</span><span class="p">;</span><span class="">
</span><span class="c1">// Inject the mock
</span><span class="n">proxy</span><span class="p">.</span><span class="n">setClient</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mockClient</span><span class="p">)</span><span class="">
</span><span class="c1">// Set an expectation on the mock to be called with 42 and return 84
</span><span class="n">EXPECT_CALL</span><span class="p">(</span><span class="n">mockClient</span><span class="p">,</span><span class=""> </span><span class="n">foo_</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span><span class="p">)</span><span class="p">.</span><span class="n">WillOnce</span><span class="p">(</span><span class="n">Return</span><span class="p">(</span><span class="mi">84</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// Trigger the call
</span><span class="k">auto</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">MyProxy</span><span class="p">.</span><span class="n">foo</span><span class="p">(</span><span class="mi">42</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="c1">// If everything has been mocked out synchronously, we can just check the
</span><span class="c1">// value of the future directly
</span><span class="n">EXPECT_EQ</span><span class="p">(</span><span class="mi">84</span><span class="p">,</span><span class=""> </span><span class="n">f</span><span class="p">.</span><span class="n">value</span><span class="p">(</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div></section><section class="dex_document"><h1>Pitfalls</h1><p class="dex_introduction"></p><h2 id="eventbase-eventbasemanag">EventBase, EventBaseManager, Executor <a href="#eventbase-eventbasemanag" class="headerLink">#</a></h2>

<p>It&#039;s not uncommon to hit a snag (especially when using via()) where you&#039;re hanging for (a) being on the wrong thread (b) talking to an EventBase which is not actually spinning (loopForever).</p>

<p>Some tips:</p>

<ul>
<li>evb-&gt;isInRunningEventBase()</li>
<li>evb-&gt;isRunning()</li>
</ul>

<h2 id="lambda-arguments">Lambda Arguments <a href="#lambda-arguments" class="headerLink">#</a></h2>

<p>The danger with lambdas is you&#039;ll try to read a variable that&#039;s gone</p>

<div class="remarkup-code-block remarkup-counterexample" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Object</span><span class=""> </span><span class="n">obj</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">;</span><span class="">
</span><span class="k">return</span><span class=""> </span><span class="n">future1</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="o">&amp;</span><span class="p">]</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">    </span><span class="c1">// ..work..
</span><span class="">    </span><span class="n">obj</span><span class="p">.</span><span class="n">method</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">      </span><span class="c1">// woops object is gone from the 
</span><span class="">      </span><span class="c1">// stack when this actually runs
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Sometimes it makes sense to copy inputs. Sometimes that&#039;s too expensive and a shared_ptr is best. Sometimes the nature of things lends itself to the contract &quot;this won&#039;t go away&quot; and you take a raw pointer, but this should only be used when it&#039;s a very natural fit. In particular, you don&#039;t want people wishing you took a shared pointer and having to do something like this to work around it:</p>

<div class="remarkup-code-block remarkup-counterexample" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">foo</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">make_shared</span><span class="o">&lt;</span><span class="n">Foo</span><span class="o">&gt;</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="n">yourFunction</span><span class="p">(</span><span class="n">foo</span><span class="p">.</span><span class="n">get</span><span class="p">(</span><span class="p">)</span><span class="p">,</span><span class="">
</span><span class="">  </span><span class="p">[</span><span class="n">foo</span><span class="p">]</span><span class="p">&#123;</span><span class=""> 
     </span><span class="cm">/* callback doesn&#039;t use foo, but captures the </span><span>
</span><span class="cm">      * shared pointer to keep it alive </span><span>
</span><span class="cm">      */</span><span class="">
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>In general:
prefer taking inputs by value if they&#039;re small enough
if inputs are big (measurably expensive to copy), then keep them on the heap and prefer a shared_ptr
if you are really sure you need to get more fancy, put on your wizard hat and go to it ;)</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="n">Object</span><span class=""> </span><span class="n">obj</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">;</span><span class="">
</span><span class="k">return</span><span class=""> </span><span class="n">future1</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="n">obj</span><span class="p">]</span><span class=""> </span><span class="p">&#123;</span><span class="">  </span><span class="c1">// capture by value
</span><span class="">    </span><span class="c1">// ..work..
</span><span class="">    </span><span class="n">obj</span><span class="p">.</span><span class="n">method</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">      </span><span class="c1">// works on copy of obj
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>If Object is large:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">optr</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">makeShared</span><span class="o">&lt;</span><span class="n">Object</span><span class="o">&gt;</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="k">return</span><span class=""> </span><span class="n">future1</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="n">optr</span><span class="p">]</span><span class=""> </span><span class="p">&#123;</span><span class="">  </span><span class="c1">// copy ptr, use count = 2
</span><span class="">    </span><span class="c1">// ..work..
</span><span class="">    </span><span class="n">optr</span><span class="o">-</span><span class="o">&gt;</span><span class="n">method</span><span class="p">(</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">      </span><span class="c1">// works on original object
</span><span class="">    </span><span class="c1">// use-count for optr goes to 0 and object destructs
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<h2 id="using-std-move-with-lamb">Using std::move with lambda capture <a href="#using-std-move-with-lamb" class="headerLink">#</a></h2>

<p>If you have move-only objects, like unique_ptr, then you can use generalized lambda capture (C++14) syntax:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">moveOnly</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">folly</span><span class="o">:</span><span class="o">:</span><span class="n">make_unique</span><span class="o">&lt;</span><span class="n">Object</span><span class="o">&gt;</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="k">return</span><span class=""> </span><span class="n">future1</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="n">lambdaObj</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">move</span><span class="p">(</span><span class="n">moveOnly</span><span class="p">)</span><span class="p">]</span><span class=""> </span><span class="p">&#123;</span><span class="">  
    </span><span class="c1">// ...
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Since you can only std::move() out of an object once, you can&#039;t have:</p>

<div class="remarkup-code-block remarkup-counterexample" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">auto</span><span class=""> </span><span class="n">moveOnly</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">folly</span><span class="o">:</span><span class="o">:</span><span class="n">make_unique</span><span class="o">&lt;</span><span class="n">Object</span><span class="o">&gt;</span><span class="p">(</span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="k">return</span><span class=""> </span><span class="n">future1</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="n">lambdaObj</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">move</span><span class="p">(</span><span class="n">moveOnly</span><span class="p">)</span><span class="p">]</span><span class=""> </span><span class="p">&#123;</span><span class="">  
    </span><span class="c1">// Do work:
</span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span><span class="p">.</span><span class="n">onError</span><span class="p">(</span><span class="p">[</span><span class="n">lambdaObj</span><span class=""> </span><span class="o">=</span><span class=""> </span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">move</span><span class="p">(</span><span class="n">moveOnly</span><span class="p">)</span><span class="p">]</span><span class=""> </span><span class="p">&#123;</span><span class=""> 
    </span><span class="c1">// Error handling:
</span><span class="p">&#125;</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>And note, the construction order of the lambdas in GCC is somewhat counter-intuitive when you have several declared in one statement.   The lambda instance for the .onError() case will be constructed first (the legal std::move), and then the &#039;.then()&#039; clause lambda.   See <a href="https://godbolt.org/g/B51b77" target="_blank">https://godbolt.org/g/B51b77</a>.</p></section><section class="dex_document"><h1>Future as a Monad</h1><p class="dex_introduction">A semi-formal and totally optional analysis of Future as a monad.</p><p>Future is a monad. You don&#039;t need to know this or what it means to use Futures, but if you are curious, want to understand monads better, or eat functional flakes for breakfast, then keep reading this extremely extracurricular document.</p>

<p>Let&#039;s review the definition of a monad. Formal definitions are mathematical and/or in Haskellese and therefore opaque to imperative mortals. But here&#039;s a simplified description using a subset of Haskell type notation that is useful but not confusing:</p>

<div class="remarkup-code-block" data-code-lang="hs"><pre class="remarkup-code"><span class="c1">-- &quot;unit&quot; is a function that takes a value and wraps it in the monad type.</span><span class="">
</span><span class="c1">-- Haskellers call this &quot;return&quot; as some kind of sick inside joke.</span><span class="">
</span><span class="nf">unit</span><span class=""> </span><span class="ow">::</span><span class=""> </span><span class="n">a</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="n">a</span><span class="">

</span><span class="c1">-- &quot;bind&quot; is a function that takes a monad, and a function that takes a value</span><span class="">
</span><span class="c1">-- and returns another monad. Haskellers call this &quot;&gt;&gt;=&quot; because they are</span><span class="">
</span><span class="c1">-- vying to unseat perl from the throne of illegibility.</span><span class="">
</span><span class="nf">bind</span><span class=""> </span><span class="ow">::</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="n">a</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="p">(</span><span class="n">a</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="n">b</span><span class="p">)</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="n">b</span><span class="">
</span></pre></div>

<p>Monads must also satisfy these three axioms:</p>

<div class="remarkup-code-block" data-code-lang="hs"><pre class="remarkup-code"><span class="c1">-- Left Identity</span><span class="">
</span><span class="nf">unit</span><span class=""> </span><span class="n">a</span><span class=""> </span><span class="p">`</span><span class="n">bind</span><span class="p">`</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="n">a</span><span class="">
</span><span class="c1">-- Right Identity</span><span class="">
</span><span class="nf">m</span><span class=""> </span><span class="p">`</span><span class="n">bind</span><span class="p">`</span><span class=""> </span><span class="n">unit</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">m</span><span class="">
</span><span class="c1">-- Associativity</span><span class="">
</span><span class="p">(</span><span class="n">m</span><span class=""> </span><span class="p">`</span><span class="n">bind</span><span class="p">`</span><span class=""> </span><span class="n">f</span><span class="p">)</span><span class=""> </span><span class="p">`</span><span class="n">bind</span><span class="p">`</span><span class=""> </span><span class="n">g</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="p">`</span><span class="n">bind</span><span class="p">`</span><span class=""> </span><span class="p">(</span><span class="nf">\</span><span class="n">x</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="n">x</span><span class=""> </span><span class="p">`</span><span class="n">bind</span><span class="p">`</span><span class=""> </span><span class="n">g</span><span class="p">)</span><span class="">
</span></pre></div>

<p>I won&#039;t try to explain that, there are <a href="http://lmgtfy.com/?q=what+the+hell+is+a+monad%3F" target="_blank">many blog posts and wiki pages that try to do that</a>. Instead, I&#039;ll substitute the equivalent Future monad expressions, and the whole thing will (probably) start to make sense. First, a simplified Future type:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="k">template</span><span class=""> </span><span class="o">&lt;</span><span class="k">class</span><span class=""> </span><span class="nc">A</span><span class="o">&gt;</span><span class="">
</span><span class="k">struct</span><span class=""> </span><span class="n">Future</span><span class=""> </span><span class="p">&#123;</span><span class="">
</span><span class="">  </span><span class="c1">// The constructor that takes a value is &quot;unit&quot;
</span><span class="">  </span><span class="n">Future</span><span class="p">(</span><span class="n">A</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="c1">// &quot;then&quot; is &quot;bind&quot;
</span><span class="">  </span><span class="k">template</span><span class=""> </span><span class="o">&lt;</span><span class="k">class</span><span class=""> </span><span class="nc">B</span><span class="o">&gt;</span><span class="">
</span><span class="">  </span><span class="n">Future</span><span class="o">&lt;</span><span class="n">B</span><span class="o">&gt;</span><span class=""> </span><span class="n">then</span><span class="p">(</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">function</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">B</span><span class="o">&gt;</span><span class="p">(</span><span class="n">A</span><span class="p">)</span><span class="p">)</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="">  </span><span class="p">.</span><span class="p">.</span><span class="p">.</span><span class="">
</span><span class="p">&#125;</span><span class="p">;</span><span class="">
</span><span class="">
</span><span class="c1">// &quot;makeFuture&quot; is also &quot;unit&quot;, and we will need it because constructors can&#039;t
</span><span class="c1">// really be converted to std::function (AFAIK)
</span><span class="k">template</span><span class=""> </span><span class="o">&lt;</span><span class="k">class</span><span class=""> </span><span class="nc">A</span><span class="o">&gt;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">A</span><span class="o">&gt;</span><span class=""> </span><span class="n">makeFuture</span><span class="p">(</span><span class="n">A</span><span class="p">)</span><span class="p">;</span><span class="">
</span></pre></div>

<p>Now, the three axioms (Futures don&#039;t define <tt>operator==</tt> but you get the idea):</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// Left Identity
</span><span class="n">A</span><span class=""> </span><span class="n">a</span><span class="p">;</span><span class="">
</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">A</span><span class="o">&gt;</span><span class="p">(</span><span class="n">a</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">f</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="n">f</span><span class="p">(</span><span class="n">a</span><span class="p">)</span><span class="">
</span><span class="">
</span><span class="c1">// Right Identity
</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">A</span><span class="o">&gt;</span><span class=""> </span><span class="n">m</span><span class="p">;</span><span class="">
</span><span class="n">m</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">makeFuture</span><span class="o">&lt;</span><span class="n">A</span><span class="o">&gt;</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="n">m</span><span class="">
</span><span class="">
</span><span class="c1">// Associativity
</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">A</span><span class="o">&gt;</span><span class=""> </span><span class="n">m</span><span class="p">;</span><span class="">
</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">function</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">B</span><span class="o">&gt;</span><span class="p">(</span><span class="n">A</span><span class="p">)</span><span class="o">&gt;</span><span class=""> </span><span class="n">f</span><span class="p">;</span><span class="">
</span><span class="n">std</span><span class="o">:</span><span class="o">:</span><span class="n">function</span><span class="o">&lt;</span><span class="n">Future</span><span class="o">&lt;</span><span class="n">C</span><span class="o">&gt;</span><span class="p">(</span><span class="n">B</span><span class="p">)</span><span class="o">&gt;</span><span class=""> </span><span class="n">g</span><span class="p">;</span><span class="">
</span><span class="n">m</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">f</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">g</span><span class="p">)</span><span class=""> </span><span class="o">=</span><span class="o">=</span><span class=""> </span><span class="n">m</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="p">[</span><span class="p">]</span><span class="p">(</span><span class="n">A</span><span class=""> </span><span class="n">x</span><span class="p">)</span><span class=""> </span><span class="p">&#123;</span><span class=""> </span><span class="k">return</span><span class=""> </span><span class="n">f</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="p">.</span><span class="n">then</span><span class="p">(</span><span class="n">g</span><span class="p">)</span><span class="p">;</span><span class=""> </span><span class="p">&#125;</span><span class="p">)</span><span class="">
</span></pre></div>

<p>So, in plain english this says a monad like Future has a way to get stuff in the monad (unit/makeFuture), and a way to chain things together (bind/then). unit semantics are unsurprising, and chaining is the same as nesting. Something that behaves this way is a monad, and Future is a monad.</p>

<div class="remarkup-note">Remember how Futures do more than just hold values? The nature of the underlying asynchronous operations (usually I/O) generally includes side effects, and this breaks our pure formalism. You may or may not be able to make your async operations (observable) side-effect free, but you can make your intermediate Future callbacks functionally pure (aka value semantics), and if you do you will be happier than if you mutate state. But I won&#039;t beat that dead horse here&#x2014;I know you will probably mutate state anyway because you&#039;re a perf-conscious C++ developer and speed trumps safety. But do try to minimize it.</div>

<p>Ok, so now we know Future is a monad. What can we do with this newfound power? Knowledge is power, right? Well, you can brag to your friends, for one thing. C++ doesn&#039;t really provide any concrete reusable tools for things that are monads. There&#039;s no do-blocks, or some generic monad-aware functional toolkit that includes map, filter, fold, etc. But what you do get is a way of thinking about and reasoning about your Futures that transcends our own little implementation, and doesn&#039;t require that you grok all the opaque internals of the implementation to do it.</p>

<p>But mostly it makes you cool.</p>

<h3 id="kleisli-composition-extr">Kleisli Composition (extra extra credit) <a href="#kleisli-composition-extr" class="headerLink">#</a></h3>

<p>If &quot;associative&quot; doesn&#039;t look associative to you, then you are very astute. Congratulations! You win a maths unicorn.
The three laws refer to a different formulation of the axioms, in terms of the Kleisli Composition operator (<tt>&gt;=&gt;</tt>), which basically says compose two monad-making functions in the obvious way.</p>

<div class="remarkup-code-block" data-code-lang="hs"><pre class="remarkup-code"><span class="p">(</span><span class="o">&gt;=&gt;</span><span class="p">)</span><span class=""> </span><span class="ow">::</span><span class=""> </span><span class="kt">Monad</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="ow">=&gt;</span><span class=""> </span><span class="p">(</span><span class="n">a</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="n">b</span><span class="p">)</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="p">(</span><span class="n">b</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="n">c</span><span class="p">)</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">a</span><span class=""> </span><span class="ow">-&gt;</span><span class=""> </span><span class="n">m</span><span class=""> </span><span class="n">c</span><span class="">

</span><span class="c1">-- Left Identity</span><span class="">
</span><span class="nf">unit</span><span class=""> </span><span class="o">&gt;=&gt;</span><span class=""> </span><span class="n">g</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">g</span><span class="">
</span><span class="c1">-- Right Identity</span><span class="">
</span><span class="nf">f</span><span class=""> </span><span class="o">&gt;=&gt;</span><span class=""> </span><span class="n">unit</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">f</span><span class="">
</span><span class="c1">-- Associativity</span><span class="">
</span><span class="p">(</span><span class="n">f</span><span class=""> </span><span class="o">&gt;=&gt;</span><span class=""> </span><span class="n">g</span><span class="p">)</span><span class=""> </span><span class="o">&gt;=&gt;</span><span class=""> </span><span class="n">h</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">f</span><span class=""> </span><span class="o">&gt;=&gt;</span><span class=""> </span><span class="p">(</span><span class="n">g</span><span class=""> </span><span class="o">&gt;=&gt;</span><span class=""> </span><span class="n">h</span><span class="p">)</span><span class="">
</span></pre></div>

<p>We accidentally implemented this operator, and called it <tt>chain</tt>. Then we removed it in favor of <tt>Future::thenMulti</tt>. But it totally existed, so use your imagination:</p>

<div class="remarkup-code-block" data-code-lang="cpp"><pre class="remarkup-code"><span class="c1">// Left Identity
</span><span class="n">chain</span><span class="p">(</span><span class="n">makeFuture</span><span class="p">,</span><span class=""> </span><span class="n">g</span><span class="p">)</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">g</span><span class="">
</span><span class="c1">// Right Identity
</span><span class="n">chain</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class=""> </span><span class="n">makeFuture</span><span class="p">)</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">f</span><span class="">
</span><span class="c1">// Associativity
</span><span class="n">chain</span><span class="p">(</span><span class="n">chain</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class=""> </span><span class="n">g</span><span class="p">)</span><span class="p">,</span><span class=""> </span><span class="n">h</span><span class="p">)</span><span class=""> </span><span class="err">≡</span><span class=""> </span><span class="n">chain</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class=""> </span><span class="n">chain</span><span class="p">(</span><span class="n">g</span><span class="p">,</span><span class=""> </span><span class="n">h</span><span class="p">)</span><span class="p">)</span><span class=""> </span><span class="c1">// and chain(f, g, h)
</span></pre></div>

<h3 id="further-reading">Further reading <a href="#further-reading" class="headerLink">#</a></h3>

<ul>
<li><a href="https://wiki.haskell.org/Monad_laws" target="_blank">https://wiki.haskell.org/Monad_laws</a></li>
<li><a href="http://learnyouahaskell.com/a-fistful-of-monads" target="_blank">http://learnyouahaskell.com/a-fistful-of-monads</a></li>
</ul></section><section class="dex_document"><h1>FAQ</h1><p class="dex_introduction"></p><h2 id="what-s-this-unit-thing-i">What&#039;s this <tt>Unit</tt> thing? I&#039;m confused. <a href="#what-s-this-unit-thing-i" class="headerLink">#</a></h2>

<p>If your callback returns <tt>void</tt>, it will result in a <tt>Future&lt;Unit&gt;</tt>. <tt>Future&lt;void&gt;</tt> is illegal. All you need to know is, if you would expect a <tt>Future&lt;void&gt;</tt> or <tt>Promise&lt;void&gt;</tt> or <tt>Try&lt;void&gt;</tt>, type <tt>Unit</tt> instead of <tt>void</tt>.</p>

<h2 id="why-not-use-std-future">Why not use <tt>std::future</tt>? <a href="#why-not-use-std-future" class="headerLink">#</a></h2>

<p>No callback support. See also <a href="http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2012/n3428.pdf" target="_blank">http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2012/n3428.pdf</a></p>

<h2 id="why-not-use-boost-future">Why not use boost::future? <a href="#why-not-use-boost-future" class="headerLink">#</a></h2>

<ul>
<li>At the time of writing, 1.53 (the first version with the requisite features) was brand new, not well-tested, and not available to Facebook developers.</li>
<li>It is still a bit buggy/bleeding-edge</li>
<li>They haven&#039;t fleshed out the threading model very well yet, e.g. every single then currently spawns a new thread unless you explicitly ask it to work on this thread only, and executor support was nonexistent (and now, is still experimental).</li>
</ul>

<h2 id="why-use-heap-allocated-s">Why use heap-allocated shared state? Why is Promise not a subclass of Future (like Twitter&#039;s)? <a href="#why-use-heap-allocated-s" class="headerLink">#</a></h2>

<p>C++. It boils down to wanting to return a Future by value for performance (move semantics and compiler optimizations), and programmer sanity, and needing a reference to the shared state by both the user (which holds the Future) and the asynchronous operation (which holds the Promise), and allowing either to go out of scope.</p>

<h2 id="what-about-proper-contin">What about proper continuations (fibers)? Futures suck. <a href="#what-about-proper-contin" class="headerLink">#</a></h2>

<p>People mean two things here, they either mean using continuations (as in CSP) or they mean using generators which require continuations. It&#039;s important to know those are two distinct questions, but in our context the answer is the same because continuations are a prerequisite for generators.</p>

<p>C++ doesn&#039;t directly support continuations very well. But there are some ways to do them in C/C++ that rely on some rather low-level facilities like <tt>setjmp</tt> and <tt>longjmp</tt> (among others). So yes, they are possible (cf. <a href="https://github.com/ccutrer/mordor" target="_blank">Mordor</a> and <a href="https://github.com/facebook/folly/tree/master/folly/experimental/fibers" target="_blank">folly/experimental/fibers</a>).</p>

<p>The tradeoff is memory. Each continuation has a stack, and that stack is usually fixed-size and has to be big enough to support whatever ordinary computation you might want to do on it. So each living continuation requires a relatively large amount of memory. If you know the number of continuations will be small, this might be a good fit. In particular, it might be faster, the code might read cleaner, and debugging stack traces might be much easier.</p>

<p>Futures takes the middle road between callback hell and continuations, one which has been trodden and proved useful in other languages. It doesn&#039;t claim to be the best model for all situations. Use your tools wisely.</p></section></section>
Working through [Programming Koans][1] can be a fun, lightweight, and fast way to
learn a new language or pattern with small, focused exercises. Therefore, we
present Koans for Futures.  Perhaps you will call them "Koans to Be".

Edit the topical files one at a time, moving the "compilation cursor" down one
exercise at a time, and getting them to pass by filling in the blanks.

[1] http://www.lauradhamilton.com/learn-a-new-programming-language-today-with-koans
[2] http://catb.org/esr/writings/unix-koans/ten-thousand.html
# folly/io/async: An object-oriented wrapper around libevent
----------------------------------------------------------

[libevent](https://github.com/libevent/libevent) is an excellent
cross-platform eventing library.  Folly's async provides C++ object
wrappers for fd callbacks and event_base, as well as providing
implementations for many common types of fd uses.

## EventBase

The main libevent / epoll loop.  Generally there is a single EventBase
per thread, and once started, nothing else happens on the thread
except fd callbacks.  For example:

```
EventBase base;
auto thread = std::thread([&](){
  base.loopForever();
});
```

EventBase has built-in support for message passing between threads.
To send a function to be run in the EventBase thread, use
runInEventBaseThread().

```
EventBase base;
auto thread1 = std::thread([&](){
  base.loopForever();
});
base.runInEventBaseThread([&](){
  printf("This will be printed in thread1\n");
});
```

There are various ways to run the loop.  EventBase::loop() will return
when there are no more registered events.  EventBase::loopForever()
will loop until EventBase::terminateLoopSoon() is called.
EventBase::loopOnce() will only call epoll() a single time.

Other useful methods include EventBase::runAfterDelay() to run events
after some delay, and EventBase::setMaxLatency(latency, callback) to
run some callback if the loop is running very slowly, i.e., there are
too many events in this loop, and some code should probably be running
in different threads.

EventBase always calls all callbacks inline - that is, there is no
explicit or implicit queuing.  The specific implications of this are:

* Tail-latency times (P99) are vastly better than any queueing
  implementation
* The EventHandler implementation is responsible for not taking too
  long in any individual callback.  All of the EventHandlers in this
  implementation already do a good job of this, but if you are
  subclassing EventHandler directly, something to keep in mind.
* The callback cannot delete the EventBase or EventHandler directly,
  since it is still on the call stack.  See DelayedDestruction class
  description below, and use shared_ptrs appropriately.

## EventHandler

EventHandler is the object wrapper for fd's.  Any class you wish to
receive callbacks on will inherit from
EventHandler. `registerHandler(EventType)` will register to receive
events of a specific type.

Currently supported event types:

* READ - read and EOF events
* WRITE - write events, when kernel write buffer is empty
* READ_WRITE - both
* PERSIST - The event will remain registered even after the handlerReady() fires

Unsupported libevent event types, and why-

* TIMEOUT - this library has specific timeout support, instead of
  being attached to read/write fds.
* SIGNAL - similarly, signals are handled separately, see
  AsyncSignalHandler
* EV_ET - Currently all the implementations of EventHandler are set up
  for level triggered.  Benchmarking hasn't shown that edge triggered
  provides much improvement.

  Edge-triggered in this context means that libevent will provide only
  a single callback when an event becomes active, as opposed to
  level-triggered where as long as there is still data to read/write,
  the event will continually fire each time event_wait is called.
  Edge-triggered adds extra code complexity, since the library would
  need to maintain a similar list of active FDs that libevent
  currently does between edge triggering events.  The only advantage
  of edge-triggered is that you can use EPOLLONESHOT to ensure the
  event only gets called on a single event_base - but in this library,
  we assume each event is only registered on a single thread anyway.

* EV_FINALIZE - EventBase can only be used in a single thread,
  excepting a few methods.  To safely unregister an event from a
  different thread, it would have to be done through
  EventBase::runInEventBaseThread().  Most APIs already make this
  thread transition for you, or at least CHECK() that you've done it
  in the correct thread.
* EV_CLOSED - This is an optimization - instead of having to READ all
  the data and then get an EOF, EV_CLOSED would fire before all the
  data is read.  TODO: implement this.  Probably only useful in
  request/response servers.

## Implementations of EventHandler

### AsyncSocket

A nonblocking socket implementation.  Writes are queued and written
asynchronously, even before connect() is successful.  The read api
consists of two methods: getReadBuffer() and readDataAvailable().
When the READ event is signaled, libevent has no way of knowing how
much data is available to read.   In some systems (linux), we *could*
make another syscall to get the data size in the kernel read buffer,
but syscalls are slow.  Instead, most users will just want to provide
a fixed size buffer in getReadBuffer(), probably using the IOBufQueue
in folly/io.   readDataAvailable() will then describe exactly how much
data was read.

AsyncSocket provides send timeouts, but not read timeouts - generally
read timeouts are application specific, and should use an AsyncTimer
implementation below.

Various notes:

* Using a chain of IOBuf objects, and calling writeChain(), is a very
  syscall-efficient way to add/modify data to be sent, without
  unnecessary copies.
* setMaxReadsPerEvent() - this prevents an AsyncSocket from blocking
  the event loop for too long.
* Don't use the fd for syscalls yourself while it is being used in
  AsyncSocket, instead use the provided wrappers, like
  AsyncSocket::close(), shutdown(), etc.

#### AsyncSSLSocket

Similar to AsyncSocket, but uses openssl.  Provides an additional
HandshakeCallback to check the server's certificates.

#### TAsyncUDPSocket

TODO: Currently in fbthrift.

A socket that reads/writes UDP packets.  Since there is little state
to maintain, this is much simpler than AsyncSocket.

### AsyncServerSocket

A listen()ing socket that accept()s fds, and passes them to other
event bases.

The general pattern is:

```
EventBase base;
auto socket = AsyncServerSocket::newSocket(&base);
socket->bind(port); // 0 to choose any free port
socket->addAcceptCallback(object, &base); // where object is the object that implements the accept callback, and base is the object's eventbase.  base::runInEventBaseThread() will be called to send it a message.
socket->listen(backlog);
socket->startAccepting();
```

Generally there is a single accept() thread, and multiple
AcceptCallback objects.  The Acceptee objects then will manage the
individual AsyncSockets.  While AsyncSockets *can* be moved between
event bases, most users just tie them to a single event base to get
better cache locallity, and to avoid locking.

Multiple ServerSockets can be made, but currently the linux kernel has
a lock on accept()ing from a port, preventing more than ~20k accepts /
sec.  There are various workarounds (SO_REUSEPORT), but generally
clients should be using connection pooling instead when possible.

Since AsyncServerSocket provides an fd, an AsyncSSLSocket or
AsyncSocket can be made using the same codepath

#### TAsyncUDPServerSocket

Similar to AsyncServerSocket, but for UDP messages - messages are
read() on a single thread, and then fanned out to multiple worker
threads.

### NotificationQueue (EventFD or pipe notifications)

NotificationQueue is used to send messages between threads in the
*same process*.  It is what backs EventBase::runInEventBaseThread(),
so it is unlikely you'd want to use it directly instead of using
runInEventBaseThread().

An eventFD (for kernels > 2.6.30) or pipe (older kernels) are added to
the EventBase loop to wake up threads receiving messages.   The queue
itself is a spinlock-guarded list.   Since we are almost always
talking about a single sender thread and a single receiver (although
the code works just fine for multiple producers and multiple
consumers), the spinlock is almost always uncontended, and we haven't
seen any perf issues with it in practice.

The eventfd or pipe is only notified if the thread isn't already
awake, to avoid syscalls.  A naive implementaiton that does one write
per message in the queue, or worse, writes the whole message to the
queue, would be significantly slower.

If you need to send messages *between processes*, you would have to
write the whole message to the pipe, and manage the pipe size.  See
AsyncPipe.

### AsyncTimeout

An individual timeout callback that can be installed in the event
loop.   For code cleanliness and clarity, timeouts are separated from
sockets.   There is one fd used per AsyncTimeout.  This is a pretty
serious restriction, so the two below subclasses were made to support
multiple timeouts using a single fd.

#### HHWheelTimer

Implementation of a [hashed hierarchical wheel
timer](http://www.cs.columbia.edu/~nahum/w6998/papers/sosp87-timing-wheels.pdf).
Any timeout time can be used, with O(1) insertion, deletion, and
callback time.  The wheel itself takes up some amount of space, and
wheel timers have to have a constant tick, consuming a constant amount
of CPU.

An alternative to a wheel timer would be a heap of callbacks sorted by
timeout time, but would change the big-O to O(log n).  In our
experience, the average server has thousands to hundreds of thousands
of open sockets, and the common case is to add and remove timeouts
without them ever firing, assuming the server is able to keep up with
the load.  Therefore O(log n) insertion time overshadows the extra CPU
consumed by a wheel timer tick.

#### TAsyncTimeoutSet

NOTE: currently in proxygen codebase.

If we assume that all timeouts scheduled use the same timeout time, we
can keep O(1) insertion time: just schedule the new timeout at the
tail of the list, along with the time it was actually added.  When the
current timeout fires, we look at the new head of the list, and
schedule AsyncTimeout to fire at the difference between the current
time and the scheduled time (which probably isn't the same as the
timeout time.)

This requires all AsyncTimeoutSets timeouts to have the same timeout
time though, which in practice means many AsyncTimeoutSets are needed
per application.   Using HHWheelTimer instead can clean up the code quite
a bit, because only a single HHWheelTimer is needed per thread, as
opposed to one AsyncTimeoutSet per timeout time per thread.

### AsyncSignalHandler

Used to handle AsyncSignals.  Similar to AsyncTimeout, for code
clarity, we don't reuse the same fd as a socket to receive signals.

### AsyncPipe

Async reads/writes to a unix pipe, to send data between processes.

## Helper Classes

### RequestContext (in Request.h)

Since messages are frequently passed between threads with
runInEventBaseThread(), ThreadLocals don't work for messages.
Instead, RequestContext can be used, which is saved/restored between
threads.  Major uses for this include:

* NUMA: saving the numa node the code was running on, and explicitly
  running it on the same node in other threadpools / eventbases
* Tracing: tracing requests dapper-style intra machine, as well as
  between threads themselves.

In this library only runInEventBaseThread save/restores the request
context, although other Facebook libraries that pass requests between
threads do also: folly::future, and fbthrift::ThreadManager, etc

### DelayedDestruction

Since EventBase callbacks already have the EventHandler and EventBase
on the stack, calling `delete` on either of these objects would most
likely result in a segfault.  Instead, these objects inherit from
DelayedDestruction, which provides reference counting in the
callbacks.  Instead of delete, `destroy()` is called, which notifies
that is ready to be destroyed.  In each of the callbacks there is a
DestructorGuard, which prevents destruction until all the Guards are
gone from the stack, when the actual delete method is called.

DelayedDestruction can be a painful to use, since shared_ptrs and
unique_ptrs need to have a special DelayedDestruction destructor
type.  It's also pretty easy to forget to add a DestructorGuard in
code that calls callbacks.  But it is well worth it to avoid queuing
callbacks, and the improved P99 times as a result.

### DestructorCheck

Often for an object requesting callbacks from other components (timer,
socket connect, etc.) there is a chance that the requestor will be
deallocated before it'll receive the callback.  One of the ways to avoid
dereferencing the deallocated object from callbacks is to derive the
object from DelayedDestruction, and add a delayed destruction guard
to the callback context.  In case if keeping the object around until
all the requested callbacks fire is too expensive, or if the callback
requestor can't have private destructor (it's allocated on the stack,
or as a member of a larger object), DestructorCheck can be used.
DestructorCheck is not affecting object life time. It helps other
component to detect safely that the tracked object was deallocated.

The object requesting the callback must be derived from DestructorCheck.
The callback context should contain an instance of
DestructorCheck::Safety object initialized with a reference to the
object requesting the callback.  Safety object can be captured by value
in the callback lambda, or explicitly added to a predefined callback
context class. Multiple instances of Safety object can be instantiated
for the same tracked object.  Once the callback is invoked, before
dereferencing the requester object, callback code should make sure that
`destroyed()` method for the corresponding Safety object returns false.

### EventBaseManager

DANGEROUS.

Since there is ususally only a single EventBase per thread, why not
make EventBase managed by a threadlocal?  Sounds easy!  But there are
several catches:

* The EventBase returned by `EventBaseManager::get()->getEventBase()`
  may not actually be running.
* There may be more than one event base in the thread (unusual), or
  the EventBase in the code may not be registerd in EventBaseManager.
* The event bases in EventBaseManager may be used for different
  purposes, i.e. some are AsyncSocket threads, and some are
  AsyncServerSocket threads:  So you can't just grab the list of
  EventBases and call runInEventBaseThread() on all of them and expect
  it to do the right thing.

A much safer option is to explicitly pass around an EventBase, or use
an explicit pool of EventBases.

### SSLContext

SSL helper routines to load / verify certs.  Used with
AsyncSSLSocket.

## Generic Multithreading Advice

Facebook has a lot of experience running services.  For background
reading, see [The C10k problem](http://www.kegel.com/c10k.html) and
[Fast UNIX
servers](http://nick-black.com/dankwiki/index.php/Fast_UNIX_Servers)

Some best practices we've found:

1. It's much easier to maintain latency expectations when each
   EventBase thread is used for only a single purpose:
   AsyncServerSocket, or inbound AsyncSocket, or in proxies, outbound
   AsyncSocket calls.   In a perfect world, one EventBase per thread
   per core would be enough, but the implementor needs to be extremely
   diligent to make sure all CPU work is moved off of the IO threads to
   prevent slow read/write/closes of fds.
2. **ANY** work that is CPU intensive should be offloaded to a pool of
   CPU-bound threads, instead of being done in the EventBase threads.
   runInEventBaseThread() is fast:  It can be called millions of times
   per second before the spinlock becomes an issue - so passing the
   request off to a different thread is probably fine perf wise.
3. In contrast to the first two recommendations, if there are more
   total threads than cores, context switching overhead can become an
   issue.  In particular we have seen this be an issue when a
   CPU-intensive thread blocks the scheduling of an IO thread, using
   the linux `perf sched` tool.
4. For async programming, in contrast to synchronous systems, managing
   load is extremely hard - it is better to use out-of-band methods to
   notify of overload, such as timeouts, or CPU usage.  For sync
   systems, you are almost always limited by the number of threads.
   For more details see [No Time for
   Asynchrony](https://www.usenix.org/legacy/event/hotos09/tech/full_papers/aguilera/aguilera.pdf)
Warning
=======

These portability headers are **internal implementation details**.

They are intended to ensure that Folly can build on a variety of platforms.

They are not intended to help you build your programs on these platforms.

They are, and will remain, undocumented. They are, and will remain, subject to
rapid, immediate, and drastic changes - including full rewrites and merciless
deletions - without notice.

Note that before adding a new file to this directory you should determine
whether the API you are adding is a portability header or just a platform
dependent implementation detail. Only portability headers belong in this
directory. A portability header is defined as a header that provides the exact
API of some platform or configuration that is not available on all platforms.
If the API being added does not already exist on at least one of the platforms
Folly supports, then it is an implementation detail, and does not belong in
this directory.
# folly/tracing: Utility for User-level Statically Defined Tracing
----------------------------------------------------------

## StaticTracepoint

The `StaticTracepoint.h` header file defines the Macro
```
FOLLY_SDT(provider, name, arg1, arg2, ...)
```
Invoking the Macro will add a Static Tracepoint at the calling location. Using a
tracing toolkit ([BCC](https://github.com/iovisor/bcc) is an excellent example),
a probe can be attached to the Tracepoint, consume the provided arguments and
perform other tracing / profiling works.

The Tracepoint defined using `StaticTracepoint.h` is also compatible with any
toolkit designed for consuming [SystemTap](https://sourceware.org/systemtap/)
Tracepoints.

Internally, the Macro emits a `nop` operation at the calling location, along
with an Assembler Instruction with empty template and empty output Operands,
and the provided arguments and their sizes as input Operands.

The Macro then append to the ELF `.note` section, with information including
the provider and name of the Tracepoint, address of the `nop` operation, and
size and location (register name or memory location) of the provided arguments.
This way, the tracing toolkits would be able to parse the information, attach
the probes to the correct address, and consume arguments.

The default constraint for the arguments in the Assembler Instruction as
operands is `"nor"`. It means the argument could be an immediate integer
operand, a register operand or an offsettable memory operand. This is a good
default since tracing arguments tend to be integral, and the number of arguments
is likely to be less than the number of registers.

Otherwise, you may see compiler report errors like
```
'asm' requires impossible reload
```
You may want to simplify the Tracepoint (fewer and simpler arguments) in
such case. You may also choose to override the constraint
```
#define FOLLY_SDT_ARG_CONSTRAINT "g"
```
which means the arguments can be any memory or register operands.

You could also use
```
FOLLY_SDT_WITH_SEMAPHORE(provider, name, arg1, arg2, ...)
```
to create Tracepoints that could be gated on-demand. Before using this, add
```
FOLLY_SDT_DEFINE_SEMAPHORE(provider, name)
```
anywhere outside a local function scope. Then, you could use
```
FOLLY_SDT_IS_ENABLED(provider, name)
```
to check if probing on this Tracepoint is enabled. Tools like BCC and SystemTap
would increase the Semaphore when attaching to the Tracepoint and have the
check return true. This allows the Tracepoint to use more expensive arguments
which would only be calculated when needed. You can also check the enabled
status of the Tracepoint in another module. Add
```
FOLLY_SDT_DECLARE_SEMAPHORE(provider, name)
```
anywhere outside a local function scope first, then call the check Macro.
`gdb` scripts
-----------

This directory contains a collection of `gdb` scripts that we have found helpful.
These scripts use the [gdb extension Python API](https://sourceware.org/gdb/current/onlinedocs/gdb/Python.html#Python).

### How to run the scripts

To run the scripts, fire up `gdb` and load a script with `source -v`. Example:

```lang=bash
$ gdb -p 123456
(gdb) source -v ./folly/experimental/gdb/deadlock.py
Type "deadlock" to detect deadlocks.
# At this point, any new commands defined in `deadlock.py` are available.
(gdb) deadlock
Found deadlock!
...
```

### What does each script do?

#### `deadlock.py` - Detect deadlocks

Consider the following program that always deadlocks:

```lang=cpp
void deadlock3() {
  std::mutex m1, m2, m3;
  folly::Baton<> b1, b2, b3;

  auto t1 = std::thread([&m1, &m2, &b1, &b2] {
    std::lock_guard<std::mutex> g1(m1);
    b1.post();
    b2.wait();
    std::lock_guard<std::mutex> g2(m2);
  });

  auto t2 = std::thread([&m3, &m2, &b3, &b2] {
    std::lock_guard<std::mutex> g2(m2);
    b2.post();
    b3.wait();
    std::lock_guard<std::mutex> g3(m3);
  });

  auto t3 = std::thread([&m3, &m1, &b3, &b1] {
    std::lock_guard<std::mutex> g3(m3);
    b3.post();
    b1.wait();
    std::lock_guard<std::mutex> g1(m1);
  });

  t1.join();
  t2.join();
  t3.join();
}
```

The `deadlock.py` script introduces a new `deadlock` command that can help
us identify the threads and mutexes involved with the deadlock.

```lang=bash
$ gdb -p 2174496
(gdb) source -v ./folly/experimental/gdb/deadlock.py
Type "deadlock" to detect deadlocks.
(gdb) deadlock
Found deadlock!
Thread 2 (LWP 2174497) is waiting on mutex (0x00007ffcff42a4c0) held by Thread 3 (LWP 2174498)
Thread 3 (LWP 2174498) is waiting on mutex (0x00007ffcff42a4f0) held by Thread 4 (LWP 2174499)
Thread 4 (LWP 2174499) is waiting on mutex (0x00007ffcff42a490) held by Thread 2 (LWP 2174497)
```

NOTE: This script only works on Linux and requires debug symbols to be installed
for the `pthread` library.
Exception tracer library

This library allows you to inspect the exception stack at runtime.
The library can be used in three ways:

1. Link in the exception_tracer_base library.  You get access to the functions
in ExceptionTracer.h, but no stack traces.  This has no runtime overhead,
and is compliant with the C++ ABI.

2. Link in the (full) exception_tracer library.  You get access to the
functions in ExceptionTracer.h, the std::terminate and std::unexpected
handlers are installed by default, and you get full stack traces with
all exceptions.  This has some runtime overhead (the stack trace must be
captured and stored whenever an exception is thrown) added to throw
and catch, but no runtime overhead otherwise.  This is less portable
(depends on internal details of GNU's libstdc++).

3. LD_PRELOAD libexceptiontracer.so.  This is equivalent to #2 above, but
requires no link-time changes.  On the other hand, you need to ensure that
libexceptiontracer.so is compiled with the same compiler and flags as
your binary, and the usual caveats about LD_PRELOAD apply (it propagates
to child processes, etc).
Overview
--------

This is a flexible logging library for C++, targeted primarily at debug logging
support.  It supports hierarchical log categories to easily control debug log
levels.  It also aims to have minimal performance overhead for disabled log
statements, making it possible to keep debug log statements throughout the code
base, even in performance critical sections.  This allows debug log messages to
be easily turned on for particular areas of the code at runtime when necessary
to help debug an issue, without having to worry about the overhead of log
messages during normal use.

Log Categories
--------------

## Log Category Names

All log messages get logged to a particular log category.  Log category names
are hierarchical, separated by periods.  For instance, `folly.io` and
`folly.futures` are both sub-categories of `folly`.  `folly.io.async` is a
sub-category of `folly.io`.  The root category's name is the empty string.

## Log Level Checks

When a message is logged to a given category, an admittance check is performed
to see if the log message should be enabled.  The admittance check compares the
log level of the message against the effective level of that category.

By default the effective level of a category is the minimum of its level and
the level set for any of its parent categories.  This means that when you
increase the log verbosity for a particular category you automatically turn up
the verbosity for the entire tree of children categories underneath it.

For example, setting the log level for the `folly` category to `WARN` means
that log messages to any sub-category under `folly` will be admitted if they
have a level of `WARN` or higher.  If the level for `folly.io` is `DEBUG`, then
messages to all categories under `folly.io` will admit `DEBUG` and higher
messages, while the rest of the categories `folly` under folly would admit
`WARN` and higher messages.

However, you can also configure specific log categories to turn off inheritance
of their parent log levels.  This allows you to increase the log verbosity for
a large category tree, but still use a lower verbosity for specific
sub-categories.  For example, if the `folly` category's level is set to
`DEBUG`, but you disable level inheritance for `folly.futures`, the
`folly.futures` level will not use it's parent's `DEBUG` log level, and will
only consider the level set locally on this category.

Once a log message is admitted, it is processed by the `LogCategory` where it
was logged, as well as by all parent log categories, up to the root.

## Log Handlers

`LogHandler` objects can be attached to a log category.  When a log message is
received at a given log category it will be given to all `LogHandler` objects
attached to that category.

`LogHandler` objects can perform arbitrary actions based on the log message.
They may write the message to a local file, print it to `stderr` or `stdout`,
or send the message to a remote logging service.

`LogHandlers` may perform their own additional log level check, but by default
`LogHandlers` process all messages received at the category they are attached
to.

Motivation
----------

The goal of this logging library is to provide a flexible, easy to use logging
mechanism that allows debug log statements to be used liberally throughout a
code base.

There are two primary design goals for this library:

1. Log statements should be cheap when disabled.
2. It should be easy to control log levels for specific areas of the code base.

While there are a number of other logging libraries for C++, none of the ones I
have seen fulfill both criteria.  The Google logging library (glog) satisfies
the first goal, but not the second.  Most of the other log libraries I have
examined satisfy the second goal, but not the first.

In particular, for item 1, disabled log statements should boil down to a single
conditional check.  Arguments for the log message should not be evaluated if
the log message is not enabled.  Unfortunately, this generally means that
logging must be done using preprocessor macros.

Item 2 largely boils down to having hierarchical logging categories, to allow
easily turning log levels up and down for specific sections of the code base.
For instance, this allows a service to enable a higher log level for its
primary functionality, while having slightly lower levels for libraries that it
depends on.

Other Advantages
----------------

Beyond the primary goals mentioned above, this log library does have some other
advantages over glog:

## Support for using `folly::format()` to generate formatted log messages

Two separate mechanisms are provided for formatting log messages: basic
concatenation of arguments into string (using `folly::to<std::string>()`),
and more flexible formatting using `folly::format()`.  This provides convenient
and type-safe mechanisms for formatting log messages.

## Escapes unprintable characters in log messages by default.

This makes it safer to safer to log arbitrary input data, without worrying if
the data may contain potentially malicious terminal escape sequences.

For instance, this helps avoid vulnerabilities like CVE-2013-1862 and
CVE-2009-4496.

# Support for handling multi-line log messages

The LogMessage class indicates if the message contains internal newlines,
making it easier for handlers to add a log header to each line of the message,
avoiding subsequent lines that do not start with the correct log header.
