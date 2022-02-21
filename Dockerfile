#This Dockerfile is intended for use in Deepnote but should in theory work on your local machine also
FROM deepnote/python:3.7

RUN apt update && apt install -y libcurl4-openssl-dev libssl-dev python3-dev
