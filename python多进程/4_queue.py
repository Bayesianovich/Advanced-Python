from multiprocessing import Process, Queue

def producer(queue):
    for i in range(10):
        queue.put(i)
        print(f'Producer added task {i} to queue')
    queue.put(None)  # Send end signal

def consumer(queue):
    while True:
        task = queue.get()
        if task is None:  # Check for end signal
            break
        print(f'Consumer got task {task} from queue')

def main():
    queue = Queue()
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('Main process is done!')

if __name__ == '__main__':
    main()