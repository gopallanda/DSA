#key word arguments
# def display(age,gender,name):
#     print(name,age,gender)
# display(gender='m',name='gopal',age=19)
# ---------------------------------------------------------------------------------------
#default arguments
# def display(name,age,deg='Btech'):
#     print(name,age,deg)
# display(name='gopal',age=22,deg='MBBS')
# display('gopal',22,'MBBS')
# display(22,'MBBS')
#display(name='gopal', 22, deg='MBBS')  #throw error
# ---------------------------------------------------------------------------------------

#value length parameters
# def add(x,*values):
#     print(x+sum(values))
# add(2,3)
# add(2,3,4,5)
# def addition(x,*values):
#     s=0
#     for i in values:
#         s+=i 
#     print("sum=",x+s)   
# addition(2,3)
# addition(2,3,4,5)

def add(*values):
    s=0
    for i in values:
        s+=i
    print(s)
add(2,3)
add(2,3,4,5)