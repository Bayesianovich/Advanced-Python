from threading import Thread
import time

counter = 0

def worker():
    global counter
    counter += 1
    print("counter:",counter)
    time.sleep(1)

if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("final counter:",counter)


    
