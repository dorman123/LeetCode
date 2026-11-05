from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num, multiply = 0, 1

        for digit in digits[::-1]:
            num += digit * multiply
            multiply *= 10

        num += 1
        digits_list = [int(digit) for digit in str(num)]

        return digits_list


s = Solution()
print(s.plusOne(digits=[1, 2, 3]))  # Output: [1,2,4]
print(s.plusOne(digits=[4, 3, 2, 1]))  # Output: [4,3,2,2]
print(s.plusOne(digits=[9]))  # Output: [1,0]
