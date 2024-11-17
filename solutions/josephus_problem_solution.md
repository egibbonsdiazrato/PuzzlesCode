## Josephus Problem Solution

Let us have rounds, where a round is complete when the last soldier has killed or been killed. It can be seen from
trial and error that the behaviour is different for an even and odd number of soldiers. If we consider a large enough
even number of soldier, all of the soldiers with even-numbered positions die by the end of round 1. At the start of 
round 2, the knife is once again in the hand of the soldier in position number 1. The same process is repeated for 
the next round the circle the new "even-numbered", every other soldier with odd-numbered positions, is killed. We will
consider different subsets of these two cases to build a general solution.

Let us consider the special case where N can be expressed as $2^i$ where $i$ is an integer. Below, $N=8$ is shown.
```
Start of round 0:
soldiers = [1, 2, 3, 4, 5, 6, 7, 8]
Start of round 1:
soldiers = [1, 3, 5, 7]
Start of round 2:
soldiers = [1, 5]
Start of round 3:
soldiers = [1]
```
For this special case of $N$, at the start of every round, soldier 1 holds the knife. This means that soldier 1 
ensures that he will not be killed. Thus, when $N$ can be written in the aforementioned form, soldier 1 is always the 
survivor.

What happens when we look at another example where N is even but not cannot be expressed in the form above, 
such as $N = 12$?
```
Start of round 0:
soldiers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Start of round 1:
soldiers = [1, 3, 5, 7, 9, 11]
Start of round 2:
soldiers = [1, 5, 9]
Start of round 3:
soldiers = [9]
```
This example is more complicated than the one shown before. By the start of round 1, the even-numbered soldiers are
dead. During round 1, evey other odd-numbered soldier is killed. Round 2 starts with the knife in the hands of 
soldier 1 . However, after killing soldier 5, soldier 1 is killed by soldier 9. This makes soldier 9 the survivor. The 
behaviour changed at the start of round 2, where the number of soldiers left was odd. For this round then, to find the 
outcome we can "move" the soldier in the first position to the last and save, instead of kill, soldiers in 
even-numbered positions.

These two ideas, of even and odd number of soldiers left, are enconded into the non-verbose variant of the
`josephus_simulate` function. The first few results are shown in the table below, where $J(N)$ is a function which 
returns the position of the soldier who survives.

| $N$ | $J(N)$ |
|-----|--------|
| 1   | 1      |
| 2   | 1      |
| 3   | 3      |
| 4   | 1      |
| 5   | 3      |
| 6   | 5      |
| 7   | 7      |
| 8   | 1      |
| 9   | 3      |
| 10  | 5      |
| 11  | 7      |
| 12  | 9      |
| 13  | 11     |
| 14  | 13     |
| 15  | 15     |
| 16  | 1      |

We see the special cases that were considered at the start are nodes to start at 1. For a number between two exact 
powers of two, we have linear increases in steps of two starting at 1, the lower of the two exact powers by which this
number is bounded.

Consider the general case of $N$ soldiers. The largest power of 2 which is smaller than N is given by 
$floor(\log_2 N)$. Now, we need to calculate the relative position of that number with respect to the lower bound
using $N - 2^{floor(\log_2 N)}$. Wit this we can write a general expression:

$$ J(N) = 2(N - 2^{floor(\log_2 N)}) + 1 $$

This equation illustrates the behaviour observed in the table which is lines which start at 1 for every N that is an 
exact power of 2 and increase in steps of 2 until the next power of 2 is hit.

A proof by induction is included in the Wikipedia page for this problem 
(https://en.wikipedia.org/wiki/Josephus_problem).
