#!/usr/bin/env python3


from functools import partial
from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            print("<", self.rfile, "> got: ", line)
            self.wfile.write(b'GOT: ' + line)

if __name__ == "__main__":
    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    serv.serve_forever()


