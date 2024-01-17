from multiprocessing import Pool
import time, os


def worker(i):
    print(f"Worker {i} is working...")
    time.sleep(1)
    print(f"Worker {i} finished.")
    return i ** 2


def main():
    pool = Pool(4)  # 最多允许4个进程同时运行
    start_time = time.time()  # Main process start time
    results = []
    for i in range(10):
        result = pool.apply(worker, args=(i,))
        results.append(result)

    pool.close()
    pool.join()
    print(results)

    end_time = time.time()  # Main process end time
    print(f'Total time taken: {end_time - start_time:.2f} seconds')
    print('Main process is done!')

if __name__ == '__main__':
    main()