from colorama import Fore, Style
import numpy as np
import matplotlib.pyplot as plt


def josephus_simulate(N: int, verbose: bool = False) -> int:
    """
    This function simulates the Josephus problem. There are verbose and non-verbose variants.

    Args:
        N: Number of people in the problem.
        verbose: Flag which controls whether there are prints at every stage or not.

    Returns:
        survivor: The number of the survivor which is only returned if the verbose flat is True.
    """

    # Error handling
    if not isinstance(N, int):
        raise TypeError('N has to be an integer.')
    if isinstance(N, int) and N < 1:
        raise ValueError('N has to be an integer greater than or equal to 1.')
    if not isinstance(verbose, bool):
        raise TypeError('The variable output has to be a bool.')

    # Trivial case
    if N == 1:
        return 1

    # Follow the verbose variant
    if verbose:
        soldiers = np.ones(N)  # Initialise array
        index_murderer = 0
        one_person_left = False

        print(Fore.BLUE
              + f'All the soldiers:\n{np.where(soldiers == 1)[0] + 1}.'
              + Style.RESET_ALL)

        # Simulation execution
        while not one_person_left:
            murder_this_turn = False

            # Check if murderer is alive
            if soldiers[index_murderer] == 1:
                index_victim = (index_murderer + 1) % N
                # Murder loop
                while not murder_this_turn:
                    # Check if person next to pointer is alive
                    if soldiers[index_victim] == 1:
                        soldiers[index_victim] = 0  # Person is dead now

                        print(Fore.RED
                              + f'Soldier {index_murderer + 1} has killed soldier {index_victim + 1}.'
                              + Style.RESET_ALL)
                        print(Fore.BLUE
                              + f'The remaining soldiers alive:\n{np.where(soldiers == 1)[0] + 1}.'
                              + Style.RESET_ALL)

                        index_murderer = (index_murderer + 1) % N  # Update murderer
                        murder_this_turn = True  # Breaks loop

                    # Find a new victim
                    else:
                        index_victim = (index_victim + 1) % N

            # Move murder index to the next person
            else:
                index_murderer = (index_murderer + 1) % N

            # Check if only one player is alive
            if len(np.where(soldiers == 1)[0]) == 1:
                survivor = np.where(soldiers == 1)[0][0] + 1
                one_person_left = True

        survivor = np.where(soldiers == 1)[0][0] + 1
        print(Fore.GREEN
              + f'Soldier {survivor} is the last man standing.'
              + Style.RESET_ALL)

    # The non-verbose variant
    else:
        soldiers = np.arange(1, N + 1, 1)  # Initialise array of soldiers

        # Simulation execution
        while len(soldiers) > 1:
            (shift, start_ind) = (0, 0) if len(soldiers) % 2 == 0 else (-1, 1)
            player_shifted = np.roll(soldiers, shift)
            soldiers = player_shifted[start_ind::2]  # Remove dead soldiers from array

        survivor = int(soldiers[0])

    # Only return output if requested
    return survivor


def josephus_analytic(N: int) -> int:
    """
    The analytic solution to the Josephus problem.

    Args:
        N: Number of people in the problem.

    Returns:
        survivor: The number of the survivor.
    """
    i = np.floor(np.log2(N))
    survivor = 2*(N - 2**i) + 1

    return survivor


if __name__ == '__main__':
    # Set print options to print the entire vector
    np.set_printoptions(threshold=10**5, linewidth=10**5)
    _ = josephus_simulate(67,  True)

    # Plot solution
    N_max = 100
    survivor_dict = {}  # Key is number of soldiers and value is survivor

    for N in range(1, N_max + 1):
        survivor_n = josephus_analytic(N)
        survivor_dict[N] = survivor_n

    # Plotting
    show_plot = True  # Change flag to display graph
    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111)
    ax.scatter(survivor_dict.keys(), survivor_dict.values(), c=list(survivor_dict.values()), cmap='viridis')
    ax.grid(alpha=0.7, zorder=-1)
    ax.set_xlabel(r'$N$')
    ax.set_ylabel(r'$J(n)$')

    if show_plot:
        plt.show()
