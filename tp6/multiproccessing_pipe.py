from multiprocessing import Process, Pipe
import sys, os

def hijo_lector(r):
    while True:
        men_recibido = r.recv()
        print(f"Leyendo (pid:{os.getpid()}): {men_recibido}")

def hijo_escritor(w):
    sys.stdin = open(0)
    print("Ingrese mensaje: ")
    while True:
        mensaje = input()
        w.send(mensaje)


if __name__ == "__main__":
    r, w = Pipe()
    p1 = Process(target=hijo_lector, args=(r,))
    p2 = Process(target=hijo_escritor, args=(w,))
    p1.start()
    p2.start()