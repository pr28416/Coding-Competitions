N = 0
cows = []
with open("sleepy2.in", "r") as f:
    N = int(f.readline())
    cows = [int(i) for i in f.readline().split(" ")]

sortedCows = cows.copy()
sortedCows.sort()
print(cows)
print(sortedCows)
visitedSortings = []

print("\nStarting\n")

didMoveMax = False
steps = 0
cowPlacements = cows.copy()

while cowPlacements != sortedCows:
    # Check to see if sorted
    con = 1
    if cowPlacements == sortedCows:
        break
    # Check if 0th item is largest. If so, move to the end.
    elif cowPlacements[0] == max(cowPlacements):
        cowPlacements.insert(N-1, cowPlacements.pop(0))
        didMoveMax = True
    # Else, check if 0th item is already next to its consecutive. If so, move it to its next consecutive.
    # Else, move the 0th item next to its consecutive.

    else:
        if cowPlacements[0] + 1 == cowPlacements[1]:
            con = 2

        if didMoveMax:
            print("Moved through consecutive")
            for i in range(N):
                if cowPlacements[0] + con == cowPlacements[i]:
                    cowPlacements.insert(i - 1, cowPlacements.pop(0))
                    break
            else:
                cowPlacements.insert(N - 2, cowPlacements.pop(0))
        else:
            for i in range(cows.index(max(cows)) + 1, N):
                if cowPlacements[0] + con == cowPlacements[i]:
                    cowPlacements.insert(i - 1, cowPlacements.pop(0))
                    break
            else:
                cowPlacements.insert(N - 1, cowPlacements.pop(0))

    print(cowPlacements)
    steps += 1

# steps = solve(cows, 0, False)

didMoveMax = False
# while cows != sortedCows:
#     steps += 1
#     # Check if 0th index is max
#     if cows[0] == max(cows):
#         didMoveMax = True
#         cows.insert(N-1, cows.pop(0))
#     else:
#         # Check if didMoveMax
#         checkPos = cows.index(max(cows))+1
#         if didMoveMax:
#             checkPos = 0
#         # Move 0th item until it is less than its consecutive
#         for i in range(checkPos, N):
#             if cows[0] < cows[i]:
#                 cows.insert(i-1, cows.pop(0))
#                 break
#         else:
#             cows.insert(N-2, cows.pop(0))
#     print(cows)

print(steps)
