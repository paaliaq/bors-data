FROM python:3.6-stretch
WORKDIR /bors-data
COPY src
COPY requirements.txt requirements.txt
RUN sudo pip install -r requirements.txt
RUN apt-get install cron
RUN sudo crontab -e
RUN 0 1 * * * /usr/bin/python3 /bors-data/main.py >> ~/cron.log 2>&1
## TODO EXPOSE FOR ATLAS, maybe need req for that also? 
