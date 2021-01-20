FROM python:3

COPY ./practice/ ./usr/src/practice/
COPY ./requirements.txt ./

RUN pip install --upgrade pip \
    && pip install -r ./requirements.txt

WORKDIR usr/src/

CMD ["flask", "run",  "--host",  "0.0.0.0"]