def rearrangeString(s, n):
    s, groups, lo = s+"-", [], 0

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            groups.append(s[lo:i])
            lo = i
    groups.sort(key=lambda x: (-len(x), x[0]))

    for i in range(len(groups)-1, 0, -1):
        if groups[i][0] == groups[i-1][0]:
            groups[i-1] = (groups[i]+groups[i-1])[:n]
            del groups[i]
    
    for i in range(len(groups)):
        groups[i] = groups[i][:n]
    
    return "".join(groups)