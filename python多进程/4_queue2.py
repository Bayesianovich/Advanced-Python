from multiprocessing import Process, Queue
import time
from typing import List

def write_process(queue: Queue) -> None:
    """
    write_process函数是第一个进程的目标函数。
    它接受一个Queue对象作为参数。
    然后，它将字符串“hello”写入队列，休眠1秒，然后再次写入队列。
    """
    queue.put('hello')
    time.sleep(1)
    queue.put('world')


def read_process(queue: Queue) -> None:
    """
    read_process函数是第二个进程的目标函数。
    它接受一个Queue对象作为参数。
    然后，它从队列中读取两个字符串，并将它们打印到控制台。
    """
    val1 = queue.get()
    print(val1)
    val2 = queue.get()
    print(val2)


def main() -> None:
    """
    main函数创建一个Queue对象和两个进程。
    然后，它将队列作为参数传递给两个进程。
    然后，它启动两个进程，并使用join方法阻止主进程，直到两个进程都完成。
    """
    start_time = time.time()
    queue = Queue()
    p1 = Process(target=write_process, args=(queue,))
    p2 = Process(target=read_process, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'The program ran for {elapsed_time:.2f} seconds')
    print('Main process is done!')


if __name__ == '__main__':
    main()