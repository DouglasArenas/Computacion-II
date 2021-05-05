import os

procesos = int(input("Ingrese la cantidad de procesos hijos que va a generar:"))


def hijo():
    if os.fork() == 0:
        print("Soy el Proceso:", os.getpid(), ",Mi Padre es:", os.getppid())


for i in range(procesos):
    hijo()
