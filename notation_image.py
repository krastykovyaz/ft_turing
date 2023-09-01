"""module for create plots for other notations"""
import settings as config
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

class Notation:
    """
    init coordinates, colors
    """
    def __init__(self, ax, x_coords):
        self.ax = ax
        self.x_coords = x_coords
        self.colors = list(mcolors.CSS4_COLORS.keys())
        random.shuffle(self.colors)
        
    def plot_notations(self):
        """
        function for cycle over notations
        """
        for i, notation in enumerate(config.COLOR_NOTATION):
            self.ax.plot(self.x_coords, \
                         config.COLOR_NOTATION[notation](self.x_coords), \
                         color=self.colors[i], \
                         label=notation)


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x_coords = [x for x in range(1, 101)]
    note = Notation(ax, x_coords)
    note.plot_notations()
    ax.set_xlabel('Elements')
    ax.set_xlim([0, 100])
    ax.set_ylabel('Operations')
    ax.set_ylim([0, 1000])
    ax.set_title('Big-O Complexity')
    plt.legend(loc='upper right')
    plt.grid(axis='y')
    plt.show()

