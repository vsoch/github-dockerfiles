This folder contains some sample formatters that may be helpful.

Feel free to change them, extend them, or use them as the basis for your own custom formatter(s).

More information about creating your own custom formatters can be found on the wiki:
https://github.com/CocoaLumberjack/CocoaLumberjack/wiki/CustomFormatters

## SQLCipher

SQLCipher extends the [SQLite](https://www.sqlite.org) database library to add security enhancements that make it more suitable for encrypted local data storage such as on-the-fly encryption, tamper evidence, and key derivation. Based on SQLite, SQLCipher closely tracks SQLite and periodically integrates stable SQLite release features.

SQLCipher is maintained by Zetetic, LLC, the official site can be found [here](https://www.zetetic.net/sqlcipher/).

## Features

- Fast performance with as little as 5-15% overhead for encryption on many operations
- 100% of data in the database file is encrypted
- Good security practices (CBC mode, HMAC, key derivation)
- Zero-configuration and application level cryptography
- Algorithms provided by the peer reviewed OpenSSL crypto library.
- Configurable crypto providers

## Contributions

We welcome contributions, to contribute to SQLCipher, a [contributor agreement](https://www.zetetic.net/contributions/) needs to be submitted.  All submissions should be based on the `prerelease` branch.

## Compiling

Building SQLCipher is almost the same as compiling a regular version of 
SQLite with two small exceptions: 

 1. You *must* define `SQLITE_HAS_CODEC` and `SQLITE_TEMP_STORE=2` when building sqlcipher. 
 2. If compiling against the default OpenSSL crypto provider, you will need to link libcrypto
 
Example Static linking (replace /opt/local/lib with the path to libcrypto.a). Note in this 
example, `--enable-tempstore=yes` is setting `SQLITE_TEMP_STORE=2` for the build.

	$ ./configure --enable-tempstore=yes CFLAGS="-DSQLITE_HAS_CODEC" \
		LDFLAGS="/opt/local/lib/libcrypto.a"
	$ make

Example Dynamic linking

	$ ./configure --enable-tempstore=yes CFLAGS="-DSQLITE_HAS_CODEC" \
		LDFLAGS="-lcrypto"
	$ make

## Encrypting a database

To specify an encryption passphrase for the database via the SQL interface you 
use a pragma. The passphrase you enter is passed through PBKDF2 key derivation to
obtain the encryption key for the database 

	PRAGMA key = 'passphrase';

Alternately, you can specify an exact byte sequence using a blob literal. If you
use this method it is your responsibility to ensure that the data you provide a
64 character hex string, which will be converted directly to 32 bytes (256 bits) of 
key data without key derivation.

	PRAGMA key = "x'2DD29CA851E7B56E4697B0E1F08507293D761A05CE4D1B628663F411A8086D99'";

To encrypt a database programatically you can use the `sqlite3_key` function. 
The data provided in `pKey` is converted to an encryption key according to the 
same rules as `PRAGMA key`. 

	int sqlite3_key(sqlite3 *db, const void *pKey, int nKey);

`PRAGMA key` or `sqlite3_key` should be called as the first operation when a database is open.

## Changing a database key

To change the encryption passphrase for an existing database you may use the rekey pragma
after you've supplied the correct database password;

	PRAGMA key = 'passphrase'; -- start with the existing database passphrase
	PRAGMA rekey = 'new-passphrase'; -- rekey will reencrypt with the new passphrase

The hex rekey pragma may be used to rekey to a specific binary value

	PRAGMA rekey = "x'2DD29CA851E7B56E4697B0E1F08507293D761A05CE4D1B628663F411A8086D99'";

This can be accomplished programtically by using sqlite3_rekey;
  
	sqlite3_rekey(sqlite3 *db, const void *pKey, int nKey)

## Support

The primary avenue for support and discussions is the SQLCipher discuss site:

https://discuss.zetetic.net/c/sqlcipher

Issues or support questions on using SQLCipher should be entered into the 
GitHub Issue tracker:

https://github.com/sqlcipher/sqlcipher/issues

Please DO NOT post issues, support questions, or other problems to blog 
posts about SQLCipher as we do not monitor them frequently.

If you are using SQLCipher in your own software please let us know at 
support@zetetic.net!

## License

Copyright (c) 2016, ZETETIC LLC
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the ZETETIC LLC nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY ZETETIC LLC ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL ZETETIC LLC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
Version loadable extensions to SQLite are found in subfolders
of this folder.

This directory contains an SQLite extension that implements a virtual 
table type that allows users to create, query and manipulate r-tree[1] 
data structures inside of SQLite databases. Users create, populate 
and query r-tree structures using ordinary SQL statements.

    1.  SQL Interface

        1.1  Table Creation
        1.2  Data Manipulation
        1.3  Data Querying
        1.4  Introspection and Analysis

    2.  Compilation and Deployment

    3.  References


1. SQL INTERFACE

  1.1 Table Creation.

    All r-tree virtual tables have an odd number of columns between
    3 and 11. Unlike regular SQLite tables, r-tree tables are strongly 
    typed. 

    The leftmost column is always the pimary key and contains 64-bit 
    integer values. Each subsequent column contains a 32-bit real
    value. For each pair of real values, the first (leftmost) must be 
    less than or equal to the second. R-tree tables may be 
    constructed using the following syntax:

      CREATE VIRTUAL TABLE <name> USING rtree(<column-names>)

    For example:

      CREATE VIRTUAL TABLE boxes USING rtree(boxno, xmin, xmax, ymin, ymax);
      INSERT INTO boxes VALUES(1, 1.0, 3.0, 2.0, 4.0);

    Constructing a virtual r-tree table <name> creates the following three
    real tables in the database to store the data structure:

      <name>_node
      <name>_rowid
      <name>_parent

    Dropping or modifying the contents of these tables directly will
    corrupt the r-tree structure. To delete an r-tree from a database,
    use a regular DROP TABLE statement:

      DROP TABLE <name>;

    Dropping the main r-tree table automatically drops the automatically
    created tables. 

  1.2 Data Manipulation (INSERT, UPDATE, DELETE).

    The usual INSERT, UPDATE or DELETE syntax is used to manipulate data
    stored in an r-tree table. Please note the following:

      * Inserting a NULL value into the primary key column has the
        same effect as inserting a NULL into an INTEGER PRIMARY KEY
        column of a regular table. The system automatically assigns
        an unused integer key value to the new record. Usually, this
        is one greater than the largest primary key value currently
        present in the table.

      * Attempting to insert a duplicate primary key value fails with
        an SQLITE_CONSTRAINT error.

      * Attempting to insert or modify a record such that the value
        stored in the (N*2)th column is greater than that stored in
        the (N*2+1)th column fails with an SQLITE_CONSTRAINT error.

      * When a record is inserted, values are always converted to 
        the required type (64-bit integer or 32-bit real) as if they
        were part of an SQL CAST expression. Non-numeric strings are
        converted to zero.

  1.3 Queries.

    R-tree tables may be queried using all of the same SQL syntax supported
    by regular tables. However, some query patterns are more efficient
    than others.

    R-trees support fast lookup by primary key value (O(logN), like 
    regular tables).

    Any combination of equality and range (<, <=, >, >=) constraints
    on spatial data columns may be used to optimize other queries. This
    is the key advantage to using r-tree tables instead of creating 
    indices on regular tables.

  1.4 Introspection and Analysis.

    TODO: Describe rtreenode() and rtreedepth() functions.


2. COMPILATION AND USAGE

  The easiest way to compile and use the RTREE extension is to build
  and use it as a dynamically loadable SQLite extension. To do this
  using gcc on *nix:

    gcc -shared rtree.c -o libSqliteRtree.so

  You may need to add "-I" flags so that gcc can find sqlite3ext.h
  and sqlite3.h. The resulting shared lib, libSqliteRtree.so, may be
  loaded into sqlite in the same way as any other dynamicly loadable
  extension.


3. REFERENCES

  [1]  Atonin Guttman, "R-trees - A Dynamic Index Structure For Spatial 
       Searching", University of California Berkeley, 1984.

  [2]  Norbert Beckmann, Hans-Peter Kriegel, Ralf Schneider, Bernhard Seeger,
       "The R*-tree: An Efficient and Robust Access Method for Points and
       Rectangles", Universitaet Bremen, 1990.
NOTE (2012-11-29):

The functionality implemented by this extension has been superseded
by WAL-mode.  This module is no longer supported or maintained.  The
code is retained for historical reference only.

------------------------------------------------------------------------------

Normally, when SQLite writes to a database file, it waits until the write
operation is finished before returning control to the calling application.
Since writing to the file-system is usually very slow compared with CPU
bound operations, this can be a performance bottleneck. This directory
contains an extension that causes SQLite to perform all write requests
using a separate thread running in the background. Although this does not
reduce the overall system resources (CPU, disk bandwidth etc.) at all, it
allows SQLite to return control to the caller quickly even when writing to
the database, eliminating the bottleneck.

  1. Functionality

    1.1 How it Works
    1.2 Limitations
    1.3 Locking and Concurrency

  2. Compilation and Usage

  3. Porting



1. FUNCTIONALITY

  With asynchronous I/O, write requests are handled by a separate thread
  running in the background.  This means that the thread that initiates
  a database write does not have to wait for (sometimes slow) disk I/O
  to occur.  The write seems to happen very quickly, though in reality
  it is happening at its usual slow pace in the background.

  Asynchronous I/O appears to give better responsiveness, but at a price.
  You lose the Durable property.  With the default I/O backend of SQLite,
  once a write completes, you know that the information you wrote is
  safely on disk.  With the asynchronous I/O, this is not the case.  If
  your program crashes or if a power loss occurs after the database
  write but before the asynchronous write thread has completed, then the
  database change might never make it to disk and the next user of the
  database might not see your change.

  You lose Durability with asynchronous I/O, but you still retain the
  other parts of ACID:  Atomic,  Consistent, and Isolated.  Many
  appliations get along fine without the Durablity.

  1.1 How it Works

    Asynchronous I/O works by creating a special SQLite "vfs" structure
    and registering it with sqlite3_vfs_register(). When files opened via 
    this vfs are written to (using the vfs xWrite() method), the data is not 
    written directly to disk, but is placed in the "write-queue" to be
    handled by the background thread.

    When files opened with the asynchronous vfs are read from 
    (using the vfs xRead() method), the data is read from the file on 
    disk and the write-queue, so that from the point of view of
    the vfs reader the xWrite() appears to have already completed.

    The special vfs is registered (and unregistered) by calls to the 
    API functions sqlite3async_initialize() and sqlite3async_shutdown().
    See section "Compilation and Usage" below for details.

  1.2 Limitations

    In order to gain experience with the main ideas surrounding asynchronous 
    IO, this implementation is deliberately kept simple. Additional 
    capabilities may be added in the future.

    For example, as currently implemented, if writes are happening at a 
    steady stream that exceeds the I/O capability of the background writer
    thread, the queue of pending write operations will grow without bound.
    If this goes on for long enough, the host system could run out of memory. 
    A more sophisticated module could to keep track of the quantity of 
    pending writes and stop accepting new write requests when the queue of 
    pending writes grows too large.

  1.3 Locking and Concurrency

    Multiple connections from within a single process that use this
    implementation of asynchronous IO may access a single database
    file concurrently. From the point of view of the user, if all
    connections are from within a single process, there is no difference
    between the concurrency offered by "normal" SQLite and SQLite
    using the asynchronous backend.

    If file-locking is enabled (it is enabled by default), then connections
    from multiple processes may also read and write the database file.
    However concurrency is reduced as follows:

      * When a connection using asynchronous IO begins a database
        transaction, the database is locked immediately. However the
        lock is not released until after all relevant operations
        in the write-queue have been flushed to disk. This means
        (for example) that the database may remain locked for some 
        time after a "COMMIT" or "ROLLBACK" is issued.

      * If an application using asynchronous IO executes transactions
        in quick succession, other database users may be effectively
        locked out of the database. This is because when a BEGIN
        is executed, a database lock is established immediately. But
        when the corresponding COMMIT or ROLLBACK occurs, the lock
        is not released until the relevant part of the write-queue 
        has been flushed through. As a result, if a COMMIT is followed
        by a BEGIN before the write-queue is flushed through, the database 
        is never unlocked,preventing other processes from accessing 
        the database.

    File-locking may be disabled at runtime using the sqlite3async_control()
    API (see below). This may improve performance when an NFS or other 
    network file-system, as the synchronous round-trips to the server be 
    required to establish file locks are avoided. However, if multiple 
    connections attempt to access the same database file when file-locking
    is disabled, application crashes and database corruption is a likely
    outcome.


2. COMPILATION AND USAGE

  The asynchronous IO extension consists of a single file of C code
  (sqlite3async.c), and a header file (sqlite3async.h) that defines the 
  C API used by applications to activate and control the modules 
  functionality.

  To use the asynchronous IO extension, compile sqlite3async.c as
  part of the application that uses SQLite. Then use the API defined
  in sqlite3async.h to initialize and configure the module.

  The asynchronous IO VFS API is described in detail in comments in 
  sqlite3async.h. Using the API usually consists of the following steps:

    1. Register the asynchronous IO VFS with SQLite by calling the
       sqlite3async_initialize() function.

    2. Create a background thread to perform write operations and call
       sqlite3async_run().

    3. Use the normal SQLite API to read and write to databases via 
       the asynchronous IO VFS.

  Refer to sqlite3async.h for details.


3. PORTING

  Currently the asynchronous IO extension is compatible with win32 systems
  and systems that support the pthreads interface, including Mac OSX, Linux, 
  and other varieties of Unix. 

  To port the asynchronous IO extension to another platform, the user must
  implement mutex and condition variable primitives for the new platform.
  Currently there is no externally available interface to allow this, but
  modifying the code within sqlite3async.c to include the new platforms
  concurrency primitives is relatively easy. Search within sqlite3async.c
  for the comment string "PORTING FUNCTIONS" for details. Then implement
  new versions of each of the following:

    static void async_mutex_enter(int eMutex);
    static void async_mutex_leave(int eMutex);
    static void async_cond_wait(int eCond, int eMutex);
    static void async_cond_signal(int eCond);
    static void async_sched_yield(void);

  The functionality required of each of the above functions is described
  in comments in sqlite3async.c.
This folder contains source code to the second full-text search
extension for SQLite.  While the API is the same, this version uses a
substantially different storage schema from fts1, so tables will need
to be rebuilt.

1. FTS2 Tokenizers

  When creating a new full-text table, FTS2 allows the user to select
  the text tokenizer implementation to be used when indexing text
  by specifying a "tokenizer" clause as part of the CREATE VIRTUAL TABLE
  statement:

    CREATE VIRTUAL TABLE <table-name> USING fts2(
      <columns ...> [, tokenizer <tokenizer-name> [<tokenizer-args>]]
    );

  The built-in tokenizers (valid values to pass as <tokenizer name>) are
  "simple" and "porter".

  <tokenizer-args> should consist of zero or more white-space separated
  arguments to pass to the selected tokenizer implementation. The 
  interpretation of the arguments, if any, depends on the individual 
  tokenizer.

2. Custom Tokenizers

  FTS2 allows users to provide custom tokenizer implementations. The 
  interface used to create a new tokenizer is defined and described in 
  the fts2_tokenizer.h source file.

  Registering a new FTS2 tokenizer is similar to registering a new 
  virtual table module with SQLite. The user passes a pointer to a
  structure containing pointers to various callback functions that
  make up the implementation of the new tokenizer type. For tokenizers,
  the structure (defined in fts2_tokenizer.h) is called
  "sqlite3_tokenizer_module".

  FTS2 does not expose a C-function that users call to register new
  tokenizer types with a database handle. Instead, the pointer must
  be encoded as an SQL blob value and passed to FTS2 through the SQL
  engine by evaluating a special scalar function, "fts2_tokenizer()".
  The fts2_tokenizer() function may be called with one or two arguments,
  as follows:

    SELECT fts2_tokenizer(<tokenizer-name>);
    SELECT fts2_tokenizer(<tokenizer-name>, <sqlite3_tokenizer_module ptr>);
  
  Where <tokenizer-name> is a string identifying the tokenizer and
  <sqlite3_tokenizer_module ptr> is a pointer to an sqlite3_tokenizer_module
  structure encoded as an SQL blob. If the second argument is present,
  it is registered as tokenizer <tokenizer-name> and a copy of it
  returned. If only one argument is passed, a pointer to the tokenizer
  implementation currently registered as <tokenizer-name> is returned,
  encoded as a blob. Or, if no such tokenizer exists, an SQL exception
  (error) is raised.

  SECURITY: If the fts2 extension is used in an environment where potentially
    malicious users may execute arbitrary SQL (i.e. gears), they should be
    prevented from invoking the fts2_tokenizer() function, possibly using the
    authorisation callback.

  See "Sample code" below for an example of calling the fts2_tokenizer()
  function from C code.

3. ICU Library Tokenizers

  If this extension is compiled with the SQLITE_ENABLE_ICU pre-processor 
  symbol defined, then there exists a built-in tokenizer named "icu" 
  implemented using the ICU library. The first argument passed to the
  xCreate() method (see fts2_tokenizer.h) of this tokenizer may be
  an ICU locale identifier. For example "tr_TR" for Turkish as used
  in Turkey, or "en_AU" for English as used in Australia. For example:

    "CREATE VIRTUAL TABLE thai_text USING fts2(text, tokenizer icu th_TH)"

  The ICU tokenizer implementation is very simple. It splits the input
  text according to the ICU rules for finding word boundaries and discards
  any tokens that consist entirely of white-space. This may be suitable
  for some applications in some locales, but not all. If more complex
  processing is required, for example to implement stemming or 
  discard punctuation, this can be done by creating a tokenizer 
  implementation that uses the ICU tokenizer as part of its implementation.

  When using the ICU tokenizer this way, it is safe to overwrite the
  contents of the strings returned by the xNext() method (see
  fts2_tokenizer.h).

4. Sample code.

  The following two code samples illustrate the way C code should invoke
  the fts2_tokenizer() scalar function:

      int registerTokenizer(
        sqlite3 *db, 
        char *zName, 
        const sqlite3_tokenizer_module *p
      ){
        int rc;
        sqlite3_stmt *pStmt;
        const char zSql[] = "SELECT fts2_tokenizer(?, ?)";
      
        rc = sqlite3_prepare_v2(db, zSql, -1, &pStmt, 0);
        if( rc!=SQLITE_OK ){
          return rc;
        }
      
        sqlite3_bind_text(pStmt, 1, zName, -1, SQLITE_STATIC);
        sqlite3_bind_blob(pStmt, 2, &p, sizeof(p), SQLITE_STATIC);
        sqlite3_step(pStmt);
      
        return sqlite3_finalize(pStmt);
      }
      
      int queryTokenizer(
        sqlite3 *db, 
        char *zName,  
        const sqlite3_tokenizer_module **pp
      ){
        int rc;
        sqlite3_stmt *pStmt;
        const char zSql[] = "SELECT fts2_tokenizer(?)";
      
        *pp = 0;
        rc = sqlite3_prepare_v2(db, zSql, -1, &pStmt, 0);
        if( rc!=SQLITE_OK ){
          return rc;
        }
      
        sqlite3_bind_text(pStmt, 1, zName, -1, SQLITE_STATIC);
        if( SQLITE_ROW==sqlite3_step(pStmt) ){
          if( sqlite3_column_type(pStmt, 0)==SQLITE_BLOB ){
            memcpy(pp, sqlite3_column_blob(pStmt, 0), sizeof(*pp));
          }
        }
      
        return sqlite3_finalize(pStmt);
      }

This directory contains source code for the SQLite "ICU" extension, an
integration of the "International Components for Unicode" library with
SQLite. Documentation follows.

    1. Features
    
        1.1  SQL Scalars upper() and lower()
        1.2  Unicode Aware LIKE Operator
        1.3  ICU Collation Sequences
        1.4  SQL REGEXP Operator
    
    2. Compilation and Usage
    
    3. Bugs, Problems and Security Issues
    
        3.1  The "case_sensitive_like" Pragma
        3.2  The SQLITE_MAX_LIKE_PATTERN_LENGTH Macro
        3.3  Collation Sequence Security Issue


1. FEATURES

  1.1  SQL Scalars upper() and lower()

    SQLite's built-in implementations of these two functions only 
    provide case mapping for the 26 letters used in the English
    language. The ICU based functions provided by this extension
    provide case mapping, where defined, for the full range of 
    unicode characters.

    ICU provides two types of case mapping, "general" case mapping and
    "language specific". Refer to ICU documentation for the differences
    between the two. Specifically:

       http://www.icu-project.org/userguide/caseMappings.html
       http://www.icu-project.org/userguide/posix.html#case_mappings

    To utilise "general" case mapping, the upper() or lower() scalar 
    functions are invoked with one argument:

        upper('ABC') -> 'abc'
        lower('abc') -> 'ABC'

    To access ICU "language specific" case mapping, upper() or lower()
    should be invoked with two arguments. The second argument is the name
    of the locale to use. Passing an empty string ("") or SQL NULL value
    as the second argument is the same as invoking the 1 argument version
    of upper() or lower():

        lower('I', 'en_us') -> 'i'
        lower('I', 'tr_tr') -> 'ı' (small dotless i)

  1.2  Unicode Aware LIKE Operator

    Similarly to the upper() and lower() functions, the built-in SQLite LIKE
    operator understands case equivalence for the 26 letters of the English
    language alphabet. The implementation of LIKE included in this
    extension uses the ICU function u_foldCase() to provide case
    independent comparisons for the full range of unicode characters.  

    The U_FOLD_CASE_DEFAULT flag is passed to u_foldCase(), meaning the
    dotless 'I' character used in the Turkish language is considered
    to be in the same equivalence class as the dotted 'I' character
    used by many languages (including English).

  1.3  ICU Collation Sequences

    A special SQL scalar function, icu_load_collation() is provided that 
    may be used to register ICU collation sequences with SQLite. It
    is always called with exactly two arguments, the ICU locale 
    identifying the collation sequence to ICU, and the name of the
    SQLite collation sequence to create. For example, to create an
    SQLite collation sequence named "turkish" using Turkish language
    sorting rules, the SQL statement:

        SELECT icu_load_collation('tr_TR', 'turkish');

    Or, for Australian English:

        SELECT icu_load_collation('en_AU', 'australian');

    The identifiers "turkish" and "australian" may then be used
    as collation sequence identifiers in SQL statements:

        CREATE TABLE aust_turkish_penpals(
          australian_penpal_name TEXT COLLATE australian,
          turkish_penpal_name    TEXT COLLATE turkish
        );
  
  1.4 SQL REGEXP Operator

    This extension provides an implementation of the SQL binary
    comparision operator "REGEXP", based on the regular expression functions
    provided by the ICU library. The syntax of the operator is as described
    in SQLite documentation:

        <string> REGEXP <re-pattern>

    This extension uses the ICU defaults for regular expression matching
    behavior. Specifically, this means that:

        * Matching is case-sensitive,
        * Regular expression comments are not allowed within patterns, and
        * The '^' and '$' characters match the beginning and end of the
          <string> argument, not the beginning and end of lines within
          the <string> argument.

    Even more specifically, the value passed to the "flags" parameter
    of ICU C function uregex_open() is 0.


2  COMPILATION AND USAGE

  The easiest way to compile and use the ICU extension is to build
  and use it as a dynamically loadable SQLite extension. To do this
  using gcc on *nix:

    gcc -shared icu.c `icu-config --ldflags` -o libSqliteIcu.so

  You may need to add "-I" flags so that gcc can find sqlite3ext.h
  and sqlite3.h. The resulting shared lib, libSqliteIcu.so, may be
  loaded into sqlite in the same way as any other dynamically loadable
  extension.


3 BUGS, PROBLEMS AND SECURITY ISSUES

  3.1 The "case_sensitive_like" Pragma

    This extension does not work well with the "case_sensitive_like"
    pragma. If this pragma is used before the ICU extension is loaded,
    then the pragma has no effect. If the pragma is used after the ICU
    extension is loaded, then SQLite ignores the ICU implementation and
    always uses the built-in LIKE operator.

    The ICU extension LIKE operator is always case insensitive.

  3.2 The SQLITE_MAX_LIKE_PATTERN_LENGTH Macro

    Passing very long patterns to the built-in SQLite LIKE operator can
    cause excessive CPU usage. To curb this problem, SQLite defines the
    SQLITE_MAX_LIKE_PATTERN_LENGTH macro as the maximum length of a
    pattern in bytes (irrespective of encoding). The default value is
    defined in internal header file "limits.h".
    
    The ICU extension LIKE implementation suffers from the same 
    problem and uses the same solution. However, since the ICU extension
    code does not include the SQLite file "limits.h", modifying
    the default value therein does not affect the ICU extension.
    The default value of SQLITE_MAX_LIKE_PATTERN_LENGTH used by
    the ICU extension LIKE operator is 50000, defined in source 
    file "icu.c".

  3.3 Collation Sequence Security Issue

    Internally, SQLite assumes that indices stored in database files
    are sorted according to the collation sequence indicated by the
    SQL schema. Changing the definition of a collation sequence after
    an index has been built is therefore equivalent to database
    corruption. The SQLite library is not very well tested under
    these conditions, and may contain potential buffer overruns
    or other programming errors that could be exploited by a malicious
    programmer.

    If the ICU extension is used in an environment where potentially
    malicious users may execute arbitrary SQL (i.e. gears), they
    should be prevented from invoking the icu_load_collation() function,
    possibly using the authorisation callback.
This folder contains source code to the second full-text search
extension for SQLite.  While the API is the same, this version uses a
substantially different storage schema from fts1, so tables will need
to be rebuilt.

FTS4 CONTENT OPTION

  Normally, in order to create a full-text index on a dataset, the FTS4 
  module stores a copy of all indexed documents in a specially created 
  database table.

  As of SQLite version 3.7.9, FTS4 supports a new option - "content" -
  designed to extend FTS4 to support the creation of full-text indexes where:

    * The indexed documents are not stored within the SQLite database 
      at all (a "contentless" FTS4 table), or

    * The indexed documents are stored in a database table created and
      managed by the user (an "external content" FTS4 table).

  Because the indexed documents themselves are usually much larger than 
  the full-text index, the content option can sometimes be used to achieve 
  significant space savings.

CONTENTLESS FTS4 TABLES

  In order to create an FTS4 table that does not store a copy of the indexed
  documents at all, the content option should be set to an empty string.
  For example, the following SQL creates such an FTS4 table with three
  columns - "a", "b", and "c":

    CREATE VIRTUAL TABLE t1 USING fts4(content="", a, b, c);

  Data can be inserted into such an FTS4 table using an INSERT statements.
  However, unlike ordinary FTS4 tables, the user must supply an explicit
  integer docid value. For example:

    -- This statement is Ok:
    INSERT INTO t1(docid, a, b, c) VALUES(1, 'a b c', 'd e f', 'g h i');

    -- This statement causes an error, as no docid value has been provided:
    INSERT INTO t1(a, b, c) VALUES('j k l', 'm n o', 'p q r');

  It is not possible to UPDATE or DELETE a row stored in a contentless FTS4
  table. Attempting to do so is an error.

  Contentless FTS4 tables also support SELECT statements. However, it is
  an error to attempt to retrieve the value of any table column other than
  the docid column. The auxiliary function matchinfo() may be used, but
  snippet() and offsets() may not. For example:

    -- The following statements are Ok:
    SELECT docid FROM t1 WHERE t1 MATCH 'xxx';
    SELECT docid FROM t1 WHERE a MATCH 'xxx';
    SELECT matchinfo(t1) FROM t1 WHERE t1 MATCH 'xxx';

    -- The following statements all cause errors, as the value of columns
    -- other than docid are required to evaluate them.
    SELECT * FROM t1;
    SELECT a, b FROM t1 WHERE t1 MATCH 'xxx';
    SELECT docid FROM t1 WHERE a LIKE 'xxx%';
    SELECT snippet(t1) FROM t1 WHERE t1 MATCH 'xxx';

  Errors related to attempting to retrieve column values other than docid
  are runtime errors that occur within sqlite3_step(). In some cases, for
  example if the MATCH expression in a SELECT query matches zero rows, there
  may be no error at all even if a statement does refer to column values 
  other than docid.

EXTERNAL CONTENT FTS4 TABLES

  An "external content" FTS4 table is similar to a contentless table, except
  that if evaluation of a query requires the value of a column other than 
  docid, FTS4 attempts to retrieve that value from a table (or view, or 
  virtual table) nominated by the user (hereafter referred to as the "content
  table"). The FTS4 module never writes to the content table, and writing
  to the content table does not affect the full-text index. It is the
  responsibility of the user to ensure that the content table and the 
  full-text index are consistent.

  An external content FTS4 table is created by setting the content option
  to the name of a table (or view, or virtual table) that may be queried by
  FTS4 to retrieve column values when required. If the nominated table does
  not exist, then an external content table behaves in the same way as
  a contentless table. For example:

    CREATE TABLE t2(id INTEGER PRIMARY KEY, a, b, c);
    CREATE VIRTUAL TABLE t3 USING fts4(content="t2", a, c);

  Assuming the nominated table does exist, then its columns must be the same 
  as or a superset of those defined for the FTS table.

  When a users query on the FTS table requires a column value other than
  docid, FTS attempts to read this value from the corresponding column of
  the row in the content table with a rowid value equal to the current FTS
  docid. Or, if such a row cannot be found in the content table, a NULL
  value is used instead. For example:

    CREATE TABLE t2(id INTEGER PRIMARY KEY, a, b, c, d);
    CREATE VIRTUAL TABLE t3 USING fts4(content="t2", b, c);
  
    INSERT INTO t2 VALUES(2, 'a b', 'c d', 'e f');
    INSERT INTO t2 VALUES(3, 'g h', 'i j', 'k l');
    INSERT INTO t3(docid, b, c) SELECT id, b, c FROM t2;

    -- The following query returns a single row with two columns containing
    -- the text values "i j" and "k l".
    --
    -- The query uses the full-text index to discover that the MATCH 
    -- term matches the row with docid=3. It then retrieves the values
    -- of columns b and c from the row with rowid=3 in the content table
    -- to return.
    --
    SELECT * FROM t3 WHERE t3 MATCH 'k';

    -- Following the UPDATE, the query still returns a single row, this
    -- time containing the text values "xxx" and "yyy". This is because the
    -- full-text index still indicates that the row with docid=3 matches
    -- the FTS4 query 'k', even though the documents stored in the content
    -- table have been modified.
    --
    UPDATE t2 SET b = 'xxx', c = 'yyy' WHERE rowid = 3;
    SELECT * FROM t3 WHERE t3 MATCH 'k';

    -- Following the DELETE below, the query returns one row containing two
    -- NULL values. NULL values are returned because FTS is unable to find
    -- a row with rowid=3 within the content table.
    --
    DELETE FROM t2;
    SELECT * FROM t3 WHERE t3 MATCH 'k';

  When a row is deleted from an external content FTS4 table, FTS4 needs to
  retrieve the column values of the row being deleted from the content table.
  This is so that FTS4 can update the full-text index entries for each token
  that occurs within the deleted row to indicate that that row has been 
  deleted. If the content table row cannot be found, or if it contains values
  inconsistent with the contents of the FTS index, the results can be difficult
  to predict. The FTS index may be left containing entries corresponding to the
  deleted row, which can lead to seemingly nonsensical results being returned
  by subsequent SELECT queries. The same applies when a row is updated, as
  internally an UPDATE is the same as a DELETE followed by an INSERT.
  
  Instead of writing separately to the full-text index and the content table,
  some users may wish to use database triggers to keep the full-text index
  up to date with respect to the set of documents stored in the content table.
  For example, using the tables from earlier examples:

    CREATE TRIGGER t2_bu BEFORE UPDATE ON t2 BEGIN
      DELETE FROM t3 WHERE docid=old.rowid;
    END;
    CREATE TRIGGER t2_bd BEFORE DELETE ON t2 BEGIN
      DELETE FROM t3 WHERE docid=old.rowid;
    END;

    CREATE TRIGGER t2_bu AFTER UPDATE ON t2 BEGIN
      INSERT INTO t3(docid, b, c) VALUES(new.rowid, new.b, new.c);
    END;
    CREATE TRIGGER t2_bd AFTER INSERT ON t2 BEGIN
      INSERT INTO t3(docid, b, c) VALUES(new.rowid, new.b, new.c);
    END;

  The DELETE trigger must be fired before the actual delete takes place
  on the content table. This is so that FTS4 can still retrieve the original
  values in order to update the full-text index. And the INSERT trigger must
  be fired after the new row is inserted, so as to handle the case where the
  rowid is assigned automatically within the system. The UPDATE trigger must
  be split into two parts, one fired before and one after the update of the
  content table, for the same reasons.

  FTS4 features a special command similar to the 'optimize' command that
  deletes the entire full-text index and rebuilds it based on the current
  set of documents in the content table. Assuming again that "t3" is the
  name of the external content FTS4 table, the command is:

    INSERT INTO t3(t3) VALUES('rebuild');

  This command may also be used with ordinary FTS4 tables, although it may
  only be useful if the full-text index has somehow become corrupt. It is an
  error to attempt to rebuild the full-text index maintained by a contentless
  FTS4 table.



1. OVERVIEW

  This README file describes the syntax of the arguments that may be passed to
  the FTS3 MATCH operator used for full-text queries. For example, if table 
  "t1" is an Fts3 virtual table, the following SQL query:

    SELECT * FROM t1 WHERE <col> MATCH <full-text query>

  may be used to retrieve all rows that match a specified for full-text query. 
  The text "<col>" should be replaced by either the name of the fts3 table 
  (in this case "t1"), or by the name of one of the columns of the fts3 
  table. <full-text-query> should be replaced by an SQL expression that 
  computes to a string containing an Fts3 query.

  If the left-hand-side of the MATCH operator is set to the name of the
  fts3 table, then by default the query may be matched against any column
  of the table. If it is set to a column name, then by default the query
  may only match the specified column. In both cases this may be overriden
  as part of the query text (see sections 2 and 3 below).

  As of SQLite version 3.6.8, Fts3 supports two slightly different query 
  formats; the standard syntax, which is used by default, and the enhanced
  query syntax which can be selected by compiling with the pre-processor
  symbol SQLITE_ENABLE_FTS3_PARENTHESIS defined.

    -DSQLITE_ENABLE_FTS3_PARENTHESIS

2. STANDARD QUERY SYNTAX

  When using the standard Fts3 query syntax, a query usually consists of a 
  list of terms (words) separated by white-space characters. To match a
  query, a row (or column) of an Fts3 table must contain each of the specified
  terms. For example, the following query:

    <col> MATCH 'hello world'

  matches rows (or columns, if <col> is the name of a column name) that 
  contain at least one instance of the token "hello", and at least one 
  instance of the token "world". Tokens may be grouped into phrases using
  quotation marks. In this case, a matching row or column must contain each
  of the tokens in the phrase in the order specified, with no intervening
  tokens. For example, the query:

    <col> MATCH '"hello world" joe"

  matches the first of the following two documents, but not the second or
  third:

    "'Hello world', said Joe."
    "One should always greet the world with a cheery hello, thought Joe."
    "How many hello world programs could their be?"

  As well as grouping tokens together by phrase, the binary NEAR operator 
  may be used to search for rows that contain two or more specified tokens 
  or phrases within a specified proximity of each other. The NEAR operator
  must always be specified in upper case. The word "near" in lower or mixed
  case is treated as an ordinary token. For example, the following query:

    <col> MATCH 'engineering NEAR consultancy'

  matches rows that contain both the "engineering" and "consultancy" tokens
  in the same column with not more than 10 other words between them. It does
  not matter which of the two terms occurs first in the document, only that
  they be seperated by only 10 tokens or less. The user may also specify
  a different required proximity by adding "/N" immediately after the NEAR
  operator, where N is an integer. For example:

    <col> MATCH 'engineering NEAR/5 consultancy'

  searches for a row containing an instance of each specified token seperated
  by not more than 5 other tokens. More than one NEAR operator can be used
  in as sequence. For example this query:

    <col> MATCH 'reliable NEAR/2 engineering NEAR/5 consultancy'

  searches for a row that contains an instance of the token "reliable" 
  seperated by not more than two tokens from an instance of "engineering",
  which is in turn separated by not more than 5 other tokens from an
  instance of the term "consultancy". Phrases enclosed in quotes may
  also be used as arguments to the NEAR operator.

  Similar to the NEAR operator, one or more tokens or phrases may be 
  separated by OR operators. In this case, only one of the specified tokens
  or phrases must appear in the document. For example, the query:

    <col> MATCH 'hello OR world'

  matches rows that contain either the term "hello", or the term "world",
  or both. Note that unlike in many programming languages, the OR operator
  has a higher precedence than the AND operators implied between white-space
  separated tokens. The following query matches documents that contain the
  term 'sqlite' and at least one of the terms 'fantastic' or 'impressive',
  not those that contain both 'sqlite' and 'fantastic' or 'impressive':

    <col> MATCH 'sqlite fantastic OR impressive'

  Any token that is part of an Fts3 query expression, whether or not it is
  part of a phrase enclosed in quotes, may have a '*' character appended to
  it. In this case, the token matches all terms that begin with the characters
  of the token, not just those that exactly match it. For example, the 
  following query:

    <col> MATCH 'sql*'

  matches all rows that contain the term "SQLite", as well as those that
  contain "SQL".

  A token that is not part of a quoted phrase may be preceded by a '-'
  character, which indicates that matching rows must not contain the 
  specified term. For example, the following:

    <col> MATCH '"database engine" -sqlite'

  matches rows that contain the phrase "database engine" but do not contain
  the term "sqlite". If the '-' character occurs inside a quoted phrase,
  it is ignored. It is possible to use both the '-' prefix and the '*' postfix
  on a single term. At this time, all Fts3 queries must contain at least
  one term or phrase that is not preceded by the '-' prefix.

  Regardless of whether or not a table name or column name is used on the 
  left hand side of the MATCH operator, a specific column of the fts3 table
  may be associated with each token in a query by preceding a token with
  a column name followed by a ':' character. For example, regardless of what
  is specified for <col>, the following query requires that column "col1"
  of the table contains the term "hello", and that column "col2" of the
  table contains the term "world". If the table does not contain columns
  named "col1" and "col2", then an error is returned and the query is
  not run.

    <col> MATCH 'col1:hello col2:world'

  It is not possible to associate a specific table column with a quoted 
  phrase or a term preceded by a '-' operator. A '*' character may be
  appended to a term associated with a specific column for prefix matching.

3. ENHANCED QUERY SYNTAX

  The enhanced query syntax is quite similar to the standard query syntax,
  with the following four differences:

  1) Parenthesis are supported. When using the enhanced query syntax,
     parenthesis may be used to overcome the built-in precedence of the
     supplied binary operators. For example, the following query:

       <col> MATCH '(hello world) OR (simple example)'

     matches documents that contain both "hello" and "world", and documents
     that contain both "simple" and "example". It is not possible to forumlate
     such a query using the standard syntax.

  2) Instead of separating tokens and phrases by whitespace, an AND operator
     may be explicitly specified. This does not change query processing at
     all, but may be used to improve readability. For example, the following
     query is handled identically to the one above:

       <col> MATCH '(hello AND world) OR (simple AND example)'

     As with the OR and NEAR operators, the AND operator must be specified
     in upper case. The word "and" specified in lower or mixed case is 
     handled as a regular token.

  3) The '-' token prefix is not supported. Instead, a new binary operator,
     NOT, is included. The NOT operator requires that the query specified
     as its left-hand operator matches, but that the query specified as the
     right-hand operator does not. For example, to query for all rows that
     contain the term "example" but not the term "simple", the following
     query could be used:

       <col> MATCH 'example NOT simple'

     As for all other operators, the NOT operator must be specified in
     upper case. Otherwise it will be treated as a regular token.

  4) Unlike in the standard syntax, where the OR operator has a higher
     precedence than the implicit AND operator, when using the enhanced
     syntax implicit and explict AND operators have a higher precedence
     than OR operators. Using the enhanced syntax, the following two
     queries are equivalent:

       <col> MATCH 'sqlite fantastic OR impressive'
       <col> MATCH '(sqlite AND fantastic) OR impressive'

     however, when using the standard syntax, the query:

       <col> MATCH 'sqlite fantastic OR impressive'

     is equivalent to the enhanced syntax query:

       <col> MATCH 'sqlite AND (fantastic OR impressive)'

     The precedence of all enhanced syntax operators, in order from highest
     to lowest, is:

       NEAR       (highest precedence, tightest grouping)
       NOT
       AND
       OR         (lowest precedence, loosest grouping)

  Using the advanced syntax, it is possible to specify expressions enclosed
  in parenthesis as operands to the NOT, AND and OR operators. However both
  the left and right hand side operands of NEAR operators must be either
  tokens or phrases. Attempting the following query will return an error:

    <col> MATCH 'sqlite NEAR (fantastic OR impressive)'

  Queries of this form must be re-written as:

    <col> MATCH 'sqlite NEAR fantastic OR sqlite NEAR impressive'

1. FTS3 Tokenizers

  When creating a new full-text table, FTS3 allows the user to select
  the text tokenizer implementation to be used when indexing text
  by specifying a "tokenize" clause as part of the CREATE VIRTUAL TABLE
  statement:

    CREATE VIRTUAL TABLE <table-name> USING fts3(
      <columns ...> [, tokenize <tokenizer-name> [<tokenizer-args>]]
    );

  The built-in tokenizers (valid values to pass as <tokenizer name>) are
  "simple", "porter" and "unicode".

  <tokenizer-args> should consist of zero or more white-space separated
  arguments to pass to the selected tokenizer implementation. The 
  interpretation of the arguments, if any, depends on the individual 
  tokenizer.

2. Custom Tokenizers

  FTS3 allows users to provide custom tokenizer implementations. The 
  interface used to create a new tokenizer is defined and described in 
  the fts3_tokenizer.h source file.

  Registering a new FTS3 tokenizer is similar to registering a new 
  virtual table module with SQLite. The user passes a pointer to a
  structure containing pointers to various callback functions that
  make up the implementation of the new tokenizer type. For tokenizers,
  the structure (defined in fts3_tokenizer.h) is called
  "sqlite3_tokenizer_module".

  FTS3 does not expose a C-function that users call to register new
  tokenizer types with a database handle. Instead, the pointer must
  be encoded as an SQL blob value and passed to FTS3 through the SQL
  engine by evaluating a special scalar function, "fts3_tokenizer()".
  The fts3_tokenizer() function may be called with one or two arguments,
  as follows:

    SELECT fts3_tokenizer(<tokenizer-name>);
    SELECT fts3_tokenizer(<tokenizer-name>, <sqlite3_tokenizer_module ptr>);
  
  Where <tokenizer-name> is a string identifying the tokenizer and
  <sqlite3_tokenizer_module ptr> is a pointer to an sqlite3_tokenizer_module
  structure encoded as an SQL blob. If the second argument is present,
  it is registered as tokenizer <tokenizer-name> and a copy of it
  returned. If only one argument is passed, a pointer to the tokenizer
  implementation currently registered as <tokenizer-name> is returned,
  encoded as a blob. Or, if no such tokenizer exists, an SQL exception
  (error) is raised.

  SECURITY: If the fts3 extension is used in an environment where potentially
    malicious users may execute arbitrary SQL (i.e. gears), they should be
    prevented from invoking the fts3_tokenizer() function, possibly using the
    authorisation callback.

  See "Sample code" below for an example of calling the fts3_tokenizer()
  function from C code.

3. ICU Library Tokenizers

  If this extension is compiled with the SQLITE_ENABLE_ICU pre-processor 
  symbol defined, then there exists a built-in tokenizer named "icu" 
  implemented using the ICU library. The first argument passed to the
  xCreate() method (see fts3_tokenizer.h) of this tokenizer may be
  an ICU locale identifier. For example "tr_TR" for Turkish as used
  in Turkey, or "en_AU" for English as used in Australia. For example:

    "CREATE VIRTUAL TABLE thai_text USING fts3(text, tokenizer icu th_TH)"

  The ICU tokenizer implementation is very simple. It splits the input
  text according to the ICU rules for finding word boundaries and discards
  any tokens that consist entirely of white-space. This may be suitable
  for some applications in some locales, but not all. If more complex
  processing is required, for example to implement stemming or 
  discard punctuation, this can be done by creating a tokenizer 
  implementation that uses the ICU tokenizer as part of its implementation.

  When using the ICU tokenizer this way, it is safe to overwrite the
  contents of the strings returned by the xNext() method (see
  fts3_tokenizer.h).

4. Sample code.

  The following two code samples illustrate the way C code should invoke
  the fts3_tokenizer() scalar function:

      int registerTokenizer(
        sqlite3 *db, 
        char *zName, 
        const sqlite3_tokenizer_module *p
      ){
        int rc;
        sqlite3_stmt *pStmt;
        const char zSql[] = "SELECT fts3_tokenizer(?, ?)";
      
        rc = sqlite3_prepare_v2(db, zSql, -1, &pStmt, 0);
        if( rc!=SQLITE_OK ){
          return rc;
        }
      
        sqlite3_bind_text(pStmt, 1, zName, -1, SQLITE_STATIC);
        sqlite3_bind_blob(pStmt, 2, &p, sizeof(p), SQLITE_STATIC);
        sqlite3_step(pStmt);
      
        return sqlite3_finalize(pStmt);
      }
      
      int queryTokenizer(
        sqlite3 *db, 
        char *zName,  
        const sqlite3_tokenizer_module **pp
      ){
        int rc;
        sqlite3_stmt *pStmt;
        const char zSql[] = "SELECT fts3_tokenizer(?)";
      
        *pp = 0;
        rc = sqlite3_prepare_v2(db, zSql, -1, &pStmt, 0);
        if( rc!=SQLITE_OK ){
          return rc;
        }
      
        sqlite3_bind_text(pStmt, 1, zName, -1, SQLITE_STATIC);
        if( SQLITE_ROW==sqlite3_step(pStmt) ){
          if( sqlite3_column_type(pStmt, 0)==SQLITE_BLOB ){
            memcpy(pp, sqlite3_column_blob(pStmt, 0), sizeof(*pp));
          }
        }
      
        return sqlite3_finalize(pStmt);
      }
This folder contains source code to the first full-text search
extension for SQLite.
This package contains:

 * the SQLite library amalgamation source code file: sqlite3.c
 * the sqlite3.h and sqlite3ext.h header files that define the C-language
   interface to the sqlite3.c library file
 * the shell.c file used to build the sqlite3 command-line shell program
 * autoconf/automake installation infrastucture for building on POSIX
   compliant systems
 * a Makefile.msc, sqlite3.rc, and Replace.cs for building with Microsoft
   Visual C++ on Windows

SUMMARY OF HOW TO BUILD
=======================

  Unix:      ./configure; make
  Windows:   nmake /f Makefile.msc

BUILDING ON POSIX
=================

The generic installation instructions for autoconf/automake are found
in the INSTALL file.

The following SQLite specific boolean options are supported:

  --enable-readline           use readline in shell tool   [default=yes]
  --enable-threadsafe         build a thread-safe library  [default=yes]
  --enable-dynamic-extensions support loadable extensions  [default=yes]

The default value for the CFLAGS variable (options passed to the C
compiler) includes debugging symbols in the build, resulting in larger
binaries than are necessary. Override it on the configure command
line like this:

  $ CFLAGS="-Os" ./configure

to produce a smaller installation footprint.

Other SQLite compilation parameters can also be set using CFLAGS. For
example:

  $ CFLAGS="-Os -DSQLITE_THREADSAFE=0" ./configure


BUILDING WITH MICROSOFT VISUAL C++
==================================

To compile for Windows using Microsoft Visual C++:

  $ nmake /f Makefile.msc

Using Microsoft Visual C++ 2005 (or later) is recommended.  Several Windows
platform variants may be built by adding additional macros to the NMAKE
command line.

Building for WinRT 8.0
----------------------

  FOR_WINRT=1

Using Microsoft Visual C++ 2012 (or later) is required.  When using the
above, something like the following macro will need to be added to the
NMAKE command line as well:

  "NSDKLIBPATH=%WindowsSdkDir%\..\8.0\lib\win8\um\x86"

Building for WinRT 8.1
----------------------

  FOR_WINRT=1

Using Microsoft Visual C++ 2013 (or later) is required.  When using the
above, something like the following macro will need to be added to the
NMAKE command line as well:

  "NSDKLIBPATH=%WindowsSdkDir%\..\8.1\lib\winv6.3\um\x86"

Building for UWP 10.0
---------------------

  FOR_WINRT=1 FOR_UWP=1

Using Microsoft Visual C++ 2015 (or later) is required.  When using the
above, something like the following macros will need to be added to the
NMAKE command line as well:

  "NSDKLIBPATH=%WindowsSdkDir%\..\10\lib\10.0.10586.0\um\x86"
  "PSDKLIBPATH=%WindowsSdkDir%\..\10\lib\10.0.10586.0\um\x86"
  "NUCRTLIBPATH=%UniversalCRTSdkDir%\..\10\lib\10.0.10586.0\ucrt\x86"

Building for the Windows 10 SDK
-------------------------------

  FOR_WIN10=1

Using Microsoft Visual C++ 2015 (or later) is required.  When using the
above, no other macros should be needed on the NMAKE command line.

Other preprocessor defines
--------------------------

Additionally, preprocessor defines may be specified by using the OPTS macro
on the NMAKE command line.  However, not all possible preprocessor defines
may be specified in this manner as some require the amalgamation to be built
with them enabled (see http://www.sqlite.org/compile.html). For example, the
following will work:

  "OPTS=-DSQLITE_ENABLE_STAT4=1 -DSQLITE_ENABLE_JSON1=1"

However, the following will not compile unless the amalgamation was built
with it enabled:

  "OPTS=-DSQLITE_ENABLE_UPDATE_DELETE_LIMIT=1"
This directory contains components use to build an autoconf-ready package
of the SQLite amalgamation:  sqlite-autoconf-30XXXXXX.tar.gz

To build the autoconf amalgamation, run from the top-level:

   ./configure
   make amalgamation-tarball

The amalgamation-tarball target (also available in "main.mk") runs the
script tool/mkautoconfamal.sh which does the work.  Refer to that script
for details.
This is the SQLite extension for Tcl using the Tcl Extension
Architecture (TEA).  For additional information on SQLite see

        http://www.sqlite.org/


UNIX BUILD
==========

Building under most UNIX systems is easy, just run the configure script
and then run make. For more information about the build process, see
the tcl/unix/README file in the Tcl src dist. The following minimal
example will install the extension in the /opt/tcl directory.

	$ cd sqlite-*-tea
	$ ./configure --prefix=/opt/tcl
	$ make
	$ make install

WINDOWS BUILD
=============

The recommended method to build extensions under windows is to use the
Msys + Mingw build process. This provides a Unix-style build while
generating native Windows binaries. Using the Msys + Mingw build tools
means that you can use the same configure script as per the Unix build
to create a Makefile. See the tcl/win/README file for the URL of
the Msys + Mingw download.

If you have VC++ then you may wish to use the files in the win
subdirectory and build the extension using just VC++. These files have
been designed to be as generic as possible but will require some
additional maintenance by the project developer to synchronise with
the TEA configure.in and Makefile.in files. Instructions for using the
VC++ makefile are written in the first part of the Makefile.vc
file.
===============================================================================
iGoat Server
-------------------------------------------------------------------------------

ABOUT

This file contains a very simple web server used by iGoat in some of
its exercises. It is a special purpose web server for very specific
purposes, not anything for general purpose use. It takes a specially
constructed input from iGoat, and responds back with information
needed by iGoat.

REQUIREMENTS

Most of what you'll need to run the server already comes with the default OS X
install (Ruby, etc.), but there are a few external gem requirements, which you
can install with the following command:

sudo gem install sinatra json

RUNNING

Simply invoke the igoat-server.rb script from the Terminal...

./igoat-server.rb

Ctrl-C to quit.

FURTHER DETAILS

See the comments in the script itself for ports, endpoints, etc.

And of course: ken@krvw.com, sean@krvw.com

******************************************************************************

 This file is part of iGoat, an Open Web Application Security
 Project tool. For details, please see http://www.owasp.org

 Copyright(c) 2013 KRvW Associates, LLC (http://www.krvw.com)
 The iGoat project is principally sponsored by KRvW Associates, LLC
 Project Leader, Kenneth R. van Wyk (ken@krvw.com)
 Lead Developer: Sean Eidemiller (sean@krvw.com)

 iGoat is free software; you may redistribute it and/or modify it
 under the terms of the GNU General Public License as published by
 the Free Software Foundation; version 3.

 iGoat is distributed in the hope it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or
 FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
 License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc. 59 Temple Place, suite 330, Boston, MA 02111-1307
 USA.

 Source Code: http://code.google.com/p/owasp-igoat/
 Project Home: https://www.owasp.org/index.php/OWASP_iGoat_Project

******************************************************************************
