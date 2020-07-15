# bar_charth.py

import matplotlib.pyplot as plt

def bar_charth(numbers, labels, pos):
    plt.barh(pos, numbers, color='blue')
    plt.yticks(ticks=pos, labels=labels)
    plt.show()

if __name__ == '__main__':
    numbers = [2, 1, 4, 6]
    labels = ['Electric', 'Solar', 'Diesel', 'Unleaded']
    pos = list(range(4))
    bar_charth(numbers, labels, pos)