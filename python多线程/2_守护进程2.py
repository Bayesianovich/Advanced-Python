import threading,time 

def run(n,t):
    print("task is running",n)
    time.sleep(t)
    print("task done",n)

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=("t1",12))
    t2 = threading.Thread(target=run,args=("t2",2))
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main thread done....")