import random as rand
import numpy as np
import matplotlib.pyplot as plt


#  Numpy functional style usage
def calc_square(arr):
    return np.square(arr)


def calc_sqrt(arr):
    return np.sqrt(arr)


def calc_mean(arr):
    return np.mean(arr)


my_arr = np.array([49, 81, 100])

squared_values = calc_square(my_arr)
print("Array squared:", squared_values)

sqrt_values = calc_sqrt(my_arr)
print("Array square rooted:", sqrt_values)

mean_value = calc_mean(my_arr)
print("Array mean:", mean_value)

#  Matplotlib OOP usage


class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_line(self, x_label='X', y_label='Y', title='Linear'):
        plt.plot(self.data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def plot_histogram(self, bins=10, x_label='Amount', y_label='Frequency', title='Histogram'):
        plt.hist(self.data, bins=bins)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def plot_scatter(self, x_label='X', y_label='Y', title='Spot'):
        plt.scatter(range(len(self.data)), self.data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()


my_data = rand.sample(range(100), 15)

visualizer = DataVisualizer(my_data)

visualizer.plot_line(x_label='Index', y_label='Amount', title='Linear')
visualizer.plot_histogram(bins=20, x_label='Amount', y_label='Frequency', title='Histogram')
visualizer.plot_scatter(x_label='Index', y_label='Amount', title='Spot')
