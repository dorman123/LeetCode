from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            return nums[0] - 1

        nums.sort()

        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                return nums[i] + 1

        return nums[len(nums) - 1] + 1


s = Solution()
print(s.missingNumber(nums=[3, 0, 1]))  # Output: 2
print(s.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8
print(s.missingNumber(nums=[0, 1]))  # Output: 2
