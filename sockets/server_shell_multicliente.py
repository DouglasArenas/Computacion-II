import socket, subprocess, multiprocessing


def child(client):
    socket, addr = client
    while True:
        content = clientsocket.recv(1024)
        content = content.decode("ascii")
        if len(content) == 0:
            print("Cliente %s desconectado" % str(addr))
            break
        print("Mensaje recibido de %s" % str(addr))
        command = subprocess.Popen([content], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = command.communicate()
        if command.returncode == 0:
            ans = "OK \n"+stdout
        else:
            ans = "ERROR \n"+stderr

        clientsocket.send(ans.encode('ascii'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = ""
port = 1234
server.bind((host, port))
server.listen(5)
print("Servidor esperando conexiones...")

while True:
    cliente = server.accept()
    clientsocket, addr = cliente
    print("Cliente %s conectado" % str(addr) )
    process = multiprocessing.Process(target=child, args=(cliente,))
    process.start()