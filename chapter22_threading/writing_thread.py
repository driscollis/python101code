# writing_thread.py

import random
import time
from threading import Thread


class WritingThread(Thread):

    def __init__(self, filename: str, number_of_lines: int,
                 work_time: int = 1) -> None:
        Thread.__init__(self)
        self.filename = filename
        self.number_of_lines = number_of_lines
        self.work_time = work_time

    def run(self) -> None:
        """
        Run the thread
        """
        print(f'Writing {self.number_of_lines} lines of text to '
              f'{self.filename}')
        with open(self.filename, 'w') as f:
            for line in range(self.number_of_lines):
                text = f'This is line {line+1}\n'
                f.write(text)
                time.sleep(self.work_time)
        print(f'Finished writing {self.filename}')

if __name__ == '__main__':
    files = [f'test{x}.txt' for x in range(1, 6)]
    for filename in files:
        work_time = random.choice(range(1, 3))
        number_of_lines = random.choice(range(5, 20))
        thread = WritingThread(filename, number_of_lines, work_time)
        thread.start()