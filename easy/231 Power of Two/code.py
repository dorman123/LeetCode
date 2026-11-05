class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
            # This bitwise operation checks if n is a power of two.
            # A number is a power of two if and only if (n & (n - 1)) is 0.
        return (n & (n - 1)) == 0


s = Solution()
print(s.isPowerOfTwo(n=1))  # Output: true
print(s.isPowerOfTwo(n=3))  # Output: false
