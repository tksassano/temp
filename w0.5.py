from math import dist

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p1[1] == p2[1]:
            self.m = None
        else:
            self.m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        self.b = p2[1] - self.m * p2[0]
        
    def evaluate(self, x):
        return int(self.m * x + self.b)
    
    def getCandidates(self, point):
        x, y = point
        if self.m > 0:
            return [(x+1, y+1), (x+1, y), (x, y+1)]
        elif self.m < 0:
            return [(x+1, y-1), (x+1, y), (x, y-1)]
        elif self.m == 0:
            return [(x+1, y), (x-1, y)]
        else:
            return [(x, y+1), (x, y-1)]
    
    def determineBest(self, point):
        candidates = self.getCandidates(point)
        closest = candidates[0]
        for p in candidates:
            d = dist(p, self.p2)
            if d < dist(closest, self.p2):
                closest = p
        return closest
    
    def createLine(self):
        points = [self.p1]
        while self.p1 != self.p2:
            self.p1 = self.determineBest(self.p1)
            points.append(self.p1)
        return points

p1 = (2, 1)
p2 = (5, 10)
line = Line(p1, p2)
print(line.createLine())
