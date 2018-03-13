# Social Analysis

This product ingests, persists, and analyzes data from twitter, as well as providing a frontend for visualizing social media engagement models. 

## Running the app

In one terminal

``` bash
docker-compose up
```

In another terminal

``` bash
docker-compose exec dockerapp bash
```

Now you can interact with the python code running inside the app container

For example, run:

``` bash
python app/tests/test_entrypoint.py
```

## Deploying the app to PROD

Push the image to dockerhub

```
docker login -u $DOCKER_HUB_USER_ID -p $DOCKER_HUB_PWD
docker tag socialanalysis_dockerapp $DOCKER_HUB_USER_ID/dockerapp:$CIRCLE_SHA1
docker tag socialanalysis_dockerapp $DOCKER_HUB_USER_ID/dockerapp:latest
docker push $DOCKER_HUB_USER_ID/dockerapp:$CIRCLE_SHA1
docker push $DOCKER_HUB_USER_ID/dockerapp:latest
```

Change directory to where you have your .ssh directory.

then:

```
docker-machine create --driver=generic --generic-ip-address=174.138.34.18 --generic-ssh-user=root --generic-ssh-key=.ssh/digital_ocean --generic-ssh-port=22 ubuntu-s-1vcpu-1gb-nyc1-01    
```

substitute values for parameters as needed

In another tab push the local files to the cloud machine

```
docker-machine scp -r . ubuntu-s-1vcpu-1gb-nyc1-01:/root/
```

follow the prompt by docker to set env vars for connecting to the docker machine such as: 

```
eval $(docker-machine env ubuntu-s-1vcpu-1gb-nyc1-01)
```

Note, please look at what commands this will run before using `eval`

in the same terminal session as where you ran the last command run:

```
docker-compose -f docker-compose.yml -f prod.yml up -d  --force-recreate
```

That's it, now the app is running in PROD

### MongoDB Copy

To copy the production database to your local machine for testing run the command:

```
mongodump --host 174.138.34.18:27018 
```

then 

```
mongorestore dump --host localhost:27018
```

