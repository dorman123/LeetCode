from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        option1 = nums[-1] * nums[-2] * nums[-3]
        option2 = nums[0] * nums[1] * nums[-1]

        return max(option1, option2)


s = Solution()
print(s.maximumProduct(nums=[1, 2, 3, -1]))  # Output: 6
print(s.maximumProduct(nums=[1, 3, 2, 4]))  # Output: 24
print(s.maximumProduct(nums=[-1, -2, -3]))  # Output: -6
