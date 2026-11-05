from typing import List


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        nums_dict = {}

        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1

        max_key = None
        max_value = 0
        for key, value in nums_dict.items():
            if value > max_value:
                max_value = value
                max_key = key

        return max_key


s = Solution
print(s.majorityElement([1, 2, 1, 1, 2, 2, 3, 2, 2, 3]))
