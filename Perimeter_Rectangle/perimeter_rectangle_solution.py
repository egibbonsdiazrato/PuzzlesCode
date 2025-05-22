import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # Plot parameters
    c_vals = [1, 16, 20]
    c_colors = ['#00BBF9', '#FEE440', '#F95738']
    ith_subplots = [2, 3, 4]
    x_lims = [3, 10, 12]

    fig = plt.figure(figsize=(16, 16))

    # Left subplot
    ax1 = fig.add_subplot(2, 2, 1)

    x_1 = np.arange(0, 20 + 0.1, 0.1)
    y_1 = x_1**2/16 - x_1

    ax1.plot(x_1, y_1, color='#724CF9')  # Plot of line
    # Scatter plot for each of the next subplots
    for c, c_color in zip(c_vals, c_colors):
        ax1.scatter(c, c**2/16 - c, color=c_color, zorder=2, label=f'{c=}')

    ax1.fill_between([-5, 25], 0, 6, color='#8AE6A2', alpha=0.5)

    ax1.grid(True, which='both', alpha=0.75)

    ax1.set_xlabel(r'$c$')
    ax1.set_ylabel(r'$c^{2}/16 - c$')

    ax1.set_xlim(-2, 22)
    ax1.set_ylim(-4.5, 5.5)

    ax1.legend(loc='upper left')

    # Other subplots
    for c, c_color, x_lim, ith_subplot in zip(c_vals, c_colors, x_lims, ith_subplots):
        x_2 = np.linspace(0.1, x_lim, 10001)
        y_perimeter = -x_2 + c/2
        y_area = c/x_2

        ax = fig.add_subplot(2, 2, ith_subplot)

        ax.plot(x_2, y_perimeter, color=c_color, label=f'{c=}')
        ax.plot(x_2, y_area, color=c_color)

        if c != 1:
            ax.scatter(c/4 - ((1/16)*c**2 - c)**0.5, c/(c/4 - ((1/16)*c**2 - c)**0.5), color='k', zorder=2)
            ax.scatter(c/4 + ((1/16)*c**2 - c)**0.5, c/(c/4 + ((1/16)*c**2 - c)**0.5), color='k', zorder=2)

        ax.grid(True, which='both', alpha=0.5)

        ax.set_xlabel(r'$x$')
        ax.set_ylabel(r'$y$')

        ax.set_xlim(-1*x_lim/10, x_lim + x_lim/10)
        ax.set_ylim(-1 * x_lim / 10, x_lim + x_lim / 10)

        ax.legend(loc='upper right')

    fig.suptitle('The Perimeter of a Rectangle', fontsize=16)

    plt.show()
