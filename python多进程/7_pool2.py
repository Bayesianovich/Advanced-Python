from multiprocessing import Pool
import time, os

def worker(i):
    print(f"Worker {i} is working...")
    time.sleep(1)
    print(f"Worker {i} finished.")
    return i ** 2

def main():
    pool = Pool(4)
    start_time = time.time()  # Main process start time

    results = []
    for i in range(10):
        result = pool.apply_async(worker, args=(i,))
        results.append(result)

    pool.close()
    pool.join()
    print(results)

    end_time = time.time()  # Main process end time
    print(f'Total time taken: {end_time - start_time:.2f} seconds')


if __name__ == '__main__':
    main()