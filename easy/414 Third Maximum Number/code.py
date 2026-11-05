from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]


s = Solution()
print(s.thirdMax(nums=[3, 2, 1]))  # Output: 1
print(s.thirdMax(nums=[2, 2, 3, 1]))  # Output: 1
print(s.thirdMax(nums=[1, 2]))  # Output: 2
