#
# Dart runtime Dockerfile
#
# https://github.com/dockerfile/dart-runtime
#

# Pull base image.
FROM dockerfile/dart

# Set instructions on build.
ONBUILD ADD pubspec.yaml /app/
ONBUILD ADD pubspec.lock /app/
ONBUILD RUN pub get
ONBUILD ADD . /app
ONBUILD RUN pub get

# Define working directory.
WORKDIR /app

# Define default command.
CMD ["dart", "bin/server.dart"]

# Expose ports.
EXPOSE 8080
