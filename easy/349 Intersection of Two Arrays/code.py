from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)

        return result


s = Solution()
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))  # Output: [2]
print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))  # Output: [9,4]
