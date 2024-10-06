FROM python

RUN apt-get update 
RUN pip install numpy

COPY . .

EXPOSE 8084

CMD ["python3", "-m", "http.server", "8084"]
