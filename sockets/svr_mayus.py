import sys
import socket
import getopt


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

try:
    for (op, ar) in opt:
        if (op in ['-p']):
            port = int(ar)
        else:
            sys.exit(2)
except ValueError:
    print("El argumento debe ser un numero")
    sys.exit()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
try:
    serversocket.bind((host, port))
except NameError:
    print("Puerto no definido")
    print("Utilice -p para definir el puerto")
    sys.exit()
except OverflowError:
    print("El puerto debe ser entre 0-65535")
    sys.exit()
except PermissionError:
    print("Permiso denegado")
    sys.exit()

serversocket.listen(5)
print("Esperando conexiones...")

clientsocket, addr = serversocket.accept()

data = clientsocket.recv(1024)
clientsocket.close()
print(f"Address: {str(addr)}")
print(f"Recibido: {data.decode('utf8').upper()}")
