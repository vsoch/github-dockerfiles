Building the Docker image and running the container::

    sudo docker build -t mobius-demo:0.1 .
    sudo docker run -ti -p 6081:6081 mobius-demo:0.1

End-to-end cache invalidation relies on the site's host name being `docker`.
To add this alias on Linux and Mac do::

    echo '127.0.0.1 docker' | sudo tee --append /etc/hosts

However, the cache invlidation really shines if many machines can access your
instance, in which case do the following on all Linux and Mac clients::

    echo 'your.ip.adress docker' | sudo tee --append /etc/hosts

You may now browse to docker:6081 on the clients. The Django
superuser is `admin` and the password is `local`.

