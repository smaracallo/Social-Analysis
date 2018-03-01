#!/bin/bash
echo "STARTING CONTAINER ENTRYPOINT"
echo $(which python)
echo $(which pip)
pip install numpy
celery -A workers worker --concurrency=20 --loglevel=info &
python -m workers.run_tasks
echo "FINISHED WITH SCRIPT"
sleep 500000000