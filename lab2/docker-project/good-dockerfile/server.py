from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Установка директории, откуда будут обслуживаться файлы
        os.chdir('/home/cloudtech/lab2/good-practice')  # Путь к директории
        super().__init__(*args, directory=os.getcwd(), **kwargs)

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8085):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
