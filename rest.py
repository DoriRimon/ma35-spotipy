from core.engine import Engine

from flask import Flask, request
app = Flask(__name__)

class SpotipyRest:
	def __init__(self):
		self.engine = Engine()

	@app.route("/login", methods=["GET"])
	def login(self):
		user_name = request.args.get("username")
		password = request.args.get("password")
		self.engine.login(user_name, password)
