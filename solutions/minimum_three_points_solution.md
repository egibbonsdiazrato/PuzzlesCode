## The Minimum of Three Points Solution

We are asked to consider three points, $x_1, x_2, x_3$, which are IID and $x_i = x \sim U\[0, 3\], i = \{1, 2, 3\}.
Then, to find $P(0.5 \leq min(x_1, x_2, x_3) \leq 1)$.

#### 2D Simplification:
As with many puzzles, it is good to consider simpler versions to then build up a solution. Thus, we start by only
considering two points, $x_1, x_2$. How do we find the probability for which $min(x_1, x_2)$ lies in the required 
range? We can think of the probability as a fraction of area in the $x_1-x_2$ plane. The fraction of the area where this
condition is satisfied with respect to the whole distribution of $x_1$ and $x_2$ gives us the probability. There are 
two ways to find the area where the condition is met. The region where $min(x_1, x_2) \geq 0.5$ minus the region where
$min(x_1, x_2) \geq 1$ gives us the desired region. Alternatively, one can consider the regions where 
$0.5 \leq x_1 \leq 1$ and $x_2 \geq 0.5$ as well as $0.5 \leq x_2 \leq 1$ and $x_1 \geq 0.5$. These are two identical
rectangles in perpendicular direction which overlap at the base of the L. Therefore, the desired area can be found
by multiplying the area of the rectangle by 2 and subtracting a square of side 0.5. Once the desired area is found,
it has to be normalised to be expressed as a probability. This results in 
$P(0.5 \leq min(x_1, x_2, x_3) \leq 1) = \frac{(3-0.5)^2 - (3-1)^2}{3^2} = \frac{2*(0.5*(3-0.5))- (0.5)^2}{3^2} = \frac{1}{4}$

#### 3D
We can extend out conclusions from 2D to 3D. Calculate our desired volume either by subtracting the volume of two
cubes or considering our "L" shape as a cross-sectional view of the three planes. Both perspectives yield the same
volume. Thus, the probability is $P(0.5 \leq min(x_1, x_2, x_3) \leq 1) = \frac{(3-0.5)^3 - (3-1)^3}{3^3} = \frac{61}{216}$.
