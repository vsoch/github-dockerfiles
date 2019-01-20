Para instalar Docker:

1.- Primero instalar wget:
$ sudo apt-get update
$ sudo apt-get install wget

2.- Bajar Docker con wget:
$ wget -qO- https://get.docker.com/ | sh

3.- Verificar que Docker se haya instalado correctamente (puede necesitar sudo)
$ docker run hello-world




Para correr el KRR:
1.- Ubicarse en el directorio krr

2.- Crear la imagen del KRR
$ docker build -t krr .

3.- Correr el contenedor con la imagen del KRR
$ docker run --name krr -p 8000:8000 -it krr

Con esto el KRR estará corriendo en localhost:8000


Para correr el PF:
1.- Ubicarse en el directorio krr

2.- Crear la imagen del PF
$ docker build -t pf .

3.- Correr el contenedor con la imagen del PF
$ docker run --name pf -p 8001:8001 -it pf

Con esto el PF estará corriendo en localhost:8001


Notas:
- Para detener el PF o KRR, Control-C en su terminal o $ docker stop krr
- Para iniciar nuevamente un contenedor detenido, $ docker start krr
- La opción -p indica el puerto a usar. Si se desea cambiar, se debe cambiar el segundo número
- La opción -it de 'docker run' indica que se vincule el terminal usado con el del contenedor
- Con 'docker exec' se puede ejecutar comandos en un contenedor que está corriendo
=======
# kitrr-docker
Scripts Bash para instanciar el Kit de Respuesta Rápida con Docker

- install-docker.sh para instalar Docker
- create.sh para crear las imágenes y los contenedores
- start.sh para iniciar los contenedores
- stop.sh para detener los contenedores
- remove.sh para eliminar los contenedores (no las imágenes)

