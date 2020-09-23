FROM python:3.6-stretch
WORKDIR /bors-data
ADD ./src .
COPY /docker/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install -qq --force-yes cron

ADD /docker/cron.sh /usr/bin/cron.sh
RUN chmod +x /usr/bin/cron.sh

ADD /docker/cronpy /etc/cron.d/cronpy
RUN chmod 0644 /etc/cron.d/cronpy

RUN touch /var/log/cron.log

ENTRYPOINT ["/bin/sh", "/usr/bin/cron.sh"]

# TODO
# Default takes this configuration (with DB string and so on), however you like it
# During testing and deployment I need to pass a different one with the actual credentials
# thus your application needs to read that from somewhere. If you don't like files,
# environment variables are also fine
#CMD ["config.json"]
