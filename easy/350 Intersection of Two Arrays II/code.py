from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        result = []

        for key in dict1.keys():
            if key in dict2:
                if dict1[key] > dict2[key]:
                    n = dict2[key]
                else:
                    n = dict1[key]

                for i in range(n):
                    result.append(key)

        return result


s = Solution()
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))  # Output: [2, 2]
print(s.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))  # Output: [9,4]
