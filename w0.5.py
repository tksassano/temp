import math

def lineFromPoints(p1, p2):
    m = (p2[1]-p1[1]) / (p2[0]-p1[0])
    b = p2[1] - m * p2[0]
    def evaluate(x):
        return int(m * x + b)
    return m, evaluate

def getCandidates(f, m, p1, p2):
    x, y = p1
    if m > 0:
        candidates = [(x+1, y+1), (x+1, y), (x, y+1)]
    elif m < 0:
        candidates = [(x+1, y-1), (x+1, y), (x, y-1)]
    elif m == 0:
        candidates = [(x+1, y), (x-1, y)]
    else: 
        candidates = [(x, y+1), (x, y-1)]
    return candidates

def determineBest(f, m, p1, p2):
    x, y = p1
    candidates = getCandidates(f, m, p1, p2)
    closest = candidates[0]
    for p in candidates:
        d = math.dist(p, p2)
        if d < math.dist(closest, p2):
            closest = p
    return closest

def createLine(f, m, p1, p2):
    points = [p1]
    while p1 != p2:
        p1 = determineBest(f, m, p1, p2)
        points.append(p1)
    return points

p1 = (2, 1)
p2 = (5, 10)

m, f = lineFromPoints(p1, p2)

line = createLine(f, m, p1, p2)
print(line)
