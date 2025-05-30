s1 = int(input("enter marks in test 1"))
s2 = int(input("enter marks in test2"))
s3 = int(input("enter marks in test3"))
if s1 > s2 and s1 > s3:
    print("maximum marks in test-1", s1)
else:
    if s2 > s1 and s2 > s3:
        print("maximum marks in test-2 ", s2)
    else:
        print("maximum marks is in test-3", s3)

average = (s1 + s2 + s3) / 3
percentage = ((s1 + s2 + s3) / 300) * 100
print("average score is", average, "and percentage is", percentage)
# -------------------------------------------------------------------------------------------------
