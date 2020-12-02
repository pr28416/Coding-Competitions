# The Flying Cow

Recently, Farmer John has been interested in buying new machines
to plow his farm. His newest purchase, the Flying Cow 2000, is
the latest model available on the market which comes with the
ability of flight. Farmer John has too much fun flying the machine
however and accidentally crashes the Flying Cow, which means that
now it can only fly to specific spots on his farm.

Farmer John's farm can be visualized as a number line with a plot
of grass at every number. FJ lives at the number 1 (and so does
his Flying Cow), but he would like to plow the plot located at the
number N (1 <= N <= 1,000,000). The Flying Cow can only fly from a
patch i to a patch 3*i. Farmer John can also push the Flying Cow
either one patch to the right or to the left, i.e. from patch i to
patch i+1 or to patch i-1. All three of these moves consumes one
unit of energy each.

Being the highly efficient farmer that he is, Farmer John wants to
know the minimum units of energy needed to get to his desired plot.
Can you help him?

PROGRAM NAME: `flyingcow`

INPUT FORMAT:

* Line 1: a single integer N, indicating the location of the plot to be plowed

OUTPUT FORMAT:

* Line 1: a single integer, M, the minimum units of energy needed to get to the plot

SAMPLE INPUT:

```
5
```

SAMPLE OUTPUT:

```
3
```

OUTPUT DETAILS:

Farmer John can fly with the Flying Cow once, consuming one units
of energy, moving from 1->3. Then he can push the Flying Cow two
units to the right, using a total of three units of energy.

# Paint Job

It's been springtime in the rocky mountains, which means storms
have been coming and going on the farm. The barns and stalls
used to have beautiful colors on the outside, but now they've
all faded away! Farmer John enlisted Bessie to help restore order
by giving her various paint jobs around the farm.

As you know, buckets of paint have numerical colors ranging from
1 to P (1 <= P <= 10,000). Bessie owns a paint bucket of color A
(1 <= A <= P) that she will use for the job, but FJ wants her to
paint a color B (1 <= B <= P) instead. To help her, FJ looks for
spare paint buckets that he has lying around in the barn and finds
N (1 <= N <= 10,000) paint buckets. Bessie can use these paint
buckets by picking one of them and pouring some of its paint into
her bucket, effectively mixing the two colors. The resulting color
is the remainder upon division by P of the product of her bucket's
color and the color she mixed in. Being the skilled painter that
she is, Bessie can use the N paint buckets as many times as she likes.

FJ is having some relatives over soon, so he wants the farm to be
clean and pristine as soon as possible. What is the minimum number
of mixes Bessie needs in order to get Farmer John’s color?

PROGRAM NAME: `paintjob`

INPUT FORMAT:

* Line 1: contains two integers, A and B, indicating the color of Bessie’s paint and the desired paint color respectively.

* Line 2: contains two integers, N and P, as explained in the problem statement.

* Line 3: contains N integers, the list of paint colors at Bessie's disposal.

OUTPUT FORMAT:

* Line 1: a single integer, M, representing the minimum number of mixes Bessie needs to perform. Output -1 if Bessie cannot make FJ’s desired paint color.

SAMPLE INPUT:

```
3 30
3 100
2 5 7
```

SAMPLE OUTPUT:

```
2
```

OUTPUT DETAILS:

Bessie starts with a paint color of 3. She can then mix the paint
color 2 into it, and then the paint color 5 to get a paint color of
3x2x5=30 as desired.

# Pathfinding

Bessie is stranded on a deserted arctic island and wants to determine
all the paths she might take to return to her pasture. She has
tested her boat and knows she can travel from one island to another
island in 1 unit of time if a route with proper currents connects
the pair.

She has experimented to create a map of the ocean with valid
single-hop routes between each pair of the N (1 <= N <= 100) islands,
conveniently numbered 1..N. The routes are one-way (unidirectional),
owing to the way the currents push her boat in the ocean. It's
possible that a pair of islands is connected by two routes that use
different currents and thus provide a bidirectional connection. The
map takes care to avoid specifying that a route exists between an
island and itself.

Given her starting location M (1 <= M <= N) and a representation
of the map, help Bessie determine which islands are one 'hop' away,
two 'hops' away, and so on. If Bessie can take multiple different
paths to an island, consider only the path with the shortest distance.

By way of example, below are N=4 islands with connectivity as shown
(for this example, M=1):

```
       start--> 1-------->2
                |         |
                |         |
                V         V
                4<--------3
```

Bessie can visit island 1 in time 0 (since M=1), islands 2 and 4
at time 1, and island 3 at time 2.

The input for this task is a matrix C where a nonzero entry C_rc
(0 <= C_rc <= 1) in row r and column c means "Currents enable Bessie
to travel directly from island r to island c in one time unit". Row
C_r has N elements, respectively C_r1..C_rN, each one of which is
0 or 1.

PROBLEM NAME: `pathfind`

INPUT FORMAT:

* Line 1: Two space-separated integers: N and M

* Lines 2..N+1: Line i+1 contains N space-separated integers: C_r

SAMPLE INPUT:

```
4 1
0 1 0 1
0 0 1 0
0 0 0 1
0 0 0 0
```

OUTPUT FORMAT:

* Lines 1..???: Line i+1 contains the list of islands (in ascending numerical order) that Bessie can visit at time i.  Do not include any lines of output after all reachable islands have been listed.

SAMPLE OUTPUT:

```
1
2 4
3
```

# Bronze Lilypad Pond

Farmer John has installed a beautiful pond for his cows' esthetic
enjoyment and exercise. The rectangular pond has been partitioned
into square cells of M rows and N columns (1 <= M <= 30; 1 <= N <=
30). Some of the cells have astonishingly sturdy lilypads; others
have rocks; the remainder are just beautiful, cool, blue water.

Bessie is practising her ballet moves by jumping from one lilypad
to another and is currently located at one of the lilypads (see the
input data for the location's specifier). She wants to travel to
another lilypad in the pond by jumping from one lilypad to another.
She can jump neither into the water nor onto a rock.

Surprising only to the uninitiated, Bessie's jumps between lilypads
always appear as a sort of chess-knight's move: move M1 (1 <= M1
<= 30) 'squares' in one direction and then M2 (1 <= M2 <= 30; M1
!= M2) more in an orthogonal direction (or perhaps M2 in one direction
and then M1 in an orthogonal direction). Bessie sometimes might
have as many as eight choices for her jump.

Given the pond layout and the format of Bessie's jumps, determine
the smallest number of leaps that Bessie must make to move from her
starting location to her final destination, a feat which is always
possible for the given test data.

PROBLEM NAME: `bronlily`

INPUT FORMAT:

* Line 1: Four space-separated integers: M, N, M1, and M2

* Lines 2..M+1: Line i+1 describes row i of the pond using N space-separated integers with these values: 0 indicates empty water; 1 indicates a lilypad; 2 indicates a rock; 3 indicates the lilypad Bessie upon which she starts; 4 indicates the lilypad that is Bessie's destination.

SAMPLE INPUT:

```
4 5 1 2
1 0 1 0 1
3 0 2 0 4
0 1 2 0 0
0 0 0 1 0
```

INPUT DETAILS:

Bessie starts on the left in row 2; her destination is on the right in row
2. Several lilypads and rocks occupy the pond.

OUTPUT FORMAT:

* Line 1: A single integer that is the minimum number of jumps between lilypads that Bessie must make to travel from her starting place to her destination.

SAMPLE OUTPUT:

```
2
```

OUTPUT DETAILS:

Bessie cleverly hops onto the pad at row 1, column 3 on her way to the
right hand side.
