N = 0
with open("moobuzz.in", "r") as f:
    N = int(f.readline())

a = [1, 2, 4, 7, 8, 11, 13, 14]
x = [8, 1, 2, 3, 4, 5, 6, 7]
c = (N-x[N%8])//8
b = a[N%8-1]+15*(c)
# print("%s = %s + 15 * (%s - %s mod 8)//8" % (b, a[N%8-1], N, N))
# print("%s = %s + 15 * (%s - %s)//8" % (b, a[N%8-1], N, N % 8))
# numbers = []
# i = 1
# while len(numbers) < N:
#     if not (i % 3 == 0 or i % 5 == 0):
#         numbers.append(i)
#     i += 1
# b = numbers[len(numbers)-1]

with open("moobuzz.out", "w") as f:
    f.write("%s\n" % b)