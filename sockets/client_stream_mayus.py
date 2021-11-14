import sys, socket, getopt


(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')
for (op, ar) in opt:
    if op == '-a':
        host = (ar)
    if op == '-p':
        port = int(ar)

socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socketclient.connect((host, port))
except OSError:
    print("Host o puerto invalido (defaul host = 0)\nSaliendo...")
    sys.exit(1)
mensaje = input("Introduzca una cadena de texto: ")
socketclient.send(mensaje.encode('utf8'))
socketclient.close()