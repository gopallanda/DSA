# str = input("enter a string..:")
# l = len(str)
# print(l)
# rev = ""
# for i in range(l):
#     rev = rev + str[l - i - 1]
# print(rev)
# print(str[::-1])


# def noOfVowels(str):
#     l = len(str)
#     a = "aeiouAEIOU"
#     count = 0
#     for i in range(l):
#         if str[i] in a:
#             count = count + 1

#     return count


# str = input("enter a string :")
# counts = noOfVowels(str)
# print("number of vowels in the string:", counts)


# def removeChar(name, chr):
#     for i in range(len(name)):
#         if name[i] == chr:
#             name = name.replace(name[i], "")
#             #break to find bug don't use break statement
#     return name


# name = input("enter a string:")
# chr = input("enter a character to remove:")
# res = removeChar(name, chr)
# print(res)
# there is a bug in above code find it ✌️
 
# def removeChar(name, chr):
#     name=name.replace(chr,"")
#     return name


# name = input("enter a string:")
# chr = input("enter a character to remove:")
# res = removeChar(name, chr)
# print(res)

# str = "gopal"
# c = str.count("al", 0, len(str))
# if c == 0:
#     print("NO")
# else:
#     print("Yes")

# str = "Gopal landa"
# print(str[0 : len(str) : 2])

# str = "874"
# print(str.isdigit())


# str = "Gopal krishna gokhle"
# print(str.replace(" ", "-"))

#re module
# import re
# name="Landa Gopal"
# sub1="Landa"
# sub2="Gopal"
# print(re.match(sub1,name))
# print(re.match(sub2,name))
# if re.match(sub1,name):
#     print("match found..")
# else:
#     print("match not found")


# The re.match() function does not directly return True or False. Instead, it returns:
# A match object if a match is found.
# None if no match is found.

import re
name="Landa Gopal"
sub1="Landa"
sub2="Gopal"
print(re.search(sub1,name))
print(re.search(sub2,name))
if re.search(sub2,name):
    print("match found..")
else:
    print("match not found")