from socketIO_client import SocketIO, LoggingNamespace


socketio = SocketIO('localhost', 8080, LoggingNamespace)


def pimessage(args):
    try:
        print(args["user"] + " says: " + args["message"])
    except:
        errorcode = ""


while 1:
    socketio.on('message', pimessage)
    socketio.wait(seconds=1)
