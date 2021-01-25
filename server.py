
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
import requests
import urllib
import time
from tornado.ioloop import IOLoop
import os
import torn
import json
from pyngrok import ngrok
from routes import *

def fetch(url:str,public_ip):
	return requests.post(url, data = json.dumps({'DNS':public_ip})).status_code

settings = dict(
		debug=torn.Debug(),
	)

application = Application(route, **settings)


if __name__ == "__main__":
	public_ip=ngrok.connect(8000)
	print(public_ip)
	code=None
	while code!=200:
		  code=fetch("https://boscts.herokuapp.com/",public_ip)
		  time.sleep(3)
	server = HTTPServer(application)
	server.listen(torn.Port())
	IOLoop.current().start()

					