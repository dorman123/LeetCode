class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for f in factors:
            while n % f == 0:
                n //= f

        return n == 1


s = Solution()
print(s.isUgly(n=6))  # Output: true
print(s.isUgly(n=14))  # Output: false