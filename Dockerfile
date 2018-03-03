FROM python:3.5
#ADD requirements.txt /app/requirements.txt
ADD ./ /app/
WORKDIR /app/
#RUN bash start_app.sh
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
