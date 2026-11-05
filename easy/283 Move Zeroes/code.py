from typing import List


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

        print(nums)


s = Solution()
s.moveZeroes(nums=[0, 1, 0, 3, 12])  # Output: [1,3,12,0,0]
s.moveZeroes(nums=[0])  # Output: [0]
