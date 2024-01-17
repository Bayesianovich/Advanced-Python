# 使用multiprocessing模块来创建并启动多个进程，
# 并使用锁机制防止对共享资源的同时访问。
from multiprocessing import Process, Lock
import time, os
from typing import List 

def prints(lock: Lock) -> None:
    """
    prints函数是每个进程将运行的目标函数。它接受一个Lock对象作为参数。
    调用lock.acquire()方法来设置锁。
    这将阻止下一个进程获取锁，直到当前进程释放它。
    然后，函数打印进程ID，休眠5秒，并再次打印。
    然后调用lock.release()方法来释放锁，允许下一个进程获取它。
    函数还计算并打印每个进程所花费的时间。
    """
    lock.acquire()
    start_time = time.time()  # Getting the current timestamp
    print(f'run {os.getpid()} ----- lock close')
    print(f'run {os.getpid()} is running')
    time.sleep(5)
    print(f'run {os.getpid()} is done')
    print(f'run {os.getpid()} ----- lock open')
    lock.release()
    end_time = time.time()  # Getting the current timestamp
    print(f'Process {os.getpid()} took {end_time - start_time:.2f} seconds')  # Calculating and printing the time difference

def main() -> None:
    """
    main函数创建一个Lock对象和一个空列表来保存进程。
    然后，它创建5个进程，每个进程的目标函数都是prints，并将锁作为参数。
    每个进程都被添加到列表中，并使用start方法启动。
    在列表中的每个进程上调用join方法，这将阻止主进程，直到所有进程都完成。
    函数还计算并打印所有进程所花费的总时间。
    """
    lock = Lock()
    processes = []
    start_time = time.time()  # Main process start time

    for i in range(5):
        p = Process(target=prints, args=(lock,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()  # Main process end time
    print(f'Total time taken: {end_time - start_time:.2f} seconds')
    print('Main process is done!')
if __name__ == '__main__':
    main()
