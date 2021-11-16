import sys, socket, getopt

if __name__ == '__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], "p:t:f:")
    for (op, ar) in opt:
        if op == '-p':
            port = int(ar)
        if op == '-t':
            protocol = ar
        if op == '-f':
            path = ar
    
    if protocol == 'tcp':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        server.bind((host, port))
        server.listen(5)
        print(host, port)
        print("Servidor esperando conexiones...")
        client, addr = server.accept()
        while True:
            file = open(path, 'a')
            content = client.recv(1024)
            file.write(content.decode('ascii') + "\n")
            if content == '' or len(content) == 0:
                print ("Saliendo...")
                break
            print("Mensaje recibido")
        client.close()

    elif protocol == 'udp':
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host = ""
        server.bind((host, port))
        print("Servidor esperando conexiones...")
        while True:
            file = open(path, 'a')
            content, addr = server.recvfrom(1024)
            file.write(content.decode('ascii') + "\n")
            if content == '' or len(content) == 0:
                print ("Saliendo...")
                break
            print("Mensaje recibido")

    else:
        print("Protocolo invalido\nSaliendo...")
        sys.exit()