# README pythonFrontEnd

This is the README file for the python Front end folder. The only major change that is needed to get this up and running
is to modify the data_access_layer.py and change the database service to link to your cockroach db external ip link that
you get after deploying the CockroachDB on Kubernetes. 

After that, you run this command to build the image

```
docker build -t IMAGENAME .
```

and execute this command to run the image you just created. 

```
docker run -d -p 5001:5001 -p 26257:26257 IMAGENAME
```

Your public front end should now be visible on your instance ip on port 5001.
