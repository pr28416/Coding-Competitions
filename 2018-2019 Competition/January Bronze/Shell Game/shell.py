bowls = [0, 0, 0]
numSwaps = 0
swaps = []
maxPoints = 0

# Need to iterate possibilities of where the pebble starts.
# From here it is easy to iterate N times to swap bowls.

with open("shell.in", "r") as f:
    numSwaps = int(f.readline())
    for i in range(numSwaps):
        swaps.append([int(i) for i in f.readline().split(" ")])

# print(numSwaps, swaps)

# Position pebble in a random bowl
for p in range(3):
    # Put the pebble under the bowl
    bowls[p] = 1

    # Run tests on this scenario
    points = 0
    for bowlSwap in swaps:
        # Swap the bowls
        bowls[bowlSwap[0]-1], bowls[bowlSwap[1]-1] = bowls[bowlSwap[1]-1], bowls[bowlSwap[0]-1]

        # Guess the swap
        if bowls[bowlSwap[2]-1] == 1:
            points += 1

    # Check if points exceeds max
    if points > maxPoints: maxPoints = points
    # Reset the bowls
    bowls[0], bowls[1], bowls[2] = 0, 0, 0

# print(maxPoints)
with open("shell.out", "w") as f:
    f.write("%s\n" % maxPoints)