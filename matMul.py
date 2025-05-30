r1=int(input("enter no of rows for matrix 1:"))
c1=int(input("enter no of columns for matrix 1:"))
mat1=[]
print("enter matrix 1 elements:")
for i in range(r1):
    t=[]
    for j in range(c1):
        x=int(input(f"enter the value of({i,j}:"))
        t.append(x)
    mat1.append(t)
mat2=[]
r2=int(input("enter no of rows for matrix 2:"))
c2=int(input("enter no of columns for matrix 2:"))
print("enter matrix 2 elements:")
for i in range(r2):
    t=[]
    for j in range(c2):
        x=int(input(f"enter the value of({i,j}:"))
        t.append(x)
    mat2.append(t)
print("entered matrix1")
for i in range(r1):
    for j in range(c1):
        print(mat1[i][j],end=" ")
    print()
print("entered matrix2")
for i in range(r2):
    for j in range(c2):
        print(mat2[i][j],end=" ")
    print()
if c1!=r2:
    print("Matrix multiplication not possible, please ensure col1=row2")
else:
    mat3=[ [0 for j in range(r2)] for i in range(c1)]
    #sum=0
    for i in range(r2):
        for j in range(c1):
            for k in range(r2):
                mat3[i][j]+=mat1[i][k]*mat2[k][j]
print("resultant matrix:")
for i in range(r2):
    for j in range(c1):
        print(mat3[i][j],end=" ")
    print()
    
            
        
