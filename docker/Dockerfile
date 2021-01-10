FROM python:3.8
WORKDIR /bors-data
ADD ./src .
COPY /docker/requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD /docker/run.sh .
RUN chmod +x run.sh

ENTRYPOINT ["/bin/bash", "run.sh"]
CMD ["config.json"]
