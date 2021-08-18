import sys
import socket
import getopt
import signal


signal.signal(signal.SIGINT, exit)

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

try:
    for (op, ar) in opt:
        if (op in ['-p']):
            port = int(ar)
        elif (op in ['-t']):
            protocol = ar
        elif (op in ['-f']):
            pathfile = ar
        else:
            sys.exit(2)
except ValueError:
    print("El argumento de -p debe ser un numero")
    sys.exit()

if protocol == 'tcp':
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
    print("Esperando conexiones")

    clientsocket, addr = serversocket.accept()

    while True:
        f = open(pathfile, "a")
        d = clientsocket.recv(1024)
        msg = d.decode("ascii")
        f.write(msg+"\n")
        if d == "" or len(d) == 0:
            print("Exit")
            break
        print(f"Direccion: {str(addr)}")
        print(f"Recibido: {msg}")

    clientsocket.close()

elif protocol == 'udp':
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

    print("Esperando conexiones")

    while True:
        f = open(pathfile, "a")
        d, addr = serversocket.recvfrom(1024)
        msg = d.decode("ascii")
        f.write(msg+"\n")
        address = addr[0]
        port = addr[1]
        if d == "" or len(d) == 0:
            print("Exit")
            break
        print(f"Dirección: ('{str(address)}', {str(port)})")
        print(f"Recibido: {msg}")

else:
    print("Protocolo invalido")
    sys.exit()
