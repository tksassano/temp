import math

def lineFromPoints(p1, p2):
    m = (p2[1]-p1[1]) / (p2[0]-p1[0])
    b = p2[1] - m * p2[0]
    def evaluate(x):
        return int(m * x + b)
    return evaluate

def determineBest(f, p1, p2):
    x = p1[0]
    y = p1[1]
    candidates = [(x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
    closest = candidates[0]
    for p in candidates:
        d = math.dist(p, p2)
        if d < math.dist(closest, p2):
            closest = p
    return closest

p1 = (2, 1)
p2 = (5, 10)
points = []

f = lineFromPoints(p1, p2)
print(determineBest(f, p1, p2))
