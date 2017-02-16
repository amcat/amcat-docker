### (Experimental) AmCAT DockerFile

This contains the code to build AmCAT, including apt and pip prerequisites. 
To run it separately (i.e. outside the compose), you will need to link to the other docker images from the compose file or point to different hostnames in the amcat.ini file. 

The docker image also requires the /etc/amcat volume to be loaded, e.g. from the amcat-etc folder in this repository. 

Something like this worked on my setup:

```{sh}
docker run -tp 8000:8000 -v amcat-etc:/etc/amcat --name amcat --link postgres:postgres --link elastic:elastic --link rabbit:rabbit --link redis:redis amcat
```
