import sys
import socket
import getopt
from datetime import datetime


def log_file(logfile):
    command = (fecha+": \""+msg+"\"\n")
    logf = open(logfile, "a")
    logf.writelines(command)


try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'l:', [])
    
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

logfile = 0
for (op, ar) in opt:
    if (op == '-l'):
        logfile = ar

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 9009

try:
    s.connect((host, port))

except ConnectionRefusedError:
    print("Conexión rechazada")
    sys.exit()

while True:
    fecha = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    try:
        msg = input("> ")
        if msg == "":
            pass
        else:
            if logfile != 0:
                log_file(logfile)
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