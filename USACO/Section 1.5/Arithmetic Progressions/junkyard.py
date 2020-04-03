def alg2():
    for (i, b) in enumerate(bisquares):
        # print("Starting b: %s" % b)
        for incrementer in range(1, int((bisquares[len(bisquares)-1]+1)/2)+2):
            # print("Starting incrementer: %s" % incrementer)
            counter = 1
            keepGoing = True
            while keepGoing and counter < N:
                keepGoing = False
                if b+incrementer*counter in bisquares[i:]:
                    # print("\t%s works" % (b+incrementer*counter))
                    keepGoing = True
                    counter += 1
            if counter == N:
                answers.append([b, incrementer])

def alg3():
    cycles = 0
    last = bisquares[len(bisquares)-1]
    # Generate sequences
    for (i1, b) in enumerate(bisquares):
        for d in bisquares[i1+1:]:
            incrementer = d-b

            # Check if a sequence of at least 3 will appear
            if b+2*incrementer <= last:
                if b+2*incrementer in bisquares:
                    seq = [b]
                    counter = 1
                    keepGoing = True
                    while keepGoing:
                        keepGoing = False
                        cycles += 1
                        if b+incrementer*counter in bisquares[i1:]:
                            keepGoing = True
                            seq.append(b+incrementer*counter)
                            counter += 1

                    # print(seq)
                    if len(seq) == N:
                        answers.append([b, incrementer])
                    elif len(seq) > N:
                        for i in range(len(seq)+1):
                            cycles += 1
                            answers.append([i, incrementer])
            else:
                break
    
    return cycles

def alg2_2():
    cycles = 0
    for(i1, b) in enumerate(bisquares):
        if i1 < len(bisquares)-1:
            if b + 2*(bisquares[i1+1]-b) <= bisquares[len(bisquares)-1]:
                for c in bisquares[i1+1:]:
                    incrementer = c-b
                    if bisquares[len(bisquares)-1]-(b+incrementer*(N-1)) >= 0:
                        counter = 1
                        keepGoing = True

                        # Generate the sequence
                        seq = [b]
                        while counter < N:
                            seq.append(b+incrementer*counter)
                            counter += 1
                            cycles += 1

                        # print(seq)

                        x = i1 # For bisquares
                        y = 0 # For seq

                        # if b == 37 and incrementer == 3:
                        #     print(37, 3)

                        # print(keepGoing, x < len(bisquares), y < len(seq))
                        while keepGoing and x < len(bisquares) and y < len(seq):
                            # print("M - ", end="")
                            cycles += 1
                            keepGoing = False
                            # if b == 37 and incrementer == 4: print("Checking", y)
                            if bisquares[x] == seq[y]:
                                keepGoing = True
                                x, y = x+1, y+1
                            elif bisquares[x] < seq[y]:
                                keepGoing = True
                                x += 1
                            else: # bisquares[x] > seq[y]
                                break
                        
                        # if b == 37 and incrementer == 4: print("Final", y)
                        if y == N:
                            answers.append([b, incrementer])

                    else:
                        break
            else:
                break
        else:
            break
    return cycles


def alg2_3():
    cycles = 0
    for(i1, b) in enumerate(bisquares):
        if i1 < len(bisquares)-1:
            if b + 2*(bisquares[i1+1]-b) <= bisquares[len(bisquares)-1]:
                for c in bisquares[i1+1:]:
                    incrementer = c-b
                    if bisquares[len(bisquares)-1]-(b+incrementer*(N-1)):
                        # print("N: %s, b: %s, incrementer: %s, bisquares[%s]: %s" % (N, b, incrementer, end, bisquares[end]))
                        counter = 1
                        while counter < N and binaryFind(b+incrementer*counter, bisquares) != -1:
                            counter += 1
                        if counter == N:
                            answers.append([b, incrementer])
                    else:
                        break
            else:
                break
        else:
            break
    return cycles

def alg5():
    for(i1, b) in enumerate(bisquares):
        # print("A: b =", b)
        if i1 < len(bisquares)-1:
            if b + 2*(bisquares[i1+1]-b) <= bisquares[len(bisquares)-1]:
                for c in bisquares[i1+1:]:
                    incrementer = c-b
                    # print("\tB: incrementer =", incrementer)
                    if [b, incrementer] not in answers:
                        if (b+2*incrementer in bisquares[i1:]):
                            if bisquares[len(bisquares)-1]-(b+incrementer*(N-1)) >= 0:
                                counter = 3
                                keepGoing = True
                                while keepGoing:
                                    # print("\t\tC: counter =", counter)
                                    cycles += 1
                                    keepGoing = False
                                    if b+incrementer*counter in bisquares[i1:]:
                                        keepGoing = True
                                        counter += 1
                                # print(b, incrementer, counter)
                                if counter == N:
                                    answers.append([b, incrementer])
                                elif counter > N:
                                    numProgressions = N-counter+1
                                    for i in range(numProgressions):
                                        answers.append(b+i*incrementer, incrementer)
                            else:
                                break
            else:
                break
        else:
            break