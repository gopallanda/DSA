# yield function
# ✅ What is a Generator in Python?
# A generator is a special type of function that produces a sequence of results lazily, meaning it generates values on the fly and does not store the entire sequence in memory.
# Generators are written like regular functions but use the yield statement instead of return.

# normal function 
def function(n):
    for i in range(n):
        return i

res=function(5)
print(res) #0

# in the above example using return statement we can retrieve only one element

def fun(n):
    for i in range(n):
        yield i
for v in fun(5):
    print(v)
# out put
# 0
# 1
# 2
# 3
# 4
# using this generators we can iterate over a function

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
for num in fibonacci(10):
    print(num, end=' ')

from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
    
    
    