FROM python:3.5
ADD requirements.txt /app/requirements.txt
ADD ./app/workers/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
RUN which python
RUN which pip
ENTRYPOINT bash start_app.sh
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
