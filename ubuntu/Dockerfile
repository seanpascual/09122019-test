FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /example-app/requirements.txt

WORKDIR /example-app

RUN pip3 install -r requirements.txt

COPY . /example-app

ENTRYPOINT [ "python3" ]

CMD [ "example.py" ]
