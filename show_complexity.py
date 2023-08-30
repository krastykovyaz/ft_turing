
from ft_turing import ft_turing
import matplotlib.pyplot as plt
from notation_image import Notation

def find_complexity():

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x_coords = [x for x in range(1, 101)]
    notation = Notation(ax, x_coords)
    notation.plot_notations()

    formula = [lambda x: f"{x * '1'}-{x * '1'}=",
               lambda x: f"{x * '1'}-1=",
               lambda x: f"{x * '1'}+{x * '1'}=",
               lambda x: f"1{x * '0'}1",
               lambda x: f"{x * '0'}1{x * '0'}",
               lambda x: f"{x * '0'}{x * '1'}",
               lambda x: f"{x * '0'}"
               ]
    machines = []
    for i, machine in enumerate(['unary_sub', 'unary_sub', 'unary_add','palindrome','palindrome',
                                 'equal','is_pair']):
        y_coords = []
        for coord in x_coords:
            turing =  ft_turing(f"machines/{machine}.json", formula[i](coord), mode="sample")
            y_coords.append(turing)
            if y_coords[-1:][0] > 1000:
                for _ in range(coord, 100):
                    y_coords.append(y_coords[-1:][0])
                break
        if machine in machines:
            machine += '2'
        ax.plot(x_coords, y_coords, "--", color=notation.colors[len(formula):][i], label=machine)
        machines.append(machine)
    ax.set_xlabel('Elements')
    ax.set_xlim([0, 100])
    ax.set_ylabel('Operations')
    ax.set_ylim([0, 1000])
    ax.set_title('Big-O Complexity')
    plt.legend(loc='upper right')
    plt.grid(axis='y')
    plt.show()



if __name__ == "__main__":
    find_complexity()

