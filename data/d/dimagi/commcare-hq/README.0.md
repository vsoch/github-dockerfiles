"Minimalist" Skin
====================

A port of the default CKEditor skin, Moono, without the gradients.

Jeff Lyon
[Albatross Digital](albatrossdigital.com)
In all of the commands below, you will need `commcare-cloud` to be accessible.

```
commcare-cloud production ssh control

# check that commcare-cloud is accessible
$ commcare-cloud --help

$ cd /home/cchq/www/production/current
```

Create all necessary databases
```
python_env/bin/python scripts/cloudant/create_databases.py --databases `commcare-cloud production django-manage list_couchdbs` --username <myuser>
```

Generate a new api key and add it to all necessary dbs (read-only unless `--admin` is used)
```
python_env/bin/python scripts/cloudant/generate_api_key.py --databases `commcare-cloud production django-manage list_couchdbs` --username <myuser>
```

Revoke a api key from all necessary dbs
```
python_env/bin/python scripts/cloudant/revoke_api_key.py mynolongernecessaryapikey --databases `commcare-cloud production django-manage list_couchdbs` --username <myuser>
```

And for completeness, if you already have an API (and don't want to create a new one),
add it to all necessary dbs (read-only unless `--admin` is used)
```
python_env/bin/python scripts/cloudant/grant_api_key.py myexistingapikey --databases `commcare-cloud production django-manage list_couchdbs` --username <myuser>
```
This is an app for (usually single-use) scripts to be run on CommCare HQin commcare-hq root, run

bash app_builder_live_test/fetch_app_source.sh $username app_builder_live_test/hitlist.txt

Checkout master and then run

./manage.py build_apps app_builder_live_test/ master

Checkout feature branch and run

./manage.py build_apps app_builder_live_test/ feature

Then do a diff on the two directories:

diff -r app_builder_live_test/master app_builder_live_test/feature

OR

Just run ./app_builder_live_test/diff feature
See note in form_designer.html
# Pact Documentation

This is just some high-level pointers about the custom pact workflows.

## DOTs Processing

There is some good information on how the dots processing works on the mobile here: https://confluence.dimagi.com/display/pactsbir/Technical+Specifications.

On the HQ side this is mostly handled by the `process_dots_submission` function in `signals.py`.

Roughly what happens during a submissions is:

1. If a form is a DOTS form it is queued up for post-processing
2. This entails:
  1. Finding the relevant case.
  2. Running some calculations to get the latest DOTS data (`get_dots_case_json`).
  3. Submitting a *second* form that submits the DOTS data as a JSON case property. This should mirror the format of the confluence page above.


## CHW Schedules

Schedules are managed with a mapping of a user ID to a set of days.
You can view the schedule UI by going to "DOT Patient List" --> Search for a patient --> click on "profile" --> click on "schedule" tab.
This should take you to a page like this: https://www.commcarehq.org/a/pact/reports/custom/patient/?patient_id=66a4f2d0e9d5467e34122514c341ed92&view=schedule.
You can fill in a user for each day of the week and click "save" to save the schedule.

Behind the scenes what this does is appends the latest schedule to the `computed_` property on the case.
In particular it sets `case.computed_[PACT_SCHEDULES_NAMESPACE]` to a data structure that looks like:

```
{
    "pact_weekly_schedule": [
        {
            "comment": "",
            "doc_type": "CDotWeeklySchedule",
            "edited_by": null,
            "monday": "cs783",
            "started": "2014-10-17T18:29:09Z",
            "deprecated": false,
            "tuesday": "cs783",
            "friday": "cs783",
            "wednesday": "cs783",
            "thursday": "cs783",
            "sunday": null,
            "ended": "2014-10-17T18:29:12Z",
            "schedule_id": "f85d4686ede443ca99711cd114c49040",
            "created_by": "rachel@pact.commcarehq.org",
            "saturday": null
        },
        {
            "comment": "",
            "doc_type": "CDotWeeklySchedule",
            "edited_by": null,
            "monday": "cs783",
            "started": "2014-10-17T18:29:13Z",
            "deprecated": false,
            "tuesday": "cs783",
            "friday": "cs783",
            "wednesday": "cs783",
            "thursday": "cs783",
            "sunday": null,
            "ended": "2014-10-17T18:39:42Z",
            "schedule_id": "7654a0ba8ae245c784a8322a2d703cd0",
            "created_by": "rachel@pact.commcarehq.org",
            "saturday": null
        }
    ]
}
```

In addition to this a series of case properties named `dotSchedule[day]` e.g. `dotSchedulemonday` and `dotScheduletuesday` are set on the case that represent the *current* schedule.
This is accomplished by manually setting them when updated in `set_schedule_case_properties` as well as running a daily job to set them on all cases (if changed).
See `tasks.py` for more information on this.
dots observation by patient and date compound key.


dots structure is:

days [
   day_data, #anchor_date-len(days)
   day_data,
   day_data = [
    #nonart drug class
    [
        #dose observation
        [ <adherence>*, <method>*, <day_note>, <day_slot>],
        ...
    ],

    #art drug class
    [

        #dose observation
        [ <adherence>*, <method>*, <day_note>, <day_slot>],
        ...
    ]
   ]
   day_data, # == anchor_date
],

anchor_date (str)# Millennium Villages Project Reports

## Overview

MVP reports are build off of a very complicated indicator framework. The configuration for the indicators lives in a combination of the code and couch. The indicators themselves live on copies of the form and case documents that are saved to a second database (commcarehq__mvp-indicators). The indicators live in a property called `computed_`  which is added to the documents by two pillows (the `MVPFormIndicatorPillow` and `MVPCaseIndicatorPillow`). The pillows are also responsible for copying the document from the primary database to the secondary one, which happens at the same time.

## The `INDICATOR_CONFIGURATION` Document

The `INDICATOR_CONFIGURATION` document (which lives in Couch DB) maps domains to indicator namespaces. On prod there is only one namespace (`"mvp_indicators"`). This document is how CommCare HQ knows that a domain is using the indicators in this framework.

### Initializing the `INDICATOR_CONFIGURATION` Document

Create a document in Couch DB with the following structure:

```
{
   "_id": "INDICATOR_CONFIGURATION",
   "namespaces": {}
}
```

### Add a Project to the `INDICATOR_CONFIGURATION` Document

If your project has the slug `mvp-sauri` (this is what comes after
`www.commcarehe.org/a/ in your project's URL), then you would add the following
 to the `namespaces` dictionary, so that it looks like:

 ```
 "namespaces": {
    "mvp-sauri": [
        ["mvp_indicators", "MVP"]
    ]
 }
 ```

## The `IndicatorDefinition` documents

The `IndicatorDefinition` documents also live in the Couch Database. Each `IndicatorDefinition` has a number of attributes (namespace, domain, etc.) that describe how it should be applied to data.

Indicators get computed whenever a form or case is submitted. They can depend on the form/case itself as well as the forms/cases referenced in that form/case. They do not depend on any other indicators and only on primary data.

Here is a quick summary of some supported types.


Type                              | Purpose
----------------------------------|-----------------------
FormLabelIndicatorDefinition      | Map an xmlns to a label and save it on the document
FormDataAliasIndicatorDefinition  | Get a specific value from a form (based on a question ID)
CaseDataInFormIndicatorDefinition | Lookup a case property from the case that was submitted with the form
FormDataInCaseIndicatorDefinition | A _case_ indicator, that updates forms whenever they are submitted against a case


## Form processing

This walks through what happens when a form is processed by the pillow. An analogous set of steps happen for cases (although cases are actually more complicated).

1. The `change_transform` function handles deletions and then calls `process_indicators`
2. All `FormIndicatorDefinition` objects for the form's `(domain, xmlns)` combination are pulled out
3. Those `FormIndicatorDefinition`s are applied to the form in bulk
4. The form is saved back to the new database.

## Case processing

Case processing is very similar to form processing except there is a final step. All form-dependent indicators are applied to all the case's forms each time the case is processed. This means that the case processing can update indicators in forms!


## Debugging Tips

### Have a Copy of the Project, its Applications, and its Users on a Local Instance

1) Make sure your project has the same `slug`. For instance, if your project on
production is located at www.commcarehq.org/a/mvp-sauri/ make sure that locally
the project lives at localhost:8000/a/mvp-sauri/.

2) Make sure your LOCAL user is a Django Admin by going to localhost:8000/admin/
search for your user and checking staff and is admin. Then and subscribe your
project to the Dimagi Enterprise plan, by going to Project Settings > Current Subscription >
Change Plan and select Enterprise.

3) On the PRODUCTION machine, navigate to each application that project and
follow the steps outlined for [Transferring an Application Between
Projects or Servers](https://help.commcarehq.org/display/commcarepublic/Transferring+an+Application+Between+Projects+or+Servers)
to copy each application to your LOCAL project.

4) LOCALLY: Navigate to the Reports section of your project. If you do not
see the Administer Indicators option as a second tier of navigation (blue bar
below the main navigation), then add the project to your
`INDICATOR_CONFIGURATION` document in Couch DB (steps described earlier in
this document).

5) Once you are able to see the Administer Indicators option under reports
on the PRODUCTION copy of your application, navigate to Other Actions >
Download Indicators Export. Save the .json file. Visit the LOCAL copy of your
project space, and click on Bulk Import Indicators. Select the file you just
downloaded and upload the file. You should now have a copy of your indicator
definitions locally.

6) Copy the Mobile Workers from PRODUCTION by visiting your project space's Users
tab > Mobile Workers and clicking Bulk Upload. Download the Mobile Workers
excel spreadsheet and add a password for each mobile worker.

Make sure that the `celeryd` process is running LOCALLY:

```
python manage.py celeryd -v 2 -BE
````

Navigate to Users > Mobile Workers and click Bulk Upload. Upload the excel
file that you downloaded from production here.


### Submit Forms to Your Local Project Space

The best way to test whether or not your indicator views have the correct logic
is to submit real forms to your local instance.

1) For indicators to process incoming forms properly, you need to be running
pillowtop alongside your server instance. Do this by running:

```
python manage.py run_ptop --all
```

2) If you know the ID of your form, download its XML from the PRODUCTION copy
of your project space by visiting:

```
/a/<project_name>/reports/form_data/<form_id>/download/
```

3) LOCALLY: Go to your project space's Project Settings > Basic and un-check
"Only accept secure submissions"

4) Follow the steps outlined in the [Submission API help](https://help.commcarehq.org/display/commcarepublic/Submission+API)
to submit your downloaded form (as an .xml document) to your local copy of
CommCare HQ.


### Check Form Processing in Couch DB

Once you've submitted your form to HQ, you can see how it was processed by
visiting

```
http://localhost:5984/_utils/document.html?<database_name>/<form_id>
```

Things to look for:

- Is `mvp_indicators` populated with data? If no, then check:
    - is ptop running?
    - were there errors in the couch view? (look at your couch db's log file)

- Are the values what you expect?

- Are some of the indicators present, but others that should be there missing?
If so, check your couch view for those missing indicators, as you may have a
javascript error.


### Debugging Report Views

Both the MVIS and CHW reports have debug views that could be useful in gathering
document IDs that are contributing toward some indicator totals.

#### MVIS Debugging

The MVIS indicator API can be accessed by visiting:

```
/a/<project_name>/reports/custom/partial/health_coordinator/?indicator=<indicator_slug>&debug=true&cache=false&num_prev=1
```

`cache` parameter turns on and off caching. `num_prev` is the number of months
to include in the retrospective. An additional parameter called `current_month`
is the month you'd like to start the retrospective from. For example if we
wanted October 2014, we would specify `current_month=2014-10`.

NOTE: It's highly recommended that you only fetch one or two months at a time
(`num_prev` is 0 or 1) because some of the debugging calculations can take a VERY
long time.

#### CHW Debugging

The CHW indicator API can be accessed by visiting:

```
/a/<project_name>/reports/custom/partial/chw_manager/?indicator=<indicator_slug>&debug=true&cache=false
```
OpenClinica integration
=======================

Getting Started
---------------

This section is addressed to OpenClinica administrators, but it is
useful for project managers and field managers to know how studies are
managed with CommCare.

1. In OpenClinica, create the study, import the CRFs, and add all the
   users who will be using CommCare.

   When creating the users, please let the Dimagi/CommCare administrator
   know the convention you use to set their usernames, or give them the
   list of usernames. They will need this because the Study Metadata
   that OpenClinica provides includes the first names and last names of
   the users, but not their usernames, and corresponding users will need
   to be created on CommCare with matching usernames.

2. Save the Study Metadata from Study > "Download the study metadata
   **here**". Give this to the Dimagi/CommCare developer or project
   manager.

   They will store the Study Metadata in the project settings in
   CommCare, and add CommCare mobile workers with the same usernames,
   first names and last names.

3. Using CommCare, users will register subjects, and enter study data
   throughout the project.

4. In CommCareHQ, go to Reports > View All > Custom Reports: ODM Export.
   The report will list all the study subjects and their study events.

   If you do not have OpenClinica web services enabled for this
   project, you will need to add all the subjects and schedule their
   events in OpenClinica. This is necessary because OpenClinica does
   not import subjects or events via CDISC ODM.

5. Click the "Export to OpenClinica" button on the report. This will
   create a CDISC ODM document.

   If you have OpenClinica web services enabled for this project, this
   will also create the subjects for you and schedule the events of
   newly-created subjects. (You will need to schedule new events of
   existing subjects in OpenClinica due to limitations in event
   management in OpenClinica web services.)

   You can now import the CDISC ODM document into OpenClinica.


CommCare Integration with OpenClinica
-------------------------------------

CommCare integration with OpenClinica is bidirectional, in that
CommCare can import CDISC ODM-formatted study metadata to create an app,
and can export data using OpenClinica's Web Service, and as a CDISC ODM
document for OpenClinica to import.


Creating a CommCare app from Study Metadata
-------------------------------------------

Apps are created using a management command: ::

    $ python manage.py odm_to_app <domain> <app-slug> <odm-doc>

Generated apps have two case types, "subject" for study subjects, and a
child case type, "event" for the subject's study events. Questions will
have the name assigned to them in the study metadata.

Apps include a module for registering subjects. Subject screening is
out of the scope of the CRF documents that define a study, and so
subject registration introduces an important aspect of using CommCare
for clinical studies: CommCare can be used to manage workflow in a way
that OpenClinica cannot.

App builders can modify the generated app to include workflow processes,
and edit and split up forms in a way that makes them more useable. As
long as forms remain in modules of "event" case type and question names
match their CDSIC ODM IDs, the export will be able to build a CDISC ODM
document with all the necessary data.


OpenClinica Web Service
-----------------------

The OpenClinica web service is different from many other CommCare
integrations with third-party services in that the web service is best
suited to the end of a project, instead of as data arrives.

There are two reasons for this. The first is that the web service
accepts data in CDISC ODM format, which does not allow CommCare forms
to be submitted to OpenClinica as they arrive. It is best suited to
submitting complete data for a study subject. The second is that the
the web service has a limited ability to manage study events. (All data
for a subject is organised by study event.)

As a result, web service integration is associated with data export
instead of form submission. As mentioned before, we use the web service
to create subjects and schedule their study events in OpenClinica in
preparation for importing the CDISC ODM document.

For more information about the OpenClinica web service, see:
https://docs.openclinica.com/3.1/technical-documents/openclinica-web-services-guide


CDISC ODM Export
----------------

CDISC ODM is an XML-based format for exchanging clinical trial data. The
disadvantage of using an export is that the process is manual. But the
benefit is that building the export can be done entirely on the CommCare
side to meet the OpenClinica configuration, without any changes to
OpenClinica required.

For more information, see: http://www.cdisc.org/odm

.. NOTE:: This integration is written for OpenClinica 3.5. From version 3.6,
          the ``UpsertOn`` XML tag is available to perform imports of
          existing data.

ICDS Dashboard
==============

Information for the custom ICDS reporting dashboard. It can be accessed at \<url\>/a/\<domain\>/icds_dashboard.
Currently it's only possible for one domain on each environment to access this dashboard,
so only test locally and don't add random domains to the feature flag

Aggregate Data Tables
---------------------

child_health_monthly - unique rows for child_health case and month

agg_child_health - child_health data that is unique for location, age, gender, caste, etc

ccs_record_monthly - unique rows for ccs_record case and month

agg_ccs_record - ccs_record data that is unique for location, age, gender, caste, etc

agg_awc - unique rows for each location

Current workflow to get the data in these tables is shown [here](docs/current_state_aggregation.png)


Collecting New Data
-------------------

A flowchart to help guide you can be found [here](docs/new_indicator.png)

### Gather Requirements

- What pages will this be displayed?
- How will this be aggregated?
- Is this a property that is set and never changes, or a property that changes over time?
- How is this set in the app?
- What filters will be applied to this data?

### Collecting data

All data should be collected via a UCR data source.
Document lookups in these UCRs should be avoided as they increase processing time and related case changes are not picked up correctly
Location lookups are often necessary and ok. Use `ancestor_location` to ensure that there is only one database lookup.
If you absolutely need one, it should be a custom expression and heavily cached.

First look to see if a data source exists for the data you want to track.
If a data source does exist, add the appropriate column to the data source as a nullable column and rebuild the data source in place.
If an appropriate data source does not exist, create one in the dashboard UCR folder.

New UCRs should have the following data:
- Associated case or AWC id
- State id
- timeEnd (Only for forms. Tables should be partitioned on this attribute)
- received_on (Only for forms)
- data points from the app to be collected

### Aggregating the data

The work flow shown in the following picture is the eventual ideal,
and there is ongoing work to make all of the aggregation follow [this pattern](docs/goal_state_aggregation.png)

Currently Complementary Feeding Forms follows this work flow if you want an example.

If you're collecting data from a form, the first step is to aggregate the data per case id or awc id.
Then insert this data into the appropriate monthly table.
If necessary, pass it through to the next tables in the work flow (such as child_health information to agg_awc)

Think through the performance of your additions to this script. Previous mistakes:

- https://github.com/dimagi/commcare-hq/pull/19924

### Other Notes

- Don't look up other documents in a UCR
- Only collect raw data in the UCR. Use as few expressions in the UCR as possible.
- Keep the same names as the app as far as possible into the aggregation.
  It's very confusing when properties change between tables such as sex changing to gender.
- Prefer small_integer when possible and always use small_boolean instead of boolean
- When recording a property that can have multiple results, prefer an enumeration (using switch) instead of storing the raw value

Rebuilding UCR Data Sources
---------------------------

### Steps

1. Make changes to the UCR data source
   - Always add nullable columns so that the rebuilds can be done without deleting the table first
2. Kick off a rebuild using ./manage.py async_rebuild_table
   - This uses celery queues to rebuild the table so that the rebuild is parallelized
3. Monitor rebuild with "Asynchronous UCR Dashboard" in datadog

### Estimating Time to Rebuild

This is to give a small idea of how long a rebuild will take.
These should be periodically reviewed and updated as they will change as the project scales and improvements to scale data sources are added.

#### Important variables

- Number of forms/cases to be rebuilt
- Time it takes for one doc to be processed
  - Data sources without extra document lookups will be faster
  - Forms and cases likely have different times to process by default because forms also need to fetch from riak, but no current data on what that difference is
- Number of "ucr_indicator_queue"s we have deployed
- Size of current table/indexes
  - Theoretically larger tables and tables with more indexes are more expensive to insert to. We haven't done any performance tests on this
  - Can use table partitioning to solve this
- Other concurrent rebuilds
  - Currently the monthly tables for child_health and ccs_record are in the same queues and will take some processing as well

#### Basic formula

(number of forms/cases) * (doc processing time) / (number of queues)

#### Data

Currently number of queues on ICDS is 79

| Data Source Table | Per Doc Processing | Estimate of number of documents |
| --- | --- | --- |
| child_health monthly | 1.5 s | 100 per AWC |
| ccs_record monthly | 1.5 s | 50 per AWC |
| Complementary Feeding/PNC forms | 0.25 s | |

The complementary feeding and PNC forms should give a good baseline for documents we haven't rebuilt before, as they have few related documents.

Extracting forms references from case UCR data sources
------------------------------------------------------

### Steps

1. Identify form xmlns to be extracted from either (or both) child_health or ccs_record tableau data sources
2. Create a UCR data source for that form to collect the raw data necessary [Example here](https://github.com/dimagi/commcare-hq/blob/f19872d54fe482e130cdcf0f0c7e83eb1c894072/custom/icds_reports/ucr/data_sources/dashboard/postnatal_care_forms.json)
3. Add tests using forms from the QA domain (icds-dashboard-qa on india) [Example here](https://github.com/dimagi/commcare-hq/blob/f19872d54fe482e130cdcf0f0c7e83eb1c894072/custom/icds_reports/ucr/tests/test_pnc_form_ucr.py)
4. Add a model that will follow the same format as the tableau data sources (unique for case_id and month) [Example Here](https://github.com/dimagi/commcare-hq/blob/f19872d54fe482e130cdcf0f0c7e83eb1c894072/custom/icds_reports/models.py#L665-L725)
5. Create an aggregation helper that will take data from the UCR data source and insert it into the aggregate table [Example Here](https://github.com/dimagi/commcare-hq/blob/f19872d54fe482e130cdcf0f0c7e83eb1c894072/custom/icds_reports/utils/aggregation.py#L229-L315)
6. In that helper, write a query that compares it to the old data [Example Here](https://github.com/dimagi/commcare-hq/blob/f19872d54fe482e130cdcf0f0c7e83eb1c894072/custom/icds_reports/utils/aggregation.py#L317-L351)
7. PR & deploy this.
8. Build the UCR, likely using async_rebuild_table.
9. Aggregate the data using `aggregate` on the model.
10. Verify that the data is the same using `compare_with_old_data` on the model.
11. Change the aggregation script to use the new tables.
12. After some test time, remove the references to the old columns that you have replaced from the original tableau data source.

Metrics to follow/tradeoff
--------------------------
Processing time

UCR query time

Dashboard query time

Known areas that can be changed to improve performance
------------------------------------------------------
1. The aggregation step should be able to be split by state.
   These tasks can then be kicked off in parallel.
2. Caching of location lookups.
   Locations are mostly static so they can be cached quite heavily if we believe it's effective.
3. Moving to custom queries for some UCRs.

   Following up on [this PR](https://github.com/dimagi/commcare-hq/pull/20452) it could be useful experimenting with joins, multiple queries or SQL not supported in UCR reports.

   The highest ROI are moving reports based on ccs_record_monthly_v2, child_health_monthly_v2 and person_cases_v2 (in that order).

   The end goal being no longer needed either monthly UCR (queries only on the base case UCR & appropriate form UCR) and reducing the number of columns in person_cases_v2
4. Move to native postgres partitioning.

   Postgres 10 introduced a native partitioning feature that we could use.

   Postgres 11 will be adding some more features and performance improvements

   Currently the dashboard tables are manually partitioned by inserting directly into the partitioned tables and UCR data sources use triggers created by architect.
5. Reduce number of partitions on tables.

   Check constraints are processed linearly so having many partitions can negatively impact query times.

   Currently a new partition is created for every day in agg_awc_daily and every month 5 are created in agg_child_health & agg_ccs_record

   In postgres 11, this is less of an issue as the query planner can create better queries based on native partitioning
6. Make use of inserted_at and/or received on to intelligently update the tables
   Currently we loop over the previous month and fully delete are re-aggregate all data for the month.
7. Change the aggregation step to insert into temporary tables before dropping real table.

   This should reduce/eliminate any locking that is not needed and also remove any on disk inefficiency introduced by inserting then updating
8. Sort data before inserting into the aggregate table. Use BRIN indexes on those sorted columns
9. Include full location hierarchy in each table.

   Currently we join with a location table to get the location's name and full hierarchy. Testing this out may be useful
10. General postgres config updates.
11. Experiment with Foreign Data Wrappers

    a) Try out writing different UCR data sources to different databases and aggregating them on a separate dashboard database server

    b) Try out either moving old less accessed data to an older server or separating different state's data on different dashboard servers
This directory is for reports referenced in ICDS applications for mobile UCRs.
# dimagi.utils.dev

Utilities for developer testing.

# CouchDB Caching

## Why Cache?

Sometimes a page does too many couch queries that despite couch's advantages, can get slow when doing a lot.

However, while caching is easy, invalidation is hard. This framework seeks to make this easier.

## Caching Documents

cache_core has a wrapper method that calls your couch call and caches it based upon the doc_id.

## Caching Doc Properties

Likewise, cache_core can cache helper data for a given doc_id that's commonly requested. Say if there's supporting information you want
pegged to a version of a document, cache it alongside it based upon the doc_id and the custom property name. When the doc is invalidated, these
properties will be invalidated as well.

## Caching Views

Views are cached in a similar manner to the documents, using the view parameters as a key for the redis cache.

However, invalidation with views is difficult, especially with reduce views that don't necessarily have doc_ids with them.

To remedy this, we implemented a generational caching system for views, keyed by doc_type.

## Generational Caching of Views

For a given view, the view is dependent on a doc_type being part of its makeup. When a document is altered, its doc_type is noted.
If it matches a doc_type with known views that depend on it, the generation_id of these views will invalidate_all - invalidating all the views
associated with that doc_type.

The `GenerationCache` class is a registry for matching doc_types along with views to group them under 1 generational key.

At runtime, these are bootstrapped and created into a look up table to match doc changes and seeing if they need generation updates.


## Debugging

Use the debugdatabase via the devserver plugin to find slow areas of repeated queries.

You can toggle caching behavior by setting the `COUCH_CACHE_DOCS` and `COUCH_CACHE_VIEWS` localsettings flags True or False.

# Couchdbkit debug output for django-devserver

Install django-devserver

add `devserver` to your APPS or LOCAL_APPS

To your settings make sure `DEVSERVER_MODULES` has the devmodule added:

`DEVSERVER_MODULES = ('dimagi.utils.dev.couchdb_module.CouchDBDevModule',)`


If you want the full gory details of your couch use/abuse there are additional settings to add to your localsettings.py

`COUCHDB_DEVSERVER_VERBOSE=True # shows verbose output of views and gets`

`COUCHDB_DEVSERVER_STACKTRACE=True # shows last line of the stacktrace that calls the code in question`

`COUCHDB_DEVSERVER_STACK_SIZE=1 # integer number to specify lines of stack trace to show for view`

toggle
======

Simple couchdb-backed django app for doing user-level toggles.

Is designed to be _simple_ and _fast_ (automatically caches all toggles).

To use, make sure `toggle` is in your `INSTALLED_APPS` and `COUCHDB_DATABASES`.

To create a toggle:

```
./manage.py make_toggle mytogglename user1@example.com user2@example.com
```

To toggle a feature in code:

```python

if toggle_enabled('mytogglename', someuser.username):
    do_toggled_work()
else:
    do_normal_work()
```
This is an app that provides the phone facing API for CommCare phones.  It 
relies on the case model to generate appropriate case xml blocks for phones 
based on login credentials.pillowtop
=========
A couchdb listening framework to transform and process changes.

NOTE: this readme is out of date and does not reflect the latest changes to the library.
Please see [read the docs](http://commcare-hq.readthedocs.org/change_feeds.html) for more up to date information and best practices.


Django Config
=============

See CommCare HQ's `settings.py`for a complete example.

To configure a subset of pillows to run, just copy that setting to your `localsettings.py` and remove anything you don't want.


Running pillowtop
=================

    python manage.py run_ptop --all

This will fire off 1 gevent worker per pillow in your PILLOWTOPS array listening continuously on
the changes feed of their interest.

This process does not pool right now the changes listeners, so be careful,
or suggest an improvement :)

You can also run this for only a single pillow in your PILLOWTOPS array with:

    python manage.py run_ptop --pillow-key=KEY

Pillowtop also will keep checkpoints in couch so as to not keep going over changes when the
process is restarted - all BasicPillows will keep a document unique to its class name in the DB
to keep its checkpoint based upon the _seq of the changes listener it is on.


Understanding pillowtop
=======================

At its core, pillowtop can be thought of as executing the following pseudo-code:

    for line in get_changes_forever():
        if filter(line):
            intermediate_1 = change_trigger(line)
            intermediate_2 = change_transform(intermediate_1)
            change_transport(intermediate_2)

Conceptually, it may be easier to think of if you think of pillowtop as an ETL tool.
Doing that the methods roughly map as follows (using the common examples in our stack):

```
change_trigger --> extract --> get document from couch
change_transform --> transform --> reformat document (this is often a no-op)
change_transport --> load --> save document somewhere else (usually elastic search or postgres)
```

The various subclasses of pillows override various parts of these depending on what they are trying to do.
Two important ones are `AliasedElasticPillow` and `PythonPillow`.

AliasedElasticPillow
--------------------

`AliasedElasticPillow` conceptually maps the following functions:

```
change_trigger --> if the document is being deleted, delete it in elasticsearch as well. otherwise return it from couch.
change_transform --> do some fancy stuff with indices and then save to elastic
```

All of the rest of the complicated logic inside it is related to index management and the process of saving to elastic.
It would be nice if these were more encapsulated.


PythonPillow
------------

PythonPillow conceptually doesn't touch any of the ETL functions.
Instead it just provides a wrapper around around the processing, such that instead of relying on couch-based filters on the changes feed, it uses python filters.
It also adds the ability to process documents in chunks.

It would be nice if you could use PythonPillow as more of a mixin instead of subclassing it, but this is not possible today.


Extending pillowtop
===================

Use `ConstructedPillow` whenever possible.
Fluff
=====
Fluff is a library that works with pillowtop and couchdbkit and
lets you define a set of computations to do
on all docs of a `doc_type`, i.e. perform a map over them, and then use
couchdb to aggregate over the output.

The advantages of this over a normal map reduce are that you get to write
your map in python with full access to the database.

This document describes the intended capabilities;
what's currently here is very preliminary.

Example:

```python

import fluff

class VisitCalculator(fluff.Calculator):

    @fluff.date_emitter
    def all_visits(self, case):
        for action in case.actions:
            yield action.date

    @fluff.date_emitter
    def bp_visits(self, case):
        for action in case.actions:
            if is_bp(case):
                yield action.date

    @fluff.custom_date_emitter('max')
    def temp_max(self, case):
        for action in case.actions:
            if is_temp(case):
                yield [action.date, action.temperature]
    
    @fluff.date_emitter
    def group_list(self, case):
        # Note that you can override the group_by values as follows.
        # They MUST always match up in number and ordering to what is defined
        # in the IndicatorDocument class that this calculator is included in.
        yield dict(date=date(2013, 1, 1), value=3, group_by=['abc', 'xyz'])


class MyIndicators(fluff.IndicatorDocument):
    document_class = CommCareCase
    group_by = (
        # this is the standard style of group_by
        'domain',
        # this is the more complicated style of group_by - redundant here,
        # but useful for more complex things
        # note: if you use anything more complicated than a string (like here),
        # group_by should be a tuple, else couchdbkit will complain
        fluff.AttributeGetter('owner_id', getter_function=lambda item: item['owner_id']),
    )
    domains = ('droberts', 'test', 'corpora')

    visits_week = VisitCalculator(window=timedelta(days=7))
    visits_month = VisitCalculator(window=timedelta(days=30))


# add this pillow to settings.PILLOWTOPS
MyIndicatorsPillow = MyIndicators.pillow()

```

By creating a simple setup of this sort, you'll get a bunch of stuff for free:

* Whenever a doc changes, the corresponding indicator document will be updated
* You can get aggregated results back straight from couch with a simple
`MyIndicators.get_result('visits_week', key=[domain, owner_id])`, which will be correct
for the current date/time with no real-time computation, and will return the
data in the following format:

    ```json
    {
        "all_visits": 26,
        "bp_visits": 15,
        "bp_max": 140
    }
    ```

## Emitting custom values
Yield a list where the second value in the list is the value you want to be emitted.

This is useful if you want to do more than just count events. Options for aggregation are:
  * count
  * sum
  * max
  * min
  * sumsqr


In the example above the `temp_max` emitter emits `action.temperature` for each action.
It also specifies that the final value should be the `max` of all the emitted values in the date range.


Dynamically export your couch models to excel (or other formats).## Debugging functions

Your options are:
1. Log from inside the function
  * http://www.postgresql.org/docs/current/static/plpgsql-errors-and-messages.html
2. Use the pgadmin debugger (see below for installation instructions)

### Install pgadmin3 debugger

Install prerequisites:
* libreadline-dev
* postgresql-server-dev-9.X

Then follow instructions here: http://kirk.webfinish.com/?p=277

**Note if you have multiple versions of PG installed**
You need to build the extensions for the correction version of PostgreSQL. To do this
you must supply the *PG_CONFIG* environment variable:

  $ pwd
  /path/to/postgresql-9.4.5/contrib
  $ PG_CONFIG=/usr/lib/postgresql/9.4/bin/pg_config make
  $ cd pldebugger
  $ PG_CONFIG=/usr/lib/postgresql/9.4/bin/pg_config USE_PGXS=1 make
  $ sudo PG_CONFIG=/usr/lib/postgresql/9.4/bin/pg_config USE_PGXS=1 make install
# Migrating certain doc types to their own db

## Do prepwork to decouple your doc types

**Note**: These instructions are for people *writing* a migration.
If you're interested in running a migration someone else already wrote,
see [Running the doctype migration](#run-the-doctype-migration) below.

Do a full-text search for each doc_type you're migrating across all `map.js` files
```bash
$ grep -r --include=map.js CommCareUser
```
Are each of those views going to work properly after the doctype is migrated to the new database?

Do any work you need to in order make sure that the doc_types in the apps you're migrating are decoupled
from other ones:
- You may need to break apart design documents so that:
  - Any views that need to be in the new db will end up in the new db
  - Any views that need to be in the current db will remain in the current db
- You may need to have certain design documents show up on *both* the current and new dbs
  - If there are functions that referenced these views wanting both,
    you may need to rewrite those functions to check both dbs
- etc.


## Setting up the migration

### Register the new database
This step creates a new database and allows you to start populating it.
The new database will not yet be used by any production code.

Add variables to `settings.py` representing (1) the database you're currently
using for the apps you're migrating, probably set to `None` (== main db), and
(2) the database you _will_ be using.

Add the new db to the list of extra databases in `COUCH_SETTINGS_HELPER`.

```python
# settings.py

NEW_USERS_GROUPS_DB = 'users'  # the database we will be using
USERS_GROUPS_DB = None  # the database to use (will later be changed to NEW_USERS_GROUPS_DB)
...
COUCH_SETTINGS_HELPER = CouchSettingsHelper(
    COUCH_DATABASE,
    COUCHDB_APPS,
    [NEW_USERS_GROUPS_DB],  # list of secondary databases to register
)
```

### Specify which database to read/write docs to
You'll be migrating at module-level granularity, so replace the modules'
entries in `COUCHDB_APPS` with a `('module_name', DB_TO_USE_FOR_MODULE)` tuple.
```python
# settings.py
...
COUCHDB_APPS = [
...
    ('groups', USERS_GROUPS_DB),
    ('users', USERS_GROUPS_DB),
...
]
```
Remember, `USERS_GROUPS_DB` will point to the main db until you flip it to the
new one in a later step.

### Register the migrator instance
In `corehq/doctypemigrations/migrator_instances.py`, add an object representing your migration
going off the following model:

```python
users_migration = Migrator(
    slug='user_db_migration',
    source_db_name=None,
    target_db_name=settings.NEW_USERS_GROUPS_DB,
    doc_types=(
        'Group',
        'DeleteGroupRecord',
        'UserRole',
        'AdminUserRole',
        'CommCareUser',
        'WebUser',
        'Invitation',
        'DomainRemovalRecord',
        'OrgRemovalRecord',
    )
)
```
You'll want to be deliberate about assembling the list of doc types, but as a
starting point, you can try:
```python
import inspect
from corehq.apps.app_manager import model
for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj) and issubclass(obj, models.Document):
        print name
```
(do make sure that you're including only doc types defined *in* the app)

### Specify which databases need which views
The migrator instance will take care of syncing documents to the new db, but
you also need to control which views to start indexing in the new db. Enter
`ExtraPreindexPlugin`.  In a module's `AppConfig`, you can register that
module's design docs to additional databases:

```python
from corehq.preindex import ExtraPreindexPlugin
from django.apps import AppConfig
from django.conf import settings

class UsersAppConfig(AppConfig):
    name = 'corehq.apps.users'

    def ready(self):
        ExtraPreindexPlugin.register('users', __file__, settings.NEW_USERS_GROUPS_DB)
```
There, now the module's views will be in both the old database (as per the line
in `COUCHDB_APPS`), and the new database.

We have some views which aren't tied to modules, some of which are meant to
work on roughly all doc types.  Take a look at `corehq/couchapps/__init__.py`
and make sure to register the appropriate views to your new database.  That
module's README should have some more context.

### Deploy migrator
This can be merged whenever, as the new database will not be used until later, when you flip to it.


## Run the doctype migration

All of the following commands should be run in a screen as the cchq user on a production machine. You can do that by running these commands:

```bash
sudo -iu cchq bash
script /dev/null  # to "own the shell" for screen to work
screen
# hit enter to pass screen's opening page.
# If the current release is too old, set up a new release and use that instead
cd /home/cchq/www/production/current
source python_env/bin/activate
```

To see your options run

```bash
$ ./manage.py run_doctype_migration
CommandError: You may run either of the following commands

./manage.py run_doctype_migration <slug> --initial
./manage.py run_doctype_migration <slug> --continuous

with with the following slugs:

user_db_migration

```

The migration we want to run is called `user_db_migration`, as listed in the help message.

To get a general idea of what we're dealing with, run

```bash
$ ./manage.py run_doctype_migration user_db_migration --stats
Source DB: https://commcarehq:****@commcarehq.cloudant.com/commcarehq
Target DB: https://commcarehq:****@commcarehq.cloudant.com/commcarehq__users

           doc_type             Source  Target
AdminUserRole                   0       0
AdminUserRole-Deleted           0       0
CommCareUser                    82031   0
CommCareUser-Deleted            1       0
DeleteGroupRecord               2904    0
DeleteGroupRecord-Deleted       0       0
DomainRemovalRecord             1259    0
DomainRemovalRecord-Deleted     0       0
Group                           20981   0
Group-Deleted                   2885    0
Invitation                      8498    0
Invitation-Deleted              0       0
OrgRemovalRecord                1       0
OrgRemovalRecord-Deleted        0       0
UserRole                        38102   0
UserRole-Deleted                0       0
WebUser                         13151   0
WebUser-Deleted                 0       0
```

You'll see that by default `-Deleted`-suffixed doc_types are also added to the migration.

Staging cannot create new databases, so you'll need to manually create the appropriate database through cloudant's UI.  It'll be something like `staging_commcarehq__users`.

Now you can begin. Run

```bash
$ ./manage.py run_doctype_migration user_db_migration --initial
```

To do the main dump. You may notice that nothing appears in the target db for a long time.
That is because data is first copied from the source db to `./user_db_migration.log`, and then copied from that file
to the target db.

Once this is done you can check `--stats` again for a basic sanity check. Then run

```bash
$ ./manage.py run_doctype_migration user_db_migration --continuous
```

for a continuous topoff based on the couchdb changes feed.
As that's running, you can check `--stats` to monitor whether you're fully caught up.
`--continuous` will also output "All caught up" each time it reaches the end of the changes feed.

If you're running this after the blocking migration has already been added to the code then you can go ahead and re-deploy which will flip the DB. Don't forget to clean up afterward (see below).


## Flipping the db

Once you're confident the two databases are in sync and sync'ing in realtime,
you'll need to make some commits.

### Commit 1: Add a blocking django migration
Add a blocking django migration to keep anyone from deploying before migrating:

```
./manage.py makemigrations --empty doctypemigrations
```

and then edit the generated file:

```diff
  from django.db import models, migrations
+ from corehq.doctypemigrations.djangomigrations import assert_initial_complete
+ from corehq.doctypemigrations.migrator_instances import users_migration

      operations = [
+         migrations.RunPython(assert_initial_complete(users_migration))
      ]
```

### Commit 2: Flip the db
And then actually do the flip; edit `settings.py`:

```diff
  NEW_USERS_GROUPS_DB = 'users'
- USERS_GROUPS_DB = None
+ USERS_GROUPS_DB = NEW_USERS_GROUPS_DB
```

### Commit 3 [maybe]: Use new views
If there are views with different names in the old and new dbs, your flip PR
should also update those names.

### Commit 4 [maybe]: Flip pillowtop and/or elasticsearch
If a doctype you're migrating is read by pillowtop, you'll need to reset the
checkpoint after the merge.  If it's an elasticsearch pillow, you can instead
trigger an index rebuild by updating the index name in the appropriate mapping
file.

### Do it!
PR, and merge it. Then while `--continuous` is still running, deploy it.

Once deploy is complete, kill the `--continuous` command with `^C`.

## Cleanup

### Delete documents from old db
After you're confident in the change and stability of the site,
it's time to delete the old documents still in the source db.

First you should clean up any doc conflicts, as that can get in the way of
deleting stuff.

```bash
$ ./manage.py delete_doc_conflicts
```

Now you can actually delete the documents:

```bash
$ ./manage.py run_doctype_migration user_db_migration --cleanup
```

Keep in mind that this will likely incur some reindexing overhead in the source db.

If you run `$ ./manage.py run_doctype_migration user_db_migration --stats`, you
should see that only the target database has these doc types in it now.
Updating SQL Case and Form models
---------------------------------

1. Update python models
2. Run command
  - `python manage.py makemigrations form_processor`
3. Update psycopg2 type adapters
  - `corehq/form_processor/utils/sql.py`
3. Update SQL functions. Most likely these ones but possible others:
  - `save_form_and_related_models.sql`
4. Run commands:
  - `./manage.py makemigrations sql_accessors --empty`
5. Add operations to empty migration to update the changed SQL functions
6. Run `form_processor` tests


Renaming a SQL function
-----------------------

1. Rename the function definition
2. Rename the function references
3. Rename the function template file to match the function name
4. Create a new migration to delete the old function and add the new one
5. Delete any references to the old SQL template file in old migrations (or
replace them with a `noop_migration` operation if it is the only operation in the migration)
6. Do steps 3-5 for the plproxy function as well


Updating a SQL function
-----------------------

1. Make a copy of the file the function is being declared in with a new name
   e.g. `get_case.sql -> get_case_2.sql`
    1. We do this avoid situations where the migrations aren't added which
    wouldn't fail in tests but would fail in production.
2. Rename the SQL function so both versions can coexist (to prevent failures
   during deploy, and so the function can be reverted).
3. Create a migration to drop and re-create the new function.
    1. Make sure you include any context variables required in the function

    ```
    # -*- coding: utf-8 -*-
    from __future__ import absolute_import
    from __future__ import unicode_literals
    from django.db import migrations
    from corehq.sql_db.operations import RawSQLMigration

    migrator = RawSQLMigration(('corehq', 'sql_accessors', 'sql_templates'), {
        'context_key': 'context_value'
    })

    class Migration(migrations.Migration):

        dependencies = [
            ('sql_accessors', 'XXXX_migration_name'),
        ]

        operations = [
            migrator.get_migration('get_case_2.sql'),
        ]
    ```

4. Make changes to the function as required.
5. Update callers of the function in code to point to the new function.

If the function signature is changing:

6. Repeat steps 1-4 above for the pl_proxy function (file in `corehq/sql_proxy_accessors`)

Make a separate PR to drop the old function (to be merged later) following [this
example](https://github.com/dimagi/commcare-hq/pull/19195):

1. Create a new migration to drop the old function:
    ```
    $ ./manage.py makemigrations sql_accessors --name drop_OLD_FUNCTION_NAME_fn --empty
    ```
    Edit this file to run the `DROP FUNCTION...` line of the old `.sql` file:
    ```
    from __future__ import absolute_import
    from __future__ import unicode_literals

    from django.db import migrations

    from corehq.sql_db.operations import HqRunSQL


    class Migration(migrations.Migration):

        dependencies = [
            ('sql_accessors', '0057_filter_get_reverse_indexed_cases'),
        ]

        operations = [
            HqRunSQL("DROP FUNCTION IF EXISTS get_reverse_indexed_cases(TEXT, TEXT[]);"),
        ]
    ```
2. Delete the `.sql` files containing the old function definition.
3. Replace all references to the old file in existing migrations with `noop_migration`
    1. Or you can just remove it completely if there are other migration operations
    happening in the migration.
4. Repeat the above for the pl_proxy function defined in `sql_proxy_accessors`
   if applicable.

These `HqRunSQL` operations can later be replaced with `noop_migration`s, but
there's no urgency in that, so we can wait until someone goes through and
squashes all these migrations.
================
A django application for integrating with the UNICEL SMS gateway 
================

PUSH SMS URL (to send outgoing sms): 

http://www.unicel.in/SendSMS/sendmsg.php?uname=[account]&pass=[password]&send=Promo&dest=[destination]&msg=[content]

Inbound SMS URL
http://yourdomain.com/unicel/in/&send=[sender]&dest=[destination]&msg=[content]&stime=[m/d/y h:m:s AM/PM]Based on the django-timezones app
=================================

Source: https://github.com/brosner/django-timezones

Data Warehouse
==============
See background [design document](https://docs.google.com/document/d/1sMTEAG-iZyo0nfp2S4sUaN2MgY31Z8B3kRDBqPFXvnI/edit#)
for an overview of design of our data warehouse. This doc mainly explains steps for developing warehouse models.

## Key Models

All the data required to filter and render a particular report is captured in that report's 'facts' data models.
CommCareHQ's raw data models are processed to extract report 'facts'.
This process can be thought of as an ETL.
The warehousing app consists of various data models, the ETL processing code and some additional
utilities such as Airflow to administer the ETL process.

Below describes data warehouse models and the process to load and clear the data for these models.

There are three kinds of warehouse data models. Fact, Dimension and Staging models.
Generally, fact models represent final report data, dimension models represent the 'dimensions' under which report
data can be filtered and staging models represent raw data read from CommCareHQ's raw data models before they are
inserted into a dimension or fact table.
See `facts.py`, `dimensions.py` and `staging.py` for examples.

Each data model has a `dependencies` attribute that specifies what other data model data it depends on.

ETL involves running commands to:

- initialize a 'batch' to indicate date range for the data
- for the batch date range, load raw data into staging tables, and then 
- process staging tables to insert data into dimension and fact tables. 

Most of ETL business logic lives in raw SQL queries. See `corehq.warehouse.transforms.sql`.

## Commands

Use `create_batch` to create a batch. This just creates a new batch record.

```
./manage.py create_batch 222617b9-8cf0-40a2-8462-7f872e1f1344 -s 2012-05-05 -e 2018-06-05
```

Use `commit_table <data_model_slug> <batch_id>` to load the data of data_model for the duration specified by the batch_id.

E.g.

```
./manage.py commit_table user_staging 222617b9-8cf0-40a2-8462-7f872e1f1344
```

Note that you may have to run this for given data model's dependencies first to load data.

To flush staging data of a particular batch use `./manage.py clear_staging_records`.
During the development, you could use `TRUNCATE TABLE` (or `./manage.py migrate warehouse zero`) sql commands to clear fact/dimension data.
MOTECH
======

MOTECH is a Data Integration Layer

It allows sending simple and aggregate data payloads to third-party
systems when certain triggers are met. Triggers and Payloads are easily
defined through custom methods in the MOTECH codebase, and a full suite
of management tools is available to audit and debug sent, queued and
cancelled messages.

Currently, MOTECH is fully integrated to leverage CommCare's frameworks,
including:

* To take advantage of CommCare HQ's multi-tenant architecture
* To make it easier and faster for CommCare HQ developers to maintain
and extend it, considering CommCare integrations are the primary use
case currently.
* If you are interesting in using this without the full CommCare
scaffolding, please reach out to the mailing list to discuss.


Framework
---------

MOTECH is designed to enable multiple types of integration:

* Simple transactional integration where a single action triggers one or
more atomic messages with third-party systems in either direction.  An
example is importing OpenMRS patients into CommCare.
* Complex transactional integration where a single action requires
multiple API calls to complete the integration.  An example is a single
registration form in CommCare generating a patient and encounter in
OpenMRS.
* Aggregate data integration where multiple actions in CommCare are
aggregated and the result is pushed to a third-party system.  An example
is CommCare transactional data being aggregated into a
[Data Source](../apps/userreports/README.md) and being pushed to DHIS2
as aggregate data.


Current Integrations
--------------------

MOTECH currently allows for the following integrations:

* Standard trigger-based integration which forwards all CommCare Case,
Form or Application data to any third-party endpoint. This requires no
code, and is easily configured through a UI.
* Custom trigger-based integrations sending custom payloads to any
third-party endpoint. Triggers and Payloads are defined in code.
* DHIS2
* OpenMRS


Repeaters
---------

Repeaters allow integrators to send data from CommCare and send it as an
authenticated user to third-party systems over HTTP or HTTPS.

MOTECH ships with a suite of **standard repeaters** which can be enabled
through the MOTECH management dashboard. These send all case, form, or
application data to any third-party endpoint. The payload for these is
sent whenever a change is detected. The schema is
[predefined](https://confluence.dimagi.com/pages/viewpage.action?pageId=12224128)
and can be sent as either `XML` or `JSON`.

**Custom repeaters** are defined in code, and subclass any of the
`BaseRepeater` classes. They allow the developer to create custom
payloads that can compile data from multiple sources and be sent as
`JSON` or `XML`. Custom triggers for when to
send this data are also defined in code. These trigger methods are run
whenever the model in question (`case`, `form`, or `application`) is
changed.

All repeaters are hooked into the **MOTECH management dashboard**. This
allows project managers to create and delete specific repeater
instances, and contains tools to audit and debug sent, queued and
cancelled messages.

You can find more details in [the Repeaters README](./repeaters/README.md).


DHIS2 Module
------------

[DHIS2](https://www.dhis2.org/) is a Health Information System that
offers organisations and governments a visual dashboard of health-
related data, across geographical areas, time periods, and demographics.

DHIS2 allows third-party systems like CommCare to send it two kinds of
data:

* Data that pertains to single events and individuals, for DHIS2 to
aggregate within DHIS2.
* Data that has already been aggregated

The DHIS2 integration module in MOTECH enables aggregate data to be sent
to DHIS2. Currently, the DHIS2 module does not send individual data.

CommCare aggregates and categorises data for DHIS2 using UCRs, and sends
it at regular intervals.

Configuring a DHIS2 server is done under *Project Settings* >
*DHIS2 Connection Settings*. Mapping UCR columns to DHIS2 data types is
done under *Project Settings* > *DHIS2 DataSet Maps*


OpenMRS (& Bahmni) Module
-------------------------

[OpenMRS](https://openmrs.org/) is used for storing and managing patient
data. [Bahmni](https://www.bahmni.org/) is an EMR and hospital system
built on top of OpenMRS. Integration with Bahmni implies integration
with OpenMRS.

### Importing data from OpenMRS to CommCare

CommCare can import data from OpenMRS using OpenMRS's Reporting API and
OpenMRS's Atom feed API. The Reporting API is used for periodic imports,
for example monthly. The Atom feed API is for importing data as it is
added or changed in OpenMRS.

### Sending data from CommCare to OpenMRS

CommCare sends data to OpenMRS using its Web Services API.

All data sent to OpenMRS relates to what OpenMRS refers to as
"patients", "visits", "encounters" and "observations". In CommCare these
correspond to properties of one or a handful of case types, and values
of form questions.

CommCare uses Repeaters to build and send a workflow of requests to
OpenMRS, populated using both cases and forms.

Using an OpenMRS Repeater in conjunction with its OpenMRS server's Atom
feed allows bidirectional live updates.


History
-------

There was a previous version of MOTECH based on
[OSGI](https://www.osgi.org/) and the
[Spring Framework](https://projects.spring.io/spring-framework/)
originally developed by the Grameen Foundation.  Information on MOTECH
1.0 can be found [here](http://docs.motechproject.org/en/latest/). This
platform supported both web-application use cases as well as data
integration.  Due to the incompatability of OSGI and Spring in
subsequent releases, MOTECH is now focused on data integration.
MOTECH Repeaters
================

See the [MOTECH README](../README.md#repeaters) for a brief introduction to repeaters.


How Do They Work?
-----------------

A good place to start is [signals.py](TODO). From the bottom of the file you can see that a repeat record is created when a form is received, or after a case or user or location is saved.

The `create_repeat_records()` function will iterate through the [`Repeater`](./models.py) instances of a given class type that are configured for the domain. For example, after a case has been saved, `create_repeat_records()` is called with `CaseRepeater`, then `CreateCaseRepeater` and then `UpdateCaseRepeater`. A domain can have many CaseRepeaters configured to forward case changes to different URLs (or the same URL with different credentials). The `register()` method of each of the domain's CaseRepeaters will be called with the case as its payload.

The same applies to forms that are received, or users or locations that are saved.

The `register()` method creates a `RepeatRecord` instance, and associates it with the payload using the payload's ID. The RepeatRecord's `next_check` property is set to `datetime.utcnow()`.

Next we jump to [tasks.py](./tasks.py). The `check_repeaters()` function will run every `CHECK_REPEATERS_INTERVAL` (currently set to 5 minutes). Each RepeatRecord due to be processed will be added to the CELERY_REPEAT_RECORD_QUEUE.

When it is pulled off the queue and processed, if its Repeater is paused it will be postponed. If its Repeater is deleted it will be deleted. And if it's waiting to be sent, or resent, its `fire()` method will be called ... which will call its Repeater's `fire_for_record()` method.

The Repeater will transform the payload into the right format for the Repeater's class type and configuration, and then send the transformed data to the Repeater's destination URL.

The response from the destination will be handled according to whether the request succeeded, failed, or raised an exception. It will create a RepeatRecordAttempt, and may include other actions depending on the class of Repeater.

RepeatRecordAttempts are listed under Data Forwarding Records.
MOTECH's OpenMRS Module
=======================

See the [MOTECH README](../README.md#openMRS----bahmni--module) for a
brief introduction to OpenMRS and Bahmni in the context of MOTECH.


The OpenmrsRepeater
-------------------

The OpenmrsRepeater is responsible for updating OpenMRS patients with
changes made to cases in CommCare. It is also responsible for creating
OpenMRS "visits", "encounters" and "observations" when a corresponding
visit form is submitted in CommCare.

It is different from other repeaters in two important details:

1. It updates the OpenMRS equivalent of cases like a CaseRepeater, but
it reads forms like a FormRepeater. So it subclasses CaseRepeater, but
its payload format is form_json.

2. It makes many API calls for each payload.


OpenmrsConfig
-------------

Configuration for an OpenmrsRepeater is stored in an OpenmrsConfig
document. Patient data, which is mapped from a CommCare case, is stored
in OpenmrsConfig.case_config, and adheres to the OpenmrsCaseConfig
document schema. Event, encounter and observation data, which is mapped
from CommCare forms, is stored in OpenmrsConfig.form_configs.

Currently we support one case type and multiple forms. That may change
in the future if we need to map multiple CommCare case types to OpenMRS
patients.


An OpenMRS Patient
------------------

The way we map case properties to an OpenMRS patient is based on how
OpenMRS represents a patient. Here is an example of an OpenMRS patient
(with some fields removed):

```javascript
    {
      "uuid": "d95bf6c9-d1c6-41dc-aecf-1c06bd71386c",
      "display": "GAN200000 - Test DrugDataOne",

      "identifiers": [
        {
          "uuid": "6c5ab204-a128-48f9-bfb2-3f65fd06785b",
          "identifier": "GAN200000",
          "identifierType": {
            "uuid": "81433852-3f10-11e4-adec-0800271c1b75",
          }
        }
      ],

      "person": {
        "uuid": "d95bf6c9-d1c6-41dc-aecf-1c06bd71386c",
        "display": "Test DrugDataOne",
        "gender": "M",
        "age": 3,
        "birthdate": "2014-01-01T00:00:00.000+0530",
        "birthdateEstimated": false,
        "dead": false,
        "deathDate": null,
        "causeOfDeath": null,
        "deathdateEstimated": false,
        "birthtime": null,

        "attributes": [
          {
            "display": "primaryContact = 1234",
            "uuid": "2869508d-3484-4eb7-8cc0-ecaa33889cd2",
            "value": "1234",
            "attributeType": {
              "uuid": "c1f7fd17-3f10-11e4-adec-0800271c1b75",
              "display": "primaryContact"
            }
          },
          {
            "display": "caste = Tribal",
            "uuid": "06ab9ef7-300e-462f-8c1f-6b65edea2c80",
            "value": "Tribal",
            "attributeType": {
              "uuid": "c1f4239f-3f10-11e4-adec-0800271c1b75",
              "display": "caste"
            }
          },
          {
            "display": "General",
            "uuid": "b28e6bbc-91aa-4ba4-8714-cdde0653eb90",
            "value": {
              "uuid": "c1fc20ab-3f10-11e4-adec-0800271c1b75",
              "display": "General"
            },
            "attributeType": {
              "uuid": "c1f455e7-3f10-11e4-adec-0800271c1b75",
              "display": "class"
            }
          }
        ],

        "preferredName": {
          "display": "Test DrugDataOne",
          "uuid": "760f18ea-9321-4c31-9a43-338089fc5b4b",
          "givenName": "Test",
          "familyName": "DrugDataOne"
        },

        "preferredAddress": {
          "display": "123",
          "uuid": "c41f82e2-6af2-459c-96ff-26b66c8887ae",
          "address1": "123",
          "address2": "gp123",
          "address3": "Raigarh",
          "cityVillage": "RAIGARH",
          "countyDistrict": "Raigarh",
          "stateProvince": "Chattisgarh",
          "country": null,
          "postalCode": null
        },

        "names": [
          {
            "display": "Test DrugDataOne",
            "uuid": "760f18ea-9321-4c31-9a43-338089fc5b4b",
            "givenName": "Test",
            "familyName": "DrugDataOne"
          }
        ],

        "addresses": [
          {
            "display": "123",
            "uuid": "c41f82e2-6af2-459c-96ff-26b66c8887ae",
            "address1": "123",
            "address2": "gp123",
            "address3": "Raigarh",
            "cityVillage": "RAIGARH",
            "countyDistrict": "Raigarh",
            "stateProvince": "Chattisgarh",
            "country": null,
            "postalCode": null
          }
        ]
      }
    }
```

There are several things here to note:

* A patient has a UUID, identifiers, and a person.

* Other than "uuid", most of the fields that might correspond to case
  properties belong to "person".

* "person" has a set of top-level items like "gender", "age",
  "birthdate", etc.  And then there are also "attributes". The top-level
  items are standard OpenMRS person properties. "attributes" are custom,
  and specific to this OpenMRS instance. Each attribute is identified by
  a UUID.

* There are two kinds of custom person attributes:

  1. Attributes that take any value (of its data type). Examples from
    above are "primaryContact = 1234" and "caste = Tribal".

  2. Attributes whose values are selected from a set. An example from
    above is "class", which is set to "General". OpenMRS calls these
    values "Concepts", and like everything else in OpenMRS each concept
    value has a UUID.

* A person has "names" and a "preferredName", and similarly "addresses"
  and "preferredAddress". Case properties are only mapped to
  preferredName and preferredAddress. We do not keep track of other
  names and addresses.


OpenmrsCaseConfig
-----------------

Now that we know what a patient looks like, the OpenmrsCaseConfig schema
will make more sense. It has the following fields that correspond to
OpenMRS's fields:

* patient_identifiers
* person_properties
* person_attributes
* person_preferred_name
* person_preferred_address

Each of those assigns values to a patient one of three ways, and each
way is configured in an OpenmrsCaseConfig using a subclass of
ValueSource:

1. It can assign a constant. This uses the ConstantString subclass of
   ValueSource. e.g.
   ```javascript
       "person_properties": {
         "birthdate": {
           "doc_type": "ConstantString",
           "value": "Oct 7, 3761 BCE"
         }
       }
   ```

2. It can assign a case property value. Use CaseProperty for this. e.g.
   ```javascript
       "person_properties": {
         "birthdate": {
           "doc_type": "CaseProperty",
           "case_property": "dob"
         }
       }
    ```

3. It can map a case property value to a Concept UUID.
   CasePropertyMap does this. e.g.
   ```javascript
       "person_attributes": {
         "c1f455e7-3f10-11e4-adec-0800271c1b75": {
           "doc_type": "CasePropertyMap",
           "case_property": "class",
           "value_map": {
             "sc": "c1fcd1c6-3f10-11e4-adec-0800271c1b75",
             "general": "c1fc20ab-3f10-11e4-adec-0800271c1b75",
             "obc": "c1fb51cc-3f10-11e4-adec-0800271c1b75",
             "other_caste": "c207073d-3f10-11e4-adec-0800271c1b75",
             "st": "c20478b6-3f10-11e4-adec-0800271c1b75"
           }
         }
       }
    ```

**GOTCHA**: An easy mistake when configuring "person_attributes": The
OpenMRS UUID of a Person Attribute Type is different from the UUID of
its Concept. For the Person Attribute Type UUID, navigate to
Administration > Person > Manage Person Attribute Types and select the
Person Attribute Type you want. Note the greyed-out UUID. This is the
UUID that you need. If the Person Attribute Type is a Concept, navigate
to Administration > Concepts > View Concept Dictionary and search for
the Person Attribute Type by name. Select it from the search results.
Note the UUID of the concept is different. Select each of its Answers.
Use their UUIDs in the "value_map".

There are two more OpenmrsCaseConfig fields:

* match_on_ids
* patient_finder

`match_on_ids` is a list of patient identifiers. They can be all or a
subset of those given in OpenmrsCaseConfig.patient_identifiers. When a
case is updated in CommCare, these are the IDs to be used to select the
corresponding patient from OpenMRS. This is done by
[`repeater_helpers`](repeater_helpers.py)`.get_patient_by_id()`

This is sufficient for projects that import their patient cases from
OpenMRS, because each CommCare case will have a corresponding OpenMRS
patient, and its ID, or IDs, will have been set by OpenMRS.

**NOTE**: MOTECH has the ability to create or update the values of
patient identifiers. If an app offers this ability to users, then that
identifier should not be included in `match_on_ids`. If the case was
originally matched using only that identifier and its value changes,
MOTECH may be unable to match that patient again.

For projects where patient cases can be registered in CommCare, there
needs to be a way of finding a corresponding patient, if one exists.

If `repeater_helpers.get_patient_by_id()` does not return a patient, we
need to search OpenMRS for a corresponding patient. For this we use
PatientFinders. OpenmrsCaseConfig.patient_finder will determine which
class of PatientFinder the OpenmrsRepeater must use.


PatientFinders
--------------

The [PatientFinder](finders.py) base class was developed as a way to
handle situations where patient cases are created in CommCare instead of
being imported from OpenMRS.

When patients are imported from OpenMRS, they will come with at least
one identifier that MOTECH can use to match the case in CommCare with
the corresponding patient in OpenMRS. But if the case is registered in
CommCare then we may not have an ID, or the ID could be wrong. We need
to search for a corresponding OpenMRS patient.

Different projects may focus on different kinds of case properties, so
it was felt that a base class would allow some flexibility, without too
much "YAGNI".

The `PatientFinder.wrap()` method allows you to wrap documents of
subclasses.

The `PatientFinder.find_patients()` method must be implemented by
subclasses. It returns a list of zero, one, or many patients. If it
returns one patient, the OpenmrsRepeater.find_or_create_patient() will
accept that patient as a true match.

**NOTE**: The consequences of a false positive (a Type II error) are
severe: A real patient will have their valid values overwritten by those
of someone else. So PatientFinders should be written and configured to
skew towards false negatives (Type I errors). In other words, it is much
better not to choose a patient than to choose the wrong patient.


### Creating Missing Patients

If a corresponding OpenMRS patient is not found for a CommCare case,
then a PatientFinder has the option to create a patient in OpenMRS. This
is an optional property named "create_missing". Its value defaults to
`false`. If it is set to `true`, then it will create a new patient if
none are found.

For example:

    "patient_finder": {
        "doc_type": "WeightedPropertyPatientFinder",
        "property_weights": [
            {"case_property": "given_name", "weight": 0.5},
            {"case_property": "family_name", "weight": 0.6}
        ],
        "searchable_properties": ["family_name"],
        "create_missing": true
    }

If more than one matching patient is found, a new patient will not be
created.

All required properties must be included in the payload. This is sure to
include a name and a date of birth, possibly estimated. It may include
an identifier. You can find this out from the OpenMRS Administration UI,
or by testing the OpenMRS REST API.


### WeightedPropertyPatientFinder

The first (and currently only) subclass of `PatientFinder` is the
`WeightedPropertyPatientFinder` class. As the name suggests, it assigns
weights to case properties, and scores the patients it finds in OpenMRS
to select an OpenMRS patient that matches a CommCare case.

See [the source code](finders.py) for more details on its properties and
how to define it.


OpenmrsFormConfig
-----------------

MOTECH sends case updates as changes to patient properties and
attributes. Form submissions can also create Visits, Encounters and
Observations in OpenMRS.

Configure this in the "Form configs" section of the OpenMRS Forwarder
configuration.

An example value of Form configs might look like this:

    [
      {
        "doc_type": "OpenmrsFormConfig",
        "xmlns": "http://openrosa.org/formdesigner/9481169B-0381-4B27-BA37-A46AB7B4692D",
        "openmrs_start_datetime": {
          "form_question": "/metadata/timeStart",
          "doc_type": "FormQuestion",
          "external_data_type": "omrs_date"
        },
        "openmrs_visit_type": "c22a5000-3f10-11e4-adec-0800271c1b75",
        "openmrs_encounter_type": "81852aee-3f10-11e4-adec-0800271c1b75",
        "openmrs_observations": [
          {
            "doc_type": "ObservationMapping",
            "concept": "5090AAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "value": {
              "form_question": "/data/height",
              "doc_type": "FormQuestion"
            }
          },
          {
            "doc_type": "ObservationMapping",
            "concept": "5089AAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "value": {
              "form_question": "/data/weight",
              "doc_type": "FormQuestion"
            }
          }
        ]
      }
    ]

This example will use two form question values, "/data/height" and
"/data/weight". They are sent as values of OpenMRS concepts
5090AAAAAAAAAAAAAAAAAAAAAAAAAAAA and 5089AAAAAAAAAAAAAAAAAAAAAAAAAAAA
respectively.

Set the UUIDs of Visit type and Encounter type appropriately according
to the context of the form in the CommCare app.

"openmrs_start_datetime" is an optional setting. By default, MOTECH will
set the start of the Visit and the Encounter to the time when the form
was completed on the mobile worker's device.

To change which timestamp is used, the following "form questions" are
available:
* "/metadata/timeStart": The timestamp, according to the mobile worker's
  device, when the form was started
* "/metadata/timeEnd": The timestamp, according to the mobile worker's
  device, when the form was completed
* "/metadata/received_on": The timestamp when the form was submitted
  to HQ.

The value's default data type is datetime. But some organisations may
need the value to be submitted to OpenMRS as just a date. To do this,
change the "external_data_type" to "omrs_date", as shown in the example.


Provider
--------

Every time a form is completed in OpenMRS, it
[creates a new Encounter](https://wiki.openmrs.org/display/docs/Encounters+and+observations).

Observations about a patient, like their height or their blood pressure,
belong to an Encounter; just as a form submission in CommCare can have
many form question values.

The OpenMRS [Data Model](https://wiki.openmrs.org/display/docs/Data+Model)
documentation explains that an Encounter can be associated with health
care providers.

It is useful to label data from CommCare by creating a Provider in
OpenMRS for CommCare.

OpenMRS Configuration has a field called "Provider UUID", and the value
entered here is stored in OpenmrsConfig.openmrs_provider.

There are three different kinds of entities involved in setting up a
provider in OpenMRS: A Person instance; a Provider instance; and a User
instance.

Use the following steps to create a provider for CommCare:

From the OpenMRS Administration page, choose "Manage Persons" and click
"Create Person". Name, date of birth, and gender are mandatory fields.
"CommCare Provider" is probably a good name because OpenMRS will split
it into a given name ("CommCare") and a family name ("Provider").
CommCare HQ's first Git commit is dated 2009-03-10, so that seems close
enough to a date of birth. OpenMRS equates gender with sex, and is quite
binary about it. You will have to decided whether CommCare is male or
female. When you are done, click "Create Person". On the next page, 
"City/Village" is a required field. You can set "State/Province" to
"Other" and set "City/Village" to "Cambridge". Then click "Save Person".

Go back to the OpenMRS Administration page, choose "Manage Providers"
and click "Add Provider". In the "Person" field, type the name of the
person you just created. You can also give it an Identifier, like
"commcare". Then click Save.

You will need the UUID of the new Provider. Find the Provider by
entering its name, and selecting it.

**Make a note of the greyed UUID**. This is the value you will need for
"Provider UUID" in the configuration for the OpenMRS Repeater.

Next, go back to the OpenMRS Administration page, choose "Manage Users"
and click "Add User". Under "Use a person who already exists" enter the
name of your new person and click "Next". Give your user a username
(like "commcare"), and a password. **Under "Roles" select "Provider"**.
Click "Save User".

Now CommCare's "Provider UUID" will be recognised by OpenMRS as a
provider. Copy the value of the Provider UUID you made a note of earlier
into your OpenMRS configuration in CommCare HQ.


Atom Feed Integration
---------------------

The [OpenMRS Atom Feed Module](https://wiki.openmrs.org/display/docs/Atom+Feed+Module)
allows MOTECH to poll feeds of updates to patients and encounters. The 
feed adheres to the
[Atom syndication format](https://validator.w3.org/feed/docs/rfc4287.html).

An example URL for the patient feed would be like
http://www.example.com/openmrs/ws/atomfeed/patient/recent

Example content:

    <?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <title>Patient AOP</title>
      <link rel="self" type="application/atom+xml" href="http://www.example.com/openmrs/ws/atomfeed/patient/recent" />
      <link rel="via" type="application/atom+xml" href="http://www.example.com/openmrs/ws/atomfeed/patient/32" />
      <link rel="prev-archive" type="application/atom+xml" href="http://www.example.com/openmrs/ws/atomfeed/patient/31" />
      <author>
        <name>OpenMRS</name>
      </author>
      <id>bec795b1-3d17-451d-b43e-a094019f6984+32</id>
      <generator uri="https://github.com/ICT4H/atomfeed">OpenMRS Feed Publisher</generator>
      <updated>2018-04-26T10:56:10Z</updated>
      <entry>
        <title>Patient</title>
        <category term="patient" />
        <id>tag:atomfeed.ict4h.org:6fdab6f5-2cd2-4207-b8bb-c2884d6179f6</id>
        <updated>2018-01-17T19:44:40Z</updated>
        <published>2018-01-17T19:44:40Z</published>
        <content type="application/vnd.atomfeed+xml"><![CDATA[/openmrs/ws/rest/v1/patient/e8aa08f6-86cd-42f9-8924-1b3ea021aeb4?v=full]]></content>
      </entry>
      <entry>
        <title>Patient</title>
        <category term="patient" />
        <id>tag:atomfeed.ict4h.org:5c6b6913-94a0-4f08-96a2-6b84dbced26e</id>
        <updated>2018-01-17T19:46:14Z</updated>
        <published>2018-01-17T19:46:14Z</published>
        <content type="application/vnd.atomfeed+xml"><![CDATA[/openmrs/ws/rest/v1/patient/e8aa08f6-86cd-42f9-8924-1b3ea021aeb4?v=full]]></content>
      </entry>
      <entry>
        <title>Patient</title>
        <category term="patient" />
        <id>tag:atomfeed.ict4h.org:299c435d-b3b4-4e89-8188-6d972169c13d</id>
        <updated>2018-01-17T19:57:09Z</updated>
        <published>2018-01-17T19:57:09Z</published>
        <content type="application/vnd.atomfeed+xml"><![CDATA[/openmrs/ws/rest/v1/patient/e8aa08f6-86cd-42f9-8924-1b3ea021aeb4?v=full]]></content>
      </entry>
    </feed>

Similarly, an encounter feed URL would be like
http://www.example.com/openmrs/ws/atomfeed/encounter/recent

Example content:

    <?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <title>Patient AOP</title>
      <link rel="self" type="application/atom+xml" href="https://13.232.58.186/openmrs/ws/atomfeed/encounter/recent" />
      <link rel="via" type="application/atom+xml" href="https://13.232.58.186/openmrs/ws/atomfeed/encounter/335" />
      <link rel="prev-archive" type="application/atom+xml" href="https://13.232.58.186/openmrs/ws/atomfeed/encounter/334" />
      <author>
        <name>OpenMRS</name>
      </author>
      <id>bec795b1-3d17-451d-b43e-a094019f6984+335</id>
      <generator uri="https://github.com/ICT4H/atomfeed">OpenMRS Feed Publisher</generator>
      <updated>2018-06-13T08:32:57Z</updated>
      <entry>
        <title>Encounter</title>
        <category term="Encounter" />
        <id>tag:atomfeed.ict4h.org:af713a2e-b961-4cb0-be59-d74e8b054415</id>
        <updated>2018-06-13T05:08:57Z</updated>
        <published>2018-06-13T05:08:57Z</published>
        <content type="application/vnd.atomfeed+xml"><![CDATA[/openmrs/ws/rest/v1/bahmnicore/bahmniencounter/0f54fe40-89af-4412-8dd4-5eaebe8684dc?includeAll=true]]></content>
      </entry>
      <entry>
        <title>Encounter</title>
        <category term="Encounter" />
        <id>tag:atomfeed.ict4h.org:320834be-e9c8-4b09-a99e-691dff18b3e4</id>
        <updated>2018-06-13T05:08:57Z</updated>
        <published>2018-06-13T05:08:57Z</published>
        <content type="application/vnd.atomfeed+xml"><![CDATA[/openmrs/ws/rest/v1/bahmnicore/bahmniencounter/0f54fe40-89af-4412-8dd4-5eaebe8684dc?includeAll=true]]></content>
      </entry>
      <entry>
        <title>Encounter</title>
        <category term="Encounter" />
        <id>tag:atomfeed.ict4h.org:fca253aa-b917-4166-946e-9da9baa901da</id>
        <updated>2018-06-13T05:09:12Z</updated>
        <published>2018-06-13T05:09:12Z</published>
        <content type="application/vnd.atomfeed+xml"><![CDATA[/openmrs/ws/rest/v1/bahmnicore/bahmniencounter/c6d6c248-8cd4-4e96-a110-93668e48e4db?includeAll=true]]></content>
      </entry>
    </feed>

At the time of writing, the Atom feeds do not use ETags or offer HEAD
requests. MOTECH uses a GET request to fetch the document, and checks
the timestamp in the `<updated>` tag to tell whether there is new
content.

The feeds are paginated, and the page number is given at the end of the
`href` attribute of the `<link rel="via" ...` tag, which is found at the
start of the feed. A `<link rel="next-archive" ...` tag indicates that
there is a next page.

MOTECH stores the last page number polled in the
`OpenmrsRepeater.patients_last_page` and 
`OpenmrsRepeater.encounters_last_page`  properties. When it polls again,
it starts at this page, and iterates "next-archive" links until all have
been fetched.

If this is the first time MOTECH is polling an Atom feed, it uses the
`/recent` URL (as given in the example URL above) instead of starting
from the very beginning. This is to allow Atom feed integration to be
enabled for ongoing projects that may have a lot of established data.
Administrators should be informed that enabling Atom feed integration
will not import all OpenMRS patients into CommCare, but it will add
CommCare cases for patients created in OpenMRS from the moment Atom
feed integration is enabled.

### Adding cases for OpenMRS patients

MOTECH needs three kinds of data in order to add a case for an OpenMRS
patient:

1. The **case type**. This is set using the OpenMRS Repeater's "Case
   Type" field (i.e. OpenmrsRepeater.white_listed_case_types). It must
   have exactly one case type specified.

2. The **case owner**. This is determined using the OpenMRS Repeater's
   "Location" field (i.e. OpenmrsRepeater.location_id). The owner is set
   to the first mobile worker (specifically CommCareUser instance) found
   at that location.

3. The **case properties** to set. MOTECH uses the patient_identifiers,
   person_properties, person_preferred_name, person_preferred_address,
   and person_attributes given in "Case config"
   (OpenmrsRepeater.openmrs_config.case_config) to map the values of an
   OpenMRS patient to case properties. All and only the properties in
   "Case config" are mapped.

The **name of cases** updated from the Atom feed are set to the display
name of the *person* (not the display name of patient because it often
includes punctuation and an identifier).

When a new case is created, its case's owner is determined by the
CommCare location of the OpenMRS repeater. (You can set the location
when you create or edit the OpenMRS repeater in *Project Settings* >
*Data Forwarding*.) The case will be assigned to the first mobile worker
found at the repeater's location. The intention is that this mobile
worker would be a supervisor who can pass the case to the appropriate
person.


Import-Only and Export-Only Values
----------------------------------

In configurations like Atom feed integration that involve both sending
data to OpenMRS and importing data from OpenMRS, sometimes some values
should only be imported, or only exported.

Use the "direction" property to determine whether a value should only be
exported, only imported, or (the default behaviour) both.

For example, to import a patient value named "hivStatus" as a case
property named "hiv_status" but not export it, use `"direction": "in"`:

    {
      "hivStatus": {
        "doc_type": "CaseProperty",
        "case_property": "hiv_status",
        "direction": "in"
      }
    }

To export a form question, for example, but not import it, use
`"direction": "out"`:

    {
      "hivStatus": {
        "doc_type": "FormQuestion",
        "case_property": "hiv_status",
        "direction": "out"
      }
    }

Omit "direction", or set it to `null`, for values that should be both
imported and exported.


Data Types
----------

Integrating structured data with OpenMRS can involve converting data
from one format or data type to another.

For standard OpenMRS properties, MOTECH will set data types correctly,
and integrators do not need to worry about them.

But OpenMRS administrators may expect a value that is a date in CommCare
to a datetime in OpenMRS, or vice-versa. To convert from one to the
other, set data types for values in the Repeater configuration.

The default is for both the CommCare data type and the external data
type not to be set. e.g.

    {
      "expectedDeliveryDate": {
        "doc_type": "CaseProperty",
        "case_property": "edd",
        "commcare_data_type": null,
        "external_data_type": null
      }
    }

To set the CommCare data type to a date and the OpenMRS data type to a
datetime for example, use the following:

    {
      "expectedDeliveryDate": {
        "doc_type": "CaseProperty",
        "case_property": "edd",
        "commcare_data_type": "cc_date",
        "external_data_type": "omrs_datetime"
      }
    }

For the complete list of CommCare data types, see
[MOTECH constants](../const.py). For the complete list of OpenMRS data
types, see [OpenMRS constants](./const.py).
MOTECH's DHIS2 Module
=====================

See the [MOTECH README](../README.md#dhis2-module) for a brief
introduction to DHIS2 in the context of MOTECH.

MOTECH currently supports two ways of integrating with DHSI2: Forwarding
aggregated data as DHIS2 DataSets; and forwarding form question values
as DHIS2 Anonymous Events.

Use the "Enable DHIS2 integration" feature flag for both.


Logging
-------

All requests sent to DHIS2, and the responses from DHIS2, are logged
and available under **Project Settings** > **MOTECH Logs**.


DataSets
--------

DataSets are sets of aggregated data. In the context of MOTECH, this is
data that has been collected using CommCare over a month or a quarter,
and then aggregated with a user-configurable report (UCR).


### UCRs for DataSets

Each column of the UCR maps to a DHIS2 DataElement + CategoryOptionCombo
pair. You will need to refer to DHIS2 to know what data you want, and
how it needs to be broken down, to determine the DataElements and the
CategoryOptionCombos you need.

If different rows have data from different periods, you can add a column for
the DHIS2 DataSet period, given in the format "yyyyMM" if the period is
monthly, e.g. "200403", or "yyyyQn" if the period is quarterly, where
"Q" is a literal "Q" and "n" is a number from 1 to 4, e.g. "2004Q1".

If different rows belong to different organisation units, you can
include a column for the row's orgUnitID.


### DataSet Map Configuration

To map UCR columns for a DHIS2 DataSet, go to **Project Settings** >
**DHIS2 DataSet Maps**.

The first part is where you set properties that apply to the whole
DataSet. If all the data in the UCR is for the same organisation unit,
specify it here, otherwise configure the name of the column where the
OrgUnitID can be found.

There are three ways to determine the period for the DataSet:

1. If the UCR is always for the same period, set it in "Period
   (YYYYMM)".
2. If different rows have data from different periods, set the column
   that contains the period in "Period column".
3. If MOTECH should pull the report for the previous period (month or
   quarter), and if the report has a date filter, choose "Report filter
   sets Period"

Then proceed to set the UCR Column, DataElementID,
CategoryOptionComboID, and optionally a comment, for each DataValue to
be sent to DHIS2.

You can map multiple DataSets here. Each will be sent in a separate API
call to DHIS2.

Save your configuration by clicking the "Update DHIS2 DataSet maps"
button.


### Testing

To test your configuration, click "Send data now".

Check **Project Settings** > **MOTECH Logs** to inspect the requests
sent to DHIS2, and the responses from DHIS2.


Anonymous Events
----------------

CommCare form data can be sent to DHIS2 as Anonymous Events. Form data
will be sent as forms are submitted.

This is configured under **Project Settings** > **Data Forwarding** >
**Forward to DHIS2**.

If it is not already defined, add a forwarding location. (This is
sometimes refered to as a "forwarder", and in the source code it is a
[`Dhis2Repeater`](./repeaters.py).) Enter the details of the DHIS2
server. When you are done, click "Start Forwarding".

To configure the integration, click "Configure".

**NOTE**: The Anonymous Events configuration uses a JSON interface, like
user-configurable reports. It was found that integrators preferred this
to an HTML interface because it allowed them to reuse their own
templates, and copy-and-paste configurations from their text editor of
choice.

"Form configs" are a list of [`Dhis2FormConfig`](./dhis2_config.py)
definitions. The following is an example:

    [
      {
        "doc_type": "Dhis2FormConfig",
        "xmlns": "http://openrosa.org/formdesigner/C3156B64-C380-4A38-B00E-C8E4D81EDCF9",
        "program_id": "WomWTaHk5mx",
        "event_date": {
          "doc_type": "FormQuestion",
          "form_question": "/data/event_date",
        },
        "event_status": "COMPLETED",
        "org_unit_id": {
          "doc_type": "ConstantString",
          "value": "NwGKQaHk5mx",
        },
        "datavalue_maps": [
          {
            "doc_type": "FormDataValueMap",
            "data_element_id": "M8yQ1rWomWT",
            "value": {
              "doc_type": "FormQuestionMap",
              "form_question": "/data/home_delivery",
              "value_map": {
                "yes": 1,
                "no": 0
              }
            }
          },
          {
            "doc_type": "FormDataValueMap",
            "data_element_id": "Hk5mxrWomWT",
            "value": {
              "doc_type": "FormQuestion",
              "form_question": "/data/birth_outcome"
            }
          }
        ]
      }
    ]

There is only one Dhis2FormConfig definition in this example. The form
is identified by its XMLNS,
"http://openrosa.org/formdesigner/C3156B64-C380-4A38-B00E-C8E4D81EDCF9".

The event date is determined from a form question, "/data/event_date".
(It is possible to use the time when the form was opened on the device
("/data/meta/timeStart") or when it was completed ("/data/meta/timeEnd")
but if the device's clock is inaccurate, or has been changed, then the
date could be wrong. Depending on the nature of the data, the user may
be reporting an event that has already occurred. Sometimes it is best to
prompt the user for the event date.)

"datavalue_maps" map form data to DHIS2 DataValues. They are
[`FormDataValueMap`](./dhis2_config.py) definitions. In each one a DHIS2
DataElement ID is given, and a CommCare ValueSource. The value source
can be a ConstantString if the value of the data element is always the
same; or a FormQuestion; or a FormQuestionMap if CommCare values map to
DHIS2 values.

There are several ways to set the DHIS2 organisation unit ID:

* It could be set to a constant for all submissions of this form. This
  is the case in the example given above. The ValueSource is set to a
  "ConstantString", and a constant value is given. This is unlikely
  though, because usually forms will be submitted for many locations or
  organisation units.
* It could be that the organisation unit is selected by the user from a
  lookup table. In this scenario, the org_unit_id would be saved to a
  hidden value in the form, and the ValueSource would be a FormQuestion
  where "form_question" is set to the hidden value.
* It could be that locations in the project space have equivalent
  organisation units in DHIS2. If "org_unit_id" is not specified in the
  Dhis2FormConfig definition, then the MOTECH uses the CommCare location
  of the mobile worker who submitted the form, and checks its location
  fields for a location property named "dhis_id".


### Matching CommCare locations with DHIS2 oganisation units

1. Navigate to **Users** > **Organization Structure** and click the "Edit
   Location Fields" button.
2. Add a field with "Location Property" set to "dhis_id". (It is
   important that you use this spelling.) Set "Label" to something like
   "DHIS2 OrgUnit ID".
3. Click "Save Fields".

You can now either add the DHIS2 OrgUnit ID to each location one by one,
or download the Organization Structure, and add them in bulk using, for
example, a spreadsheet with a lookup to match CommCare locations with
DHIS2 OrgUnits.


### Testing

Once the integration is configured, you can test it by submitting a
form, and checking **Project Settings** > **Data Forwarding Records**.
Form submissions will appear here with "Record Status" "Pending". Queued
payloads are forwarded every four minutes. To send it immediately, click
"Resend Payload".

Check **Project Settings** > **MOTECH Logs** to inspect the requests
sent to DHIS2, and the responses from DHIS2.
# Call Center / Supervisor statistics

This Django app comprises the majority of the code related to the 'supervisor app' feature.

This feature allows supervisors to view performance related statistics about mobile field workers
as part of a CommCare application.

This is accomplished as follows:

1. A case is created for each mobile user in a domain (the case type is configured by the user
   under project settings).
2. A fixture is generated that contains indicators for each mobile user and links them to the user's
   case (by using the case id).

With these two pieces in place it is possible to build an app in CommCare that will list all the
mobile worker cases and show the indicators for each one.

See https://help.commcarehq.or/display/commcarepublic/How+to+set+up+a+Supervisor-Call+Center+Application
    for user docs.

## Fixture format
    <fixture id="indicators:call-center" user_id="...">
        <indicators>
            <case id="user_case1">
                <indicator_a>1</indicator_a>
                <indicator_b>2</indicator_2>
            </case>
        </indicators>
    </fixture>

## Date ranges

Assume all dates are at 00h00.00.

| Date Range    | Description                       | Lower Bound (Inclusive)   | Upper Bound (Exclusive)   |
|---------------|-----------------------------------|---------------------------|---------------------------|
| Week0         | The last 7 days                   | (today-7)                 | today                     |
| Week1         | The last 7 days prior to week0    | (today-14)                | (today-8)                 |
| Month0        | The last 30 days                  | (today-30)                | today                     |
| Month1        | The last 30 days prior to Month0  | (today-60)                | (today-31)                |


## Indicators
### Forms Submitted
**Name**: forms_submitted_{period_name}

**Definition**: count of the number of forms submitted by each mobile worker during the time period

### Total Cases
**Name**: cases_total_{period_name} e.g. cases_total_week1

**Definition**: count of (case_created <= end_date and (case_closed >= start_date or case_not_closed).

Include cases that are owned by mobile worker or cases that are owned by a case owner group that the
mobile worker is part of.

### Total Cases By Case Type
This should be calculated for all known case types in the project, which includes any cases
from form submissions and any cases types defined in the projects applications.

**Name**: cases_total_{case_type}_{period_name} e.g. cases_total_mother_week0

**Definition**: Same as cases_total, but restrict the cases by case type.

### Opened Cases
**Name**: cases_opened_{period_name}

**Definition**: count of (case_opened >= start_date and case_opened <= end_date).

Include cases opened by the mobile worker.

### Opened Cases By Case Type
Similar to total cases by case type, this should be calculated for all known case types in the project.

**Name**: cases_opened_{case_type}_{period_name}

**Definition**:  Same as cases_opened, but restrict the cases by case type.

### Closed Cases
**Name**: cases_closed_{period_name}

**Definition**:  count of (case_closed >= start_date and case_closed <= end_date).

Include cases closed by the mobile worker.

### Closed Cases By Case Type
Similar to total cases by case type, this should be calculated for all known case types in the project.

**Name**: cases_closed_{case_type}_{period_name}

**Definition**:  Same as cases_closed, but restrict the cases by case type.

### Active Cases
**Naming**: cases_active_{period_name}

**Definition**:  count of cases where a case modification occurred between the start and end dates of the period (inclusive).  Include cases that are owned by mobile worker or cases that are owned by a case owner group that the mobile worker is part of.

### Active Cases By Case Type
Similar to total cases by case type, this should be calculated for all known case types in the project.

**Name**: cases_active_{case_type}_{period_name}

**Definition**:  Same as cases_active, but restrict the cases by case type.

## User assignment
When a fixture is generated for a supervisor it should only include data for users who are 'assigned' to the
supervisor. A user may be assigned to a supervisor in one of two ways:

1. The user's case is owned by the supervisor.
2. The user's case is owned by a case sharing group which the supervisor is part of.

## Caching
Since the indicators only include data up until midnight of the previous day the indicator values will
not change until the following midnight and should therefore be cached to avoid having to regenerate them
for each request.

The indicators for a specific user are cached in Django's default cache as JSON object and set to expire
at midnight of the current day.

## Timezones
All dates are adjusted to refer to the default timezone of the domain.

## Legacy indicators
In order to provide backwards compatibility for existing applications the following indicators are
also included in the fixture output:

* formsSubmitted{period_name} - the same values as forms_submitted_{period_name}
* casesUpdated{period_name} - the same values as cases_active_{period_name}
* totalCases - the total number of open cases at time of generation where case.user_id = mobile_user.user_id
# Case Migrations

This feature allows technical users to handle their own case migrations using xforms.

## Current components

* Basic form to trigger a case migration
* Restore endpoint to be used by webapps

## TODOs

* WebApps component to run a migration
  * `send_migration_to_formplayer` should do what it says
  * Web apps can then send each case ID to
    `/a/<domain>/case_migrations/restore/<case_id>/`
    to get a restore containing that case's network.
* Store migrations in a DB
* One-click revert
This app is currently just a collection of management commands that are useful for copying data between HQ instances.
# Customized styles

This is the parent directory of styles customised for HQ and mobile.
Customized styles belong here. Use the .less files in this directory as a
guide to see which included files your changes belong in.
# Linking Domains

* Ability to sync models between two domains (master domain -> linked domain)
* Can be within the same HQ instance or between remote instances.

# Remote linking

### On 'master domain':

```
DomainLink.link_domains('https://url.of.linked.hq/a/linked_domain_name', 'master_domain_name')
```

This gets used as a permissions check during remote requests to ensure
that the remote domain is allowed to sync from this domain.

### On 'linked domain'

```
remote_details = RemoteLinkDetails(
    url_base='https://url.of.master.hq',
    username='username@email.com',
    api_key='api key for username'
)
DomainLink.link_domains('linked_domain_name', 'master_domain_name', remote_details)
```

### Pulling changes from master

On remote HQ, enable `linked_domains` feature flag and navigate to `project settings > Linked Projects` page which has a UI to pull changes from master domain for custom data fields for Location, User and Product models, user roles and feature flags/previews.

Linked apps can be setup between linked domains by running `link_app_to_remote` command on linked domain.
Changes Feed Application
------------------------

This app provides a [kafka-based](https://kafka.apache.org/) implementation of a changes feed.
This allows for creating an abstraction layer between CouchDB and Pillows so that pillows are not dependent on on the underlying database.
More information about this approach is available on [read the docs](http://commcare-hq.readthedocs.io/change_feeds.html).

# Dependencies

These pillows are dependent on Kafka, which is dependent on Zookeeper.
It is necessary to run these services to provide steady-state synchronization of data to ElasticSearch.
The recommended installation mechanism is via Docker.
See the [HQ docker readme](https://github.com/dimagi/commcare-hq/blob/master/docker/README.md) for more information on doing that.


## Alternative installations

You can also use any of the alternative installation mechanisms if you don't want to or can't use Docker.

### Manually via quickstart

Kafka provides a [quickstart guide](http://kafka.apache.org/documentation.html#quickstart) to getting up and running quickly.


### Natively, on Mac

You can follow the quick start guide above, or you can use brew to install kafka (it installs a slightly older version 0.8).

```
brew install kafka
brew services start zookeeper
brew services start kafka
```

### Via Ansible

You can use Ansible to setup Zookeeper and Kafka on your dev environment, or in a VM.
This can be accomplished using the following script (assuming you have an appropriate ansible environment configured):

```
ansible-playbook -i inventories/development -e '@vars/dev.yml' deploy_stack.yml --tags=kafka
```

# Configuration

If you use the default configuration you should not have to do anything.
If you are running kafka in a VM, on another machine, or on a nonstandard port, you will need to override `KAFKA_BROKERS` in your `localsettings.py`.

To more easily manage Kafka's settings, try installing [kafkat](https://github.com/airbnb/kafkat)

Finally, once you have kafka running, initialize it with

```
./manage.py create_kafka_topics
```
# Commcare Reporting

See https://commcare-hq.readthedocs.io/reporting.html
Don't Use
=========

Do not use anything in this directory.
If you see something you can delete, go for it.
User Configurable Reporting
===========================
An overview of the design, API and data structures used here.


**Table of Contents**

- [Data Flow](#data-flow)
- [Data Sources](#data-sources)
    - [Data Source Filtering](#data-source-filtering)
        - [Filter type overview](#filter-type-overview)
        - [Expressions](#expressions)
        - [JSON snippets for expressions](#json-snippets-for-expressions)
            - [Constant Expression](#constant-expression)
            - [Property Name Expression](#property-name-expression)
            - [Property Path Expression](#property-path-expression)
            - [Conditional Expression](#conditional-expression)
            - [Switch Expression](#switch-expression)
            - [Array Index Expression](#array-index-expression)
            - [Iterator Expression](#iterator-expression)
            - [Base iteration number expressions](#base-iteration-number-expressions)
            - [Related document expressions](#related-document-expressions)
            - [Ancestor Location Expression](#ancestor-location-expression)
            - [Nested expressions](#nested-expressions)
            - [Dict expressions](#dict-expressions)
            - ["Add Days" expressions](#add-days-expressions)
            - ["Add Months" expressions](#add-months-expressions)
            - ["Diff Days" expressions](#diff-days-expressions)
            - ["Evaluator" expression](#evaluator-expression)
            - [Function calls within evaluator expressions](#function-calls-within-evaluator-expressions)
            - ["Month Start Date" and "Month End Date" expressions](#month-start-date-and-month-end-date-expressions)
            - [Filter, Sort, Map and Reduce Expressions](#filter-sort-map-and-reduce-expressions)
                - [map_items Expression](#map_items-expression)
                - [filter_items Expression](#filte_ritems-expression)
                - [sort_items Expression](#sort_items-expression)
                - [reduce_items Expression](#reduce_items-expression)
                - [flatten expression](#flatten-expression)
            - [Named Expressions](#named-expressions)
        - [Boolean Expression Filters](#boolean-expression-filters)
            - [Operators](#operators)
        - [Compound filters](#compound-filters)
            - ["And" Filters](#and-filters)
            - ["Or" Filters](#or-filters)
            - ["Not" Filters](#not-filters)
        - [Practical Examples](#practical-examples)
    - [Indicators](#indicators)
        - [Indicator Properties](#indicator-properties)
        - [Indicator types](#indicator-types)
            - [Boolean indicators](#boolean-indicators)
            - [Expression indicators](#expression-indicators)
            - [Choice list indicators](#choice-list-indicators)
            - [Ledger Balance Indicators](#ledger-balance-indicators)
        - [Practical notes for creating indicators](#practical-notes-for-creating-indicators)
            - [Fractions](#fractions)
    - [Saving Multiple Rows per Case/Form](#saving-multiple-rows-per-caseform)
- [Report Configurations](#report-configurations)
    - [Samples](#samples)
    - [Report Filters](#report-filters)
        - [Numeric Filters](#numeric-filters)
        - [Date filters](#date-filters)
        - [Quarter filters](#quarter-filters)
        - [Dynamic choice lists](#dynamic-choice-lists)
            - [Choice providers](#choice-providers)
        - [Choice lists](#choice-lists)
        - [Drilldown by Location](#drilldown-by-location)
        - [Internationalization](#internationalization)
    - [Report Columns](#report-columns)
        - [Field columns](#field-columns)
        - [Percent columns](#percent-columns)
            - [Formats](#formats)
        - [AggregateDateColumn](#aggregatedatecolumn)
        - [Expanded Columns](#expanded-columns)
        - [Expression Columns](#expression-columns)
        - [The "aggregation" column property](#the-aggregation-column-property)
            - [Column IDs](#column-ids)
        - [Calculating Column Totals](#calculating-column-totals)
        - [Internationalization](#internationalization)
    - [Aggregation](#aggregation)
        - [No aggregation](#no-aggregation)
        - [Aggregate by 'username' column](#aggregate-by-username-column)
        - [Aggregate by two columns](#aggregate-by-two-columns)
    - [Transforms](#transforms)
        - [Translations and arbitrary mappings](#translations-and-arbitrary-mappings)
        - [Displaying username instead of user ID](#displaying-username-instead-of-user-id)
        - [Displaying username minus @domain.commcarehq.org instead of user ID](#displaying-username-minus-domaincommcarehqorg-instead-of-user-id)
        - [Displaying owner name instead of owner ID](#displaying-owner-name-instead-of-owner-id)
        - [Displaying month name instead of month index](#displaying-month-name-instead-of-month-index)
        - [Rounding decimals](#rounding-decimals)
        - [Generic number formatting](#generic-number-formatting)
            - [Round to the nearest whole number](#round-to-the-nearest-whole-number)
            - [Always round to 3 decimal places](#always-round-to-3-decimal-places)
        - [Date formatting](#date-formatting)
        - [Converting an ethiopian date string to a gregorian date](#converting-an-ethiopian-date-string-to-a-gregorian-date)
        - [Converting a gregorian date string to an ethiopian date](#converting-a-gregorian-date-string-to-an-ethiopian-date)
    - [Charts](#charts)
        - [Pie charts](#pie-charts)
        - [Aggregate multibar charts](#aggregate-multibar-charts)
        - [Multibar charts](#multibar-charts)
    - [Sort Expression](#sort-expression)
- [Mobile UCR](#mobile-ucr)
    - [Filters](#filters)
        - [Custom Calendar Month](#custom-calendar-month)
- [Export](#export)
    - [Export example](#export-example)
- [Practical Notes](#practical-notes)
    - [Getting Started](#getting-started)
    - [Static data sources](#static-data-sources)
    - [Static configurable reports](#static-configurable-reports)
    - [Custom configurable reports](#custom-configurable-reports)
    - [Extending User Configurable Reports](#extending-user-configurable-reports)
    - [Inspecting database tables](#inspecting-database-tables)


# Data Flow

Reporting is handled in multiple stages. Here is the basic workflow.

Raw data (form or case) → [Data source config] → Row in database table → [Report config] → Report in HQ

Both the data source config and report config are JSON documents that live in the database. The data source config determines how raw data (forms and cases) gets mapped to rows in an intermediary table, while the report config(s) determine how that report table gets turned into an interactive report in the UI.

# Data Sources

Each data source configuration maps a filtered set of the raw data to indicators. A data source configuration consists of two primary sections:

1. A filter that determines whether the data is relevant for the data source
2. A list of indicators in that data source

In addition to these properties there are a number of relatively self-explanatory fields on a data source such as the `table_id` and `display_name`, and a few more nuanced ones. The full list of available fields is summarized in the following table:

Field                | Description
-------------------- | -----------
filter               | Determines whether the data is relevant for the data source
indicators           | List of indicators to save
table_id             | A unique ID for the table
display_name         | A display name for the table that shows up in UIs
base_item_expression | Used for making tables off of repeat or list data
named_expressions    | A list of named expressions that can be referenced in other filters and indicators
named_filters        | A list of named filters that can be referenced in other filters and indicators


## Data Source Filtering

When setting up a data source configuration, filtering defines what data applies to a given set of indicators. Some example uses of filtering on a data source include:

- Restricting the data by document type (e.g. cases or forms). This is a built-in filter.
- Limiting the data to a particular case or form type
- Excluding demo user data
- Excluding closed cases
- Only showing data that meets a domain-specific condition (e.g. pregnancy cases opened for women over 30 years of age)

### Filter type overview

There are currently four supported filter types. However, these can be used together to produce arbitrarily complicated expressions.


Filter Type        | Description
------------------ | -----------
boolean_expression | A expression / logic statement (more below)
and                | An "and" of other filters - true if all are true
or                 | An "or" of other filters - true if any are true
not                | A "not" or inverse expression on a filter

To understand the `boolean_expression` type, we must first explain expressions.

### Expressions

An *expression* is a way of representing a set of operations that should return a single value. Expressions can basically be thought of as functions that take in a document and return a value:

*Expression*: `function(document) → value`

In normal math/python notation, the following are all valid expressions on a `doc` (which is presumed to be a `dict` object:

- `"hello"`
- `7`
- `doc["name"]`
- `doc["child"]["age"]`
- `doc["age"] < 21`
- `"legal" if doc["age"] > 21 else "underage"`

In user configurable reports the following expression types are currently supported (note that this can and likely will be extended in the future):

Expression Type | Description  | Example
--------------- | ------------ | ------
identity        | Just returns whatever is passed in | `doc`
constant        | A constant   | `"hello"`, `4`, `2014-12-20`
property_name   | A reference to the property in a document |  `doc["name"]`
property_path   | A nested reference to a property in a document | `doc["child"]["age"]`
conditional     | An if/else expression | `"legal" if doc["age"] > 21 else "underage"`
switch          | A switch statement | `if doc["age"] == 21: "legal"` `elif doc["age"] == 60: ...` `else: ...`
array_index     | An index into an array | `doc[1]`
split_string    | Splitting a string and grabbing a specific element from it by index | `doc["foo bar"].split(' ')[0]`
iterator        | Combine multiple expressions into a list | `[doc.name, doc.age, doc.gender]`
related_doc     | A way to reference something in another document | `form.case.owner_id`
root_doc        | A way to reference the root document explicitly (only needed when making a data source from repeat/child data) | `repeat.parent.name`
ancestor_location | A way to retrieve the ancestor of a particular type from a location |
nested          | A way to chain any two expressions together | `f1(f2(doc))`
dict            | A way to emit a dictionary of key/value pairs | `{"name": "test", "value": f(doc)}`
add_days        | A way to add days to a date | `my_date + timedelta(days=15)`
add_months      | A way to add months to a date | `my_date + relativedelta(months=15)`
month_start_date| First day in the month of a date | `2015-01-20` -> `2015-01-01`
month_end_date  | Last day in the month of a date | `2015-01-20` -> `2015-01-31`
diff_days       | A way to get duration in days between two dates | `(to_date - from-date).days`
evaluator       | A way to do arithmetic operations | `a + b*c / d`
base_iteration_number | Used with [`base_item_expression`](#saving-multiple-rows-per-caseform) - a way to get the current iteration number (starting from 0). | `loop.index`


Following expressions act on a list of objects or a list of lists (for e.g. on a repeat list) and return another list or value. These expressions can be combined to do complex aggregations on list data.

Expression Type | Description  | Example
--------------- | ------------ | ------
filter_items    | Filter a list of items to make a new list | `[1, 2, 3, -1, -2, -3] -> [1, 2, 3]`  (filter numbers greater than zero)
map_items       | Map one list to another list | `[{'name': 'a', gender: 'f'}, {'name': 'b, gender: 'm'}]` -> `['a', 'b']`  (list of names from list of child data)
sort_items      | Sort a list based on an expression | `[{'name': 'a', age: 5}, {'name': 'b, age: 3}]` -> `[{'name': 'b, age: 3}, {'name': 'a', age: 5}]`  (sort child data by age)
reduce_items    | Aggregate a list of items into one value | sum on `[1, 2, 3]` -> `6`
flatten   | Flatten multiple lists of items into one list | `[[1, 2], [4, 5]]` -> `[1, 2, 4, 5]`



### JSON snippets for expressions

Here are JSON snippets for the various expression types. Hopefully they are self-explanatory.

##### Constant Expression

There are two formats for constant expressions. The simplified format is simply the constant itself. For example `"hello"`, or `5`.

The complete format is as follows. This expression returns the constant `"hello"`:

```
{
    "type": "constant",
    "constant": "hello"
}
```


##### Property Name Expression

This expression returns `doc["age"]`:
```
{
    "type": "property_name",
    "property_name": "age"
}
```
An optional `"datatype"` attribute may be specified, which will attempt to cast the property to the given data type. The options are "date", "datetime", "string", "integer", and "decimal". If no datatype is specified, "string" will be used.

##### Property Path Expression

This expression returns `doc["child"]["age"]`:
```
{
    "type": "property_path",
    "property_path": ["child", "age"]
}
```
An optional `"datatype"` attribute may be specified, which will attempt to cast the property to the given data type. The options are "date", "datetime", "string", "integer", and "decimal". If no datatype is specified, "string" will be used.

##### Conditional Expression

This expression returns `"legal" if doc["age"] > 21 else "underage"`:
```
{
    "type": "conditional",
    "test": {
        "operator": "gt",
        "expression": {
            "type": "property_name",
            "property_name": "age",
            "datatype": "integer"
        },
        "type": "boolean_expression",
        "property_value": 21
    },
    "expression_if_true": {
        "type": "constant",
        "constant": "legal"
    },
    "expression_if_false": {
        "type": "constant",
        "constant": "underage"
    }
}
```
Note that this expression contains other expressions inside it! This is why expressions are powerful. (It also contains a filter, but we haven't covered those yet - if you find the `"test"` section confusing, keep reading...)

Note also that it's important to make sure that you are comparing values of the same type. In this example, the expression that retrieves the age property from the document also casts the value to an integer. If this datatype is not specified, the expression will compare a string to the `21` value, which will not produce the expected results!

##### Switch Expression

This expression returns the value of the expression for the case that matches the switch on expression. Note that case values may only be strings at this time.
```json
{
    "type": "switch",
    "switch_on": {
        "type": "property_name",
        "property_name": "district"
    },
    "cases": {
        "north": {
            "type": "constant",
            "constant": 4000
        },
        "south": {
            "type": "constant",
            "constant": 2500
        },
        "east": {
            "type": "constant",
            "constant": 3300
        },
        "west": {
            "type": "constant",
            "constant": 65
        },
    },
    "default": {
        "type": "constant",
        "constant": 0
    }
}
```

##### Coalesce Expression

This expression returns the value of the expression provided, or the value of the default_expression if the expression provided evalutes to a null or blank string.
```json
{
    "type": "coalesce",
    "expression": {
        "type": "property_name",
        "property_name": "district"
    },
    "default_expression": {
    	"type": "constant",
        "constant": "default_district"
    }
}
```

##### Array Index Expression

This expression returns `doc["siblings"][0]`:
```json
{
    "type": "array_index",
    "array_expression": {
        "type": "property_name",
        "property_name": "siblings"
    },
    "index_expression": {
        "type": "constant",
        "constant": 0
    }
}
```
It will return nothing if the siblings property is not a list, the index isn't a number, or the indexed item doesn't exist.

##### Split String Expression

This expression returns `(doc["foo bar"]).split(' ')[0]`:
```json
{
    "type": "split_string",
    "string_expression": {
        "type": "property_name",
        "property_name": "multiple_value_string"
    },
    "index_expression": {
        "type": "constant",
        "constant": 0
    },
    "delimiter": ","
}
```
The delimiter is optional and is defaulted to a space.  It will return nothing if the string_expression is not a string, or if the index isn't a number or the indexed item doesn't exist.
The index_expression is also optional. Without it, the expression will return the list of elements.

##### Iterator Expression

```json
{
    "type": "iterator",
    "expressions": [
        {
            "type": "property_name",
            "property_name": "p1"
        },
        {
            "type": "property_name",
            "property_name": "p2"
        },
        {
            "type": "property_name",
            "property_name": "p3"
        },
    ],
    "test": {}
}
```

This will emit `[doc.p1, doc.p2, doc.p3]`.
You can add a `test` attribute to filter rows from what is emitted - if you don't specify this then the iterator will include one row per expression it contains regardless of what is passed in.
This can be used/combined with the `base_item_expression` to emit multiple rows per document.


#### Base iteration number expressions

These are very simple expressions with no config. They return the index of the repeat item starting from 0 when used with a `base_item_expression`.

```json
{
    "type": "base_iteration_number"
}
```

#### Related document expressions

This can be used to lookup a property in another document. Here's an example that lets you look up `form.case.owner_id` from a form.

```json
{
    "type": "related_doc",
    "related_doc_type": "CommCareCase",
    "doc_id_expression": {
        "type": "property_path",
        "property_path": ["form", "case", "@case_id"]
    },
    "value_expression": {
        "type": "property_name",
        "property_name": "owner_id"
    }
}
```

#### Ancestor location expression
This is used to return a json object representing the ancestor of the given type of the given location.
For instance, if we had locations configured with a hierarchy like `country -> state -> county -> city`, we could
pass the location id of Cambridge and a location type of state to this expression to get the Massachusetts
location.

```json
{
    "type": "ancestor_location",
    "location_id": {
        "type": "property_name",
        "name": "owner_id"
    },
    "location_type": {
        "type": "constant",
        "constant": "state"
    }
}
```

#### Nested expressions

These can be used to nest expressions. This can be used, e.g. to pull a specific property out of an item in a list of objects.

The following nested expression is the equivalent of a `property_path` expression to `["outer", "inner"]` and demonstrates the functionality.
More examples can be found in the [practical examples](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/userreports/examples/examples.md).

```json
{
    "type": "nested",
    "argument_expression": {
        "type": "property_name",
        "property_name": "outer"
    },
    "value_expression": {
        "type": "property_name",
        "property_name": "inner"
    }
}
```

#### Dict expressions

These can be used to create dictionaries of key/value pairs. This is only useful as an intermediate structure in another expression since the result of the expression is a dictionary that cannot be saved to the database.

See the [practical examples](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/userreports/examples/examples.md) for a way this can be used in a `base_item_expression` to emit multiple rows for a single form/case based on different properties.

Here is a simple example that demonstrates the structure. The keys of `properties` must be text, and the values must be valid expressions (or constants):

```json
{
    "type": "dict",
    "properties": {
        "name": "a constant name",
        "value": {
            "type": "property_name",
            "property_name": "prop"
        },
        "value2": {
            "type": "property_name",
            "property_name": "prop2"
        }
    }
}
```

#### "Add Days" expressions

Below is a simple example that demonstrates the structure.
The expression below will add 28 days to a property called "dob".
The date_expression and count_expression can be any valid expressions, or simply constants.

```json
{
    "type": "add_days",
    "date_expression": {
        "type": "property_name",
        "property_name": "dob",
    },
    "count_expression": 28
}
```

#### "Add Months" expressions

`add_months` offsets given date by given number of calendar months.
If offset results in an invalid day (for e.g. Feb 30, April 31), the day of resulting date will be adjusted to last day of the resulting calendar month.

The date_expression and months_expression can be any valid expressions, or simply constants, including negative numbers.

```json
{
    "type": "add_months",
    "date_expression": {
        "type": "property_name",
        "property_name": "dob",
    },
    "months_expression": 28
}
```

#### "Diff Days" expressions

`diff_days` returns number of days between dates specified by `from_date_expression` and `to_date_expression`.
The from_date_expression and to_date_expression can be any valid expressions, or simply constants.

```json
{
    "type": "diff_days",
    "from_date_expression": {
        "type": "property_name",
        "property_name": "dob",
    },
    "to_date_expression": "2016-02-01"
}
```

#### "Evaluator" expression
`evaluator` expression can be used to evaluate statements that contain arithmetic (and simple python like statements). It evaluates the statement specified by `statement` which can contain variables as defined in `context_variables`.

```json
{
    "type": "evaluator",
    "statement": "a + b - c + 6",
    "context_variables": {
        "a": 1,
        "b": 20,
        "c": 2
    }
}
```
This returns 25 (1 + 20 - 2 + 6).

`statement` can be any statement that returns a valid number. All python math [operators](https://en.wikibooks.org/wiki/Python_Programming/Basic_Math#Mathematical_Operators) except power operator are available for use.

`context_variables` is a dictionary of Expressions where keys are names of variables used in the `statement` and values are expressions to generate those variables.
Variables can be any valid numbers (Python datatypes `int`, `float` and `long` are considered valid numbers.) or also expressions that return numbers. In addition to numbers the following types are supported:

* `date`
* `datetime`

#### Function calls within evaluator expressions
Only the following functions are permitted:

* `rand()`: generate a random number between 0 and 1
* `randint(max)`: generate a random integer between 0 and `max`
* `int(value)`: convert `value` to an int. Value can be a number or a string representation of a number
* `float(value)`: convert `value` to a floating point number
* `str(value)`: convert `value` to a string
* `timedelta_to_seconds(time_delta)`: convert a TimeDelta object into seconds. This is useful for getting the number of seconds between two dates.
  * e.g. `timedelta_to_seconds(time_end - time_start)`
* `range(start, [stop], [skip])`: the same as the python [`range` function](https://docs.python.org/2/library/functions.html#range). Note that for performance reasons this is limited to 100 items or less.

#### "Month Start Date" and "Month End Date" expressions

`month_start_date` returns date of first day in the month of given date and `month_end_date` returns date of last day in the month of given date.

The `date_expression` can be any valid expression, or simply constant

```json
{
    "type": "month_start_date",
    "date_expression": {
        "type": "property_name",
        "property_name": "dob",
    },
}
```
#### 'Get Case Sharing Groups' expression
'get_case_sharing_groups' will return an array of the case sharing groups that are assigned to a provided user ID.  The array will contain one document per case sharing group.
```json
{
    "type": "get_case_sharing_groups",
    "user_id_expression": {
        "type": "property_path",
        "property_path": ["form", "meta", "userID"]
    }
}
```
#### 'Get Reporting Groups' expression
'get_reporting_groups' will return an array of the reporting groups that are assigned to a provided user ID.  The array will contain one document per reporting group.
```json
{
    "type": "get_reporting_groups",
    "user_id_expression": {
        "type": "property_path",
        "property_path": ["form", "meta", "userID"]
    }
}
```

#### Filter, Sort, Map and Reduce Expressions

We have following expressions that act on a list of objects or list of lists. The list to operate on is specified by `items_expression`. This can be any valid expression that returns a list. If the `items_expression` doesn't return a valid list, these might either fail or return one of empty list or `None` value.

##### map_items Expression

`map_items` performs a calculation specified by `map_expression` on each item of the list specified by `items_expression` and returns a list of the calculation results. The `map_expression` is evaluated relative to each item in the list and not relative to the parent document from which the list is specified. For e.g. if `items_expression` is a path to repeat-list of children in a form document, `map_expression` is a path relative to the repeat item.

`items_expression` can be any valid expression that returns a list. If this doesn't evaluate to a list an empty list is returned. It may be necessary to specify a `datatype` of `array` if the expression could return a single element.

`map_expression` can be any valid expression relative to the items in above list.

```json
{
    "type": "map_items",
    "items_expression": {
        "datatype": "array",
        "type": "property_path",
        "property_path": ["form", "child_repeat"]
    },
    "map_expression": {
        "type": "property_path",
        "property_path": ["age"]
    }
}
```
Above returns list of ages. Note that the `property_path` in `map_expression` is relative to the repeat item rather than to the form.


##### filter_items Expression

`filter_items` performs filtering on given list and returns a new list. If the boolean expression specified by `filter_expression` evaluates to a `True` value, the item is included in the new list and if not, is not included in the new list.

`items_expression` can be any valid expression that returns a list. If this doesn't evaluate to a list an empty list is returned. It may be necessary to specify a `datatype` of `array` if the expression could return a single element.

`filter_expression` can be any valid boolean expression relative to the items in above list.

```json
{
    "type": "filter_items",
    "items_expression": {
        "datatype": "array",
        "type": "property_name",
        "property_name": "family_repeat"
    },
    "filter_expression": {
       "type": "boolean_expression",
        "expression": {
            "type": "property_name",
            "property_name": "gender"
        },
        "operator": "eq",
        "property_value": "female"
    }
}
```

##### sort_items Expression

`sort_items` returns a sorted list of items based on sort value of each item.The sort value of an item is specified by `sort_expression`. By default, list will be in ascending order. Order can be changed by adding optional `order` expression with one of `DESC` (for descending) or `ASC` (for ascending) If a sort-value of an item is `None`, the item will appear in the start of list. If sort-values of any two items can't be compared, an empty list is returned.

`items_expression` can be any valid expression that returns a list. If this doesn't evaluate to a list an empty list is returned. It may be necessary to specify a `datatype` of `array` if the expression could return a single element.

`sort_expression` can be any valid expression relative to the items in above list, that returns a value to be used as sort value.

```json
{
    "type": "sort_items",
    "items_expression": {
        "datatype": "array",
        "type": "property_path",
        "property_path": ["form", "child_repeat"]
    },
    "sort_expression": {
        "type": "property_path",
        "property_path": ["age"]
    }
}
```

##### reduce_items Expression

`reduce_items` returns aggregate value of the list specified by `aggregation_fn`.

`items_expression` can be any valid expression that returns a list. If this doesn't evaluate to a list, `aggregation_fn` will be applied on an empty list. It may be necessary to specify a `datatype` of `array` if the expression could return a single element.

`aggregation_fn` is one of following supported functions names.


Function Name  | Example
-------------- | -----------
`count`        | `['a', 'b']` -> 2
`sum`          | `[1, 2, 4]` -> 7
`min`          | `[2, 5, 1]` -> 1
`max`          | `[2, 5, 1]` -> 5
`first_item`   | `['a', 'b']` -> 'a'
`last_item`    | `['a', 'b']` -> 'b'

```json
{
    "type": "reduce_items",
    "items_expression": {
        "datatype": "array",
        "type": "property_name",
        "property_name": "family_repeat"
    },
    "aggregation_fn": "count"
}
```
This returns number of family members

##### flatten expression

`flatten` takes list of list of objects specified by `items_expression` and returns one list of all objects.

`items_expression` is any valid expression that returns a list of lists. It this doesn't evaluate to a list of lists an empty list is returned. It may be necessary to specify a `datatype` of `array` if the expression could return a single element.
```json
{
    "type": "flatten",
    "items_expression": {},
}
```

#### Named Expressions

Last, but certainly not least, are named expressions.
These are special expressions that can be defined once in a data source and then used throughout other filters and indicators in that data source.
This allows you to write out a very complicated expression a single time, but still use it in multiple places with a simple syntax.

Named expressions are defined in a special section of the data source. To reference a named expression, you just specify the type of `"named"` and the name as follows:

```json
{
    "type": "named",
    "name": "my_expression"
}
```

This assumes that your named expression section of your data source includes a snippet like the following:

```json
{
    "my_expression": {
        "type": "property_name",
        "property_name": "test"
    }
}
```

This is just a simple example - the value that `"my_expression"` takes on can be as complicated as you want _as long as it doesn't reference any other named expressions_.

### Boolean Expression Filters

A `boolean_expression` filter combines an *expression*, an *operator*, and a *property value* (a constant), to produce a statement that is either `True` or `False`. *Note: in the future the constant value may be replaced with a second expression to be more general, however currently only constant property values are supported.*

Here is a sample JSON format for simple `boolean_expression` filter:
```
{
    "type": "boolean_expression",
    "expression": {
        "type": "property_name",
        "property_name": "age",
        "datatype": "integer"
    },
    "operator": "gt",
    "property_value": 21
}
```
This is equivalent to the python statement: `doc["age"] > 21`

#### Operators

The following operators are currently supported:

Operator   | Description  | Value type | Example
---------- | -----------  | ---------- | -------
`eq`       | is equal     | constant   | `doc["age"] == 21`
`not_eq`   | is not equal | constant   | `doc["age"] != 21`
`in`       | single value is in a list | list | `doc["color"] in ["red", "blue"]`
`in_multi` | a value is in a multi select | list | `selected(doc["color"], "red")`
`any_in_multi` | one of a list of values in in a multiselect | list | `selected(doc["color"], ["red", "blue"])`
`lt`       | is less than | number | `doc["age"] < 21`
`lte`      | is less than or equal | number | `doc["age"] <= 21`
`gt`       | is greater than | number | `doc["age"] > 21`
`gte`      | is greater than or equal | number | `doc["age"] >= 21`

### Compound filters

Compound filters build on top of `boolean_expression` filters to create boolean logic. These can be combined to support arbitrarily complicated boolean logic on data. There are three types of filters, *and*, *or*, and *not* filters. The JSON representation of these is below. Hopefully these are self explanatory.

#### "And" Filters

The following filter represents the statement: `doc["age"] < 21 and doc["nationality"] == "american"`:
```
{
    "type": "and",
    "filters": [
		{
            "type": "boolean_expression",
            "expression": {
                "type": "property_name",
                "property_name": "age",
                "datatype": "integer"
            },
            "operator": "lt",
            "property_value": 21
        },
        {
            "type": "boolean_expression",
            "expression": {
                "type": "property_name",
                "property_name": "nationality",
            },
            "operator": "eq",
            "property_value": "american"
        }
    ]
}
```
#### "Or" Filters

The following filter represents the statement: `doc["age"] > 21 or doc["nationality"] == "european"`:
```
{
    "type": "or",
    "filters": [
		{
            "type": "boolean_expression",
            "expression": {
                "type": "property_name",
                "property_name": "age",
                "datatype": "integer",
            },
            "operator": "gt",
            "property_value": 21
        },
		{
            "type": "boolean_expression",
            "expression": {
                "type": "property_name",
                "property_name": "nationality",
            },
            "operator": "eq",
            "property_value": "european"
        }
    ]
}
```
#### "Not" Filters

The following filter represents the statement: `!(doc["nationality"] == "european")`:
```
{
    "type": "not",
    "filter": [
        {
            "type": "boolean_expression",
            "expression": {
                "type": "property_name",
                "property_name": "nationality",
            },
            "operator": "eq",
            "property_value": "european"
        }
    ]
}
```
*Note that this could be represented more simply using a single filter with the `not_eq` operator, but "not" filters can represent more complex logic than operators generally, since the filter itself can be another compound filter.*

### Practical Examples

See [examples.md](examples/examples.md) for some practical examples showing various filter types.


## Indicators

Now that we know how to filter the data in our data source, we are still left with a very important problem: *how do we know what data to save*? This is where indicators come in. Indicators are the data outputs - what gets computed and put in a column in the database.

A typical data source will include many indicators (data that will later be included in the report). This section will focus on defining a single indicator. Single indicators can then be combined in a list to fully define a data source.

The overall set of possible indicators is theoretically any function that can take in a single document (form or case) and output a value. However the set of indicators that are configurable is more limited than that.

### Indicator Properties

All indicator definitions have the following properties:

Property        | Description
--------------- | -----------
type            | A specified type for the indicator. It must be one of the types listed below.
column_id       | The database column where the indicator will be saved.
display_name    | A display name for the indicator (not widely used, currently).
comment         | A string describing the indicator

Additionally, specific indicator types have other type-specific properties. These are covered below.

### Indicator types

The following primary indicator types are supported:

Indicator Type  | Description
--------------  | -----------
boolean         | Save `1` if a filter is true, otherwise `0`.
expression      | Save the output of an expression.
choice_list     | Save multiple columns, one for each of a predefined set of choices
ledger_balances | Save a column for each product specified, containing ledger data

*Note/todo: there are also other supported formats, but they are just shortcuts around the functionality of these ones they are left out of the current docs.*

#### Boolean indicators

Now we see again the power of our filter framework defined above! Boolean indicators take any arbitrarily complicated filter expression and save a `1` to the database if the expression is true, otherwise a `0`.  Here is an example boolean indicator which will save `1` if a form has a question with ID `is_pregnant` with a value of `"yes"`:

```
{
    "type": "boolean",
    "column_id": "col",
    "filter": {
	    "type": "boolean_expression",
	    "expression": {
	        "type": "property_path",
	        "property_path": ["form", "is_pregnant"],
	    },
	    "operator": "eq",
	    "property_value": "yes"
	}
}
```

#### Expression indicators

Similar to the boolean indicators - expression indicators leverage the expression structure defined above to create arbitrarily complex indicators. Expressions can store arbitrary values from documents (as opposed to boolean indicators which just store `0`'s and `1`'s). Because of this they require a few additional properties in the definition:

Property        | Description
--------------- | -----------
datatype        | The datatype of the indicator. Current valid choices are: "date", "datetime", "string", "decimal", "integer", and "small_integer".
is_nullable     | Whether the database column should allow null values.
is_primary_key  | Whether the database column should be (part of?) the primary key. (TODO: this needs to be confirmed)
create_index    | Creates an index on this column. Only applicable if using the SQL backend
expression      | Any expression.
transform       | (optional) transform to be applied to the result of the expression. (see "Report Columns > Transforms" section below)

Here is a sample expression indicator that just saves the "age" property to an integer column in the database:

```
{
    "type": "expression",
    "expression": {
        "type": "property_name",
        "property_name": "age"
    },
    "column_id": "age",
    "datatype": "integer",
    "display_name": "age of patient"
}
```

#### Choice list indicators

Choice list indicators take a single choice column (select or multiselect) and expand it into multiple columns where each column represents a different choice. These can support both single-select and multi-select quesitons.

A sample spec is below:

```
{
    "type": "choice_list",
    "column_id": "col",
    "display_name": "the category",
    "property_name": "category",
    "choices": [
        "bug",
        "feature",
        "app",
        "schedule"
    ],
    "select_style": "single"
}
```

#### Ledger Balance Indicators

Ledger Balance indicators take a list of product codes and a ledger section,
and produce a column for each product code, saving the value found in the
corresponding ledger.

Property            | Description
--------------------|------------
ledger_section      | The ledger section to use for this indicator, for example, "stock"
product_codes       | A list of the products to include in the indicator.  This will be used in conjunction with the `column_id` to produce each column name.
case_id_expression  | An expression used to get the case where each ledger is found.  If not specified, it will use the row's doc id.

```
{
    "type": "ledger_balances",
    "column_id": "soh",
    "display_name": "Stock On Hand",
    "ledger_section": "stock",
    "product_codes": ["aspirin", "bandaids", "gauze"],
    "case_id_expression": {
        "type": "property_name",
        "property_name": "_id"
    }
}
```

This spec would produce the following columns in the data source:

soh_aspirin | soh_bandaids | soh_gauze
------------|--------------|----------
 20         |  11          |  5
 67         |  32          |  9


If the ledger you're using is a due list and you wish to save the dates instead of integers, you can change the "type" from "ledger_balances" to "due_list_dates".


### Practical notes for creating indicators

These are some practical notes for how to choose what indicators to create.

#### Fractions

All indicators output single values. Though fractional indicators are common, these should be modeled as two separate indicators (for numerator and denominator) and the relationship should be handled in the report UI config layer.

## Saving Multiple Rows per Case/Form

You can save multiple rows per case/form by specifying a root level `base_item_expression` that describes how to get the repeat data from the main document.
You can also use the `root_doc` expression type to reference parent properties
and the `base_iteration_number` expression type to reference the current index of the item.
This can be combined with the `iterator` expression type to do complex data source transforms.
This is not described in detail, but the following sample (which creates a table off of a repeat element called "time_logs" can be used as a guide).
There are also additional examples in the [examples](examples/examples.md):

```
{
    "domain": "user-reports",
    "doc_type": "DataSourceConfiguration",
    "referenced_doc_type": "XFormInstance",
    "table_id": "sample-repeat",
    "display_name": "Time Logged",
    "base_item_expression": {
        "type": "property_path",
        "property_path": ["form", "time_logs"]
    },
    "configured_filter": {
    },
    "configured_indicators": [
        {
            "type": "expression",
            "expression": {
                "type": "property_name",
                "property_name": "start_time"
            },
            "column_id": "start_time",
            "datatype": "datetime",
            "display_name": "start time"
        },
        {
            "type": "expression",
            "expression": {
                "type": "property_name",
                "property_name": "end_time"
            },
            "column_id": "end_time",
            "datatype": "datetime",
            "display_name": "end time"
        },
        {
            "type": "expression",
            "expression": {
                "type": "property_name",
                "property_name": "person"
            },
            "column_id": "person",
            "datatype": "string",
            "display_name": "person"
        },
        {
            "type": "expression",
            "expression": {
                "type": "root_doc",
                "expression": {
                    "type": "property_name",
                    "property_name": "name"
                }
            },
            "column_id": "name",
            "datatype": "string",
            "display_name": "name of ticket"
        }
    ]
}
```

# Report Configurations

A report configuration takes data from a data source and renders it in the UI. A report configuration consists of a few different sections:

1. [Report Filters](#report-filters) - These map to filters that show up in the UI, and should translate to queries that can be made to limit the returned data.
2. [Aggregation](#aggregation) - This defines what each row of the report will be. It is a list of columns forming the *primary key* of each row.
3. [Report Columns](#report-columns) - Columns define the report columns that show up from the data source, as well as any aggregation information needed.
4. [Charts](#charts) - Definition of charts to display on the report.
5. [Sort Expression](#sort-expression) - How the rows in the report are ordered.

## Samples

Here are some sample configurations that can be used as a reference until we have better documentation.

- [Dimagi chart report](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/userreports/examples/dimagi/dimagi-chart-report.json)
- [GSID form report](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/userreports/examples/gsid/gsid-form-report.json)


## Report Filters

The documentation for report filters is still in progress. Apologies for brevity below.

**A note about report filters versus data source filters**

Report filters are _completely_ different from data source filters. Data source filters limit the global set of data that ends up in the table, whereas report filters allow you to select values to limit the data returned by a query.

### Numeric Filters
Numeric filters allow users to filter the rows in the report by comparing a column to some constant that the user specifies when viewing the report.
Numeric filters are only intended to be used with numeric (integer or decimal type) columns. Supported operators are =, &ne;, &lt;, &le;, &gt;, and &ge;.

ex:
```
{
  "type": "numeric",
  "slug": "number_of_children_slug",
  "field": "number_of_children",
  "display": "Number of Children"
}
```

### Date filters

Date filters allow you filter on a date. They will show a datepicker in the UI.

```
{
  "type": "date",
  "slug": "modified_on",
  "field": "modified_on",
  "display": "Modified on",
  "required": false
}
```
Date filters have an optional `compare_as_string` option that allows the date
filter to be compared against an indicator of data type `string`. You shouldn't
ever need to use this option (make your column a `date` or `datetime` type
instead), but it exists because the report builder needs it.

### Quarter filters

Quarter filters are similar to date filters, but a choice is restricted only to the particular quarter of the year. They will show inputs for year and quarter in the UI.

```
{
  "type": "quarter",
  "slug": "modified_on",
  "field": "modified_on",
  "display": "Modified on",
  "required": false
}
```

### Pre-Filters

Pre-filters offer the kind of functionality you get from
[data source filters](#data-source-filtering). This makes it easier to use one
data source for many reports, especially if some of those reports just need
the data source to be filtered slightly differently. Pre-filters do not need
to be configured by app builders in report modules; fields with pre-filters
will not be listed in the report module among the other fields that can be
filtered.

A pre-filter's `type` is set to "pre":
```
{
  "type": "pre",
  "field": "at_risk_field",
  "slug": "at_risk_slug",
  "datatype": "string",
  "pre_value": "yes"
}
```

If `pre_value` is scalar (i.e. `datatype` is "string", "integer", etc.), the
filter will use the "equals" operator. If `pre_value` is null, the filter will
use "is null". If `pre_value` is an array, the filter will use the "in"
operator. e.g.
```
{
  "type": "pre",
  "field": "at_risk_field",
  "slug": "at_risk_slug",
  "datatype": "array",
  "pre_value": ["yes", "maybe"]
}
```

(If `pre_value` is an array and `datatype` is not "array", it is assumed that
`datatype` refers to the data type of the items in the array.)

You can optionally specify the operator that the prevalue filter uses by adding a pre_operator argument. e.g.
```
{
  "type": "pre",
  "field": "at_risk_field",
  "slug": "at_risk_slug",
  "datatype": "array",
  "pre_value": ["maybe", "yes"],
  "pre_operator": "between"
}
```

Note that instead of using `eq`, `gt`, etc, you will need to use `=`, `>`, etc.

### Dynamic choice lists

Dynamic choice lists provide a select widget that will generate a list of options dynamically.

The default behavior is simply to show all possible values for a column, however you can also specify a `choice_provider` to customize this behavior (see below).

Simple example assuming "village" is a name:
```json
{
  "type": "dynamic_choice_list",
  "slug": "village",
  "field": "village",
  "display": "Village",
  "datatype": "string"
}
```

#### Choice providers

Currently the supported `choice_provider`s are supported:


Field                | Description
-------------------- | -----------
location             | Select a location by name
user                 | Select a user
owner                | Select a possible case owner owner (user, group, or location)


Location choice providers also support three additional configuration options:

* "include_descendants" - Include descendants of the selected locations in the results. Defaults to `false`.
* "show_full_path" - Display the full path to the location in the filter. Defaults to `false`.
  The default behavior shows all locations as a flat alphabetical list.

Example assuming "village" is a location ID, which is converted to names using the location `choice_provider`:
```json
{
  "type": "dynamic_choice_list",
  "slug": "village",
  "field": "location_id",
  "display": "Village",
  "datatype": "string",
  "choice_provider": {
      "type": "location",
      "include_descendants": true,
      "show_full_path": true
  }
}
```

### Choice lists

Choice lists allow manual configuration of a fixed, specified number of choices and let you change what they look like in the UI.
```
{
  "type": "choice_list",
  "slug": "role",
  "field": "role",
  "choices": [
    {"value": "doctor", "display": "Doctor"},
    {"value": "nurse"}
  ]
}
```

### Drilldown by Location

This filter allows selection of a location for filtering by drilling down from top level.
```
{
  "type": "location_drilldown",
  "slug": "by_location",
  "field": "district_id",
  "include_descendants": true,
  "max_drilldown_levels": 3
}
```
* "include_descendants" - Include descendant locations in the results. Defaults to `false`.
* "max_drilldown_levels" - Maximum allowed drilldown levels. Defaults to 99

### Internationalization

Report builders may specify translations for the filter display value.
Also see the sections on internationalization in the Report Column and
the [translations transform](#translations-and-arbitrary-mappings).

```json
{
    "type": "choice_list",
    "slug": "state",
    "display": {"en": "State", "fr": "État"},
    ...
}
```

## Report Columns

Reports are made up of columns. The currently supported column types ares:

* [_field_](#field-columns) which represents a single value
* [_percent_](#percent-columns) which combines two values in to a percent
* [_aggregate_date_](#aggregatedatecolumn) which aggregates data by month
* [_expanded_](#expanded-columns) which expands a select question into multiple columns
* [_expression_](#expression-columns) which can do calculations on data in other columns

### Field columns

Field columns have a type of `"field"`. Here's an example field column that shows the owner name from an associated `owner_id`:

```json
{
    "type": "field",
    "field": "owner_id",
    "column_id": "owner_id",
    "display": "Owner Name",
    "format": "default",
    "transform": {
        "type": "custom",
        "custom_type": "owner_display"
    },
    "aggregation": "simple"
}
```

### Percent columns

Percent columns have a type of `"percent"`. They must specify a `numerator` and `denominator` as separate field columns. Here's an example percent column that shows the percentage of pregnant women who had danger signs.

```
{
  "type": "percent",
  "column_id": "pct_danger_signs",
  "display": "Percent with Danger Signs",
  "format": "both",
  "denominator": {
    "type": "field",
    "aggregation": "sum",
    "field": "is_pregnant",
    "column_id": "is_pregnant"
  },
  "numerator": {
    "type": "field",
    "aggregation": "sum",
    "field": "has_danger_signs",
    "column_id": "has_danger_signs"
  }
}
```

#### Formats

The following percentage formats are supported.

Format          | Description                                    | example
--------------- | -----------------------------------------------| --------
percent         | A whole number percentage (the default format) | 33%
fraction        | A fraction                                     | 1/3
both            | Percentage and fraction                        | 33% (1/3)
numeric_percent | Percentage as a number                         | 33
decimal         | Fraction as a decimal number                   | .333


### AggregateDateColumn

AggregateDate columns allow for aggregating data by month over a given date field.  They have a type of `"aggregate_date"`. Unlike regular fields, you do not specify how aggregation happens, it is automatically grouped by month.

Here's an example of an aggregate date column that aggregates the `received_on` property for each month (allowing you to count/sum things that happened in that month).

```json
 {
    "column_id": "received_on",
    "field": "received_on",
    "type": "aggregate_date",
    "display": "Month"
  }
```

AggregateDate supports an optional "format" parameter, which accepts the same [format string](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior) as [Date formatting](#date-formatting). If you don't specify a format, the default will be "%Y-%m", which will show as, for example, "2008-09".

Keep in mind that the only variables available for formatting are `year` and `month`, but that still gives you a fair range, e.g.

| format    | Example result    |
| --------- | ----------------- |
| "%Y-%m"   | "2008-09"         |
| "%B, %Y"  | "September, 2008" |
| "%b (%y)" | "Sep (08)"        |


### ConditionalAggregationColumn

**NOTE** This feature is only available to static UCR reports maintained by Dimagi developers.

Conditional aggregation columns allow you to define a series of conditional expressions with corresponding names, then group together rows which which meet the same conditions. They have a type of `"conditional_aggregation"`.

Here's an example that groups children based on their age at the time of registration:

```json
{
    "display": "age_range",
    "column_id": "age_range",
    "type": "conditional_aggregation",
    "whens": {
        "0 <= age_at_registration AND age_at_registration < 12": "infant",
        "12 <= age_at_registration AND age_at_registration < 36": "toddler",
        "36 <= age_at_registration AND age_at_registration < 60": "preschooler"
    },
    "else_": "older"
}
```

The `"whens"` attribute maps conditional expressions to labels.  If none of the conditions are met, the row will receive the `"else_"` value, if provided.

Here's a more complex example which uses SQL functions to dynamically calculate ranges based on a date property:

```json
{
    "display": "Age Group",
    "column_id": "age_group",
    "type": "conditional_aggregation",
    "whens": {
        "extract(year from age(dob))*12 + extract(month from age(dob)) BETWEEN 0 and 5": "0_to_5",
        "extract(year from age(dob))*12 + extract(month from age(dob)) BETWEEN 6 and 11": "6_to_11",
        "extract(year from age(dob))*12 + extract(month from age(dob)) BETWEEN 12 and 35": "12_to_35",
        "extract(year from age(dob))*12 + extract(month from age(dob)) BETWEEN 36 and 59": "36_to_59",
        "extract(year from age(dob))*12 + extract(month from age(dob)) BETWEEN 60 and 71": "60_to_71"
    }
}
```

### Expanded Columns

Expanded columns have a type of `"expanded"`. Expanded columns will be "expanded" into a new column for each distinct value in this column of the data source. For example:

If you have a data source like this:
```
+---------|----------|-------------+
| Patient | district | test_result |
+---------|----------|-------------+
| Joe     | North    | positive    |
| Bob     | North    | positive    |
| Fred    | South    | negative    |
+---------|----------|-------------+
```
and a report configuration like this:
```
aggregation columns:
["district"]

columns:
[
  {
    "type": "field",
    "field": "district",
    "column_id": "district",
    "format": "default",
    "aggregation": "simple"
  },
  {
    "type": "expanded",
    "field": "test_result",
    "column_id": "test_result",
    "format": "default"
  }
]
```
Then you will get a report like this:
```
+----------|----------------------|----------------------+
| district | test_result-positive | test_result-negative |
+----------|----------------------|----------------------+
| North    | 2                    | 0                    |
| South    | 0                    | 1                    |
+----------|----------------------|----------------------+
```

Expanded columns have an optional parameter `"max_expansion"` (defaults to 10) which limits the number of columns that can be created.  WARNING: Only override the default if you are confident that there will be no adverse performance implications for the server.

### Expression columns

Expression columns can be used to do just-in-time calculations on the data coming out of reports.
They allow you to use any UCR expression on the data in the report row.
These can be referenced according to the `column_id`s from the other defined column.
They can support advanced use cases like doing math on two different report columns,
or doing conditional logic based on the contents of another column.

A simple example is below, which assumes another called "number" in the report and shows
how you could make a column that is 10 times that column.


```json
{
    "type": "expression",
    "column_id": "by_tens",
    "display": "Counting by tens",
    "expression": {
        "type": "evaluator",
        "statement": "a * b",
        "context_variables": {
            "a": {
                "type": "property_name",
                "property_name": "number"
            },
            "b": 10
        }
    }
}
```

### The "aggregation" column property

The aggregation column property defines how the column should be aggregated. If the report is not doing any aggregation, or if the column is one of the aggregation columns this should always be `"simple"` (see [Aggregation](#aggregation) below for more information on aggregation).

The following table documents the other aggregation options, which can be used in aggregate reports.

Format          | Description
--------------- | -----------------------------------------------
simple          | No aggregation
avg             | Average (statistical mean) of the values
count_unique    | Count the unique values found
count           | Count all rows
min             | Choose the minimum value
max             | Choose the maximum value
sum             | Sum the values

#### Column IDs

Column IDs in percentage fields *must be unique for the whole report*. If you use a field in a normal column and in a percent column you must assign unique `column_id` values to it in order for the report to process both.


### Calculating Column Totals

To sum a column and include the result in a totals row at the bottom of the report, set the `calculate_total` value in the column configuration to `true`.

Not supported for the following column types:
- expression

### Internationalization
Report columns can be translated into multiple languages.
To translate values in a given column check out
the [translations transform](#translations-and-arbitrary-mappings) below.
To specify translations for a column header, use an object as the `display`
value in the configuration instead of a string. For example:
```
{
    "type": "field",
    "field": "owner_id",
    "column_id": "owner_id",
    "display": {
        "en": "Owner Name",
        "he": "שם"
    },
    "format": "default",
    "transform": {
        "type": "custom",
        "custom_type": "owner_display"
    },
    "aggregation": "simple"
}
```
The value displayed to the user is determined as follows:
- If a display value is specified for the users language, that value will appear in the report.
- If the users language is not present, display the `"en"` value.
- If `"en"` is not present, show an arbitrary translation from the `display` object.
- If `display` is a string, and not an object, the report shows the string.

Valid `display` languages are any of the two or three letter language codes available on the user settings page.


## Aggregation

Aggregation in reports is done using a list of columns to aggregate on.
This defines how indicator data will be aggregated into rows in the report.
The columns represent what will be grouped in the report, and should be the `column_id`s of valid report columns.
In most simple reports you will only have one level of aggregation. See examples below.

### No aggregation

Note that if you use `is_primary_key` in any of your columns, you must include all primary key columns here.

```json
["doc_id"]
```

### Aggregate by 'username' column

```json
["username"]
```

### Aggregate by two columns

```json
["column1", "column2"]
```

## Transforms

Transforms can be used in two places - either to manipulate the value of a column just before it gets saved to a data source, or to transform the value returned by a column just before it reaches the user in a report.
Here's an example of a transform used in a report config 'field' column:

```json
{
    "type": "field",
    "field": "owner_id",
    "column_id": "owner_id",
    "display": "Owner Name",
    "format": "default",
    "transform": {
        "type": "custom",
        "custom_type": "owner_display"
    },
    "aggregation": "simple"
}
```

The currently supported transform types are shown below:

### Translations and arbitrary mappings

The translations transform can be used to give human readable strings:

```json
{
    "type": "translation",
    "translations": {
        "lmp": "Last Menstrual Period",
        "edd": "Estimated Date of Delivery"
    }
}
```

And for translations:

```json
{
    "type": "translation",
    "translations": {
        "lmp": {
            "en": "Last Menstrual Period",
            "es": "Fecha Última Menstruación",
        },
        "edd": {
            "en": "Estimated Date of Delivery",
            "es": "Fecha Estimada de Parto",
        }
    }
}
```

To use this in a mobile ucr, set the `'mobile_or_web'` property to `'mobile'`

```json
{
    "type": "translation",
    "mobile_or_web": "mobile",
    "translations": {
        "lmp": "Last Menstrual Period",
        "edd": "Estimated Date of Delivery"
    }
}
```

### Displaying username instead of user ID

```json
{
    "type": "custom",
    "custom_type": "user_display"
}
```

### Displaying username minus @domain.commcarehq.org instead of user ID

```json
{
    "type": "custom",
    "custom_type": "user_without_domain_display"
}
```

### Displaying owner name instead of owner ID

```json
{
    "type": "custom",
    "custom_type": "owner_display"
}
```

### Displaying month name instead of month index

```json
{
    "type": "custom",
    "custom_type": "month_display"
}
```

### Rounding decimals

Rounds decimal and floating point numbers to two decimal places.

```json
{
    "type": "custom",
    "custom_type": "short_decimal_display"
}
```

### Generic number formatting

Rounds numbers using Python's [built in formatting](https://docs.python.org/2.7/library/string.html#string-formatting).

See below for a few simple examples. Read the docs for complex ones. The input to the format string will be a _number_ not a string.

If the format string is not valid or the input is not a number then the original input will be returned.


#### Round to the nearest whole number

```json
{
    "type": "number_format",
    "format_string": "{0:.0f}"
}
```

#### Always round to 3 decimal places

```json
{
    "type": "number_format",
    "format_string": "{0:.3f}"
}
```

### Date formatting
Formats dates with the given format string. See [here](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior) for an explanation of format string behavior.
If there is an error formatting the date, the transform is not applied to that value.
```json
{
   "type": "date_format", 
   "format": "%Y-%m-%d %H:%M"
}
```


### Converting an ethiopian date string to a gregorian date
Converts a string in the YYYY-MM-DD format to a gregorian date. For example,
2009-09-11 is converted to date(2017, 5, 19). If it is unable to convert the date,
it will return an empty string.

```json
{
   "type": "custom",
   "custom_type": "ethiopian_date_to_gregorian_date"
}
```

### Converting a gregorian date string to an ethiopian date
Converts a string in the YYYY-MM-DD format to an ethiopian date. For example,
2017-05-19 is converted to date(2009, 09, 11). If it is unable to convert the date,
it will return an empty string.

```json
{
   "type": "custom",
   "custom_type": "gregorian_date_to_ethiopian_date"
}
```

## Charts

There are currently three types of charts supported. Pie charts, and two types of bar charts.

### Pie charts

A pie chart takes two inputs and makes a pie chart. Here are the inputs:


Field              | Description
------------------ | -----------------------------------------------
aggregation_column | The column you want to group - typically a column from a select question
value_column       | The column you want to sum - often just a count

Here's a sample spec:

```
{
    "type": "pie",
    "title": "Remote status",
    "aggregation_column": "remote",
    "value_column": "count"
}
```

### Aggregate multibar charts

An aggregate multibar chart is used to aggregate across two columns (typically both of which are select questions). It takes three inputs:

Field                 | Description
--------------------- | -----------------------------------------------
primary_aggregation   | The primary aggregation. These will be the x-axis on the chart.
secondary_aggregation | The secondary aggregation. These will be the slices of the bar (or individual bars in "grouped" format)
value_column          | The column you want to sum - often just a count

Here's a sample spec:

```
{
    "type": "multibar-aggregate",
    "title": "Applicants by type and location",
    "primary_aggregation": "remote",
    "secondary_aggregation": "applicant_type",
    "value_column": "count"
}
```

### Multibar charts

A multibar chart takes a single x-axis column (typically a user, date, or select question) and any number of y-axis columns (typically indicators or counts) and makes a bar chart from them.

Field          | Description
---------------| -----------------------------------------------
x_axis_column  | This will be the x-axis on the chart.
y_axis_columns | These are the columns to use for the secondary axis. These will be the slices of the bar (or individual bars in "grouped" format).

Here's a sample spec:

```
{
    "type": "multibar",
    "title": "HIV Mismatch by Clinic",
    "x_axis_column": "clinic",
    "y_axis_columns": [
        {
            "column_id": "diagnoses_match_no",
            "display": "No match"
        },
        {
            "column_id": "diagnoses_match_yes",
            "display": "Match"
        }
    ]
}
```

## Sort Expression

A sort order for the report rows can be specified. Multiple fields, in either ascending or descending order, may be specified. Example:

Field should refer to report column IDs, not database fields.

```
[
  {
    "field": "district", 
    "order": "DESC"
  }, 
  {
    "field": "date_of_data_collection", 
    "order": "ASC"
  }
]
```

# Mobile UCR

Mobile UCR is a beta feature that enables you to make application modules and charts linked to UCRs on mobile.
It also allows you to send down UCR data from a report as a fixture which can be used in standard case lists and forms throughout the mobile application.

The documentation for Mobile UCR is very sparse right now.

## Filters

On mobile UCR, filters can be automatically applied to the mobile reports based on hardcoded or user-specific data, or can be displayed to the user.

The documentation of mobile UCR filters is incomplete. However some are documented below.

### Custom Calendar Month

When configuring a report within a module, you can filter a date field by the 'CustomMonthFilter'.  The choice includes the following options:
- Start of Month (a number between 1 and 28)
- Period (a number between 0 and n with 0 representing the current month). 

Each custom calendar month will be "Start of the Month" to ("Start of the Month" - 1).  For example, if the start of the month is set to 21, then the period will be the 21th of the month -> 20th of the next month. 

Examples:
Assume it was May 15:
Period 0, day 21, you would sync April 21-May 15th
Period 1, day 21, you would sync March 21-April 20th
Period 2, day 21, you would sync February 21 -March 20th

Assume it was May 20:
Period 0, day 21, you would sync April 21-May 20th
Period 1, day 21, you would sync March 21-April 20th
Period 2, day 21, you would sync February 21-March 20th

Assume it was May 21:
Period 0, day 21, you would sync May 21-May 21th
Period 1, day 21, you would sync April 21-May 20th
Period 2, day 21, you would sync March 21-April 20th

# Export

A UCR data source can be exported, to back an excel dashboard, for instance.
The URL for exporting data takes the form https://www.commcarehq.org/a/[domain]/configurable_reports/data_sources/export/[data source id]/
The export supports a "$format" parameter which can be any of the following options: html, csv, xlsx, xls.
The default format is csv.

This export can also be filtered to restrict the results returned.
The filtering options are all based on the field names:


URL parameter          | Value          | Description
-----------------------|----------------|-----------------------------
{field_name}           | {exact value}  | require an exact match
{field_name}-range     | {start}..{end} | return results in range
{field_name}-lastndays | {number}       | restrict to the last n days

This is configured in `export_data_source` and tested in `test_export`.  It
should be pretty straightforward to add support for additional filter types.

### Export example

Let's say you want to restrict the results to only cases owned by a particular
user, opened in the last 90 days, and with a child between 12 and 24 months old as an xlsx file.
The querystring might look like this:
```
?$format=xlsx&owner_id=48l069n24myxk08hl563&opened_on-lastndays=90&child_age-range=12..24
```

# Practical Notes

Some rough notes for working with user configurable reports.

## Getting Started


The easiest way to get started is to start with sample data and reports.

First copy the dimagi domain to your developer machine.
You only really need forms, users, and cases:

```
./manage.py copy_domain https://<your_username>:<your_password>@commcarehq.cloudant.com/commcarehq dimagi --include=CommCareCase,XFormInstance,CommCareUser
```

Then load and rebuild the data table:

```
./manage.py load_spec corehq/apps/userreports/examples/dimagi/dimagi-case-data-source.json --rebuild
```

Then load the report:

```
./manage.py load_spec corehq/apps/userreports/examples/dimagi/dimagi-chart-report.json
```

Fire up a browser and you should see the new report in your domain.
You should also be able to navigate to the edit UI, or look at and edit the example JSON files.
There is a second example based off the "gsid" domain as well using forms.

The tests are also a good source of documentation for the various filter and indicator formats that are supported.

## Static data sources

As well as being able to define data sources via the UI which are stored in the database you
can also define static data sources which live as JSON documents in the source repository.

These are mainly useful for custom reports.

They conform to a slightly different style:
```
{
    "domains": ["live-domain", "test-domain"],
    "config": {
        ... put the normal data source configuration here
    }
}
```

Having defined the data source you need to add the path to the data source file to the `STATIC_DATA_SOURCES`
setting in `settings.py`. Now when the static data source pillow is run it will pick up the data source
and rebuild it.

Changes to the data source require restarting the pillow which will rebuild the SQL table. Alternately you
can use the UI to rebuild the data source (requires Celery to be running).


## Static configurable reports

Configurable reports can also be defined in the source repository.  Static configurable reports have
the following style:
```
{
    "domains": ["my-domain"],
    "data_source_table": "my_table",
    "report_id": "my-report",
    "config": {
        ... put the normal report configuration here
    }
}
```

## Custom configurable reports

Sometimes a client's needs for a rendered report are outside of the scope of the framework.  To render
the report using a custom Django template or with custom Excel formatting, define a subclass of
`ConfigurableReportView` and override the necessary functions.  Then include the python path to the class
in the field `custom_configurable_report` of the static report and don't forget to include the static
report in `STATIC_DATA_SOURCES` in `settings.py`.

## Extending User Configurable Reports

When building a custom report for a client, you may find that you want to extend
UCR with custom functionality. The UCR framework allows developers to write
custom expressions, and register them with the framework. To do so, simply add
a tuple to the `CUSTOM_UCR_EXPRESSIONS` setting list. The first item in the tuple
is the name of the expression type, the second item is the path to a function
with a signature like conditional_expression(spec, context) that returns an
expression object. e.g.:

```
# settings.py

CUSTOM_UCR_EXPRESSIONS = [
    ('abt_supervisor', 'custom.abt.reports.expressions.abt_supervisor'),
]
```

Following are some custom expressions that are currently available.

- `location_type_name`:  A way to get location type from a location document id.
- `location_parent_id`:  A shortcut to get a location's parent ID a location id.
- `get_case_forms`: A way to get a list of forms submitted for a case.
- `get_subcases`: A way to get a list of subcases (child cases) for a case.
- `indexed_case`: A way to get an indexed case from another case.

You can find examples of these in [practical examples](examples/examples.md).

## Scaling UCR

### Profiling data sources

You can use `./manage.py profile_data_source <domain> <data source id> <doc id>`
to profile a datasource on a particular doc. It will give you information such
as functions that take the longest and number of database queries it initiates.

### Faster Reporting

If reports are slow, then you can add `create_index` to the data source to any
columns that have filters applied to them.

### Asynchronous Indicators

If you have an expensive data source and the changes come in faster than the
pillow can process them, you can specify `asynchronous: true` in the data source.
This flag puts the document id in an intermediary table when a change happens
which is later processed by a celery queue. If multiple changes are submitted
before this can be processed, a new entry is not created, so it will be processed
once. This moves the bottle neck from kafka/pillows to celery.

The main benefit of this is that documents will be processed only once even if many
changes come in at a time. This makes this approach ideal datasources that don't
require 'live' data or where the source documents change very frequently.

It is also possible achieve greater parallelization than is
currently available via pillows since multiple Celery workers can process
the changes.

A diagram of this workflow can be found [here](examples/async_indicator.png)

## Inspecting database tables

The easiest way to inspect the database tables is to use the sql command line utility.

This can be done by runnning `./manage.py dbshell` or using `psql`.

The naming convention for tables is: `config_report_[domain name]_[table id]_[hash]`.

In postgres, you can see all tables by typing `\dt` and use sql commands to inspect the appropriate tables.
Reports Overview
================

There are two main components involved in producing a report:

* a data source configuration
* a report configuration


The data source
---------------

A data source is a table in PostgreSQL. It is defined in a DataSourceConfiguration instance. This determines where its data comes from (cases or forms), and how the data is filtered. The data source is populated by a background task. Generally, there is one row per case or form. (Rarely, there can be more than one.)


Report configurations
---------------------

Report configurations define queries on data sources. They are stored in ReportConfiguration instances.

Report configurations offer two kinds of filters:

* Default filters
* User filters

**User filters** offer the user the ability to filter report results themselves. This is usually for limiting results to a specific location, or date range, or mobile worker.

**Default filters** are applied first, and are transparent to end users; i.e. users who use the report will not be made aware that default filters have been applied before results are filtered by their user filters.

More than one report configuration can use the same data source configuration, but the Report Builder creates a new data source for each new report. (In the case of UCRs, default filters are a useful way to reuse data sources.)

Report configurations select columns from data source indicators. They can create new columns by aggregating data, or counting discrete values.

In report builder, "list" reports are not aggregated, and "summary" reports are. Report Builder limits aggregations to *average*, *sum* and *count*.


User-Configurable Reports
=========================

UCRs allow developers and TFMs/TPMs to define data sources and reports using JSON. You can find comprehensive documentation at [corehq/apps/userreports/README.md](../README.md).


Report Builder
==============

Report Builder is a friendlier user interface for defining UCRs. Its emphasis is on usability, with a trade-off on report functionality.

The front end is built on the KnockoutJS framework.

You can find an overview of how the KnockoutJS ViewModel is populated at [corehq/apps/userreports/reports/builder/README.md](./builder/README.md).

The ViewModel itself is [corehq/apps/userreports/static/userreports/js/builder_view_models.js](../static/userreports/js/builder_view_models.js).

When the user opens Report Builder, and chooses whether their data comes from cases or forms, Django will create a temporary data source for the Report Builder preview. The data source includes columns for as many indicators as possible (with a maximum of 300 columns). The same data source is used for "list" reports and "summary" reports. It will be populated with up to 100 rows.

Every change the user makes in the interface will fetch an updated preview by running the current state of the report configuration against the data source, and rendering the result as the final report would be rendered.
The "Report Builder" feature allows users to configure User Configurable Reports through a GUI, instead of writing
the JSON configuration "by hand."


# Design overview

## Populating the front end

### `DataSourceBuilder.data_source_properties`
This dictionary represents the set of all possible form questions or metadata or case
properties that could appear in a report data source.

### `DataSourceBuilder.report_column_options`
This dictionary represents the set of all possible indicators that could appear in a
report. `report_column_options` are mostly derived from `data_source_properties`, but
there are some indicators that can be displayed in a report that don't map directly to
any data source column, such as a "Count" column in an aggregated report, which would
show the number of rows aggregated.

Each data source property yields corresponding report column options through
`DataSourceProperty.to_report_column_option()`

In the report builder front end, report_column_options are used to populate the select
widgets for the report indicators, but data_source_properties are used for configuring
filters.


## Generating the report from user configuration
The configuration created in the browser must be converted to a data source and report
configuration.

### Data Source
The data source indicators are created by mapping the data source property and report
column option ids sent from the browser to the corresponding `DataSourceProperty` and
`ReportColumnOption` objects. We then call `ReportColumnOption.get_indicators()` and
`DataSourceProperty.to_report_filter_indicator()` to get the actual indicator configs

### Report configuration
`ReportColumnOption.to_column_dicts()` returns the column configuration necessary for the
given report column option.
This is an app that wraps the phone facing API for CommCare phones.  
# Analytics
We use multiple analytics platforms, tracking events used primarily by the product and growth teams. This includes tracking general usage (like page visits), tracking custom events (like when a user clicks a specific button), and managing A/B tests.

[Directory of events and properties we track in these platforms](https://docs.google.com/spreadsheets/d/1frMdFeznNcMAIyMW3pG3zes6mmY03UG67HyMUHXlb-s/edit#gid=1804103672)

## Technical Overview

### Server Side

This varies depending on the service; see details on individual services below.

### Client Side

For passing data from the server to the client, which is mostly API keys, analytics uses a variation on [initial_page_data](https://github.com/dimagi/js-guide/blob/master/integration-patterns.md): same general idea, but with better namespacing and accessed via [initial.js](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/static/analytix/js/initial.js). Most of the analytics templates just contain this initial data, while a few contain the actual third-party scripts (for the services that don't interact with any other HQ JavaScript).

Analytics has its own logging infrastructure, is set up in [logging.js](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/static/analytix/js/logging.js) and prints to the browser console. The logging level can be controlled via `settings.ANALYTICS_CONFIG['LOG_LEVEL']` (see "Debugging" below).

Analytics code is inherently somewhat fragile because it depends on third-party services. There are two ways this fragility has repeatedly manifested:
- Script inclusions: Each service has a script they host that we have to include on our pages, which may fail due to an adblocker or other reason. Analytics needs to fail gracefully in these cases. This leads to analytics code being promise-driven.
- Callbacks: Events are often fired when a user takes an action that will lead them to a different page. The event triggers an ajax request to the third-party service, and we have to wait for it to complete before letting the user move on, since leaving the page would cancel the pending request and we'd lose the data. This leads to a pattern where the "main" behavior of a tracked button (e.g., submitting a form) is contained in a callback which is executed when the analytics request is finished (or when that request has failed, or when that request has taken too long to justify making the user wait for it...).

Beyond the general infrastructure, there's a JavaScript module for each of the major analytics services. Each of these has initialization logic that checks if analytics is available for the given server and user, loads the service's script(s), and then typically makes a call to the service to identify the current user. These modules generally expose one or more tracking functions to be called from various other parts of HQ.

### A/B tests

New tests need to be added to [ab_tests](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/ab_tests.py). Typically, view code will check the test's `version` and set a corresponding flag in the template context, which will then use that flag to deliver the appropriate content for the user's test group.

### Handling different environments and debugging

In production, analytics are tracked only\* on SaaS servers - that is, on [www.commcarehq.org](http://www.commcarehq.org). This is controlled by the `isEnabled` property in [global.html](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/templates/analytics/initial/global.html). All other servers bypass the setup code.

Analytics are run in staging via a debug flag. This debug flag, along with the necessary API keys, can be set in localsettings to enable analytics on your local server:
- `ANALYTICS_IDS`: Analytics code doesn't run if the relevant API key isn't provided. For most purposes, setting the key to a dummy value is sufficient. We have test API keys for Google Analytics and Kissmetrics; you can pull these from the [staging vault](https://github.com/dimagi/commcare-cloud/tree/master/src/commcare_cloud/ansible/README.md#managing-secrets-with-vault).
- `ANALYTICS_CONFIG.DEBUG`: Set `DEBUG` to `True` to enable analytics and override the server-specific checks (you still need to set the API keys, too).
- `ANALYTICS_CONFIG.LOG_LEVEL`: Controls the client-side logging. Turning it up to `verbose` can help debug.

\* ICDS also tracks some analytics, but this happens outside of the main analytics framework described in these docs.

## Individual Services

### Google Analytics

Used primarily by product team.

No server component, just [google.js](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/static/analytix/js/google.js). We track events using `<module>.track.click` and `<module>.track.event`. We also use the default tracking (page views, etc.). Google has a few tracking options; we use their [gtag.js](https://developers.google.com/analytics/devguides/collection/gtagjs/).

### Kissmetrics

Used primarily by product team.

Most A/B tests are tracked using client side Kissmetrics code, so [kissmetrix.js](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/static/analytix/js/kissmetrix.js) includes test setup.

There is documentation for setting up A/B tests with kissmetrics via [SessionABTest](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/ab_tests.py).

Most events are tracked client side using `<module>.track.event`. Some are done server side, using `track_workflow` and `identify` functions in the [analytics tasks](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/tasks.py) file. `track_workflow` is used to register events and accepts an optional argument to update properties as well. `identify` can be used if you are only looking to update a property. From the data side, it doesn't matter whether the tracking was done on the client or the server.

In addition to the event-based code, the `track_periodic_data` task runs nightly and sends a variety of aggregated data to Hubspot and Kissmetrics (form submission count, mobile worker count, etc.).

We have a sandbox "site" on Kissmetrics that allows you to test and debug Kissmetrics usage if you set `ANALYTICS_IDS.KISSMETRICS_KEY` in localsettings (key is in the staging vault).

You can also see events arriving almost in real time at [https://app.kissmetrics.com/live](https://app.kissmetrics.com/live).

### HubSpot

Used heavily by growth team.

Most of the code is server side [analytics tasks](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/tasks.py) that sends a "form" to Hubspot when a particular action happens on HQ.

On the client side, [hubspot.js](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/static/analytix/js/hubspot.js) has functions to identify users and track events, but these are barely used. We do include a Hubspot-provided script that tracks basic usage (e.g., page visits) and also sets a cookie to identify the user (described [here](https://knowledge.hubspot.com/articles/kcs_article/reports/what-cookies-does-hubspot-set-in-a-visitor-s-browser) as the "hubspotutk" cookie). The server's form-sending code checks for this cookie and, if it isn't present, doesn't send forms.

In addition to the event-based code, the `track_periodic_data` task runs nightly and sends a variety of aggregated data to Hubspot and Kissmetrics (form submission count, mobile worker count, etc.).

#### Adding/Removing Hubspot properties

We track various user properties as [Hubspot Contact Properties](http://knowledge.hubspot.com/contacts-user-guide-v2/how-to-use-contact-and-company-properties). We have bunch of celery tasks and function that update these contact properties via [Hubspot REST API](http://developers.hubspot.com/docs/methods/contacts/create_or_update). We can update only those properties that are available on Hubspot portal. When we mention new Hubspot properties in HQ-Hubspot API calls, make sure that these properties are available in Hubspot portal. If they are not available, [create](http://knowledge.hubspot.com/contacts-user-guide-v2/how-to-create-contact-and-company-properties) them or ping marketing team to have them created on Hubspot portal first. To update a list of properties you can use the [update_hubspot_properties](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/tasks.py#L174) function.

#### Hubspot Form Submissions
We use the hubspot form API to submit forms to hubspot via the `_send_form_to_hubspot` function in the analytics tasks file. You can look through that file for examples but the general procedure is to create a new function with the `@analytics_task()` decorator to make it asynchronous and ensure it is retried on failure. This function should then call `_send_form_to_hubspot` with the form id of the form you are trying to submit. All form ids are listed as constants at the top of the file, and new forms can be created on the hubspot site.

#### Sign-In and Sign-Up Hubspot Form Tracking
A special signup form are sent down to hubspot in `track_user_sign_in_on_hubspot`. This is just for handling the specific hubspot forms during the sign in / sign up process.

#### User Registration Hubspot Analytics
Much of the analytics we use in hubspot are generated during the user registration process. We send down those analytics in the `track_web_user_registration_hubspot`.
Any changes to user properties related to the registration forms should be made here.

#### Testing

To start testing, run Celery and update `HUBSPOT_API_KEY` and `HUBSPOT_ID` in `settings.ANALYTICS_IDS`. Hubspot provides a public demo portal with API access for testing. The credentials for this are available on their [API overview page](http://developers.hubspot.com/docs/overview). If you need to test using our production portal the credentials can be found in dimagi_shared keepass. Let marketing know before testing on production portal and clean up after the testing is finished

When troubleshooting in Hubspot's portal, it's often useful to create lists based on key events.

### Drift

This is the live chat feature available for new users. There's a [drift.js](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/static/analytix/js/drift.js) HQ module, though it doesn't do much. No server component.

### Fullstory

Generally available in areas of interest to the product and growth teams: signup, app builder, report builder. We include their script but there's no other interaction with their code - no events, etc. Not much related code; there's a [fullstory.html](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/analytics/templates/analytics/fullstory.html) template to include their script but no HQ JavaScript module and no server component.

### Facebook Pixel

Their script is included in [signup](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/registration/templates/registration/register_new_user.html), but we don't do any event tracking or other interaction with it. Very little related code, just the script inclusion.
# Exports

### Architecture

Exports are designed to build off the corresponding application to generate a schema that represents the questions, properties, and system properties that are available to the user to select. There is exactly one schema for each Application/Module/Form triplet or Application/Case Type pair. On initial generation of an export schema, the export will be generated by only taking into account the current or "live" application. If the user chooses to view deleted questions, it will iterate through each built application that has `has_submissions` set to True.

Example:

Suppose there exists the following app builds

| app_id  | build_version | questions |
|---|---|---|
| 1234  | 12 (current) | q1,q2,q4   |
| 1234  | 10  | q1,q3   |
| 1234  | 1  | q1,q2,q3   |

Below illustrates what the schema will look like after processing each app from beginning to current. The example schema is simplified for understanding. Each question has an app_id and version associated with it.

After processing build_version 1:
```
q1.last_occurences = { app_id: 1 }
q2.last_occurences = { app_id: 1 }
q3.last_occurences = { app_id: 1 }
```

After processing build_version 10:
```
q1.last_occurences = { app_id: 10 }
q2.last_occurences = { app_id: 1 }
q3.last_occurences = { app_id: 10 }
```

After processing build_version 12 (current version, not necessarily built):
```
q1.last_occurences = { app_id: 12 }
q2.last_occurences = { app_id: 12 }
q3.last_occurences = { app_id: 10 }
q4.last_occurences = { app_id: 12 }
```

The export that is then generated will look something like this:

| question | is selected (by default) | is marked deleted | is hidden from user |
|------|---|---|---|
| q1 | ✓ |  |  |
| q2 | ✓ |  |  |
| q3 | | ✓ | ✓ |
| q4 | ✓ |  |  |

Since q3's latest build_version is 10, the code deduces that it has been deleted and therefore hides it and marks it as deleted.

### Exporting remote apps / defining your own schema

In order to export remote apps, you will need to define your own schema for the export since there are no forms and modules to build the export off of.

To enable the ability to do this turn on the toggle:
```
ALLOW_USER_DEFINED_EXPORT_COLUMNS ('Allows users to specify their own export columns')
```

The UI will then enable you to add columns and tables with a blank textbox to add a path. Paths are specified in a dot notation.

Support the form looked like this:

```
<data>
  <question1></question1>
<data>
```

To specify this in `.` notation, it'd look like this in the schema:
```
form.question1
```

If you need to specify a repeat group and the form looks like this:

```
<data>
  <repeat>
    <question1></question1>
  </repeat>
</data>
```

The table path for this repeat would be:
```
form.repeat[]
```
Note the `[]` after the question. This tells the schema that it is a repeat group.

Any columns added to this table will need to be prefixed with this path. So a column in the table would be:

```
form.repeat[].question1
```

### System Properties

System properties are properties that CommCareHQ adds to the form or case that are essentially meta data.  Examples of these include: form id, case type, case id, form xmlns, etc. System properties are added to a white list. This means that by default a system property on the form will _not_ be added to the export for selection. A list of the system properties can be found in [corehq/apps/export/system_properties.py](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/export/system_properties.py)

### Optimizations

Often times iterating through each build in an application can be time consuming. To reduce the time to process an application, the code only processes applications that have been marked as having submissions.

### Caveats and edge cases

- Unknown deleted questions: It is possible to have an export where there lists properties that do not have any data associated with them. This case can arise when adding a question, `q1`, to the current application (without making a build), opening an export (to kick off the processing of the current application), then deleting `q1` before making a build. `q1` will now always be in the schema but will be shown as deleted.
# Application terminology

For any given application, there are a number of different documents.

The primary application document is an instance of `Application`.  This
document's id is what you'll see in the URL on most app manager pages. Primary
application documents should have `copy_of == None` and `is_released ==
False`. When an application is saved, the field `version` is incremented.

When a user makes a build of an application, a copy of the primary
application document is made. These documents are the "versions" you see on
the deploy page. Each build document will have a different id, and the
`copy_of` field will be set to the ID of the primary application document.
Additionally, some attachments such as `profile.xml` and `suite.xml` will be
created and saved to the build doc (see `create_all_files`).

When a build is starred, this is called "releasing" the build.  The parameter
`is_released` will be set to True on the build document.

You might also run in to "remote" applications and applications copied to be
"published on the exchange", but those are quite infrequent.
Vellum
======

[![Build Status](https://travis-ci.org/dimagi/Vellum.svg?branch=master)](https://travis-ci.org/dimagi/Vellum)

Vellum is a JavaRosa [XForm](http://en.wikipedia.org/wiki/XForms) designer used
in [CommCare HQ](http://github.com/dimagi/commcare-hq).

![](http://i.imgur.com/PvrL8Rr.jpg)

Image courtesy of the [ReMIND
project](https://www.commcarehq.org/exchange/325775003aa58cfcefbc75cfdf132e4d/info/).

Usage
-----

Checkout the source from [GitHub](https://github.com/dimagi/Vellum)

Optionally, build an optimized version

```sh
$ make # artifacts will be in _build dir and also vellum.tar.gz
```

Then load it on a page using [RequireJS](http://requirejs.org), optionally with
an existing jQuery instance:

```html
<link rel="stylesheet" href="path/to/bootstrap.css"></link>
<link rel="stylesheet" href="path/to/vellum/style.css"></link>
<!-- optional, if using bundled jquery et al -->
<link rel="stylesheet" href="path/to/vellum/global-deps.css"></link>

<!-- 
Optionally reuse existing jQuery instance with Bootstrap.  
If not present, bundled versions will be loaded.  -->
<script src="jquery.js"></script>
<script src="bootstrap.js"></script>

<script src="require.js"></script>
<script>
    require.config({
        packages: [
            {
                name: 'jquery.vellum',
                location: "/path/to/vellum/src"
            }
        ]
    });

    require(["jquery.vellum"], function () {
        require(["jquery"], function ($) {
            $(function () {
                $('#some_div').vellum(VELLUM_OPTIONS);
            });
        });
    });
</script>
```

See
[here](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/app_manager/templates/app_manager/v1/form_designer.html)
and `tests/main.js` for example options usage.

Vellum targets modern browsers.  IE8 and earlier are not supported.

Tests
-----

Make sure everything is up to date:

```
$ bower update
$ npm update
```

Test in a browser:
```
$ `npm bin`/http-server -c-1
$ chromium-browser http://localhost:8080
```

By default, the test page will load the non-built version unless a `built`
parameter is present in the query string.

Commands to run tests headlessly:
```
grunt test
grunt test --grep="test grep"
```

You can also use `grunt watch` to test as file changes happen.

Contributing
------------

Follow the [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript).

Install dependencies:
```
$ npm install
```

Build optimized version (test locally by changing `useBuilt` in `tests/main.js`):
```
$ make
```
# CKEditor 4 - The best browser-based WYSIWYG editor

[![devDependency Status](https://david-dm.org/ckeditor/ckeditor-dev/dev-status.svg)](https://david-dm.org/ckeditor/ckeditor-dev#info=devDependencies)

This repository contains the development version of CKEditor.

**Attention:** The code in this repository should be used locally and for
development purposes only. We do not recommend using it in production environment
because the user experience will be very limited. For that purpose, you should
either build the editor (see below) or use an official release available on the
[CKEditor website](http://ckeditor.com).

## Code Installation

There is no special installation procedure to install the development code.
Simply clone it to any local directory and you are set.

## Available Branches

This repository contains the following branches:

  - **master** &ndash; Development of the upcoming minor release.
  - **major** &ndash; Development of the upcoming major release.
  - **stable** &ndash; Latest stable release tag point (non-beta).
  - **latest** &ndash; Latest release tag point (including betas).
  - **release/A.B.x** (e.g. 4.0.x, 4.1.x) &ndash; Release freeze, tests and tagging.
    Hotfixing.

Note that both **master** and **major** are under heavy development. Their
code did not pass the release testing phase, though, so it may be unstable.

Additionally, all releases have their respective tags in the following form: 4.4.0,
4.4.1, etc.

## Samples

The `samples/` folder contains some examples that can be used to test your
installation. Visit [CKEditor SDK](http://sdk.ckeditor.com/) for plenty of samples
showcasing numerous editor features, with source code readily available to view, copy
and use in your own solution.

## Code Structure

The development code contains the following main elements:

  - Main coding folders:
    - `core/` &ndash; The core API of CKEditor. Alone, it does nothing, but
    it provides the entire JavaScript API that makes the magic happen.
    - `plugins/` &ndash; Contains most of the plugins maintained by the CKEditor core team.
    - `skin/` &ndash; Contains the official default skin of CKEditor.
    - `dev/` &ndash; Contains some developer tools.
    - `tests/` &ndash; Contains the CKEditor tests suite.

## Building a Release

A release-optimized version of the development code can be easily created
locally. The `dev/builder/build.sh` script can be used for that purpose:

	> ./dev/builder/build.sh

A "release ready" working copy of your development code will be built in the new
`dev/builder/release/` folder. An Internet connection is necessary to run the
builder, for its first time at least.

## Testing Environment

Read more on how to set up the environment and execute tests in the [CKEditor Testing Environment](http://docs.ckeditor.com/#!/guide/dev_tests) guide.

## Reporting Issues

Please use the [CKEditor Developer Center](https://dev.ckeditor.com/) to report bugs and feature requests.

## License

Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.

For licensing, see LICENSE.md or [http://ckeditor.com/license](http://ckeditor.com/license)
# Media Uploader component

by Biyeun Buczyk, extracted from CommCare HQ.

YUI files built with http://yuilibrary.com/yui/configurator/

See Vellum and CommCare HQ for usage examples.

## Guess at original build procedure

NOTE: tried this procedure with YUI 3.17.2, both with and without the "loader"
rollup. The result was broken so either there is a regression beteen 3.16.0 and
3.17.2 or this procedure is incomplete.

Go to http://yuilibrary.com/yui/configurator/

Options:

    File Type: Raw
    Combine Files: Yes

Selected Modules (this is a guess):

    node-core
    uploader

Getting the files:

- Copy the Output Console into yui-config.html
- Use download the JS files (URLs abbreviated for readability)

    curl "http://yui.yahooapis.com/combo?.../yui-base/yui-base.js&..." > yui-base.js
    curl "http://yui.yahooapis.com/combo?.../uploader/uploader.js" > yui-uploader.js

## Components added later to fix Firefox blocked content errors

Procedure: load Vellum in Chrome and watch the network pane (with caching
disabled) in developer tools for requests to yui.yahooapis.com. Then download
the content into local files:

    curl "http://yui.yahooapis.com/combo?3.16.0/widget-base/assets/skins/sam/widget-base.css&3.16.0/cssbutton/cssbutton-min.css" > yui-combo.css
    curl http://yui.yahooapis.com/3.16.0/build/loader/loader.js > yui-loader.js

NOTE while the CSS is probably necessary, the loader should not be.
TODO figure out why the loader is being requested and make it not happen.
Syncing local HQ instance with an Android Phone
===========================

## No syncing or submitting, easy method

If you would like to use a url or barcode scanner to download the application to
your phone here is what you need to setup. You won't be able to submit or sync
using this method, but it is easier.

### Make sure your local django application is accessible over the network

The django server will need to be running on an ip address instead of localhost.
To do this, run the application using the following command, substituting your
local IP address.

`./manage.py runserver 192.168.1.5:8000`

Try accessing this url from the browser on your phone to make sure it works.

### Make CommCare use this IP address

The url an application was created on gets stored for use by the app builder
during site creation. This means if you created a site and application
previously, while using a 'localhost:8000' url, you will have to make a code
tweak to have the app builder behave properly.

The easiest way to check this is to see what url is shown below the barcode on
the deploy screen.

If it is currently displaying a `localhost:8000/a/yourapp/...` url then open
`localsettings.py` and set `BASE_ADDRESS = "192.168.1.5:8000"` substituting
`192.168.1.5` with your local IP address.

### Try it out

With this set up, you should be able to scan the barcode from your phone to
download and install your own locally built CommCare application!

## Submitting and syncing from your local HQ instance (harder method)

### Install nginx

`sudo apt-get install nginx` or

`brew install nginx`

### Install the configuration file

In `/etc/nginx/nginx.conf`, at the bottom of the `http{}` block, above any other site includes, add the line:

`include /path/to/commcarehq/deployment/nginx/cchq_local_nginx.conf;`

### Start nginx

`sudo nginx`

### Make sure your local django application is accessible over the network

`./manage.py runserver`

Try accessing `http://localhost/a/domain` and see if it works. nginx should
proxy all requests to localhost to your django server. You should also be able
to access `http://your_ip_address/a/domain` from a phone or other device on the
same network.

### Make Commcare use your local IP address

Set the `BASE_ADDRESS` setting in `localsettings.py` to your IP address (e.g.
`192.168.0.10`), without a port. You'll have to update this if you ever change
networks or get a new IP address.

### Rebuild and redeploy your application
You'll have to rebuild and redeploy your application to get it to sync.

Adding CommCare (J2ME) Builds to CommCare HQ
=====================================

Following is a manual process to find and import a build. Alternatively, you can run
`./manage.py commcare_build_importer` to do the same without leaving your console.
This will run you through all the builds and let you import the build you need.

* First you need to get the CommCare build off the Dimagi build server:
    1. Go here https://jenkins.dimagi.com/
    2. Select the commcare-core job for the version of CommCare you are interested in (e.g. "commcare-core-2.30")
    3. Pick a build (probably the first one in the table on the left) and write down
       the build number (under "#"). This will be referenced as `$build_number`
       below
    4. Click on that row
    5. Select the "Environment Variables" tab and write down the VERSION (all
       the way at the bottom of the table.) This will
       be referenced as `$version` below
    6. Go back, and select "Build Artifacts" -> "application" -> "posttmp" -> "artifacts.zip".   If you use the commandline option below,
       note the path of the downloaded file. This will be
       referenced as `$build_path`.
       If you use the web UI, copy the download URL. This will be called `build_url`.

You now have two options for how to install it.

* Command line:
    * `cd` into the commcare-hq root directory, and run the following command:
      `python manage.py add_commcare_build $build_path $version $build_number`
* Web UI
    * Go to `/builds/edit_menu/` and follow the instructions at the bottom for adding your build.

Now make sure the build is available in the app settings.  Go to `/builds/edit_menu/`, then add the version and a label. You can also set the default here to be the version you've added.

Finally, in order to get full permissions on a J2ME phone, you need to set up jar signing. To do so, you will need
acquire a code signing certificate (from e.g. Thawte).

* To enable jar signing, put your certificate information in localsettings.py as follows:

<!-- language: lang-py -->

    JAR_SIGN = dict(
        key_store = "/PATH/TO/KEY_STORE",
        key_alias = "KEY",
        store_pass = "*****",
        key_pass = "*****",
    )

* If you don't need this, skip this step by commenting out the code entirely:

<!-- language: lang-py -->

    #JAR_SIGN = dict(
    #    key_store = "/PATH/TO/KEY_STORE",
    #    key_alias = "KEY",
    #    store_pass = "*****",
    #    key_pass = "*****",
    #)

You're done!
# CommCare HQ Indicators

## Overview

You can split the indicators into two categories:

- Document Indicators
- Dynamic Indicators

## Document Indicators

Document Indicators are precomputed and stored inside of the `computed_` property of an `XFormInstance` or
`CommCareCase`. Each indicator is namespaced, and the result that's stored inside the document looks something like:

```javascript
computed_: {
    namepspace: {
        indicator_slug: {
            version: <int>, // the version number
            value: '', // result from from get_clean_value()
            multi_value: <bool>, // true if value contains a dict, false otherwise
            type: '', // doc_type of the Indicator Definition used to create this
            updated: <date> // date of last document update for this indicator
        }
    }
}
```

### Versioning

Version numbers are used if when indicator definition changes and you want to update the indicators set in documents
that have already been processed. This comes from `update_computed_namespace`.

### How are indicators updated?

#### Pillowtop

As `XFormInstance` or `CommCareCase` documents are created or updated (by processes not related to indicator updates)
they will get picked up in the changes feed by the `MVPFormIndicatorPillow` or `MVPCaseIndicatorPillow`, respectively.

#### Retrospectively with `mvp_force_update`

Right now there is a management command that lives inside the `mvp-reports` submodule. This management command grabs
all of the related documents by `xmlns` and `domain` (for `XFormInstance`) and `case_type` and `domain`
(for `CommCareCase`). It checks to see whether the indicator inside each document exists with the version number
specified by the indicator definition. If it doesn't exist, the indicator is added and the document is saved.

Because some domains have quite a few documents, this management command is throttled to update only 100 documents at
a time, and runs `prime_views` in between each set of 100 documents. It's a work in progress, and we should definitely
find a better solution for this process in the future.

## Dynamic Indicators

Dynamic Indicators are computed 'on-the-fly' when the report referencing that indicator is rendered (or cached data is
retrieved). Existing examples of such reports can be found in the `mvp-reports` submodule: `mvp.reports.mvis` and
'mvp.reports.chw`.

There are essentially two types of Dynamic Indicators.

### Couch-Based Indicators

The simplest form is `CouchIndicatorDef`. It uses couch views that emit lines in the following format:

```
emit(["all", doc.domain, <indicator_key>, <year>, <month>, <day>, <optional_suffix>], 1 or <something>);
emit(["user", doc.domain, user_id, <indicator_key>, <year>, <month>, <day>, <optional_suffix>], 1 or <something>);
```

The value of what is emitted is used for computing different flavors of the Couch-Based Indicators. The simplest type,
however, just returns the reduced value of the view for whatever indicator key + date range you specify.

#### Essentials for Couch-Based Indicators

- `couch_view` - The name of the couch_view that contains the indicator key that you are interested in.
- `indicator_key` - The value in the emit string above where `<indicator_key>` is present.

Optional date shifts:
- `startdate_shift` - Shift the startdate of the datespan by n days. (+n is forward -n is backwards, as you expect)
- `enddate_shift` - Shift the enddate of the datespan by n days.
- `fixed_datespan_days` - Starddate of the datespan is completely discarded and a new startdate of `enddate - fixed_datespan_days` is used.
- `fixed_datespan_months` - Same functionality as above, except instead of days, it's months.

#### Other types of Couch-Based Indicators

##### `CountUniqueCouchIndicatorDef`

This counts the number of unique emitted entries. Example usage: Form indicators emit a case_id. This counts the # of unique case_ids at the end.

##### `MedianCouchIndicatorDef`

Takes the median of the emitted values.

##### `SumLastEmittedCouchIndicatorDef`

The emitted value looks something like:

```javascript
{
    _id: "", // unique ID string
    value: <int>
}
```

This will take all the values of the last emit with a unique id and sum those values.

#### Example Usage

Couch views for Couch-Based Indicators can be found in the `submodules/mvp/mvp_apps` couchapp.

Visit [http://www.commcarehq.org/a/mvp-potou/indicators/](http://www.commcarehq.org/a/mvp-potou/indicators/) for example
indicator definitions.


### Combined Indicators

For the indicators that require ratios between two existing indicators (always referenced by their slugs), use
`CombinedCouchViewIndicatorDefinition` and specify the `numerator_slug` and `denominator_slug`.


## Dev instructions for setting up a test locally
1. Create a doc called with id 'INDICATOR_CONFIGURATION' in the main db in couch with the following format:

    ```json
    {
        "_id": "INDICATOR_CONFIGURATION",
        "_rev": "3-a9b15be07f90fe19a55315c5f5036dec",
        "namespaces": {
            "indicator-project": [
                ["my_indicators", "MY INDICATORS!"]
            ]
        }
    }
    ```
    (`indicator-project` should be the name of the project you want to test on.)
2. Make sure you have an app in your domain, and note down the XMLNS of a form
3. Go to your domain > Reports > Administer Indicators > Form Label Indicators
and add a new Form Label Indicator. (You'll need the XMLNS from step 2.)
4. Run

    ```bash
    ./manage.py run_ptop --pillow-name=MVPFormIndicatorPillow
    ```
5. Submit a form with that XMLNS to your domain. (Can even do from commandline with something like

    ```bash
    curl -v -X POST --digest -u <user>@indicator-project.commcarehq.org \
    http://localhost:8000/a/indicator-project/receiver/secure/<app_id>/ -d @form.xml
    ```
6. Look up your form by id (it's in the 'X-CommCareHQ-FormID' header, so use -v/--verbose if using curl)
in couch and make sure that the 'computed_' property is set to something like {"my_indicators": ...}
Custom Data Fields
==================

This module provides tools for defining a custom data schema per domain for
a given entity type, such as User, Product, or Location.


Editing the model
-----------------

``CustomDataFieldsDefinition``
    This is a couch doc describing a particular schema.  It lists the
    entity type, but aside from that is completely generic - there are no
    special functions here for *Custom User Data*, for example.

``CustomDataModelMixin``
    Each entity type must provide a subclass of this mixin to provide the
    interface for editing the ``CustomDataFieldsDefinition``.  This
    subclass handles permissions and integration with the rest of that
    entity's section of HQ.

    For an example subclass, check out
    ``corehq.apps.users.views.mobile.custom_data_field.UserFieldsView``

    Currently, this view is passed to the generic components as a config
    object for the entity type.  We hope to split this out into a separate
    config class at some point.

``CustomDataFieldsForm``
    This is initialized by ``CustomDataModelMixin`` and shouldn't need to
    be accessed directly.  It handles it's own rendering.


Editing data for a particular entity
------------------------------------

``CustomDataEditor``
    A tool for editing the data for a particular entity, like an individual
    user.  This is intented to be used by composition.  For an example use
    case, check out
    ``corehq.apps.users.views.mobile.users.EditCommCareUserView``
    The *edit entity* view can have, for example, an instance of this
    Editor - ``custom_data`` - which will provide a form to be passed to
    the template.  The template need only include::

        {% if data_fields_form.fields %}
            {% crispy data_fields_form %}
        {% endif %}

    When handling the form submission on ``POST``, you should also call
    ``custom_data.is_valid()`` when validating the main form, and use
    ``custom_data.get_data_to_save()`` to update the custom data for that
    object before saving it.


Export and Bulk Upload
----------------------

This module does not alter the way data is stored on the individual
entities, so export should **Just Work**.

For upload, this module provides a validator accessible via the subclass of
``CustomDataModelMixin`` described above.  For example::

    custom_data_validator = UserFieldsView.get_validator(domain)

This ``custom_data_validator`` should then be passed the custom data for
each entity being uploaded, and it will verify that the data matches the
schema.  It will return either an error message or an empty string.

.. code-block:: python

    error = custom_data_validator(data)
    if error:
        raise UserUploadError(error)


Setting up a new entity type
----------------------------

To add a schema to custom data for an entiy, you need to do the following:

# Provide a subclass of ``CustomDataModelMixin`` specific to that entity
type.
# Add that view to the appropriate ``urls.py`` and to the site map in
``corehq.apps.hqwebapp.models``.  You should have available
``UserFieldsView.page_name()`` and ``UserFieldsView.urlname`` for this.
# Initialize and use the ``CustomDataEditor`` in the create and edit views
for that entity (and their templates).
# Use the *custom data validator* on bulk upload.
# Make a management command to bootstrap the custom data fields for
existing domains.  This should be run on the inital deploy.  You can
probably just start with a copypasta of one of the management commands in
this module.
### Adding a new Privilege

To add a new `Privilege`

+ Make sure there are no existing Privileges that you can reuse
+ Add the new privilege in appropriate places in `privileges.py` according to software plans
+ Run `python manage.py makemigrations --empty accounting` to create a migration
+ Rename the migration file to something more meaningful. (From Django 1.8+ you can supply a name to the makemigrations command: --name <migration_name>)
+ Add the following operation to the list of operations:

```python
migrations.RunPython(cchq_prbac_bootstrap),
```

This will create a new `Privilege` for you to use. See (Django data migrations)[https://docs.djangoproject.com/en/1.8/topics/migrations/#data-migrations] for more information.

### Removing a deprecated Privilege

To remove an old `Privilege`

+ Remove occurrences of the desired Privilege from all the places.
+ Add the privilege to `cchq_prabac_bootstrap.Command.OLD_PRIVILEGES`
+ Run migration

This will clean up discontinued privileges.
# Writing tests by using ES fakes

In order to be able to use these ES fakes. All calls to ES in the code you want to test
must go through one of the ESQuery subclasses, such as UserES or GroupES.

In testing, a **fake** is a component that provides an actual implementation of an API,
but which is incomplete or otherwise unsuitable for production.
(See http://stackoverflow.com/a/346440/240553 for the difference between fakes, mocks, and stubs.)

`ESQueryFake` and its subclasses (`UserESFake`, etc.) do just this for the `ESQuery`
classes. Whereas the real classes hand off the work to an Elasticsearch cluster,
the fakes do the filtering, sorting, and slicing in python memory, which is lightweight
and adequate for tests. Beware that this method is, of course,
inadequate for assuring that the `ESQuery` classes themselves are producing
the correct Elasticsearch queries, and also introduces the potential for bugs to go
unnoticed because of bugs in `ESQueryFake` classes themselves. But assuming correct
implementations of the fakes, it does an good job of testing the calling code,
which is usually the primary subject of a test.

The anatomy of a fake is something like this:
- For each real `ESQuery` subclass (I'll use `UserES` as the example),
  there is a corresponding fake (`UserESFake`).
  In cases where such a fake does not exist when you need it,
  follow the instructions below for getting started on a new fake.
- For each filter method or public method used on the `ESQuery` base class
  a method should exist on `ESQueryFake` that has the same behavior
- For each filter method on `UserES`, a method should exist on `UserESFake`
  that has the same behavior.

New fakes and methods are implemented only as actually needed by tests
(otherwise it's very difficult to be confident the implementations are correct),
so until some mythical future day in which all code that relies on ES goes through
an `ESQuery` subclass and is thoroughly tested, the fake implementations are
intentionally incomplete. As such, an important part of their design is that they alert
their caller (the person using them to write a test) if the code being tested calls a
method on the fake that is not yet implemented. Since more often than not a number of
methods will need to be added for the same test, the fakes currently are designed to have
each call to an unimplemented filter result in a no-op, and will output a logging statement
telling the caller how to add the missing method. This lets the caller run the test once
to see a print out of every missing function, which they can then add in one go and re-run
the tests. (The danger is that they will miss the logging output; however in cases where
a filter method is missing, it is pretty likely that the test will fail which will prod
them to look further and find the logging statement.)

## How to set up your test to use ES fakes

Patch your test to use `UserESFake` (assuming you want to patch `UserES`),
making sure to patch `UserES` in the *files in which it is used*, not the file in which
it is declared

```diff
+ @mock.patch('corehq.apps.users.analytics.UserES', UserESFake)
+ @mock.patch('corehq.apps.userreports.reports.filters.choice_providers.UserES', UserESFake)
  class MyTest(SimpleTestCase):
      def setUp(self):
...
+         UserESFake.save_doc(user._doc)
...
      def tearDown(self):
          UserESFake.reset_docs()
```

## How to set up a new ES fake

Adding a new fake is very easy. See [users_fake.py](./users_fake.py) for a simple example.
Mocha Tests
===========

## Adding a new app to test

There are three steps to adding a new app to test:

  1. Add the app name to the `Gruntfile.js` file. Note: the app has to correspond to an actual Django app.
  2. Create a mocha template in `corehq/apps/<app>/templates/<app>/spec/mocha.html` to run tests. See an example on [here](https://github.com/dimagi/commcare-hq/blob/master/corehq/apps/app_manager/templates/app_manager/spec/mocha.html).
  3. Create tests that are included in the template in `corehq/apps/<app>/static/<app>/spec/`


## Creating an alternative configuration for an app

Occasionally there's a need to use a different mocha template to run tests for the same app. In order to create multiple configurations, specify the app in the `Gruntfile.js` like this:

```
<app>#<config>
```

Now mocha will look for that template in `corehq/apps/<app>/templates/<app>/spec/<config>/mocha.html`

The url to visit that test suite is `http://localhost:8000/mocha/<app>/<config>`
# Sharding postgresql

We use [PL/Proxy](https://plproxy.github.io/) for sharding.

## Dev setup
The following PostgreSQL extensions are required:

* [PL/Proxy](https://plproxy.github.io)
* [pghashlib][pghashlib]

### Installing PL/Proxy

```
  $ sudo apt-get install postgresql-9.X-plproxy
```

### Installing pghashlib

* Download and extract source from [github][pghashlib]
* Build and install:

```
  $ PG_CONFIG=/usr/lib/postgresql/9.X/bin/pg_config make
  $ sudo PG_CONFIG=/usr/lib/postgresql/9.X/bin/pg_config make install
```

[pghashlib]: https://github.com/markokr/pghashlib

## Prod setup

1. Create the databases and update localsettings:

  * Assuming a 5 DB setup with 1024 shards
  * Update environment ansible YAML config as follows:

```
postgresql_dbs:
  - django_alias: default
    name: "{{localsettings.PG_DATABASE_NAME}}"
  - django_alias: proxy
    name: commcarehq_proxy
  - django_alias: p1
    name: commcarehq_p1
    shards: [0, 204]
  - django_alias: p2
    name: commcarehq_p2
    shards: [205, 409]
  - django_alias: p3
    name: commcarehq_p3
    shards: [410, 614]
  - django_alias: p4  
    name: commcarehq_p4  
    shards: [615, 819]  
  - django_alias: p5
    name: commcarehq_p5  
    shards: [820, 1023]
    
localsettings:
  USE_PARTITIONED_DATABASE: True
```

  * Run the `postgresql` ansible tag.
  * Run the `localsettings` ansible tag.

2. Migrate the databases

```
  $ fab [environment] manage:'migrate_multi --noinput'
```

3. Setup the sharding configuration for PL/Proxy

```
  $ fab [environment] manage:configure_pl_proxy_cluster
```
# HQ Pillowtop Infrastructure and Workflow

## About Pillows

Pillows are Couch `_changes` feed listeners. They listen to couch changes and do an operation on them in python, and do something.

Many pillows defined here take a couch (kafka) change, and send it over to elasticsearch to be indexed.
They may be transformed to make querying/indexing easier. What's sent to ES need not be 1:1 with what's from couch.

## HQPillow Elastic Workflow

Expect the following structure and components.

 * A mapping in `corehq/pillows/mappings`
    * Mappings are pre-determined structures you send to ES to help type out stuff you want to index.
 * A pillow class generator in `corehq/pillows`
 * A reindexer in the same file
 * Update the `corehq/apps/hqcase/management/commands/ptop_reindexer_v2.py`  management command to register the pillow in the pillowtop preindexing workflow
 * Add your pillow to the main `settings.py`


## Command Reference
 * `ptop_preindex` will call all the registered ptop_fast_reindexers
 * `ptop_es_manage` when called in our deployment workflow (see command flags for reference) - it can flip the index aliases to what's considered master to turn on preindexed indices.
# Couchapps

This app is a collection of couch design documents that are isolated from any
sort of module or code context. This is often useful for stuff like code
organization, syncing the design docs to multiple dbs, or performance (see
below).


## Note on CouchDB

For a more in-depth overview, I recommend @dannyroberts' excellent article:
["What every developer should know about CouchDB"](https://gist.github.com/dannyroberts/8d514fb6460a9f4f0404)

#### Databases
**Problem:**
Couch databases do not distinguish between different document types.  Any views
you write have to interact with every document in that database.

**Solution:**
Store each type of document in a separate database. CommCareHQ has historically
used one monolithic couch database, but we are gradually moving things into
their own databases.  This module's `__init__.py` lets you specify which
databases to sync each design document (and by extention, view) to.

#### Design documents and views
**Problem:**
A design document stores any number of views (and filters, but we rarely use
those).  Changing or deleting a view is considered a change to the design
document, and the whole design document (including all the views) must be
synced.

**Solution:**
Make your design documents as small as possible - usually just one view.
`couchapps` helps facilitate this.


## What this module does

Normal apps (modules) in our codebase  can have a `_design` directory which
defines a design doc. In this directory will be some number of views.

```
- app_manager/
   - _design/
      + filters/
      - views/
         - builds_by_date/
            map.js
            reduce.js
         + saved_app/
         + forms_by_xmlns/
```

This creates a single design doc with three views.  Here's what they might look
like in action:

```python
Application.view("app_manager/builds_by_date", ...)
Application.view("app_manager/saved_app", ...)
# in our hypothetical example, this view works on doc_type "XFormInstance"
Application.view("app_manager/forms_by_xmlns", ...)
```

Because of the limitations mentioned above, you can instead create your views
here, where each directory is a separate design doc.  What that file structure
might look like is:

```
- couchapps/
   - app_builds_by_date
      - views
         - view
            map.js
            reduce.js
   + saved_apps
   + forms_by_xmlns
```

Where the convention `corehq/couchapps/<view name>/views/view/` produces the
following views:

```python
Application.view("app_builds_by_date/view", ...)
Application.view("saved_apps/view", ...)
XFormInstance.view("forms_by_xmlns/view", ...)
```

#### Benefits
With this new structure, you can make a change to `"app_builds_by_date"`
without needing to also reindex `"saved_apps"` and `"forms_by_xmlns"`.

In the example above, the `forms_by_xmlns` view operates on XFormInstance, but
for some reason lives in `app_manager`.  By moving it here, you can explicitly
choose in which dbs to include that view.

Writing `Application.view("app_manager/forms_by_xmlns", ...)` should seem a
little weird to you, because it makes sense for views to be associated with the
doc type they operate on, not the module (if the two disagree).
# The `export_forms/by_xmlns` Map-Reduce View

## Output format

The view uses a fairly non-standard reduce to interleave information from
applications and form submissions. Here is an overview of the output format.

### Emit Value

`exports_forms/by_xmlns` outputs information in the following format:

```js
{
    xmlns: string,
    app: {name: string, langs: [string], id: string},
    is_user_registration: bool,
    module: {name: {*: string}, id: int},
    form: {name: {*: string}, id: int},
    app_deleted: bool,
    submissions: int
}
```

When reduced, this has the effect of

1. Listing out all possible combinations seen of (domain, app, xmlns)
   in apps or submissions
2. Giving info aobut the accociated app form if applicable
3. Counting how many forms have been submitted in that category

### Emit Key

There are three basic key types. The main one is

- `[domain, app_id, xmlns]`

but there are also two others that split out the sources of this info into
just apps or just form submissions:

- `['^XFormInstance', domain, app_id, xmlns]`
- `['^Application', domain, xmlns]`



## Usages in our code

There are only 3 usages of this view in our code. I've outlined them below.

### With reduce

- [corehq/apps/app_manager/models.py](https://github.com/dimagi/commcare-hq/blob/23740fd5943a82c3f5a4afeeb91860a05d852a9e/corehq/apps/app_manager/models.py#L3288-3288)
  - `key=[domain, {}, xmlns]`
  - Get info forms in `domain` that have `xmlns` (regardless of app)
- [corehq/apps/reports/display.py](https://github.com/dimagi/commcare-hq/blob/23740fd5943a82c3f5a4afeeb91860a05d852a9e/corehq/apps/reports/display.py#L85-85)
  - `key=[domain, app_id, xmlns]`
  - Get info forms in `domain` in app with `app_id` that have `xmlns`

### Without reduce

- [corehq/apps/cleanup/views.py](https://github.com/dimagi/commcare-hq/blob/23740fd5943a82c3f5a4afeeb91860a05d852a9e/corehq/apps/cleanup/views.py#L36-36)
  - `key=['^XFormInstance', domain, app_id, xmlns]` with `include_docs`
  - Get all forms that were submitted in `domain` against `app_id` with `xmlns`
# Dimagi JavaScript Guide

Dimagi's internal JavaScript guide for use in the CommCare HQ project


## Table of contents

- [Code Organization](./code-organization.md)
- [Third Party Libraries](./libraries.md)
- [Server Integration Patterns](./integration-patterns.md) (toggles, i18n, etc.)
- [External packages](./external-packages.md) (bower)
- [Production Static Files](./static-files.md) (collectstatic, compression, map files, CDN)
- [Testing](./testing.md)
- [Linting](./linting.md)
- [Migrating](./migrating.md)
# eslint-plugin-eslint-dimagi

Dimagi-specific ESLint rules.
Intended for developers of [CommCareHQ](https://github.com/dimagi/commcare-hq).

## Installation

You'll first need to install [ESLint](http://eslint.org):

```
$ npm i eslint --save-dev
```

Next, install `eslint-plugin-eslint-dimagi`:

```
$ npm install eslint-plugin-eslint-dimagi --save-dev
```

**Note:** If you installed ESLint globally (using the `-g` flag) then you must also install `eslint-plugin-eslint-dimagi` globally.

## Usage

Add `eslint-dimagi` to the plugins section of your `.eslintrc` configuration file. You can omit the `eslint-plugin-` prefix:

```json
{
    "plugins": [
        "eslint-dimagi"
    ]
}
```


Then configure the rules you want to use under the rules section.

```json
{
    "rules": {
        "eslint-dimagi/rule-name": 2
    }
}
```

## Supported Rules

* no-unblessed-new: Disallows use of the `new` keyword except with specified object types.





CommCare HQ docker
==================

Initial setup
-------------
* Linux
   * Install [Docker](https://docs.docker.com/engine/installation/)
   * Install [Docker Compose](https://docs.docker.com/compose/install/) (Note you can also install in a virtualenv with `$ pip install docker-compose`)
* OS X
   * Preferred: install [Docker for Mac](https://docs.docker.com/docker-for-mac/install/).
   * Alternate for older Macs that do not support Docker for Mac:
     * Install [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_mac/). Go through the full tutorial, which will create a default machine.
     * To create a new VM manually, run `docker-machine create default --driver=virtualbox` (not necessary if you followed the Docker Toolbox tutorial).
     * If not using the Quick Start terminal, run `eval $(docker-machine env default)` to set up Docker's environment variables.

* If you have any HQ services currently running (couch, postgres, redis, etc.), you should stop them now. 
* Bootstrap the setup. Skip this step and go to [Configure your localsettings](#configure-your-localsettings) below if you came here from the [CommCare HQ README](https://github.com/dimagi/commcare-hq/blob/master/DEV_SETUP.md#setup-localsettings).

    ```
      $ ./scripts/docker runserver --bootstrap
    ```
    
    This will do the following:
    
    * build all the images (if not already built)
    * run all the service containers
    * migrate the DB and sync the Couch views
    * bootstrap a superuser and domain:
      * username: admin@example.com
      * password: password
      * domain: demo
    * run the Django dev server

    If all goes according to plan you should be able to log into CommCare: http://localhost:8000 using
    the login details above.
    
    You can create another user and domain with `$ ./manage.py make_superuser <email>`
    
    On Mac, run `docker-machine ip` to get the VM's IP address, which replaces `localhost` in the URL.

### Configure your localsettings

There are two different localsettings configurations, depending on whether HQ is running inside a docker container or on your local machine. If you are planning on doing local development, it is recommended to run HQ on your local machine, and use docker only for supporting services

  * Running docker services only (do this if you came here from the CommCare HQ README)
    * If you are using _Docker Toolbox_ (not _Docker for Mac_): change all service host settings (DATABASES HOST, COUCH_SERVER_ROOT, etc.) in your localsettings.py file to point to the IP address of your virtualbox docker VM.
    * Run `./scripts/docker up -d` to start docker services in the background. Sometimes this gets stuck waiting for Riak to start. If that happens break (CTRL+C) and try again.
    * Once the services are all up (`./scripts/docker ps` to check) you can return to the CommCare HQ README and [Setup your Django environment](https://github.com/dimagi/commcare-hq/blob/master/DEV_SETUP.md#set-up-your-django-environment).

  * Running HQ inside a docker container

    Do nothing; `docker/localsettings.py` will be used inside the container.


General usage
-------------

```
  $ ./scripts/docker --help
```

**The services (couch, postgres, elastic, redis, zookeeper, kafka)**
```
  $ ./scripts/docker up -d  # start docker services in background
  $ ./scripts/docker stop
  $ ./scripts/docker logs postgres
```
The following services are included. Their ports are mapped to the local host so you can connect to them
directly.

* Elasticsearch (9200 & 9300)
* PostgreSQL (5432)
* CouchDB (5984)
* Redis (6397)
* Zookeeper (2181)
* Kafka (9092)
* Riak CS (9980)

**Run the django server**

```
  $ ./scripts/docker runserver
```

Notes
-----
**copying old data**
If you don't want to start fresh, Farid wrote up some notes on copying data from an old dev environment [here](https://gist.github.com/proteusvacuum/a3884ce8b65681ebaf95).

Caveats
-------

* CloudCare is not currently part of this set up. It should probably be another docker image, different from CommCareHQ.
* Celery, rabbitmq and other components not strictly necessary for a laptop install are not part of this setup.


Travis
------
Travis also uses Docker to run the HQ test suite. To simulate the travis build you can use the `./scripts/docker`
script:

```
  $ JS_SETUP=yes ./scripts/docker test
  runs python tests

  $ TEST=javascript ./scripts/docker test
  runs the javascript tests

  $ TEST=python-sharded ./scripts/docker test
  runs the python sharded tests
  
  $ ./scripts/docker test corehq/apps/app_manager/tests/test_suite.py:SuiteTest
  runs only the corehq.apps.app_manager.tests.test_suite.SuiteTest
  
  $ ./scripts/docker bash
  drops you into a bash shell in the docker web container from where you can
  run any other commands
  
  $ ./scripts/docker hqtest teardown
  remove all test containers and volumes
  
```

ENV Vars
~~~~~~~~

* JS_SETUP=yes
  * Run `npm` and `bower` installs
* TEST=[javascript|python|python-sharded]
  * javascript: extra setup and config for JS tests. Also only run JS tests
  * python: default tests
  * python-sharded: configure django for sharded setup and only run subset of tests
* NOSE_DIVIDED_WE_RUN
  * used to only run a subset of tests
  * see .travis.yml for exact options
* REUSE_DB
  * Same as normal REUSE_DB
 
See .travis.yml for env variable options used on travis.
