FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat

RUN useradd ctf && \
    mkdir challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chown -R root:root . && \
    chmod +x deceiving entrypoint.sh

EXPOSE 1337

CMD ["./entrypoint.sh"]


