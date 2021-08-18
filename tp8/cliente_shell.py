import sys
import socket
import getopt

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:t:', [])
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 6000

try:
    s.connect((host,port))
except ConnectionRefusedError:
    print("Conexión rechazada")
    sys.exit()

while True:
    try:
        msg = input("> ")
        if msg == "":
            pass
        else:
            s.send(msg.encode('utf8'))
            data = s.recv(1024).decode('utf8')
            print(data)
            if msg == 'exit':
                print("Saliendo...")
                s.close()
                break
    except EOFError:
        s.close()
        break
