from multiprocessing import Process, Pipe, Manager
import time
from typing import List

def producer(shared_task_queue: List[int], conn: Pipe) -> None:
    for i in range(10):
        shared_task_queue.append(i)
        conn.send(i)
        print(f'Producer added task {i} to queue')
        time.sleep(0.5)

def consumer(shared_task_queue: List[int], conn: Pipe) -> None:
    while True:
        task = conn.recv()
        print(f'Consumer got task {task} from queue')
        shared_task_queue.remove(task)
        time.sleep(0.5)
        if not shared_task_queue:  # 如果共享任务队列为空，退出循环
            break

def main() -> None:
    manager = Manager()
    shared_task_queue = manager.list()  # 创建一个Manager List
    parent_conn, child_conn = Pipe()

    p1 = Process(target=producer, args=(shared_task_queue, parent_conn))
    p2 = Process(target=consumer, args=(shared_task_queue, child_conn))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('Main process is done!')

if __name__ == '__main__':
    main()