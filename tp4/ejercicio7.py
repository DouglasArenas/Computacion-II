import os
import getopt
import sys
import signal
import time

def handler_hijo(s, f):
    print(f"Soy el PID: {os.getpid()}, recibí la señal {s} de mi padre PID {os.getppid()}")
    os._exit(0)


def padre(hijos):
    signal.signal(signal.SIGUSR2, signal.SIG_IGN)
    for i in range(hijos):
        ret = os.fork()
        if ret == 0:
            signal.signal(signal.SIGUSR2, handler_hijo)
            signal.pause()
        else:
            print("Creando el proceso:", ret)
            time.sleep(0.1)
            os.kill(ret, signal.SIGUSR2)

hijos = 0

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['process='])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

try:
    for (op, ar) in opt:
        if (op in ['-p', '--process']):
            if (hijos == 0):
                hijos = int(ar)
            else:
                sys.exit(2)
except ValueError:
    print("El argumento debe ser un numero decimal")
    sys.exit()

padre(hijos)
