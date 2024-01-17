from multiprocessing import Process
import time

def run(name, t):
    print(f'run {name} ----- running')
    time.sleep(t)
    print(f'run {name} is done {t} seconds')

def main():
    p1 = Process(target=run, args=('p1', 10)) #wechat
    p2 = Process(target=run, args=('p2', 8)) #qq
    p3 = Process(target=run, args=('p3', 6)) #bilibili
    p4 = Process(target=run, args=('p4', 12)) #youtube
    p5 = Process(target=run, args=('p5', 8)) #facebook
    p6 = Process(target=run, args=('p6', 6)) #twitter

    ps = [p1, p2, p3, p4, p5, p6]
    start_time = time.time()  # get the start time
    for p in ps:
        p.start()

    for p in ps:
        p.join()

# 在代码中，p.join()被用于确保所有子进程（p1, p2, p3, p4, p5, p6）都完成执行后，
# 主进程才会继续执行并打印出程序运行的总时间。
# 如果没有p.join()，主进程可能会在子进程完成之前就打印出程序运行的总时间，这将导致打印出的时间不准确。
    end_time = time.time()  # get the end time
    elapsed_time = end_time - start_time  # calculate the elapsed time
    print('main process is done!')
    print(f'The program ran for {elapsed_time} seconds')

if __name__ == '__main__':
    main()