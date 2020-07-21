# pie_chart_plain.py

import matplotlib.pyplot as plt

def pie_chart():
    numbers = [40, 35, 15, 10]
    labels = ['Python', 'Ruby', 'C++', 'PHP']

    fig1, ax1 = plt.subplots()
    ax1.pie(numbers, labels=labels)
    plt.show()

if __name__ == '__main__':
    pie_chart()