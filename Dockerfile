FROM continuumio/miniconda:4.5.4

ADD requirements.txt /
RUN pip install -r requirements.txt