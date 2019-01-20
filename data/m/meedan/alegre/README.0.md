Put models here. The one included in the repo is very small and only for testing purposes. You can download the Google one from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit, Glove ones from https://nlp.stanford.edu/projects/glove/ (and use the script here to convert to Gensim format) or other models from the list at https://github.com/3Top/word2vec-api#where-to-get-a-pretrained-models.
This is a plugin for ElasticSearch. You can compile it with Maven and then install.

Compile:

```
mvn clean install 
```

Install:

```
/usr/share/elasticsearch/bin/elasticsearch-plugin install --verbose --batch file:///path/to/es-script-cosine-scoring/target/releases/meedan-cosine-0.0.1.zip

```

After the plugin is installed, you're able to use the Meedan Cosine function for score calculation:

```
'function_score': {
    'functions': [
        {
            'script_score': {
                'script': {
                    'source': 'cosine',
                    'lang': 'meedan_scripts',
                    'params': {
                        'vector': <vector>
                    }
                }
            }
        }
    ]
}
```
