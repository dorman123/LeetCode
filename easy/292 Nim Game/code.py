class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        return True


s = Solution()
print(s.canWinNim(n=4))  # Output: false
print(s.canWinNim(n=2))  # Output: true
