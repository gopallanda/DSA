def intervalListIntersection(firstList,secondList):
    res=[]
    i,j=0,0
    while i<len(firstList) and j<len(secondList):
        a1,b1=firstList[i]
        a2,b2=secondList[j]
        start=max(a1,b1)
        end=min(a2,b2)
        if start<=end:
            res.append([start,end])
        if a2<b2:
            i+=1
        else:
            j+=1
    return res 