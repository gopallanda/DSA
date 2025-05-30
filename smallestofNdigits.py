n = int(input("enter number of digits :"))
p = int(input("enter a  n digit number:"))
if p == 10 ** (n - 1):
    print("the entered number is the smallest n digit number")
else:
    print("entered number is not an n digit smallest number")
