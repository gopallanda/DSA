n = int(input("enter the n value:"))
val = int(input("enter the number:"))
if n == 0:
    print("n should'nt be 0, enter n value again✌️")
elif n == 1:
    if val == 0:
        print(f"{val} is the smallest {n} digit number")
    else:
        print(f"{val} is not the smallest {n} digit number")
else:
    if val == 10 ** (n - 1):
        print(f"{val} is the smallest {n} digit number")
    else:
        print(f"{val} is not the smallest {n} digit number")
