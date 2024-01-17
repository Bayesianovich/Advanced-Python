# 自定义线程: 继承threading.Thread类, 重写run方法
import threading, time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n
        
    def run(self):
        print("task is running", self.n)
        time.sleep(2)
        print("task done", self.n)

if __name__ == '__main__':
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t1.start()
    t2.start()
    print("main thread done....")

