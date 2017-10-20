# discord.py runs on Python3
FROM python:3

# create app directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# bundle app source
COPY . /usr/src/app
RUN pip install -r requirements.txt

# start!
RUN launcher.sh
