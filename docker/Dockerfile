FROM python:3.8
ARG PAALIAQ_ALNAIR_TOKEN

WORKDIR /bors-data
COPY . .

RUN pip install poetry==1.1.4

RUN poetry config repositories.paaliaq-alnair https://gitlab.paaliaq.xyz/api/v4/projects/35/packages/pypi/simple
RUN poetry config http-basic.paaliaq-alnair gitlab-ci-token $PAALIAQ_ALNAIR_TOKEN
RUN poetry add --source paaliaq-alnair alnair
RUN poetry install

ADD /docker/run.sh .
RUN chmod +x run.sh

ENTRYPOINT ["/bin/bash", "run.sh"]
CMD ["config.json"]
