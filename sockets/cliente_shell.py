import sys, socket, getopt, datetime


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 1234
client.connect((host, port))
print("Conectado\nIngrese un comando")
command = ""

while command != "exit":
    command = input(">")
    client.send(command.encode("ascii"))
    answer = client.recv(1024).decode("ascii")
    print(answer)
    (opt, arg) = getopt.getopt(sys.argv[1:], "l:")
    for op, ar in opt:
        if op == "-l":
            date = datetime.datetime.today()
            path = str(ar)
            file = open(path, "a")
            file.writelines(date + "\t" + command + "\n")            