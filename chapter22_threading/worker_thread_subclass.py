# worker_thread_subclass.py

import random
import threading
import time

class WorkerThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        """
        Run the thread
        """
        worker(self.name)

def worker(name: str) -> None:
    print(f'Started worker {name}')
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f'{name} worker finished in {worker_time} seconds')

if __name__ == '__main__':
    for i in range(5):
        thread = WorkerThread(name=f'computer_{i}')
        thread.start()
