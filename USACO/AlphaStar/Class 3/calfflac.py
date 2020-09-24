string = ""
for i in range(2500):
    try: string += input() + "\n" # f"{i}:"
    except: break

# print(string)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print('preparing')
modString = "#".join(list(string))
# print(modString)
code = [1 if i.lower() in alphabet else 0 for i in modString]
# print('starting')

def expand(string, idx):
    # Single center
    fin = (idx, idx)
    lo, up = idx, idx
    while lo > -1 and up < len(string):
        if not code[lo]: lo -= 1
        elif not code[up]: up += 1
        elif string[lo].lower() == string[up].lower():
            fin = (lo, up)
            lo -= 1; up += 1
        else: break

    return fin

    # if idx == len(string)-1: return (singleFin,)
    # # Double center

    # doubleFin = (idx, idx+1)
    # lo, up = idx, idx+1
    # while lo > -1 and up < len(string):
    #     if not code[lo]: lo -= 1
    #     elif not code[up]: up += 1
    #     elif string[lo].lower() == string[up].lower():
    #         singleFin = (lo, up)
    #         lo -= 1; up += 1
    #     else: break

    # return (singleFin, doubleFin)

answers = []
for i in range(len(modString)):
    # print(f"{i}: {string[i]}")
    answers.append(expand(modString, i))
        # print(j)
# if string[:4] == "AAAA": raise Exception("breakpoint")
# print('sorting')

# for answer in answers:
#     print(string[answer[0]:answer[1]+1])

answers.sort(key=lambda x: (-(x[1]-x[0]), x[0]))
# print(answers)
answer = modString[answers[0][0]:answers[0][1]+1]
del answers
# print(answer)
# print(answer)
answer = "".join([answer[i] for i in range(0, len(answer), 2)])
length = 0
for i in answer:
    if i.lower() in alphabet: length += 1

print(length)
print(answer)