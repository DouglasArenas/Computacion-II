from threading import Thread, current_thread
import sys
import os


def receptor(w):
    print(f"HILO receptor: {current_thread()._ident}")
    w = os.fdopen(w, 'w')
    print("Capturando entrada, utilice Ctrl + D para salir")
    print("Ingrese lineas de texto:\n")
    sys.stdin = open(0)
    while True:
        try:
            line = input() + "\n"
            w.write(line)
            w.flush()
        except EOFError:
            print("Exit")
            break


def lector(r):
    hilo = current_thread()._ident
    r = os.fdopen(r, 'r')
    while True:
        line = r.readline()[:-1]
        if line:
            print(f"Leyendo (HILO={hilo}): {line}")
        else:
            break


if __name__ == "__main__":
    print(f"MAIN: {current_thread()._ident}")
    r, w = os.pipe()
    h1 = Thread(target=receptor, args=(w,), daemon=True)
    h2 = Thread(target=lector, args=(r,), daemon=True)
    h1.start()
    h2.start()
    h1.join()
    h2.join()
