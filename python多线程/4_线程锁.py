from threading import Lock, Thread
import time

n = 0
lock = Lock()

def add():
    global n, lock
    for _ in range(1000000):
        lock.acquire()
        n += 1
        lock.release()

def sub():
    global n, lock
    for _ in range(1000000):
        lock.acquire()
        n -= 1
        lock.release()

if __name__ == '__main__':
    thread_add = Thread(target=add)
    thread_sub = Thread(target=sub)
    thread_add.start()
    thread_sub.start()
    thread_add.join()
    thread_sub.join()
    print('n = ', n,flush=True)