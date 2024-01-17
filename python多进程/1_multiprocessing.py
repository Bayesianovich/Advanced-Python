from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, name, t):
        super().__init__()
        self.name = name
        self.t = t

    def run(self):
        print(f'run {self.name} ----- running')
        time.sleep(self.t)
        print(f'run {self.name} is done {self.t} seconds')

def main():
    p1 = MyProcess('p1', 10) #wechat    
    p2 = MyProcess('p2', 8) #qq
    p3 = MyProcess('p3', 6) #bilibili
    p4 = MyProcess('p4', 12) #youtube


    ps = [p1, p2, p3, p4]

    start_time = time.time()  # get the start time
    for p in ps:
        p.start()

    for p in ps:
        p.join()

    end_time = time.time()  # get the end time

    elapsed_time = end_time - start_time  # calculate the elapsed time
    print('main process is done!')
    print(f'The program ran for {elapsed_time} seconds')

if __name__ == '__main__':
    main()