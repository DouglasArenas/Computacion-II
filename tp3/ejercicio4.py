import sys
import os


def hijo():
    if os.fork() == 0:
        if os.fork() or os.fork():
            os.fork()
            print("Soy el hijo, mi pid es:", os.getpid())
            print("Pid:", os.getpid(), "terminando")
            print("---------------------------------")
            sys.exit(0)


def padre():
    print("---------------------------------------")
    print("mi hijo, pid:", os.getpid(), "termino")
    print("---------------------------------------")
    os.fork()
    print("Soy el padre, mi pid es:", os.getppid(), ", mi hijo es:", os.getpid())
    print("----------------------------------------------------------------------")


hijo()
padre()
