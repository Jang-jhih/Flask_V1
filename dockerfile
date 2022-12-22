
# FROM alpine:latest


FROM python:3.9.16-slim
# RUN apk update
# RUN apk add py-pip
# RUN apk add --no-cache python3-dev
# RUN apk add python3-dev

# RUN pip install --upgrade pip

WORKDIR /app
COPY . /app
 
RUN pip --no-cache-dir install -r requirements


CMD ["python","api.py"]