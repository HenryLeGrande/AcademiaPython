from API import Api
from db import Db
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs
import json


PORT = 8000
HOST = 'localhost'

class HttpHandler(BaseHTTPRequestHandler):


    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):

        db = Db()
        db.getDatos()
        for result in db.myresult:
            lista = list(result)
            lista_json = json.dumps(lista)
            self.respond(lista_json)

        """for result in self.myresult:
            self.lista = list(result)
            #print(self.lista)
            self.lista_json = json.dumps(self.lista)
            print(self.lista_json)
        self.respond(db.lista_json)"""


        """code = parse_qs(urlparse(self.path).query).get('country', None)
        if code:
            country = Api(code[0])
            result = json.dumps(country.get_dict())
        else:
            result = '{}'

        self.respond(result)"""



    def handle_http(self, status, content_type, content):

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

        return bytes(content, 'UTF-8')

    def respond(self, result):
        content = self.handle_http(200, 'application/json', result)
        self.wfile.write(content)

if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), HttpHandler)
    print('Server Started... at {} : {} '.format(HOST, PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt Ctrl + C')




