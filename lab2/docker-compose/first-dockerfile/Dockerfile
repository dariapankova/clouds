# Используем легкий образ Nginx
FROM nginx:alpine

# Копируем HTML-файл и изображение в директорию Nginx
COPY index.html /usr/share/nginx/html/
COPY dolphins.jpeg /usr/share/nginx/html/

# Устанавливаем рабочий каталог
WORKDIR /usr/share/nginx/html

# Открываем порт 80
EXPOSE 80

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]

