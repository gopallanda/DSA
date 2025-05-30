# a=int(input("enter value of a :"))
# b=int(input("enter value of b :"))
# c=[1,2,3,4,5]
# try:
#      d=a/b
#      print(d)
# except ZeroDivisionError:
#     print("can't divide by zero..")
# try:
#     print(c[11])
# except IndexError:
#     print("index out of bounds...")
    
# enter value of a :2
# enter value of b :0
# can't divide by zero..
# index out of bounds...

# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=[1,2,3,4,5]
# try:
#     d=a/b
#     print(d)
#     print(c[6])
# except (ZeroDivisionError, IndexError):
#     print("exception raised...")
# enter a:1
# enter b:0
# exception raised...


# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=[1,2,3,4,5]
# try:
#     print(a/b)
#     print(c[10])
# except ZeroDivisionError:
#     print("can't divide zero..")
# except IndexError:
#     print("index out of bounds..")
    
# enter a:4
# enter b:0
# can't divide zero..