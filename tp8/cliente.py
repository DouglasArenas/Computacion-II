import sys
import socket
import getopt

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:t:', [])
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

try:
    for (op, ar) in opt:
        if (op in ['-a']):
            host = ar
        elif (op in ['-p']):
            port = int(ar)
        elif (op in ['-t']):
            protocol = ar
        else:
            sys.exit(2)
except ValueError:
    print("El argumento de -p debe ser un numero")
    sys.exit()

if protocol == 'tcp':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("No se pudo crear el socket")
        sys.exit()

    try:
        s.connect((host, port))
    except NameError:
        print("Dirección ip y/o puerto no definido")
        print("Utilice -a para definir la dirección ip")
        print("Utilice -p para definir el puerto")
        sys.exit()
    except ConnectionRefusedError:
        print("Conexion rechazada")
        sys.exit()
    except OverflowError:
        print("El puerto debe ser entre 0-65535")
        sys.exit()
    except socket.error:
        print("Fallo temporal en la resolución de nombres")
        sys.exit()

    while True:
        try:
            msg = input("Ingrese mensaje para enviar: ")
            s.send(msg.encode('ascii'))
        except EOFError:
            s.close()
            break
        except BrokenPipeError:
            print("Servidor desconectado")
            s.close()
            sys.exit()
elif protocol == 'udp':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("No se pudo crear el socket")
        sys.exit()

    while(1):
        try:
            msg = input("Ingrese mensaje para enviar: ").encode()
            s.sendto(msg, (host, port))
        except NameError:
            print("Dirección ip y/o puerto no definido")
            print("Utilice -a para definir la dirección ip")
            print("Utilice -p para definir el puerto")
            sys.exit()
        except EOFError:
            s.sendto("".encode(), (host, port))
            s.close()
            break
        except socket.error:
            print("Error: " + str(msg[0]) + " Mensaje " + msg[1])
            sys.exit()

else:
    print("Protocolo invalido")
    sys.exit()
