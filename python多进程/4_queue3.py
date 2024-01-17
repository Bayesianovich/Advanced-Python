from multiprocessing import Process, Queue
import time, os 

def consumer(queue: Queue) -> None:  # Corrected function name
    while True:
        res = queue.get()
        if res is None:  # Check for end signal
            break
        time.sleep(3)
        print(f'consumer {os.getpid()} get {res} from queue')

def producer(queue: Queue) -> None:
    for i in range(10):
        time.sleep(2)
        res = f"box{i}"  # Using f-string for string formatting
        queue.put(res)
        print(f'producer {os.getpid()} put {res} to queue')
    queue.put(None)  # Sending end signal

def main() -> None:
    queue = Queue()
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))  # Corrected function name
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Main process is done!')

if __name__ == '__main__':
    main()