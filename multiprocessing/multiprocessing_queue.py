import multiprocessing as mp
import os, time

def child(t, q):
    pid = os.getpid()
    print(f"Hijo {t}, PID={pid},")
    time.sleep(t)
    q.put(f"PID hijo: {pid}\t")


if __name__ == "__main__":
    q = mp.Queue()
    list_process = []
    print("Padre creando hijos... :v")
    for h in range(10):
        t = h + 1
        list_process.append(mp.Process(target=child, args=(t, q)))
        list_process[h].start()
        list_process[h].join()
    while not q.empty():
        print(q.get(), end='\n')
