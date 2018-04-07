#!/usr/bin/env python3

import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


class FRKLFTRequestHandler(BaseHTTPRequestHandler):
    MIME = {
        '.html': 'text/html',
        '.jpg': 'image/jpeg',
        '.png': 'image/png',
    }

    ROUTES = {
        '/': 'index.html',
        '/team': 'team.html',
        '/contact/sales': 'contact/sales.html',
        '/contact/careers': 'contact/careers.html',
    }

    PUBLIC_DIR = Path(__file__).parent.parent / 'public'

    def do_HEAD(self):
        self.send_response(200)
        mime = self.extract_mime(self.ROUTES.get(self.path, self.path))
        if mime is not None:
            self.send_header('Content-type', mime)
        self.end_headers()

    def do_GET(self):
        path = self.ROUTES.get(self.path, self.path[1:])
        if (self.PUBLIC_DIR / path).exists():
            self.respond(path=path)
        else:
            self.respond(status=404)

    def handle_http(self, status_code, path=None):
        self.send_response(status_code)
        content = b''
        if path is None:
            return content
        mime = self.extract_mime(path)
        if mime is not None:
            self.send_header('Content-type', mime)
        self.end_headers()
        content = (self.PUBLIC_DIR / path).read_bytes()
        return content

    def extract_mime(self, path):
        ext = Path(self.ROUTES.get(self.path, self.path)).suffix
        return self.MIME.get(ext)

    def respond(self, path=None, status=200):
        response = self.handle_http(status, path)
        self.wfile.write(response)


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    print(time.asctime(), 'Server Starts - http://%s:%s' % server_address)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - http://%s:%s' % server_address)


if __name__ == '__main__':
    run(handler_class=FRKLFTRequestHandler)
