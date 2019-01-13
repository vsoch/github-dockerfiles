# docker-sentencepiece

[Google SentencePiece](https://github.com/google/sentencepiece) docker image based on alpine

## End-to-End Example

```
docker run -it --rm smizy/sentencepiece sh

$ spm_train --input=data/botchan.txt --model_prefix=m --vocab_size=1000

$ echo "I saw a girl with a telescope." | spm_encode --model=m.model
▁I ▁saw ▁a ▁girl ▁with ▁a ▁ te le s c o pe .

$ echo "I saw a girl with a telescope." | spm_encode --model=m.model --output_format=id
9 459 11 939 44 11 4 142 82 8 28 21 132 6

$ echo "9 459 11 939 44 11 4 142 82 8 28 21 132 6" | spm_decode --model=m.model --input_format=id
I saw a girl with a telescope.
```