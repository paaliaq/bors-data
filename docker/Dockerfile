FROM python:latest
WORKDIR /bors-data
COPY src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
## TODO EXPOSE FOR ATLAS, maybe need req for that also? 
