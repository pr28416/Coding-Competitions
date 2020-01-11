initBarn1 = []
initBarn2 = []

barnStorage1 = 1000
barnStorage2 = 1000

with open("backforth.in", "r") as f:
    initBarn1 = [int(i) for i in f.readline().split(" ")]
    initBarn2 = [int(i) for i in f.readline().split(" ")]

# print(initBarn1)
# print(initBarn2)
possibleBarn1Storages = []

def recurseThrough(barn1, barn2, storage1, storage2, lvl):
    # Select bucket a
    if lvl == 4:
        if storage1 not in possibleBarn1Storages:
            possibleBarn1Storages.append(storage1)
            # print(storage1)
    else:
        if lvl % 2 == 0:
            # Move a from row 1 to row 2
            a = 0
            while a < len(barn1):
                val = barn1.pop(a)
                
            
                # Test it
                storage1 -= val
                storage2 += val
                barn2.append(val)
                # print(lvl)
                # print("a: %s" % a)
                # print(barn1)
                # print(barn2)
                recurseThrough(barn1, barn2, storage1, storage2, lvl+1)

                # Move it back
                storage1 += val
                storage2 -= val
                barn1.insert(a, val)
                barn2.pop()
                a += 1
                # print(barn1)
                # print(barn2)
        else:
            # Move a from row 2 to row 1
            a = 0
            while a < len(barn2):
                val = barn2.pop(a)
                

                # Test it
                storage2 -= val
                storage1 += val
                barn1.append(val)
                # print(lvl)
                # print("a: %s" % a)
                # print(barn1)
                # print(barn2)
                recurseThrough(barn1, barn2, storage1, storage2, lvl+1)

                # Move it back
                storage2 += val
                storage1 -= val
                barn2.insert(a, val)
                barn1.pop()
                a += 1
                # print(barn1)
                # print(barn2)
        

recurseThrough(initBarn1, initBarn2, barnStorage1, barnStorage2, 0)
# print(possibleBarn1Storages)
# print(len(possibleBarn1Storages))
with open("backforth.out", "w") as f:
    f.write("%s\n"%len(possibleBarn1Storages))