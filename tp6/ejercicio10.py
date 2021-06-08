from multiprocessing import Process, Queue, current_process
import time


def hijo(i, q):
    pid = current_process().pid
    print(f"Proceso {i}, PID={pid}")
    time.sleep(i)
    q.put(f"{pid}\t")


if __name__ == "__main__":
    q = Queue()
    p = []

    for h in range(10):
        i = h + 1
        p.append(Process(target=hijo, args=(i, q)))
        p[h].start()
        p[h].join()

    while not q.empty():
        print(q.get(), end='')
