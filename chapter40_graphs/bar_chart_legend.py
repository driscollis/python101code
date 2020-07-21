# bar_chart_legend.py

import matplotlib.pyplot as plt

def bar_chart(numbers, labels, pos):
    plt.bar(pos, [4, 5, 6, 3], color='green')
    plt.bar(pos, numbers, color='blue')
    plt.xticks(ticks=pos, labels=labels)
    plt.xlabel('Vehicle Types')
    plt.ylabel('Number of Vehicles')
    plt.title('Gas Used in Various Vehicles')
    plt.legend(['First Label', 'Second Label'],
               loc='upper left')
    plt.show()

if __name__ == '__main__':
    numbers = [2, 1, 4, 6]
    labels = ['Electric', 'Solar', 'Diesel', 'Unleaded']
    pos = list(range(4))
    bar_chart(numbers, labels, pos)