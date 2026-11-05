from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        start = find_first(nums, target)
        end = find_last(nums, target)
        return [start, end]


s = Solution()
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1, -1]
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3, 4]
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=5))  # [0, 0]
print(s.searchRange(nums=[0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8], target=4))  # [10, 12]
