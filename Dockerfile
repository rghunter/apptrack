FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
