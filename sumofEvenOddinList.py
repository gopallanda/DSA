n=int(input("enter the number of elements in the list:"))
list1=[]
for i in range(n):
    list1.append(int(input(f"enter the element{i+1}:")))
negSum=0
pEvenSum=0
pOddSum=0
for i in list1:
    if i<0:
        negSum+=i
    elif i%2==0:
        pEvenSum+=i
    else:
        pOddSum+=i
print("Sum of negative numbers:",negSum)
print("Sum of Positive Even numbers:",pEvenSum)
print("Sum of Positive Odd numbers:",pOddSum)


    