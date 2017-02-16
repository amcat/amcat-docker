# (Experimental) support for running AmCAT in a docker container.

This repository offers a `docker-compose.yml` file that configures a complete stack for running amcat, including postgres, elastic, redis, rabbitmq, amcat, and an amcat celery worker. 

To run, clone or download this repository and run:

```{sh}
docker-compose up
```

This should start a server on localhost:8000. You can log in with username and password `amcat`. 

## Configuration

The [amcat-etc](amcat-etc) folder contains the [amcat.ini](amcat-etc/amcat.ini) configuration file.
This folder will be mounted in the amcat Docker file and can be used to set configuration options such as postgres host if desired. 

## Dockerfiles

The dockerfile refers to a number of standard docker images, and two custom images: [amcat-docker](amcat) and [amcat-elastic-docker](https://github.com/amcat/amcat-elastic-docker). You shouldn't need to do anything with these Dockerfiles yourself, as `docker-compose` should build and run the various dockers automatically. 

# Todo

- Allow superuser username/host to be specified in amcat.ini file
- Put postgres data in external volume for persistence and maybe backup
- Use nginx (or some other proper webserver) instead of runserver? (and share static volume)
- Find a better way to distribute this than asking users to clone + run compose?
