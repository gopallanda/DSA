from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        # ----- Previous Less Element (PLE) -----
        ple = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        # ----- Next Less Element (NLE) -----
        nle = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                nle[stack.pop()] = i
            stack.append(i)

        # ----- Previous Greater Element (PGE) -----
        pge = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            pge[i] = stack[-1] if stack else -1
            stack.append(i)

        # ----- Next Greater Element (NGE) -----
        nge = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nge[stack.pop()] = i
            stack.append(i)

        # ----- Sum contributions -----
        total = 0
        for i in range(n):
            max_count = (i - pge[i]) * (nge[i] - i)
            min_count = (i - ple[i]) * (nle[i] - i)
            total += nums[i] * (max_count - min_count)

        return total
