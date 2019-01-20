[![Build Status](https://travis-ci.com/omniti-labs/pg_jobmon.svg?branch=master)](https://travis-ci.com/omniti-labs/pg_jobmon)
[![PGXN version](https://badge.fury.io/pg/pg_jobmon.svg)](https://badge.fury.io/pg/pg_jobmon)

pg_jobmon
=========

pg_jobmon is a PostgreSQL extension designed to add autonomous logging capabilities to transactions and functions. The logging is done in a NON-TRANSACTIONAL method, so that if your function/transaction fails for any reason, any information written to that point will be kept in the log tables rather than rolled back.

For more information on how to use pg_jobmon, please see [pg_jobmon/doc/pg_jobmon.md](doc/pg_jobmon.md)


INSTALLATION
------------

Requirements: PostgreSQL 9.2+, [dblink extension](https://www.postgresql.org/docs/current/static/dblink.html)

In the directory where you downloaded pg_jobmon run

    make
    make install

Log into PostgreSQL and run the following commands: 
(Note: You can change the schema name to be whatever you wish, but it cannot be changed after installation.)

    CREATE SCHEMA jobmon;
    CREATE EXTENSION pg_jobmon SCHEMA jobmon;

This extension uses dblink to connect back to the same database that pg_jobmon is running in (this is how the non-transactional magic is done). To allow non-superusers to use dblink, you'll need to enter role credentials into the dblink_mapping_jobmon table that pg_jobmon installs.
    
    INSERT INTO jobmon.dblink_mapping_jobmon (username, pwd) VALUES ('rolename', 'rolepassword');

Ensure you add the relevant line to the pg_hba.conf file for this role. It will be connecting back to the same postgres database locally.
    
    # TYPE  DATABASE       USER            ADDRESS                 METHOD
    local   dbname         rolename                                md5

The following permissions should be given to the above role (substitute relevant schema names as appropriate):
    
    grant usage on schema jobmon to rolename;
    grant usage on schema dblink to rolename;
    grant select, insert, update, delete on all tables in schema jobmon to rolename;
    grant execute on all functions in schema jobmon to rolename;
    grant all on all sequences in schema jobmon to rolename;

If you're running PostgreSQL on a port other than the default (5432), you can also use the dblink_mapping_jobmon table to change the port that dblink will use.

    INSERT INTO jobmon.dblink_mapping_jobmon (port) VALUES ('5999');

Be aware that the dblink_mapping_jobmon table can only have a single row, so if you're using a custom host, role or different port, you will need to enter those values within a single row. None of the columns are required, so just use the ones you need for your setup.

    INSERT INTO jobmon.dblink_mapping_jobmon (host,username, pwd, port) VALUES ('host','rolename', 'rolepassword', '5999');

UPGRADE
-------

Make sure all the upgrade scripts for the version you have installed up to the most recent version are in the $BASEDIR/share/extension folder. 

    ALTER EXTENSION pg_jobmon UPDATE TO '<latest version>';

For detailed change logs of each version, please see the top of each update script.

LICENSE AND COPYRIGHT
---------------------

pg_jobmon is released under the [PostgreSQL License](https://opensource.org/licenses/PostgreSQL), a liberal Open Source license, similar to the BSD or MIT licenses.

Copyright (c) 2015-2018 [OmniTI, Inc.](https://omniti.com)

Permission to use, copy, modify, and distribute this software and its documentation for any purpose, without fee, and without a written agreement is hereby granted, provided that the above copyright notice and this paragraph and the following two paragraphs appear in all copies.

IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND THE AUTHOR HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
