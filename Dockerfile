FROM registry.gitlab.com/pierzchlewicz/tmsi-usb-docker

WORKDIR /app

COPY ./src/ /app

RUN pip3 install requests
