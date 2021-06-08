from multiprocessing import Process, Pipe, current_process
import sys


def receptor(conn):
    print("Capturando entrada, utilice Ctrl + D para salir")
    print("Ingrese lineas de texto:\n")
    sys.stdin = open(0)
    while True:
        try:
            line = input()
            conn.send(line)
        except EOFError:
            print("Exit")
            break


def lector(conn):
    hijo = current_process().pid
    while True:
        line = conn.recv()
        print(f"Leyendo (PID={hijo}): {line}")


if __name__ == "__main__":
    a, b = Pipe()
    p1 = Process(target=receptor, args=(a,))
    p2 = Process(target=lector, args=(b,))
    p1.start()
    p2.start()
    p1.join()
    p2.kill()
