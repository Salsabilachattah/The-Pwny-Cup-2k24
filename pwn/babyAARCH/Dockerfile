FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y socat qemu-user qemu-user-static patchelf

RUN useradd ctf && \
    mkdir challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chown -R root:root . && \
    chmod +x entrypoint.sh babyAARCH run.sh &&\
    patchelf --set-interpreter $(pwd)/ld* ./babyAARCH &&\
    patchelf --set-rpath $(pwd) ./babyAARCH

USER ctf
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]
