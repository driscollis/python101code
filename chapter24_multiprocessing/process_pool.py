import random
import time

from multiprocessing import Pool


def worker(name: str) -> None:
    print(f'Started worker {name}')
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f'{name} worker finished in {worker_time} seconds')

if __name__ == '__main__':
    process_names = [f'computer_{i}' for i in range(15)]
    pool = Pool(processes=5)
    pool.map(worker, process_names)
    #pool.terminate()