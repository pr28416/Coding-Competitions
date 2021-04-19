def check(diffs, mid, maxlength):
    spot = mid+1
    curlength = 1
    while spot < len(diffs):
        if diffs[spot] == diffs[spot-1]: curlength += 1
        else: break
        spot += 1
    spot = mid-1
    while spot >= 0:
        if diffs[spot] == diffs[spot+1]: curlength += 1
        else: break
        spot -= 1
    return max(maxlength, curlength)

def setup(lst, diffs, i, val):
    lst[i] = val
    diffs[i-1] = lst[i]-lst[i-1]
    diffs[i] = lst[i+1]-lst[i]

def solve(lst):
    if len(lst) <= 3: return len(lst)
    diffs = [0] * (len(lst)-1)
    for i in range(len(lst)-1):
        diffs[i] = lst[i+1]-lst[i]
    # Start by finding existing largest arithmetic subarray
    maxlength = 0
    curlength = 1
    for up in range(1, len(diffs)):
        if diffs[up] == diffs[up-1]:
            curlength += 1
            maxlength = max(maxlength, curlength)
        else:
            maxlength = max(maxlength, curlength)
            curlength = 1

    finlength = maxlength

    # Change the beginning
    tmp = diffs[0]
    diffs[0] = diffs[1]
    finlength = check(diffs, 0, finlength)
    diffs[0] = tmp

    # Change the end
    tmp = diffs[-1]
    diffs[-1] = diffs[-2]
    finlength = check(diffs, len(diffs)-1, finlength)
    diffs[-1] = tmp

    # Change in between
    for i in range(1, len(lst)-1):


        #-2
        if 2 <= i:
            tmp = lst[i]
            setup(lst, diffs, i, lst[i-1]*2-lst[i-2])
            # print("-2>", lst, diffs)
            finlength = check(diffs, i, finlength)
            setup(lst, diffs, i, tmp)
            # print(lst, diffs)

        #+2
        if i <= len(lst)-3:
            tmp = lst[i]
            setup(lst, diffs, i, lst[i+1]*2-lst[i+2])
            # print("+2>", lst, diffs)
            finlength = check(diffs, i, finlength)
            setup(lst, diffs, i, tmp)
            # print(lst, diffs)

        lo, up = (lst[i-1]+lst[i+1])//2, (lst[i-1]+lst[i+1]+1)//2

        # Set up
        tmp = lst[i]
        setup(lst, diffs, i, lo)
        # Check
        # print("1lo>", lst, diffs)
        finlength = check(diffs, i, finlength)
        # Reset
        setup(lst, diffs, i, tmp)
        
        # print(lst, diffs)

        # Check if don't need additional
        if lo == up: continue

        # Set up
        tmp = lst[i]
        # print("1up>", lst, diffs)
        setup(lst, diffs, i, up)
        # Check
        finlength = check(diffs, i, finlength)
        # Reset
        setup(lst, diffs, i, tmp)

        # print(lst, diffs)

    return finlength+1

def run():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        lst = list(map(int, input().split(" ")))
        print(f"Case #{t}:", max(3, solve(lst)))

run()
# psolve = lambda lst: print(solve(lst))
# psolve([1,2,4,6,7,5,3,1])
# psolve([5, 5, 4, 5, 5, 5, 4, 5, 6])
# psolve([14, 11, 6, 5, 2])
# psolve([-1, -3, 3, -7])
# psolve([-1111, -1001, 4, 7, 11])
# psolve([3, 4, 5, 7, 6])
# psolve([2, 4, 7, 11, 13])