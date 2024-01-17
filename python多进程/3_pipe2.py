from multiprocessing import Process, Pipe
import time

class Consumer(Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe
    
    def run(self):
        self.pipe.send('Consumer: Hello!')
        time.sleep(3)
        print(f"consumer received:",self.pipe.recv())


class Producer(Process):
    def __init__(self, pipe):
        super().__init__()
        self.pipe = pipe
    
    def run(self):
        print(f"producer received:",self.pipe.recv())
        time.sleep(6)
        self.pipe.send('Producer: Hello too!')

# def main():
    # start_time = time.time()  
    # parent_conn, child_conn = Pipe()
    # p1 = Producer(child_conn)
    # p2 = Consumer(parent_conn)
    # p1.daemon = p2.daemon = True
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # end_time = time.time()
    # print(f'Total time taken: {end_time - start_time:.2f} seconds')
    # print('Main process is done!')


if __name__ == '__main__':
    start_time = time.time()  
    parent_conn, child_conn = Pipe()
    p1 = Producer(child_conn)
    p2 = Consumer(parent_conn)
    p1.daemon = p2.daemon = True
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()
    print(f'Total time taken: {end_time - start_time:.2f} seconds')
    print('Main process is done!')