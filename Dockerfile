FROM python:3-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
COPY scms/requirements.txt /requirements.txt

# Install dependencies
RUN pip install --upgrade pip \
    pip install --upgrade wheel \
    pip install -r /requirements.txt

WORKDIR /code

CMD [ "flask", "run", "-h", "0.0.0.0" ]
