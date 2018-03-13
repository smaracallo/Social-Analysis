#!/bin/bash
echo "STARTING CONTAINER ENTRYPOINT"
echo $(which python)
echo $(which pip)
echo 'ENVIRONMENT'
echo $ENVIRONMENT
echo 'CONSUMER_KEY'
echo $CONSUMER_KEY
echo 'END ECHO'
export PYTHONPATH=$PYTHONPATH:/app/
cd ./app
pip install -r requirements.txt
celery -A workers worker -B --concurrency=20 --loglevel=info &
python -m workers.run_tasks
echo "FINISHED WITH SCRIPT"
# sleep 500000000