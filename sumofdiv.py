n=4 
myList=[]
for i in range(1,n+1):
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=j
    myList.append(s)
print(sum(myList))   

# optimized code

# def sumOfDivisors(self, n):
#     	#code here 
#     	res=0
#     	for i in range(1,n+1):
#     	    res+=i*(n//i)
#     	return res