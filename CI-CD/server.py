from flask import Flask, jsonify

server = Flask(__name__)

@server.route('/healthz')
def healthz():
	return jsonify(status="200 OK")

if __name__=='__main__':
	server.run(host='0.0.0.0', port=7777)
