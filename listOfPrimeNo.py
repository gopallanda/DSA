n=int(input("enter the range:"))
list1=[]
for i in range(n+1):
    j=1
    flag=0
    while j<=i:
        if i%j==0:
            flag+=1
            j+=1
        else:
            j+=1
    if flag==2:
        list1.append(i)
print("list of prime numbers:",list1)
print("sum of prime numbers:",sum(list1))