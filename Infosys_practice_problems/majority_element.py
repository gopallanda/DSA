from collections import Counter


def majorityElement(nums):
    count = Counter(nums)
    n = len(nums)
    for key in count.keys():
        if count[key] > n // 2:
            return key
    return -1


if __name__ == "__main__":
    n = int(input("enter size of the array:"))
    nums = list(map(int, input().split()))
    print(majorityElement(nums))

"""
    The time complexity of this code is 0(n) and space complexity is 0(n) b/c we are using counter but we need the complexity 0(n) and space complexity 0(1) for that we have to Boyer-Moore Voting algorithm
"""


def majorityElement_Voting(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if candidate == num else -1
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return -1


# basically we are selecting the number that may repeat most of the times i.e (potential candidate) and we count it's occurrence instead count every element in the array
