def firstLastIndex(nums, target):
    res = []
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)
    if not res:
        return [-1, -1]
    return [res[0], res[-1]]
