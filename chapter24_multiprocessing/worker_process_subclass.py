# worker_thread_subclass.py

import random
import multiprocessing
import time

class WorkerProcess(multiprocessing.Process):

    def __init__(self, name):
        multiprocessing.Process.__init__(self)
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
    processes = []
    for i in range(5):
        process = WorkerProcess(name=f'computer_{i}')
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
