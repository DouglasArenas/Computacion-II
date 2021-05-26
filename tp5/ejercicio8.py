import os
import time
import signal

def handler_padre(s, f):
    print(f"A (PID={os.getpid()}) leyendo:")
    while True:
        line = r.readline()
        if line:
            print(line)
        else:
            break

def handler_hijo(s, f):
    w.write(f"Mensaje 1 (PID={os.getpid()})\n")
    w.flush()
    os.kill(nieto, signal.SIGUSR1)

def handler_nieto(s, f):
    w.write(f"Mensaje 2 (PID={os.getpid()})\n")
    w.flush()
    os.kill(padre, signal.SIGUSR2)

padre = os.getpid()
r, w = os.pipe()
hijo = os.fork()
if hijo != 0:
    os.close(w)
    r = os.fdopen(r)
    signal.signal(signal.SIGUSR2, handler_padre)
    time.sleep(1)
    os.kill(hijo, signal.SIGUSR1)
else:
    nieto = os.fork()
    if nieto != 0:
        os.close(r)
        w = os.fdopen(w, 'w')
        signal.signal(signal.SIGUSR1, handler_hijo)
    else:
        os.close(r)
        w = os.fdopen(w, 'w')
        signal.signal(signal.SIGUSR1, handler_nieto)

signal.pause()
