This dockerfile has been created to facilitate the creation of SimpleITK html
doxygen documentation.

Run the following commands:

docker build --build-arg TAG=v1.1.0 . -f Dockerfile -t simpleitk-doxygen
docker create --name simpleitk-doxygen simpleitk-doxygen
docker cp simpleitk-doxygen:/SimpleITK-build/SimpleITK-build/Documentation/html /tmp/
docker rm simpleitk-doxygen
