FROM python:3.5
ADD requirements.txt /app/requirements.txt
ADD ./app/workers/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
RUN pwd
RUN ls
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
