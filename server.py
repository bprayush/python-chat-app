from flask import Flask
from flask_socketio import SocketIO, send


app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on("connect")
def on_connect():
    print("Connected!")


@socketio.on("message")
def on_message(msg):
    print("User: ", end='')
    print(msg['user'])


@socketio.on("pimessage")
def on_pimessage(msg):
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True)
