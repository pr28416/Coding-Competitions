T = int(input())
for _ in range(T):
    A, B = map(lambda x: int(x)+1, input().split(" "))
    N = int(input())
    for _ in range(N):
        mid = (A+B)//2
        print(mid, flush=True)
        response = input()
        if response in {"CORRECT", "WRONG_ANSWER"}: break
        elif response == "TOO_BIG": B = mid
        else: A = mid+1