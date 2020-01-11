def split(data):
    if len(data) == 1:
        return data
    else:
        a = split(data[0:int(len(data)/2)])
        b = split(data[int(len(data)/2):len(data)])
        return merge(a, b)

def merge(a, b):
    group = []

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            group.append(a.pop(0))
        else:
            group.append(b.pop(0))
    while len(a) > 0:
        group.append(a.pop(0))
    while len(b) > 0:
        group.append(b.pop(0))

    return group