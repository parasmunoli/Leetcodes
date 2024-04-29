def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        time += max(abs(x2 - x1), abs(y2 - y1))
    return time
points = [[1,1],[3,4],[-1,0]]
print(minTimeToVisitAllPoints(points))