#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from app.logs import write_log


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open('index.html', 'rb')
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        str_post_data = str(post_data).replace('\'','')
        split_post_data = str_post_data.split('&')
        username = split_post_data[0].split('=')[1]
        password = split_post_data[1].split('=')[1]

        if username != 'Mykola' or password != 'Matsiakh':
            severity = "ERROR"
            html_data = "<html><body>EtestRROR. Check email</body></html>".encode()
        else:
            severity="DEFAULT"
            html_data = "<html><body>SUCCESS</body></html>".encode()
        write_log(username, password, severity)
        self.wfile.write(html_data)


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    run(port=3000)
