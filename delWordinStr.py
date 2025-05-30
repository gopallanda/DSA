string=input("enter a string:")
words=string.split()
print(words)
delete=input("enter a word to be delete:")
newStr=" ".join(word for word in words if word.lower()!=delete)
#newStr=string.replace(delete, "")  can write like this also
print(newStr)