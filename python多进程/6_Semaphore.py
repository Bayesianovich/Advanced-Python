from multiprocessing import Process, Semaphore
import time

def worker(s, i):
    s.acquire()
    print(f"Worker {i} is working...")
    time.sleep(1)
    print(f"Worker {i} finished.")
    s.release()

if __name__ == "__main__":
    sem = Semaphore(4)  # 最多允许4个进程同时运行

    processes = []
    for i in range(12):
        p = Process(target=worker, args=(sem, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()