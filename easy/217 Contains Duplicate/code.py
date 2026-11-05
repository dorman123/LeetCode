from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


s = Solution()
print(s.containsDuplicate(nums=[1, 2, 3, 1]))  # Output: true
print(s.containsDuplicate(nums=[1, 2, 3, 4]))  # Output: false
