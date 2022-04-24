# TCSS 506 Spring 2022 - homework 2
# Student: JP Montagnet (jpmont)
FROM python:3.9-slim-buster
RUN pip3 install flask
COPY app.py app.py
RUN python app.py
