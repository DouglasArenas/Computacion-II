import threading, sys, os


def hilo_escritor(w):
    print(f"Numero del hilo: {threading.current_thread()._ident}")
    w = os.fdopen(w, 'w')
    print("Ingrese mesaje: ")
    sys.stdin = open(0)
    while True:
        try:
            mensaje = input() + "\n"
            w.write(mensaje)
            w.flush()
        except EOFError:
            print("\nSaliendo...\n")
            break

def hilo_lector(r):
    r = os.fdopen(r, 'r')
    while True:
        men_recibido = r.readline()[:-1]
        if men_recibido:
            print(f"Leyendo (Hilo:{threading.current_thread()._ident}): {men_recibido}")
        else:
            break

if __name__ == "__main__":
    r, w = os.pipe()
    t1 = threading.Thread(target=hilo_escritor, args=(w,), daemon=True)
    t2 = threading.Thread(target=hilo_lector, args=(r,), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()