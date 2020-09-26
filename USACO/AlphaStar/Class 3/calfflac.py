import time
string = ""
for i in range(2500):
    try: string += input() + "\n" # f"{i}:"
    except: break

alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = "#".join(list(string))
# print(string)
code = [1 if i.lower() in alphabet else 0 for i in string]

# print('begin')
answer = (len(string), len(string))
#avg = 0
start = time.time()
for i in range(len(string)):
    #steps = 0
    # print('lapse', i)
    fin = None
    if i % 2 == 1: fin = (i-1, i+1)
    else: fin = (i, i)
    # fin = (i, i)
    lo, up = fin

    while lo > -1 and up < len(string):
        #steps += 1
        if not code[lo]: lo -= 2
        elif not code[up]: up += 2
        elif string[lo].lower() == string[up].lower():
            fin = (lo, up)
            lo -= 2; up += 2
        else: break
    #avg += steps
    if fin[1]-fin[0]>answer[1]-answer[0]: answer=fin
    elif fin[1]-fin[0]==answer[1]-answer[0] and fin[0]<=answer[0]: answer=fin


# print('end - ', avg/len(string))
answer = string[answer[0]:answer[1]+1]
# print(answer)
answer = "".join([answer[i] for i in range(0, len(answer), 2)])
count = 0
for i in answer:
    if i.lower() in alphabet: count += 1
print(count)
print(answer)