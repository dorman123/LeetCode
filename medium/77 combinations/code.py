from itertools import combinations

class Solution:
    def combine(self, n: int, k: int):
        arr = []
        for i in range(1, n + 1):
            arr.append(i)

        return list(combinations(arr, k))

s = Solution()
print(s.combine(4, 2))