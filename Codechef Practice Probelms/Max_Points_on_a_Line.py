def maxPoints(points):
    best = 1
    for i in range(len(points)):
        for j in range(i):
            def onLine(p):
                return (p[0] - points[i][0]) * (points[j][1] - points[i][1]) \
                       == (p[1] - points[i][1]) * (points[j][0] - points[i][0])

            best = max(best, sum(onLine(p) for p in points))
    return best
