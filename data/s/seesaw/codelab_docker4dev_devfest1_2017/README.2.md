Creiamo ora un'app funzionante. Un sito web statico.

Scaricate da [qui](https://goo.gl/phSvX6) i files per la prossima demo.

Estreteli in una folder, e create un file chiamato `Dockerfile`

Che avrà questo contenuto :

```
# our base image
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]
```
Una volta scritto il Dockerfile, bisognerà creare la build, con il comando `docker build -t codelab/happy_cats .`.

Avviare il container con `docker run -p 8888:5000 --name happy_cats codelab/happy_cats`

Espone la porta 5000 del container sulla 8888 locale.



