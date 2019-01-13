# docker-mecab-api

MeCab API docker images based on alpine

## Usage

```
# run dev server
docker run --rm -p 8080:8080 smizy/mecab-api

# with gunicorn
docker run --rm -p 8080:8080 smizy/mecab-api gunicorn -w 4 -b 0.0.0.0:8080 main:app

# api call (change "localhost" as your docker env)
curl -s "http://localhost:8080/parse?q=%E5%A4%96%E5%9B%BD%E4%BA%BA%E5%8F%82%E6%94%BF%E6%A8%A9%0A" |
python -c 'import sys,json;print json.dumps(json.loads(sys.stdin.read()),indent=4,ensure_ascii=False)'

# decoded json
{
    "result": [
        {
            "features": [
                "名詞", 
                "固有名詞", 
                "人名", 
                "一般", 
                "*", 
                "*", 
                "外国人参政権", 
                "ガイコクジンサンセイケン", 
                "ガイコクジンサンセイケン"
            ], 
            "surface": "外国人参政権"
        }
    ]
}

```