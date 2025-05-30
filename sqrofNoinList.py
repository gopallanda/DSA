n=int(input("enter the number of elements in the list:"))
list1=[]
for i in range(n):
    list1.append(int(input(f"enter the element{i+1}:")))
list2=[i*i for i in list1]
print("squares of the elements:")
print(list2)    
