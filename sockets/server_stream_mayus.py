import getopt, socket, sys

(opt, arg) = getopt.getopt(sys.argv[1:], "p:")
for (op, ar) in opt:
    if op == '-p':
        port = int(ar)
    else:
        print("Opcion invalida")


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
ss.bind((host, port))
ss.listen(5)
print(f"Host: {host}, puerto: {port}")
print("Esperando conexiones...")
clientsocket, addr = ss.accept()

data = clientsocket.recv(1024)
clientsocket.close()
print(f"Address: {str(addr)}")
print(f"Recibido: {data.decode('utf8').upper()}")
print("Cerrando servidor...")