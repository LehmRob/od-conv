FROM debian:buster

RUN apt-get update && \
    apt-get install -y python \
    python-pip

ADD https://files.pythonhosted.org/packages/32/48/0dabdd6362155cb37a2f52a261d7f9f1e746cc1a292f8d8d6b7ee2ee5b69/Gnosis_Utils-1.2.2.tar.gz .
RUN tar -xzf Gnosis_Utils-1.2.2.tar.gz && mv Gnosis_Utils-1.2.2/gnosis .
RUN mkdir /data

ADD conv.py .

ENTRYPOINT ["/bin/bash"]
