# multiple_figures.py

import matplotlib.pyplot as plt

def line_plot(numbers, numbers2):
    first_plot = plt.figure(1)
    plt.plot(numbers)

    second_plot = plt.figure(2)
    plt.plot(numbers2)
    plt.show()

if __name__ == '__main__':
    numbers = [2, 4, 1, 6]
    more_numbers = [5, 1, 10, 3]
    line_plot(numbers, more_numbers)