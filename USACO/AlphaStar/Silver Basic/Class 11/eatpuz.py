C, B = map(int, input().split(" "))
calories = list(map(int, input().split(" ")))
maxCalories = 0

def recurse(i, cur):
    global C, B, calories, maxCalories
    if i == B:
        if cur > maxCalories: maxCalories = cur
    else:
        if cur > maxCalories and cur < C: maxCalories = cur
        for j in range(i, B):
            if cur+calories[j] <= C: recurse(j+1, cur+calories[j])

recurse(0, 0)
print(maxCalories)