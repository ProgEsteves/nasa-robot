FROM alpine:3.6

RUN apk add --update python3 py3-pip
RUN pip3 install eve requests

EXPOSE 8080
RUN mkdir -p /opt/robot
ADD robot/*.py /opt/robot/

WORKDIR /opt/robot

CMD ["python3", "run.py"]
