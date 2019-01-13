#  ******************
#  dockerfiles ex00 *
#  ******************

# ex00. From an alpine image you’ll add to your container your favorite text editor, 
#   vim or emacs, that will launch along with your container.



FROM alpine

# run the command
RUN apk update && apk upgrade && apk add vim

# execute the following command
ENTRYPOINT vim test.txt

# note: # Run " docker build -t [any (image) name you want] . "
#       # Run " docker run -it [image name you just name above]"