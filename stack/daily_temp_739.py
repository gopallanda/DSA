''' daily temperatures leetcode problem 739, in this problem we are given a list of daily temperatures and we need to find out how many days we have to wait until a warmer temperature. If there is no future day for which this is possible, we should put 0 instead. 
example: input: temperatures = [73,74,75,71,69,72,76,73]
output: [1,1,4,2,1,1,0,0]'''

def dailyTemperatures(temperatures):
    n=len(temperatures)
    res=[0]*n
    stack=[]
    for i in range(n):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            pre_idx=stack.pop()
            res[pre_idx]=i-pre_idx
        stack.append(i)
    return res
if __name__=="__main__":
    temperatures=list(map(int,input("enter the temperatures:").split()))
    result=dailyTemperatures(temperatures)
    print("Output:", result)