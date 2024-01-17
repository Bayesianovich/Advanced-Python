from concurrent.futures import ThreadPoolExecutor

def worker(x):
    return x * x

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(worker, x) for x in range(10)}
        for future in futures:
            print(future.result())