import http.server
import socketserver

PORT = 8000

class MyHTTPHandler( http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("Get response")
        self.send_response(200)
        self.end_headers()
    def do_POST(self):
        print("Put response", self.path)
        print(self.rfile)
        self.send_response(200)
        self.end_headers()



Handler = MyHTTPHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()