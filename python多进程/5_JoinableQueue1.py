from multiprocessing import Process, JoinableQueue
import time, os

def consumer(queue: JoinableQueue, tim: int) -> None:
    while True:
        item = queue.get()
        if item is None:  # 结束信号
            queue.task_done()
            break
        print(f'Consumer {os.getpid()} got item {item} from queue')
        time.sleep(tim)  # 模拟处理时间
        queue.task_done()

def producer(queue: JoinableQueue, start: int, end: int, tim: int) -> None:
    for item in range(start, end):
        time.sleep(tim)  # 模拟生产时间
        print(f'Producer {os.getpid()} putting item {item} to queue')
        queue.put(item)

def main() -> None:
    num_consumers = 3
    queue = JoinableQueue()
    p1 = Process(target=producer, args=(queue, 0, 10, 4))
    p2 = Process(target=producer, args=(queue, 10, 20, 3))
    c1 = Process(target=consumer, args=(queue, 4))
    c2 = Process(target=consumer, args=(queue, 3))
    c3 = Process(target=consumer, args=(queue, 2))

    c1.daemon = c2.daemon = c3.daemon = True

    ps = [p1, p2]
    cs = [c1, c2, c3]

    for p in ps:
        p.start()

    for c in cs:
        c.start()

    for p in ps:
        p.join()

    # 等待队列中的所有项目都被处理
    queue.join()

    # 发送结束信号给消费者
    for _ in range(num_consumers):
        queue.put(None)

    # 等待所有消费者结束
    for c in cs:
        c.join()

    print('Main process is done!')

if __name__ == '__main__':
    main()