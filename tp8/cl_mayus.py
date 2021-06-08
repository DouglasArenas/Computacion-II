import sys
import socket
import getopt


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

try:
    for (op, ar) in opt:
        if (op in ['-a']):
            host = ar
        elif (op in ['-p']):
            port = int(ar)
        else:
            sys.exit(2)
except ValueError:
    print("El argumento de -p debe ser un numero")
    sys.exit()

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

msg = input("Introduzca una cadena de texto: ")
s.send(msg.encode('utf8'))
s.close()
