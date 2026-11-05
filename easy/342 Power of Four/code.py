class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n = n // 4

        return n == 1


s = Solution()
print(s.isPowerOfFour(n=16))  # Output: true
print(s.isPowerOfFour(n=5))  # Output: false
