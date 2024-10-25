# Лабораторная работа 2
## Задание

1. Написать “плохой” CI/CD файл, который работает, но в нем есть не менее пяти “bad practices” по написанию CI/CD
2. Написать “хороший” CI/CD, в котором эти плохие практики исправлены
3. В Readme описать каждую из плохих практик в плохом файле, почему она плохая и как в хорошем она была исправлена, как исправление повлияло на результат

## Ход работы

Сначала были написаны 2 ```.yml``` файла [CI/CD с bad partices](https://github.com/dariapankova/clouds/blob/main/.github/workflows/bad_file.yml) и [CI/CD с good partices](https://github.com/dariapankova/clouds/blob/main/.github/workflows/good_file.yml).

Далее был установлен OpenSSL и создан самоподписанный сертификат, чтобы можно было установить соединение по HTTPS.
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout d:\nginx-1.27.2\ssl\nginx.key -out d:\nginx-1.27.2\ssl\nginx.crt
```
Было создано два виртуальных хоста: krysyatnik1.com и krysyatnik2.com и информация о них была занесена в файл hosts. Для каждого из хостов была создана HTML-страница. После этого в кинфигурационном файле настроено перенаправление HTTP-запросов на HTTPS. Также использовался alias для создания псевдонима пути к каталогу styles. В этом каталоге хранится файл со стилями, которые использовались при создании обеих HTML-страниц.
```
#Конфигурация для первого хоста
server {
    listen 80;
    server_name krysyatnik1.com;  
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name krysyatnik1.com;

    ssl_certificate      D:/nginx-1.27.2/ssl/nginx.crt;
    ssl_certificate_key  D:/nginx-1.27.2/ssl/nginx.key;

    location / {
        root   D:/nginx-1.27.2/html/krysyatnik1;
        index  index.html;
    }
    location /styles {
	alias D:/nginx-1.27.2/html/styles; 
        }
}
```
```
#Конфигурация для второго хоста
server {
    listen 80;
    server_name krysyatnik2.com; 
    return 301 https://$host$request_uri; 
}

server {
    listen 443 ssl;
    server_name krysyatnik2.com;

    ssl_certificate      D:/nginx-1.27.2/ssl/nginx.crt;
    ssl_certificate_key  D:/nginx-1.27.2/ssl/nginx.key;

    location / {
        root   D:/nginx-1.27.2/html/krysyatnik2;
        index  index.html;
    }
   location /styles {
            alias D:/nginx-1.27.2/html/styles;  
        }
}
```
После этого мы запустили nginx, но тут столкнулись с проблемой: при попытке перехода на http://krysyatnik1.com протокол менялся на https, но открывалась страница с ошибкой 404. Для того, чтобы понять из-за чего это происходит мы включили в файл конфигурации лог-файлы.
```
error_log  C:/nginx/logs/error.log;
access_log  C:/nginx/logs/access.log;
```
После перезапуска nginx мы изучили файл error_log, но ничего там не обнаружили. После нескольких неудачных попыток все починить мы решили попробовать запустить nginx с указанием конфигурационного файла который нужно использовать с помощью команды```nginx -c conf/nginx.conf```. И тогда наконец-то все заработало. При вводе адреса hhtp://krysyatnik1.com происходит перенаправление на https://krysyatnik1.com и открывается созданная HTML-страничка.

![](images/photo1.jpg)

Точно также открывается krysyatnik2.com и подключение также происходит по протоколу HTTPS.

![](images/photo2.jpg)

