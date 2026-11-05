from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        dict_of_places = {}

        for index, value in enumerate(nums):
            if value in dict_of_places:
                if index - dict_of_places[value] <= k:
                    return True
            dict_of_places[value] = index

        return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))  # Output: true
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))  # Output: false
