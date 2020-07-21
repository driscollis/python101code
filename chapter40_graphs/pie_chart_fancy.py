# pie_chart.py

import matplotlib.pyplot as plt

def pie_chart():
    numbers = [40, 35, 15, 10]
    labels = ['Python', 'Ruby', 'C++', 'PHP']
    # Explode the first slice (Python)
    explode = (0.1, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(numbers, explode=explode, labels=labels,
            shadow=True, startangle=90,
            autopct='%1.1f%%')
    ax1.axis('equal')
    plt.show()

if __name__ == '__main__':
    pie_chart()