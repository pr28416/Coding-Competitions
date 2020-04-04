T = int(input())

def split(x):
    if len(x) == 1:
        return x
    
    a = split(x[:len(x)//2])
    b = split(x[len(x)//2:])
    return merge(a, b)

def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]:
            x.append(a.pop(0))
        elif a[0][0] > b[0][0]:
            x.append(b.pop(0))
        else:
            if a[0][1] < b[0][1]:
                x.append(a.pop(0))
            else:
                x.append(b.pop(0))
    
    while len(a) > 0:
        x.append(a.pop(0))

    while len(b) > 0:
        x.append(b.pop(0))

    return x

def split2(x):
    if len(x) == 1:
        return x
    
    a = split(x[:len(x)//2])
    b = split(x[len(x)//2:])
    return merge2(a, b)

def merge2(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][2] < b[0][2]:
            x.append(a.pop(0))
        else:
            x.append(b.pop(0))
    
    while len(a) > 0:
        x.append(a.pop(0))

    while len(b) > 0:
        x.append(b.pop(0))

    return x

def test(activities):
    times = split(activities)
    # print("\nstarting times: %s" % times)
    c_working_hours = [times.pop(0)]
    c_working_hours[0].append("C")
    t = 0
    while t < len(times):
        if times[t][0] >= c_working_hours[len(c_working_hours)-1][1]:
            c_working_hours.append(times.pop(t))
            c_working_hours[len(c_working_hours)-1].append("C")
            t -= 1
        t += 1

    # print("\nTimes after c_working took: %s" % times)

    j_working_hours = []
    if len(times) != 0:
        t = 0
        j_working_hours = [times.pop(0)]
        j_working_hours[0].append("J")
        while t < len(times):
            if times[t][0] >= j_working_hours[len(j_working_hours)-1][1]:
                j_working_hours.append(times.pop(t))
                j_working_hours[len(j_working_hours)-1].append("J")
                t -= 1
            t += 1

    # print("\nC: %s\nJ: %s" % (c_working_hours, j_working_hours))
    if len(times) > 0:
        return "IMPOSSIBLE"

    sch = []
    while len(c_working_hours) > 0 and len(j_working_hours) > 0:
        if c_working_hours[0][0] < j_working_hours[0][0]:
            sch.append(c_working_hours.pop(0))
        else:
            sch.append(j_working_hours.pop(0))

    while len(c_working_hours) > 0:
        sch.append(c_working_hours.pop(0))

    while len(j_working_hours) > 0:
        sch.append(j_working_hours.pop(0))

    sch = split2(sch)
    # print("\n\nfinal: %s" % sch)
    e = []
    for i in sch:
        e.append(i[3])
    return "".join(e)

for t in range(T):
    N = int(input())
    times = []
    for n in range(N):
        f = [int(i) for i in input().split(" ")]
        f.append(n)
        times.append(f)

    e = test(times)
    print("Case #%s: %s" % (t+1, e))