file = open("textfile.txt", "a+")
file.write("Hello Welcome to the World of Python")
file.seek(0)
line = file.readline()
print(line)
words = line.split()
print(words)
file.close()
#if we will execute write or writelines methods in "r+" or "w/w+" mode 
# old data will erase and new data will be added to the file 
#to add new data with old data we have to execute write and writelines in "a" mode 
# out put is [] because in r+ mode the file pointer is go to begining of the file
# after file.write the filepointer will go to last character of the line then checks
# for the line to split where nothing is there
# instead we can use seek(0) to go at the begining
# import os
# file = open("textfile.txt", "w+")
# file.write("Hello Welcome to the World of Python")
# file.close()
# print(file.closed)
# file = open("textfile.txt", "r")

# line = file.readline()
# words = line.split()
# print(words)
# file.close()

