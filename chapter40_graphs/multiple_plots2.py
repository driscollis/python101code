# multiple_plots2.py

import matplotlib.pyplot as plt

def multiple_plots():
    numbers = [2, 4, 1, 6]
    more_numbers = [5, 1, 10, 3]
    fig, axs = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(numbers)
    axs[1].plot(more_numbers)
    plt.show()

if __name__ == '__main__':
    multiple_plots()