import sys, socket, getopt

if __name__ == '__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], "a:p:t:")
    for op, ar in opt:
        if op == "-a":
            host = str(ar)
        if op == "-p":
            port = int(ar)
        if op == "-t":
            protocol = str(ar)
    
    if protocol == "tcp":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        while True:
            try:
                content = input("Ingrese contenido: ")
                client.send(content.encode('ascii'))
            except EOFError:
                print("Saliendo...")
                client.close()
                sys.exit()
    
    elif protocol == "udp":
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                content = input("Ingrese contenido: ")
                client.sendto(content.encode('ascii'), (host, port))
            except EOFError:
                client.sendto("".encode('ascii'), (host, port))
                print("Saliendo...")
                client.close()
                sys.exit()