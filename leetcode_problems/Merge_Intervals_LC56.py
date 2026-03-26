def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    res=[intervals[0]]
    for i in range(1,len(intervals)):
        current=intervals[i]
        prev=res[-1]
        if current[0]<=prev[1]:
            prev[1]=max(prev[1],current[1])
        else:
            res.append(current)
    return res