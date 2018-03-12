# Social Analysis

This product ingests, persists, and analyzes data from twitter, as well as providing a frontend for visualizing social media engagement models. 

# Running the app

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