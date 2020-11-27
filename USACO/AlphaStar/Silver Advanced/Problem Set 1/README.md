# The Leprechaun

Imagine Bessie's surprise as she spied a leprechaun prancing through
the north pasture. Being no one's fool, she charged at the leprechaun
at captured him with her prehensile hooves.

"One wish, bovine one. That's all I have for cows," he said.

"Riches," Bessie said dreamily. "The opportunity for riches."

Leprechauns never grant precisely the easiest form of their captor's
wishes. As the smoke cleared from the location of a loud explosion,
a shimmering donut spun slowly over the verdant green fields.

"I have made you a torus," the leprechaun cooed. "And on that torus
is an N x N matrix (1 <= N <= 200) of integers in the range
-1,000,000..1,000,000 that will determine the magnitude of your
riches. You must find the sequence of contiguous integers all in
one row, one column, or on one diagonal that yields the largest sum
from among all the possible sequences on the torus."

Bessie pondered for a moment and realized that the torus was a
device for "wrapping" the columns, rows, and diagonals of a matrix
so that one could choose contiguous elements that "wrapped around"
the side or top edge.

Bessie will share the matrix with you.  Determine the value of the
largest possible sum (which requires choosing at least one matrix
element).

By way of example, consider the 4 x 4 matrix on the left below that
has all the elements from one exemplary "wrapped" diagonal marked:

```
8   6   6*  1           8   6*  6   1
-3  4   0   5*         -3   4   0   5
4*  2   1   9           4   2   1   9*
1   -9* 9  -2           1  -9   9*  -2
```

The marked diagonal of the right-hand matrix includes two nines
(the highest available number) and a six for a total of 24. This
is the best possible sum for this matrix and includes only three
of the four possible elements on its diagonal.

PROBLEM NAME: `lepr`

INPUT FORMAT:

* Line 1: A single integer: N

* Lines 2..N+1: Line i+1 contains N space-separated integers that
        compose row i of the matrix

SAMPLE INPUT:

```
4
8 6 6 1
-3 4 0 5
4 2 1 9
1 -9 9 -2
```

OUTPUT FORMAT:

* Line 1: A single integer that is the largest possible sum computable
        using the rules above

SAMPLE OUTPUT:

```
24
```

# Angry Cows

Bessie the cow has designed what she thinks will be the next big hit 
video game: "Angry Cows". The premise, which she believes is 
completely original, is that the player shoots cows with a slingshot 
into a one-dimensional scene consisting of a set of hay bales located 
at various points on a number line. Each cow lands with sufficient 
force to detonate the hay bales in close proximity to her landing 
site. The goal is to use a set of cows to detonate all the hay bales.

There are N hay bales located at distinct integer positions 
x1,x2,...,xN on the number line. If a cow is launched with power R 
landing at position x, this will causes a blast of "radius R", 
destroying all hay bales within the range x-R...x+R.

A total of K cows are available to shoot, each with the same power R. 
Please determine the minimum integer value of R such that it is 
possible to use the K cows to detonate every single hay bale in the 
scene.

PROBLEM NAME: `angry`

INPUT FORMAT:

The first line of input contains N (1 <= N <= 50,000) and K (1 <= K 
<= 10). The remaining N lines all contain integers x1...xN (each in 
the range 0...1,000,000,000).

OUTPUT FORMAT:

Please output the minimum power R with which each cow must be 
launched in order to detonate all the hay bales.

SAMPLE INPUT:

```
7 2
20
25
18
8
10
3
1
```

SAMPLE OUTPUT:

```
5
```

# The Grand Farm-off

[Memory: 16 MB CPU: 1 sec]

Farmer John owns 3*N (1 <= N <= 500,000) cows surprisingly numbered
0..3*N-1, each of which has some associated integer weight W_i (1 <=
W_i <= d). He is entering the Grand Farm-off, a farming competition
where he shows off his cows to the greater agricultural community.

This competition allows him to enter a group of N cows. He has given
each of his cows a utility rating U_i (1 <= U_i <= h), which
represents the usefulness he thinks that a particular cow will have
in the competition, and he wants his selection of cows to have the
maximal sum of utility.

There might be multiple sets of N cows that attain the maximum
utility sum. FJ is afraid the competition may impose a total weight
limit on the cows in the competition, so a secondary priority is
to bring lighter weight competition cows.

Help FJ find a set of N cows with minimum possible total weight
among the sets of N cows that maximize the utility, and print the
remainder when this total weight is divided by M (10,000,000 <= M
<= 1,000,000,000).

Note: to make the input phase faster, FJ has derived polynomials
which will generate the weights and utility values for each cow.
For each cow 0 <= i < 3*N,

```
    W_i = (a*i^5+b*i^2+c) mod d
```

and

```
    U_i = (e*i^5+f*i^3+g) mod h
```

with reasonable ranges for the coefficients (0 <= a <= 1,000,000,000;
0 <= b <= 1,000,000,000; 0 <= c <= 1,000,000,000; 0 <= e <=
1,000,000,000; 0 <= f <= 1,000,000,000; 0 <= g <= 1,000,000,000;
10,000,000 <= d <= 1,000,000,000; 10,000,000 <= h <= 1,000,000,000).

The formulae do sometimes generate duplicate numbers; your algorithm
should handle this properly.

PROBLEM NAME: farmoff

INPUT FORMAT:

* Line 1: Ten space-separated integers: N, a, b, c, d, e, f, g, h, and M

SAMPLE INPUT:

```
2 0 1 5 55555555 0 1 0 55555555 55555555
```

INPUT DETAILS:

The functions generate weights of 5, 6, 9, 14, 21, and 30 along
with utilities of 0, 1, 8, 27, 64, and 125.

OUTPUT FORMAT:

* Line 1: A single integer representing the lowest sum of the weights
        (modulo M) of the N cows with the highest net utility.

SAMPLE OUTPUT:

```
51
```

OUTPUT DETAILS:

The two cows with the highest utility are cow 5 and 6, and their combined
weight is 21+30=51.