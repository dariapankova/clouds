FROM python

RUN apt-get update && apt-get install -y python3-pip && pip install numpy

WORKDIR /Users/riapankova/Documents/docker-project/bad-dockerfile
COPY . .

EXPOSE 8084

CMD python3 -m http.server 8084
