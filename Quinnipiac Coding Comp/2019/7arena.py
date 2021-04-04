# a1: Rect A top-left coord
# a2: Rect A bottom-right coord
# b1: Rect B top-left coord
# b2: Rect B bottom-right coord
def intersection(a1, a2, b1, b2):
    x, y = 0, 1
    xdist = (min(b1[x],b2[x])-max(a1[x], a2[x]))
    ydist = (min(b1[y],b2[y])-max(a1[y], a2[y]))
    if xdist+1 > 0 and ydist+1 > 0: return (xdist+1) * (ydist+1)
    else: return 0

    # x_dist = (min(r1[x], r2[x]) -
    #           max(l1[x], l2[x]))
 
    # y_dist = (min(r1[y], r2[y]) -
    #           max(l1[y], l2[y]))
    
def area(a1, a2, b1, b2):
    total = (a2[0]-a1[0])*(a2[1]-a1[1])
    intersect = intersection(a1,a2,b1,b2)
    return total-intersect

T = int(input())
for _ in range(T):
    line = list(map(int, input().split(" ")))
    R, C, W = line[0], line[1], line[2]
    grid = [[0] * C for _ in range(R)]
    covered = []
    for w in range(W):
        covered.append(
            [
                (line[3+4*w], line[4+4*w]),
                (line[5+4*w], line[6+4*w])
            ]
        )
    a = 0
    for rect in range(W):
        for prev in range(rect):
            q = area(covered[rect][0], covered[rect][1], covered[prev][0], covered[prev][1])
            print(rect, prev, covered[rect], covered[prev], q)
            a += q
    print(a)