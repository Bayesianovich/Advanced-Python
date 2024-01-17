import threading
import time

produced = threading.Semaphore(4)

def worker(i):
    produced.acquire()
    print("worker",i)
    time.sleep(1)
    produced.release()

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=worker,args=(i,))
        t.start()
        t.join()
    print("main thread done....")