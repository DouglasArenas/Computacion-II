import os
import signal
import time


def handler_padre(signum, frame):
    os.kill(h2, signal.SIGUSR1)


def handler_hijo(signum, frame):
    print("Soy el proceso hijo2 con PID=%d: PONG" % os.getpid())


ret = os.fork()

if ret == 0:
    time.sleep(0.1)
    for i in range(10):
        print("Soy el proceso hijo1 con PID=%d: PING" % os.getpid())
        os.kill(os.getppid(), signal.SIGUSR1)
        time.sleep(5)
else:
    signal.signal(signal.SIGUSR1, handler_padre)
    h2 = os.fork()
    if h2 == 0:
        signal.signal(signal.SIGUSR1, handler_hijo)
for i in range(10):
    signal.pause()
