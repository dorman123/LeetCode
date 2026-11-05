from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # מונה כמה איברים לא שווים ל־val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # מעתיקים את הערך למיקום הבא הפנוי
                k += 1

        return k


s = Solution()
print(s.removeElement([1, 1, 2, 3, 4, 5, 5, 6, 6], 5))
