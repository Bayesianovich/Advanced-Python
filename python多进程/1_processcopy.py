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

    p1.daemon = True
    p2.daemon = True
    p3.daemon = True
    p4.daemon = True
    p5.daemon = True
    p6.daemon = True
    for p in ps:
        p.start()

# 守护进程会在主进程代码执行结束后就终止运行

    end_time = time.time()  # get the end time
    elapsed_time = end_time - start_time  # calculate the elapsed time
    print('main process is done!')
    print(f'The program ran for {elapsed_time} seconds')

if __name__ == '__main__':
    main()