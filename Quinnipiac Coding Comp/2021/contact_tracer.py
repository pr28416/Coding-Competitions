from collections import deque

class Node:
    def __init__(self, person, num):
        self.person = person
        self.num = num
        self.neighbors = []
        self.proximity = 0
        self.infected = False
        self.visitCount = 0
    def addNeighbor(self, node):
        self.neighbors.append(node)
    def __str__(self):
        return f"({self.num}) {self.person}: isInfected ({self.infected}), neighbors ({self.neighbors})"
        # return f"{self.person}, {self.neighbors}"
    def __repr__(self): return f"{self.person}"
    def __eq__(self, other):
        return self.num == other.num

def solve(nodes, infected, D):
    setOfSets = []
    for idx, infectee in enumerate(infected):
        deq = deque()
        deq.appendleft(infectee)
        setOfSets.append(set())
        while len(deq) > 0:
            person = deq.pop()
            setOfSets[idx].add(person.num)
            if person.proximity >= D: continue
            for neighbor in person.neighbors:
                if not neighbor.infected:
                    neighbor.infected = True
                    neighbor.proximity = person.proximity+1
                    deq.appendleft(neighbor)
        for i in nodes:
            if i not in infected:
                i.infected = False
    bigSet = set()
    for s in setOfSets:
        bigSet = bigSet.union(s)
    return len(bigSet)

T = int(input())
for _ in range(T):
    peopleDict = {}
    N = int(input())
    nodes = [None] * N
    infectedPeeps = []
    for i in range(N):
        nodes[i] = Node(input().strip("\n"), i)
        peopleDict[nodes[i].person] = i
    E = int(input())
    for i in range(E):
        indiv1, indiv2 = input().split(" ")
        indiv1.strip("\n")
        indiv2.strip("\n")
        nodes[peopleDict[indiv1]].addNeighbor(nodes[peopleDict[indiv2]])
        nodes[peopleDict[indiv2]].addNeighbor(nodes[peopleDict[indiv1]])
    K, D = map(int, input().split(" "))
    for i in range(K):
        j = peopleDict[input().strip("\n")]
        nodes[j].infected = True
        infectedPeeps.append(nodes[j])
    # for node in nodes:
        # print(node)
    # print("infected:", infectedPeeps)
    print(solve(nodes, infectedPeeps, D))
    # print(nodes[0])