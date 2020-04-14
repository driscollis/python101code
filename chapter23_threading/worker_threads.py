# worker_threads.py

import random
import threading
import time


def worker(name: str) -> None:
    print(f'Started worker {name}')
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f'{name} worker finished in {worker_time} seconds')

if __name__ == '__main__':
    for i in range(5):
        thread = threading.Thread(target=worker,
                                  args=(f'computer_{i}',))
        thread.start()
