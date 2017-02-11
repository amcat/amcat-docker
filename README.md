# (Experimental) support for running AmCAT in a docker container.

This repository offers a `docker-compose.yml` file that configures a complete stack for running amcat, including postgres, elastic, redis, rabbitmq, amcat, and an amcat celery worker. 

To run, clone or download this repository and run:

```{sh}
docker-compose up
```

This should start a server on localhost:8000. You can log in with username and password `amcat`. 

## Configuration

The [amcat-etc](amcat-etc) folder contains the [amcat.ini](amcat-etc/amcat.ini) configuration file and [run_amcat.sh](amcat-etc/run_amcat.sh) shell script. 
This folder will be mounted in the amcat Docker file and can be used to set configuration options such as postgres host if desired. 

## Dockerfiles

The dockerfile refers to a number of standard docker images, and two additional images are defined in the amcat and elastic folders:

Note: You shouldn't need to do anything with these Dockerfiles yourself, as `docker-compose` should build and run the various dockers automatically. 

### amcat 

This contains the code to build AmCAT, including apt and pip prerequisites. To run it separately (i.e. outside the compose), you will need to link to the other docker images from the compose file or point to different hostnames in the amcat.ini file. 

Something like this worked on my setup:

```{sh}
docker run -tp 8000:8000 -v /home/wva/amcat-docker/amcat/etc:/etc/amcat --name amcat --link postgres:postgres --link elastic:elastic --link rabbit:rabbit --link redis:redis amcat
```
### elastic

This sets up elastic 2.4 with the plugins and scripts needed for AmCAT. 

# Todo

- Allow username/host to be specified in amcat.ini file
- Built in check to wait for postgres / elastic to come online
- Use nginx (or some other proper webserver) instead of runserver?
- Find a better way to distribute this than asking users to clone + run compose?
