# 主进程结束，守护进程也会结束
import threading, time

def run(n, t):
    print("task is running", n)
    time.sleep(t)
    print("task done", n)

if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=("t1", 12))
    t2 = threading.Thread(target=run, args=("t2", 2))
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()
    print("main thread done....")