# CouchDB
This exercise is divided into several sections. The first part of each section introduces a new concept and describes how to perform certain actions on the database. Then there is a set of exercises where you need to figure out yourself how to solve the problem. Take the opportunity to discuss with a neighbour and skim through the API-reference for guidelines.

## Resources
- CouchDB API reference: [http://docs.couchdb.org/en/2.0.0/http-api.html](http://docs.couchdb.org/en/2.0.0/http-api.html)

## Before we start

Clone the repository into a directory of your choice.

```
$ git clone http://github.com/cygni/cygni-competence-7-databases
```
Pull the docker images we will use in this exercise and create a new docker network called 'couchdb'.
```
$ docker pull cygni/7-databases:couchdb
$ docker pull cygni/7-databases:couchdb-shell
$ docker network create couchdb
```

Ensure that your current directory is the `cygni-competence-7-databases/couchdb` directory. Then start a new container from the 'cygni/7-databases:couchdb' image using the following command (WINDOWS or bash):

```
WINDOWS > docker run -d --name couch -p 5984:80 -v %cd%\db:/couchdb/data --net couchdb cygni/7-databases:couchdb
BASH    $ docker run -d --name couch -p 5984:80 -v $(pwd)/db:/couchdb/data --net couchdb cygni/7-databases:couchdb
```

Note: `-v %cd%\db:couchdb/data` and `-v $(pwd)/db:/couchdb/data` _mounts_ the `db` directory inside the container so that your database files are kept when you delete the container.

Now verify that your database is up and running at [localhost:5984/_utils][fauxton]. You should be presented to 'Fauxton', the web interface that comes with CouchDB. If not, something is wrong with your setup. Post your issue in the #7-databases channel on slack to get it resolved before the occasion.

![alt text][fauxton-first-page]

## Fauxton
Create a new database called 'music' from Fauxton. Your browser should now be looking at [http://localhost:5984/_utils/#/database/music/_all_docs](http://localhost:5984/_utils/#/database/music/_all_docs). From here, you can view, edit, create, or delete documents from the music database.

![alt text][fauxton-music-db]

Click on 'All Documents' -> '+' -> 'New document'. Fauxton will take you to its document editor where you manually can edit the initial value of the document. CouchDB already generated a unique identifier for you in the *_id* field. But you are free to change it. If the _id field is omitted, CouchDB will generate a new one before saving. So, just click 'Create Document' to save the new document.

![alt text][fauxton-new-document]

This should take you back to the view of all documents. Click the edit icon on the created document to go back to the editor.

![alt text][fauxton-all-docs]

Note the additional field called *_rev*. CouchDB generates a new value for this field each the document changes. The integer at the beginning represents the numerical revision of the document. As you will see later, to update a document in CouchDB, both the *_id* and the *_rev* fields must be provided. The update will only be accepted if the provided *_rev* field matches the current *_rev* field in the database. That is, CouchDB ensures that clients have read the latest version of a document when updating.

Now, delete the document we created. You can do this either from the view of all documents or from the document editor. Then create a brand new document. But this time, you should specify the id yourself. In the document editor, add the following json:

``` json
{
  "_id": "ramones",
  "name": "Ramones"
}
```

Save the document. Then go back and edit to add a 'albums' field:

``` json
"albums": [
    {
        "title": "Ramones",
        "year": 1976 
    },
    {
        "title": "Rocket to Russia",
        "year": 1977
    },
    {
        "title": "Road to Ruin",
        "year": 1978
    }
]
```

After saving, note the updated *_rev* field. It should start with '2'.

## Getting dirty with cURL
While the Fauxton interface provides a great overview of what features are available in CouchDB, it hides some of the details of how CouchDB works. We are going to use the command line tool *cURL* to communicate with CouchDB over its' RESTful API. Start the prepared shell using docker:

``` bash
WINDOWS > docker run -it --rm -v %cd%:/couch --net couchdb cygni/7-databases:couchdb-shell
BASH    $ docker run -it --rm -v $(pwd):/couch --net couchdb cygni/7-databases:couchdb-shell
```

Once inside the running container, issue a GET request to the root of the CouchDB endpoint. This will retrieve an informational message about the CouchDB instance.

``` bash
$ curl couch
{"couchdb":"Welcome","version":"2.0.0","vendor":{"name":"The ... 
```

Issuing a GET request on a database will retrieve information about the database including number of documents and number of operations.

``` bash
$ curl couch/music
{"db_name":"music","update_seq":"4-...
```

### Accessing documents
Documents in a database are exposed as resources on the path /{db}/{document-id}. See the [API reference][couch-api-document]. Issuing a GET request will retrieve the entire document: (you can pipe output to 'jq .' for pretty printing json)

``` bash
$ curl couch/music/ramones | jq .
{
  "_id": "ramones",
  "_rev": "2-0a47eedbed7a829478ca490dbd9b2b6f",
  "name": "Ramones",
  "albums": [
    {
      "title": "Ramones",
      "year": 1976
    },
    {
      "title": "Rocket to Russia",
      "year": 1977
    },
    {
      "title": "Road to Ruin",
      "year": 1978
    }
  ]
}
```

To create a new document you can either PUT or POST. Issue a POST request to the music database to create a new document. CouchDB will respond with generated identifier and revision values:

``` bash
$ curl -X POST couch/music/ \
-H "Content-Type: application/json" \
-d '{"name": "De Lyckliga Kompisarna"}'
{"ok":true,"id":"5dd92....","rev":"1-e4ce7...."}
```

Updates to existing documents are made using PUT requests. As mentioned earlier, we have to specify the *_id* and *_rev* fields of the latest version of the document we want to update. The *_id* value is specified in the URL: `couch/{db}/{id}`. The *_rev* value can be specified in:

- The json body with a field named `"_rev": {revision}`
- The If-Match HTTP header `If-Match: {revision}`
- The rev query parameter `localhost:5984/music/{id}?rev={revision}`

Add some albums to the 'De Lycklyga Kompisarna' document by issuing a PUT:

``` bash
$ curl -X PUT 'couch/music/5dd92d287619477369ec87e4ef00d73b?rev=1-e4ce78586222cdb35465d4bea038238a' \
-H "Content-Type: application/json" \
-d '{
    "name": "De Lyckliga Kompisarna",
    "albums": [
        "Tomat",
        "Sagoland"
    ]
}'
{"ok":true,"id":"5dd92d287619477369ec87e4ef00d73b","rev":"2-027c7d133a0ccaf9596c6aa3dbe9e30f"}
```

CouchDB responds with 200 OK and the new revision field value. Try to execute the same command again, CouchDB will responds with an error specifying a 'Document update conflict'. This is because the provided revision value does not match the latest version.

Note how we also provided the 'name' field in the body, even though it was already in the document. That is because an update in CouchDB always completely replace the previous version of the document. It is not possible to simply append values.

Finally, delete the document using a DELETE request. Similar to updates, the latest revision has to be provided in the rev query parameter or in the If-Match HTTP header:

``` bash
$ curl -X DELETE 'couch/music/5dd92d287619477369ec87e4ef00d73b?rev=2-027c7d133a0ccaf9596c6aa3dbe9e30f'
{"ok":true,"id":"5dd92d287619477369ec87e4ef00d73b","rev":"3-451e59c722e3f8fd4ae8b7463efd12eb"}
```

Note that CouchDB responds with an updated revision. Instead of actually removing the document from disk, CouchDB inserts a new empty document on the same id and marks it as deleted. So, issuing a GET on the document id will return 404 Not Found with an additional 'reason' message specifying that the document has been deleted:

``` bash
$ curl couch/music/5dd92d287619477369ec87e4ef00d73b
{"error":"not_found","reason":"deleted"}
```

## Exercises: CRUD with cURL
1. Use cURL to PUT a new artist document into the database with a specific *_id* of your choice.
2. Use cURL to create a new database with a name of your choice. Then delete it, also using cURL.
3. \* Use cURL to add the 'data/ramones.jpg' image as an [attachment][couch-api-attachments] to the 'Ramones' document. Then, look it up in Fauxton. (Hint: content type is image/jpeg, and binary data can be passed from using the --data-binary option)
4. \* Use cURL to retrieve the image attachment.

## Import data
Execute the following command to add some music data to our database. It uses the CouchDB *_bulk_docs* feature to add a batch of documents in a single POST request.

``` bash
$ zcat data/jamendo-data.json.gz | \
curl -X POST couch/music/_bulk_docs/ \
-d @- -H "Content-Type: application/json"
```

The jamendo-data.json file contains artist data in the following format: ('random' is just a random 16-bit number assigned to each artist, album and track)

``` json
{
  "_id": "XXXX",
  "name": "Artist Name",
  "country": "CTR",
  "random": 33654,
  "albums": [
    {
      "id": "YYYY",
      "name": "Album Name",
      "random": 52086,
      "tracks": [
        {
          "id": "ZZZZ",
          "name": "Track Name",
          "random": 56475,
          "tags": [
              {
                  "idstr": "tag",
                  "weight": 0.5
              }
          ],
        }
      ],
    }
  ],
}
```

## Views 
In CouchDB you access documents through *views*. The simplest predefined view is called [_all_docs][couch-api-views] and is accessible through `couch/{db}/_all_docs`. The following request will retrieve the revision values of the first 10 documents in the 'music' database ordered by document id:

```
$ curl couch/music/_all_docs?limit=10
```

Append the query parameter *include_docs=true* to include the entire documents in the response.

```
$ curl 'couch/music/_all_docs?include_docs=true&limit=10
```

In general, a view consists of a *map* and a *reduce* function. Fauxton provides a pretty decent interface for writing your own views. Views are stored in *design documents*. These are special documents, prefixed with _design/. The map function generates an ordered list of key-value pairs which can then be reduced by the optional reduce function.

Go to the *music* database page in Fauxton and click the '+' sign next to 'Design Documents' to add a new view. Name it 'by_name' and add it to a new design document called 'artists'.
![alt text][fauxton-music-new-view]

Write the following map function then hit 'Create Document' to save the design document:

```javascript
function(doc) {
  if ('name' in doc) {
    emit(doc.name, doc._id);
  }
}
```

[This][couch-api-views] page describes how views are queried. In short, they are accessed from the path:

```
/{database}/_design/{design-document}/_view/{view-name}
```

Try your new view by running the following command in curl:

```
$ curl couch/music/_design/artists/_view/by_name?limit=2 | jq .
{
  "total_rows": 2721,
  "offset": 0,
  "rows": [
    {
      "id": "5385",
      "key": " A.n.K.h // ",
      "value": "5385"
    },
    {
      "id": "338149",
      "key": " Bsl & Bass",
      "value": "338149"
    }
  ]
}
```

Each row in the response is a result of the 'emit' call in the map function. The key is the first parameter and the value is the second parameter.

Now go back to the *music* database page and create a new design document named 'albums' with a view named 'by_name'. Enter the following map function:
```javascript
function(doc) {
  if ('name' in doc && 'albums' in doc) {
    doc.albums.forEach(function(album){
      var key = album.title || album.name;
      var value = { by: doc.name, album: album };
      emit(key, value);
    });
  }
}
```

Execute a similar request to retrieve albums by name:

```
$ curl couch/music/_design/albums/_view/by_name?limit=2
{
  "total_rows": 5474,
  "offset": 0,
  "rows": [
    {
      "id": "354152",
      "key": "     la classe",
      "value": {
        "by": "N.M. mthy",
        "album": {
          "id": "53416",
          "name": "     la classe",
          "tracks": [ ... ],
          "random": 18812
        }
      }
    },
    {
      "id": "367144",
      "key": "  beautiful moments of your life",
      "value": {
        "by": "Jay Daniel Producer",
        "album": {
          "id": "94769",
          "name": "  beautiful moments of your life",
          "tracks": [ ... ],
          "random": 23039
        }
      }
    }
  ]
}
```

Note that the 'value' field contains the entire album as well as the artist name. This is exactly what we specified in the map function.

## Exercises: Views
1. Using the artists/by_name view, find all artists that start with the letter "J".
2. Create a new artist view that returns artist names keyed by their country. Then use cURL to find all artists from france ('FRA').
3. \* Create a new view that returns tracks keyed by their tag. Use cURL to retrieve all tracks tagged with 'rock'.
4. \*\* Remember the 'weight' field for tags? A track with a low weighted 'rock' tag might not be considered as 'rock'. Therefore, modify the view from the previous exercise so that it is possible to specify the minimum weight for the tag. Then find all tracks with a 'rock' tag weight of 0.8 or more.

## Advanced Views
Create a new design document for 'tags' with a 'by_name' view. Add the following map function

``` javascript
function (doc) {
  (doc.albums || []).forEach(function(album){
    (album.tracks || []).forEach(function(track){
      (track.tags || []).forEach(function(tag){
        emit(tag.idstr, 1);
      });
    });
  });
}
```

This map function will generate rows keyed by tags on album tracks and the value '1' for each tag found. We are going to *reduce* these values with a count function. Select 'CUSTOM' from the dropdown menu, the default reduce function works for us - it will count the number of values for each key.

``` javascript
function (keys, values, rereduce) {
  if (rereduce) {
    return sum(values);
  } else {
    return values.length;
  }
}
```

Execute the following command to retrieve the reduced result:

``` bash
$ curl 'couch/music/_design/tags/_view/by_name?reduce=true&group=true'
```

It is not possible to sort reduced views by value directly from couch. This is something that has to be implemented in your application. For fun we can use jq to retrieve the top 10 most popular tags of our result set.

``` bash
$ curl 'couch/music/_design/tags/_view/by_name?reduce=true&group=true' | \
jq .rows | jq 'sort_by(.value)' | jq reverse | jq .[0:10]
```

### Exercises: Advanced views
1. Modify our artist-by-country view so that it can reduce the number of artists per country.

## Changes API
CouchDB provides a [_change][couch-api-change] resource for each database which enables you to listen for changes.

```
$ curl couch/music/_changes
```

Will retrieve information about all changes in the 'music' database since creation. The result follows the following pattern:

``` json
{
  "results": [
    {
      "seq": <sequence-nr>,
      "id": <doc-id>,
      "changes": [
        {"rev": <last-update-rev>}
      ]
    }
  ]
}
```

Just like with views you can specify the 'include_docs' and 'limit' query parameters.

## Exercises: Changes API
1. Create a cURL request that gets the latest changes for a document with an id of your choice, e.g. 'nirvana'. Then go to fauxton and create/edit that document and execute your curl request again. (Hint: see API reference linked above for \_changes and use filter=_doc_id and doc_ids query parameters)
2. Create a cURL request that uses the *longpolling* feed to get document updates to the same document since the last update sequence. Go to fauxton and edit the document to see what happends.
3. Create a cURL request that uses the *continuous* feed to get document updates for the entire database since the last update sequence. Then go to fauxton and update documents at your will. Inspect the output from cURL.

## Replicating Data
CouchDB provides an easy way to replicate data between databases. Go to Fauxton and navigate to the 'Replication' page. Replicate the 'music' database into a new database called 'music-repl'.

![alt text][fauxton-replicate]

After a few seconds, the new database should have been created so it can be viewed on the 'Databases' page:

![alt text][fauxton-music-repl]

Go back to the shell and enter the following command to insert a new artist document that we are going to use to investigate conflicts:

```
$ curl -X PUT couch/music/theconflicts \
-H "Content-Type: application/json" \
-d '{ "name": "The Conflicts" }'
```

Then trigger a new replications from Fauxton. So you should be able to get 'theconflicts' artist from the `music-repl` database as well:

```
$ curl couch/music-repl/theconflicts 
{"_id":"theconflicts","_rev":"1-...","name":"The Conflicts"}
```

Now, update the document in `music-repl` database by adding a new album:

```
$ curl -X PUT couch/music-repl/theconflicts?rev=1-... \
-H "Content-Type: application/json" \
-d '{
  "name": "The Conflicts",
  "albums": ["Conflicts of Interest"] 
}'
```

Before doing any replication, also update the document in the original database by adding _different_ album:

```
$ curl -X PUT couch/music/theconflicts?rev=1-... \
-H "Content-Type: application/json" \
-d '{
  "name": "The Conflicts",
  "albums": ["Conflicting Opinions"] 
}'
```

Now we have two conflicting versions of the same document in our two databases. So, trigger a new replication to see what happens. You should notice that both `curl couch/music/theconflicts` and `curl couch/music-repl/theconflicts` returns the same version. I.e., CouchDB picked a winning version using a deterministic algorithm.

View the conflicting versions version by appending the `conflicts=true` query parameter: 

```
$ curl couch/music-repl/theconflicts?conflicts=true
```

Retrieve the 'losing' version of the document using the `rev={rev}` query parameter:

```
$ curl couch/music-repl/theconflicts?rev={conflict-rev}
```

## Exercises: Replicating
1. Figure out how to resolve the conflict using cURL.

[fauxton-first-page]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/couchdb/fuxton-first-page.PNG?raw=true "Fauxton First Page"
[fauxton-replicate]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/couchdb/fauxton-replicate.png?raw=true "Fauxton replicate"
[fauxton-music-repl]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/couchdb/fauxton-music-repl.png?raw=true "Replicated database"
[fauxton-new-document]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/couchdb/fauxton-new-document.png?raw=true "Fauxton new document"
[fauxton-all-docs]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/couchdb/fauxton-all-docs.png?raw=true "Fauxton all documents"
[fauxton-music-db]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/couchdb/fauxton-music-db.png?raw=true "Fauxton 'music' database"
[fauxton-music-new-view]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/couchdb/fauxton-music-new-view.png?raw=true "Creating new view"
[couch-download]: http://couchdb.apache.org/#download 
[fauxton]: http://localhost:5984/_utils/
[couch-api-change]: http://docs.couchdb.org/en/2.0.0/api/database/changes.html
[couch-api-attachments]: http://docs.couchdb.org/en/2.0.0/api/document/attachments.html
[couch-api-document]: http://docs.couchdb.org/en/2.0.0/api/document/common.html 
[couch-api-bulk-api]: http://docs.couchdb.org/en/2.0.0/api/database/bulk-api.html
[couch-api-views]: http://docs.couchdb.org/en/2.0.0/api/ddoc/views.html
