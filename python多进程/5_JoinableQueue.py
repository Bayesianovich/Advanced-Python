from multiprocessing import Process, JoinableQueue
import time, os

def consumer(queue: JoinableQueue) -> None:
    while True:
        item = queue.get()
        if item is None:  # 结束信号
            queue.task_done()
            break
        print(f'Consumer {os.getpid()} got item {item} from queue')
        time.sleep(1)  # 模拟处理时间
        queue.task_done()

def producer(queue: JoinableQueue, start: int, end: int) -> None:
    for item in range(start, end):
        print(f'Producer {os.getpid()} putting item {item} to queue')
        queue.put(item)
        time.sleep(1)  # 模拟生产时间
    queue.put(None)  # 发送结束信号

def main() -> None:
    num_producers = 2
    num_consumers = 3
    queue = JoinableQueue()

    # 创建生产者
    producers = [Process(target=producer, args=(queue, i*10, (i+1)*10)) for i in range(num_producers)]
    for p in producers:
        p.start()

    # 创建消费者
    consumers = [Process(target=consumer, args=(queue,)) for _ in range(num_consumers)]
    for c in consumers:
        c.start()

    # 等待所有生产者结束
    for p in producers:
        p.join()

    # 等待所有项目被处理
    queue.join()

    # 停止消费者
    for _ in consumers:
        queue.put(None)

    # 等待所有消费者结束
    for c in consumers:
        c.join()

    print('Main process is done!')

if __name__ == '__main__':
    main()
