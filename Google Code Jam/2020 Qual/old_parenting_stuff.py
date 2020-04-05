
def test(activities):
    times = split(activities)

    maxTime = 0
    for t in times:
        if t[1] > maxTime:
            maxTime = t[1]

    workingTimes = [0 for i in range(maxTime+1)] # 0 --> ending activity's start
    # print(workingTimes[len(workingTimes)-1])
    # startTimes = {i[0] for i in times}

    for i in times:
        for j in range(i[0], i[1]):
            workingTimes[j] += 1

    for i in workingTimes:
        if i > 2:
            return "IMPOSSIBLE"

    c_start, c_end = -1, -1
    j_start, j_end = -1, -1
    for t in times:
        # Check if Cameron is not working
        if c_start == -1 or c_end <= t[0]:
            # Make Cameron work
            c_start, c_end = t[0], t[1]
            t.append("C")

        # Cameron is working
        else:
            # Check if Jamie is not working
            if j_start == -1 or j_end <= t[0]:
                # Make Jamie work
                j_start, j_end = t[0], t[1]
                t.append("J")
            
            # Jamie is working
            else:
                # print("what?")
                return "IMPOSSIBLE"
    
    times = split2(times)
    fin = "".join([i[3] for i in times])
    return fin

def test2(activities):
    minTime = activities[0][0]
    maxTime = activities[0][1]
    for i in activities:
        if i[0] < minTime:
            minTime = i[0]
        if i[1] > maxTime:
            maxTime = i[1]

    fin = ""
    workingTimes = [[0, 0] for i in range(0, maxTime+1)]
    for interval in activities:
        # Check if Cameron is not working
        if workingTimes[interval[0]][0] == 0 and workingTimes[interval[1]][0] == 0:
            # Cameron is not working
            for i in range(interval[0], interval[1]):
                workingTimes[i][0] = 1

            fin += "C"

        # Cameron is working
        else:
            # Check is Jamie is not working
            if workingTimes[interval[0]][1] == 0 and workingTimes[interval[1]][1] == 0:
                # Jamie is not working
                for i in range(interval[0], interval[1]):
                    workingTimes[i][1] = 1

                fin += "J"
            
            # Jamie is working
            else:
                # Everyone is working
                return "IMPOSSIBLE"

    return fin

def checkAvailability(times):
    maxTime = 0
    for i in times:
        if i[1] > maxTime:
            maxTime = i[1]
    periods = [0 for i in range(maxTime+1)]

    for t in times:
        for i in range(t[0], t[1]):
            periods[i] += 1
            if periods[i] == 2:
                return False
    
    return True
