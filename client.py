from socketIO_client import SocketIO, LoggingNamespace

user = ''
print("Enter your username: ", end='')
user = input()
userMsg = ""


def on_connect():
    socketio.send({"user": user})
    print("Connected!")


def pimessage(args):
    print(args)


socketio = SocketIO('localhost', 8080, LoggingNamespace)
socketio.on("connect", on_connect())
while 1:
    print("Your Message: ", end='')
    userMsg = input()
    socketio.emit("pimessage", {"message": userMsg, "user": user})

# socketio.on("message", pimessage)
# socketio.wait(seconds=1)



