def isPalindrome(s, start=0, end=None):
    if end is None:
        end = len(s) - 1
    while start < end and not s[start].isalnum():
        start += 1
    while start < end and not s[end].isalnum():
        end -= 1
    if start >= end:
        return True
    if s[start].lower() != s[end].lower():
        return False
    return isPalindrome(s, start + 1, end - 1)


if __name__ == "__main__":
    s = input("Enter the string:")
    result = isPalindrome(s)
    if result:
        print("The string is a valid palindrome.")
    else:
        print("The string is not a valid palindrome.")
