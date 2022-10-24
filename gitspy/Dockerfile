# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /gitspy

# install dependencies
RUN pip install --upgrade pip
COPY ./gitspy/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .