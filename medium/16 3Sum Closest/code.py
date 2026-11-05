from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if closest is None or abs(total - target) < abs(closest - target):
                        closest = total

        return closest


s = Solution()
# print(s.threeSumClosest(nums=[-1, 2, 1, -4], target=1))  # Output = 2
print(s.threeSumClosest(nums=[0, 3, 97, 102, 200], target=300))  # Output = 300
