import matplotlib.pyplot as plt
import numpy as np


def histogram_function(rand_vars):
    plt.hist(rand_vars, bins = np.arange(len(set(rand_vars)))-0.5, edgecolor = "black")
    plt.xticks(list(range(rand_vars.max())))
    plt.show()