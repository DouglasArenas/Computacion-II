from multiprocessing import Process, Pipe
import os, time


def function(r,w, nproces):
    print("Número de proceso: %d" % nproces)
    if (nproces == 2):
        print("%d: proceso %d listo y recibiendo: %s\n" % (nproces, os.getpid(), r.recv()))
        r.send("Corriendo")
    if(nproces == 1):
        w.send("Proceso %d listo y enviando" % (os.getpid()))
        print(str(nproces) + w.recv())
    r.close()
    w.close()
    print("Saliendo...")


if __name__ == "__main__":
    r, w = Pipe()
    p1 = Process(target=function, args=(r,w,1))
    p2 = Process(target=function, args=(r,w,2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

