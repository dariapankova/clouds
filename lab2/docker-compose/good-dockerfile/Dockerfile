FROM python:3.8.10

# Создание пользователя для повышения безопасности
RUN useradd -m appuser

# Установка зависимостей с явным указанием версии
RUN pip install numpy==1.21.0

WORKDIR /app

# Копирование только необходимых файлов
COPY index.html .
COPY dolphins.jpeg .

# Переключение на созданного пользователя
USER appuser

EXPOSE 8085

ENTRYPOINT ["python3", "-m", "http.server"]
CMD ["8085"]
