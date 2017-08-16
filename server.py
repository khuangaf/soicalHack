from __future__ import print_function
from flask import Flask, render_template,request
from flask_socketio import SocketIO
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from flask_socketio import send, emit
from os import environ
from flask import Flask
import json
from data_preprocess import *



@socketio.on('calculateFinalScore')
def calculate(organization):
	# get input from user
	organization = json.dumps(organization, ensure_ascii=False).encode('utf8')[1:-1]
	topList = calculateFinalScore(organization).head(50)
	returnList = {'name':list(topList.index), 'score':list(topList['score'])}
	socketio.emit('returnScore', returnList)

@app.route('/')
def index():
	return render_template("index.html")
if __name__ == '__main__':
	HOST = environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(environ.get('PORT','5000'))
	except ValueError:
		PORT = 5000
	print ("listening on port "+ str(PORT))
	socketio.run(app, port =  PORT, host= '0.0.0.0')
