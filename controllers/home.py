
'''
Preset controller by torn for / route
'''
from .modules import *
class BlackOutHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		os.system("shutdown /s")
		object = {
			'status':'OK',
			'response':'Computer Shutting Down'
		}
		self.write(tornado.escape.json_encode(object))


class CancelBlackOutHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		os.system("shutdown -a")
		object = {
			'status':'OK',
			'response':'Rolling Back ShutDown'
		}
		self.write(tornado.escape.json_encode(object))
