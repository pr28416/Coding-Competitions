def isPrime(n):
    if n == 2 or n == 3 or n == 5: return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n < 2: return False
    else:
        for i in range(3, int(n**0.5), 2):
            if n % i == 0:
                return False
        return True

primes = [i for i in range(2, int(2*10E5)) if isPrime(i)]
# products = [primes[i] * primes[i+1] for i in range(len(primes)-1)]
# print(len(primes))

# def primes1(n):
#     """ Returns  a list of primes < n """
#     sieve = [True] * (n//2)
#     for i in range(3,int(n**0.5)+1,2):
#         if sieve[i//2]:
#             sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
#     return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

# primes = primes1(10**9)

# def bs(x, lst):
#     lo, up = 0, len(lst)
#     while lo < up:
#         y = (lo+up)//2
#         if x <= lst[y]: up = y
#         else: lo = y+1
#     return lo

from bisect import bisect_right as bs

T = int(input())
for t in range(1, T+1):
    Z = int(input())
    # i = 0
    # while i < len(products):
    #     if products[i] > Z:
    #         i -= 1
    #         break
    #     i += 1
    # print(f"Case #{t}:", products[i])

    # print(f"Case #{t}:", products[bs(products, Z)-1])

    # lo, up = 0, len(primes)-1
    # while lo < up:
    #     y = (lo+up)//2
    #     if primes[y]*primes[y+1] > Z: up = y
    #     else: lo = y+1
    # print(f"Case #{t}:", primes[lo-1]*primes[lo])

    idx = bs(primes, int(Z**0.5))
    # print(Z, Z**0.5, idx)
    # print("checking", idx, "which is", primes[idx])
    while idx >= 0:
        if idx == len(primes)-1:
            idx -= 1
        elif primes[idx] * primes[idx+1] > Z:
            idx -= 1
        else:
            print(f"Case #{t}:", primes[idx]*primes[idx+1])
            break
    else:
        print(f"Case #{t}: 2")