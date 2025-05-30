# lists = ["Gopal", 448, True, "IT-A", 9.8]
# lists[2] = False
# print(lists)
# print(type(lists))
# del lists[1]
# print(lists)
# del lists[::]
# print(lists)
# mylist = [1, 2, 3, 4]

# mylist.insert(4, 0)
# print(mylist.sort())
# print(mylist)
# a = [3, 5, 7, 3, 5, 8, 5, 9]
# b = sorted(a)
# print(sorted(a))

list1=['a','1','8','3','b','ccc','gop','998']
print(max(list1))
print(min(list1))
list1.pop(1)
print(list1)

#print(sum(list1))
#if list contains numbers, alphabets and strings
#max fun returns longest string, min fun() returns smallest number
#if alphabets and numbers are present max fun returns largest alphabet(ASCII) and min fun() returns smallest number 
#if only numbers  exist then it works asusual
#for sum fun() all elemnets should be integers otherwise it throw TypeError