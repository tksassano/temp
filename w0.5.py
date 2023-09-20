def calc_slope(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    try:
        m = (y1 - y0) / (x1 - x0)
    except:
        m = float("inf")
    return m

def draw_line(p0, p1):
    m = calc_slope(p0, p1)
    
    x, y = p0
    
    print(f"({x}, {y})")
    
    while (x, y) != p1:
        points = [(x+1, y+1), (x+1, y), (x, y+1)]
        slopes = [calc_slope(p0, point) for point in points]
        candidates = {points[i]: slopes[i] for i in range(len(points))}
        
        best = min(candidates, key=lambda point: abs(m - candidates[point]))
        x, y = best
        
        print(f"({x}, {y})")

draw_line((2, 1), (5, 10))
