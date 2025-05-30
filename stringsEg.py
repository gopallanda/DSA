# STRINGS...
# message = "Hello"
# index = 0
# for i in message:
#     print("message[", index, "] ", i)
#     index += 1

# message[ 0 ]  H
# message[ 1 ]  e
# message[ 2 ]  l
# message[ 3 ]  l
# message[ 4 ]  o

# str3 = "hello, welcome to python"
# # i = 2
# # print(str[i])
# # print(str[i * 3 + 1])


# str1 = "hello"
# var = 4


# str2 = str1 + str(var)  ## we are doing type casting here
# print(str2)
# text = input("enter a string..:")
# space1 = text.find(" ")
# space2 = text.find(" ", space1 + 1)
# space3 = text.find(" ", space2 + 1)
# newtext = text[0] + ". " + text[space1 + 1] + ". " + text[space2 + 1]
# print("New string:", newtext)
# # output
# # enter a string..:Landa Gopal Krishna
# # New string: L. G. K

##Palindrome or not

# string = input("enter a string: ")
# rev = string[::-1]
# if string == rev:
#     print(string, ": is a palindrome")
# else:
#     print(string, ":is not a palindrome")

# l = len(string)
# for i in range(l):
#     t = string[i:l] + string[0:i]
#     print(t)
# output
# madam
# adamm
# damma
# ammad
# mmada
name = "tony stark"
print(name.replace("tony", "gopal"))  # o/p gopal stark
# actual string is not changed if we do any sort of operations new string will be formed
print(name)  # o/p  tony stark
print("tony" in name)  # True
print("gopal" in name)  # False

# ----------------------------------Day-3--------------------------------------------------
