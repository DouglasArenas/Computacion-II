import sys, socket, getopt

def command(resp):
    if resp == "200":
        print(f"{resp}: OK")
    elif resp == "400":
        print(f"{resp}: Comando válido, pero fuera de secuencia")
    elif resp == "404":
        print(f"{resp}: Clave errónea")
    elif resp == "405":
        print(f"{resp}: Cadena nula")
    elif resp == "500":
        print(f"{resp}: Comando inválido")


if __name__ == '__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], "h:p:", [])
    for (op, ar) in opt:
        if op == "-h":
            host = ar
        elif op == "-p":
            port = int(ar)
        else:
            sys.exit(1)
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))


    while True:
        name = input('Ingrese su nombre: ')
        msg = 'hello|' + name
        clientsocket.send(msg.encode('ascii'))
        datos = clientsocket.recv(512).decode("ascii")
        command(datos)
        if datos == '200':
            while True:
                email = input('Ingrese su email: ')
                msg = 'email|' + email
                clientsocket.send(msg.encode('ascii'))
                datos = clientsocket.recv(512).decode('ascii')
                command(datos)
                if datos == '200':
                    while True:
                        key = str(input('Ingrese la clave: '))
                        msg = 'key|' + str(key)
                        clientsocket.send(msg.encode('ascii'))
                        datos = clientsocket.recv(512).decode('ascii')
                        command(datos)
                        if datos == '200':
                            msg = 'exit'
                            clientsocket.send(msg.encode('ascii'))
                            data = clientsocket.recv(512).decode('ascii')
                            command(datos)
                            if datos == '200':
                                print('Cerrando conexión...')
                                clientsocket.close()
                                sys.exit(0)