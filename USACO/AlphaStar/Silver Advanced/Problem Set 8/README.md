# Space Exploration

Farmer John's cows have finally blasted off from earth and are now
floating around space in their Moocraft. The cows want to reach
their fiery kin on Jupiter's moon of Io, but to do this they must
first navigate through the dangerous asteroid belt.

Bessie is piloting the craft through this treacherous N x N (1 <=
N <= 1,000) sector of space. Asteroids in this sector comprise some
number of 1 x 1 squares of space-rock connected along their edges
(two squares sharing only a corner count as two distinct asteroids).
Please help Bessie maneuver through the field by counting the number
of distinct asteroids in the entire sector.

Consider the 10 x 10 space shown below on the left. The '*'s represent
asteroid chunks, and each '.' represents a .vast void of empty space. The
diagram on the right shows an arbitrary numbering applied to the asteroids.

```
        ...**.....           ...11.....
        .*........           .2........
        ......*...           ......3...
        ...*..*...           ...3..3...
        ..*****...           ..33333...
        ...*......           ...3......
        ....***...           ....444...
        .*..***...           .5..444...
        .....*...*          ......4...6
        ..*.......          ..7........
```

It's easy to see there are 7 asteroids in this sector.

PROBLEM NAME: `space`

INPUT FORMAT:

* Line 1: A single integer: N

* Lines 2..N+1: Line i+1 contains row i of the asteroid field: N
        characters

SAMPLE INPUT:

```
10
...**.....
.*........
......*...
...*..*...
..*****...
...*......
....***...
.*..***...
.....*...*
..*.......
```

OUTPUT FORMAT:

* Line 1: A single integer indicating the number of asteroids in the
        field.

SAMPLE OUTPUT:

```
7
```

# Laserphones

The cows have a new laser-based system so they can have casual
conversations while out in the pasture which is modeled as a W x H
grid of points (1 <= W <= 100; 1 <= H <= 100).

The system requires a sort of line-of-sight connectivity in order
to sustain communication. The pasture, of course, has rocks and
trees that disrupt the communication but the cows have purchased
diagonal mirrors that deflect the laser beam through a 90 degree
turn. Below is a map that illustrates the problem.

H is 8 and W is 7 for this map.  The two communicating cows are
notated as 'C's; rocks and other blocking elements are notated as
'*'s:

```
7 . . . . . . .         7 . . . . . . .
6 . . . . . . C         6 . . . . . /-C
5 . . . . . . *         5 . . . . . | *
4 * * * * * . *         4 * * * * * | *
3 . . . . * . .         3 . . . . * | .
2 . . . . . . .         2 . /-------/ .
1 . C . . . * .         1 . C . . . * .
0 . . . . . . .         0 . . . . . . .
  0 1 2 3 4 5 6           0 1 2 3 4 5 6
```

Determine the minimum number of mirrors M that must be installed to
maintain laser communication between the two cows.

PROBLEM NAME: `lphone`

INPUT FORMAT:

* Line 1: Two space separated integers: W and H

* Lines 2..H+1: The entire pasture.

SAMPLE INPUT:

```
7 8
.......
......C
......*
*****.*
....*..
.......
.C...*.
.......
```

OUTPUT FORMAT:

* Line 1: A single integer: M

SAMPLE OUTPUT:

```
3
```

# Word Morph

Farmer John is playing a word game against his cows. It
starts like this:

  * Farmer John chooses a word, such as 'cat'
  * The cows then choose their own word, perhaps 'dog'

Farmer John then must morph his word to the cows' word by performing
a number of steps, each one of which changes one single letter at
a time to make a new, valid word.

The dictionary of valid words is given in the input. There are no 
more than 25,000 words, each with length in the range 1..20. These
'words' contain only letters in the range 'a'..'z'.

For this example, Farmer John could make the following sequence of
four words:

```
'cat' -> 'cot' -> 'cog' -> 'dog'
```

to morph words from the first word 'cat' to the final word 'dog'
in just three moves. The cows will never give Farmer John an
impossible task. Farmer John must get from his word to the cows'
word in as few moves as possible.

You will be given a starting word and an ending word. Determine
and output a number which is the least number of legal letter changes
required to morph the starting word to the ending word.

PROBLEM NAME: `wmorph`

INPUT FORMAT:

* Line 1: A single string that is the starting word

* Line 2: A single string that is the end word

* Line 3..?: Words in the dictionary; one word per line

SAMPLE INPUT:

```
cat
dog
```

OUTPUT FORMAT:

* Line 1: A single integer that is the number of times a letter must be changed to transform the starting word into the ending word.

SAMPLE OUTPUT:

```
3
```

# Corn Maze

This past fall, Farmer John took the cows to visit a corn maze. But
this wasn't just any corn maze: it featured several gravity-powered
teleporter slides, which cause cows to teleport instantly from one
point in the maze to another. The slides work in both directions:
a cow can slide from the slide's start to the end instantly, or
from the end to the start. If a cow steps on a space that hosts
either end of a slide, she must use the slide. The outside of the 
corn maze is entirely corn except for a single exit.

The maze can be represented by an N x M (2 <= N <= 300; 2 <= M
<= 300) grid. Each grid element contains one of these items:

   * Corn (corn grid elements are impassable)
   * Grass (easy to pass through!)
   * A slide endpoint (which will transport a cow to the other
     endpoint)
   * The exit

A cow can only move from one space to the next if they are adjacent
and neither contains corn. Each grassy space has four potential
neighbors to which a cow can travel. It takes 1 unit of time to
move from a grassy space to an adjacent space; it takes 0 units of
time to move from one slide endpoint to the other.

Corn-filled spaces are denoted with an octothorpe (#). Grassy spaces
are denoted with a period (.). Pairs of slide endpoints are denoted
with the same uppercase letter (A-Z), and no two different slides
have endpoints denoted with the same letter. The exit is denoted
with the equals sign (=).

Bessie got lost. She knows where she is on the grid, and marked her
current grassy space with the 'at' symbol (@). What is the minimum
time she needs to move to the exit space?

Consider the following grid, with N=5 and M=6:

```
        ###=##
        #.W.##
        #.####
        #.@W##
        ######
```

A single slide has endpoints denoted by an uppercase W. Her optimal
strategy is to move right to the slide endpoint in 1 time, take the
slide in 0 time to the other endpoint, and move right and up in 2
more time to end on the exit.  This requires a total of 3 time, the
minimum.

PROBLEM NAME: `cornmaze`

INPUT FORMAT:

* Line 1: Two space separated integers: N and M

* Lines 2..N+1: Line i+1 describes row i of the maze: M characters (no
        spaces)

SAMPLE INPUT:

```
5 6
###=##
#.W.##
#.####
#.@W##
######
```

OUTPUT FORMAT:

* Line 1: An integer, corresponding to the shortest time that Bessie
        needs to exit the maze.

SAMPLE OUTPUT:

```
3
```