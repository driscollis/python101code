# profile_test.py

import time

def quick():
    print('Running quick')
    return 1 + 1

def average():
    print('Running average')
    time.sleep(0.5)

def super_slow():
    print('Running super slowly')
    time.sleep(2)

def main():
    quick()
    super_slow()
    quick()
    average()

if __name__ == '__main__':
    main()