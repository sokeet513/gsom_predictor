from ubuntu:20.04 
MAINTAINER Evgenii Sokolov
RUN apt-get update -y
COPY . /apt/gsom_predictor
WORKDIR /apt/gsom_predictor
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py
