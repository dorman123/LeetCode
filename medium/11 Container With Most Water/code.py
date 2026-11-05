from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        biggest = 0

        left = 0
        while left < n - 1:
            for i in range(left + 1, n):
                area = min(height[left], height[i]) * (i - left)
                biggest = max(biggest, area)

            left += 1

        return biggest


s = Solution()
print(s.maxArea([1, 8, 6]))
