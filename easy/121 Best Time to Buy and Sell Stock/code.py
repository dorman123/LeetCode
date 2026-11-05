from typing import List

"""Not Finished"""


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:

        best_minus = 0

        for i in range(0, len(prices)):
            for n in range(i + 1, len(prices)):
                best_minus = min(best_minus, prices[i] - prices[n])

        return abs(best_minus)


s = Solution
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
