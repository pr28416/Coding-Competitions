def solution(xs):

    def merge(a, b):
        x = []
        while len(a) > 0 and len(b) > 0:
            if a[0] < b[0]:
                x.append(a.pop(0))
            else:
                x.append(b.pop(0))
        while len(a) > 0:
            x.append(a.pop(0))
        while len(b) > 0:
            x.append(b.pop(0))
        return x

    def split(x):
        if len(x) == 1:
            return x
        a = split(x[:len(x)//2])
        b = split(x[len(x)//2:])
        return merge(a, b)

    # Sort into positive and negative
    pos, neg = [], []
    
    for i in xs:
        if i > 0:
            for j in range(len(pos)):
                if pos[j] > i:
                    pos.insert(j, i)
                    break
            else:
                pos.append(i)
        elif i < 0:
            for j in range(len(neg)):
                if neg[j] > i:
                    neg.insert(j, i)
                    break
            else:
                neg.append(i)

    if len(pos) != 0 or len(neg) != 0:    
        # if len(pos) > 0:
        #     pos = split(pos)
        # if len(neg) > 0:
        #     neg = split(neg)
        # print(pos, neg)

        # Accumulate product
        product = 1
        for i in pos:
            product *= i
        for i in range(0, len(neg)-1, 2):
            product *= (neg[i] * neg[i+1])

        print str(product)
    else:
        print "0"

def solution(xs):
    # Sort into positive and negative
    pos, neg, zeroes = [], [], 0
    for i in xs:
        if i > 0:
            for j in range(len(pos)):
                if pos[j] > i:
                    pos.insert(j, i)
                    break
            else:
                pos.append(i)
        elif i < 0:
            for j in range(len(neg)):
                if neg[j] > i:
                    neg.insert(j, i)
                    break
            else:
                neg.append(i)
        else:
            zeroes += 1

    if len(pos) != 0 or len(neg) != 0:
        if len(pos) == 0 and len(neg) == 1:
            if zeroes > 0:
                print "0"
            else:
                print str(neg[0])
        else:
            # print(pos, neg)
            # Accumulate product
            product = 1
            for i in pos:
                product *= i
            for i in range(0, len(neg)-1, 2):
                product *= (neg[i] * neg[i+1])

            print str(product)
    else:
        print "0"

# solution([2, -3, 1, 0, -5])
# solution([2, 0, 2, 2, 0])
# solution([-2, -3, 4, -5])
solution([0, -1, -2])