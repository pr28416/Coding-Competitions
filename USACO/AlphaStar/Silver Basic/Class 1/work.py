# Sorting using a key
a = [-2, -10, 3, 5, 7]
print("Before:", a)
a.sort(key=lambda x: abs(x))
print("After:", a)

# Sorting using two keys
a = [(1, 3), (2, 5), (3, 4), (2, 1), (3, 2)]
print("Before:", a)
a.sort()
print("After:", a)

a = ["aaa", "cc", "d", "bb", "eee"]
print("Before:", a)
a.sort(key=lambda x: (len(x), x))
print("After:", a)