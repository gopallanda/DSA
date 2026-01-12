def minSubArrayLen(target, nums):
    import math

    left = 0
    current_sum = 0
    min_length = math.inf

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != math.inf else 0


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums))  # Output: 2
