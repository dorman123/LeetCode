class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False  # Powers of 3 are positive integers
        while n % 3 == 0:
            n //= 3  # Use integer division
        return n == 1


s = Solution()
print(s.isPowerOfThree(n=9))  # Output: true
print(s.isPowerOfThree(n=45))  # Output = false
