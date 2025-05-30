r=int(input("enter number of rows:"))
c=int(input("enter number of columns:"))
matrix=[]
for i in range(r):
    rows=[]
    for j in range(c):
        ele=int(input(f"enter value for ({i,j:})"))
        rows.append(ele)
    matrix.append(rows)
    
for i in range(r):
    for j in range(c):
        print(f"{matrix[i][j]} ",end="")
    print()
for i in range(r):
    print(f"sum of elements in row {i+1}: {sum(matrix[i])}")
for i in range(r):
    x=0
    for j in range(c):
        x+=matrix[j][i]
    print(f"sum of elements in column {i+1}: {x}")
        
    
#output
 
# enter number of rows:3
# enter number of columns:3
# enter value for ((0, 0))1
# enter value for ((0, 1))2
# enter value for ((0, 2))3
# enter value for ((1, 0))4
# enter value for ((1, 1))5
# enter value for ((1, 2))6
# enter value for ((2, 0))7
# enter value for ((2, 1))8
# enter value for ((2, 2))9
# 1 2 3
# 4 5 6
# 7 8 9
# sum of elements in row 1: 6
# sum of elements in row 2: 15
# sum of elements in row 3: 24
# sum of elements in column 1: 12
# sum of elements in column 2: 15
# sum of elements in column 3: 18




# we can write like this also...

# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# # Initialize the matrix
# matrix = [[0 for j in range(cols)] for i in range(rows)]
# #o/p of above line [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# for i in range(rows):
#     for j in range(cols):
#         matrix[i][j] = int(input(f"Enter element at position ({i},{j}): "))

# # Print the matrix
# for i in range(r):
#     for j in range(c):
#         print(f"{matrix[i][j]} ",end="")
#     print()