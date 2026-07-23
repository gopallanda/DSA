from collections import defaultdict
def removeBadElements(a,nums):
    myDict={}
    for num in nums:
        myDict[num]=1+myDict.get(num,0)
    print(myDict)
    if len(myDict.keys())==1:
        return 0
    else:
        max_ele=0
        for keys in myDict.keys():
            current_max=myDict[keys]
            if current_max
        
            
        