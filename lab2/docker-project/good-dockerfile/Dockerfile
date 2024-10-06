FROM python:3.12

RUN apt-get update && useradd app_user && pip install numpy==2.1.1

WORKDIR /Users/riapankova/Documents/docker-project/bad-dockerfile

COPY index.html .
COPY dolphins.jpeg .

USER app_user

EXPOSE 8085

CMD ["python3", "-m", "http.server", "8085"]
