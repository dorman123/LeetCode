from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)


s = Solution()
s.reverseString(s=["h", "e", "l", "l", "o"])  # Output: ["o","l","l","e","h"]
s.reverseString(s=["H", "a", "n", "n", "a", "h"])  # Output: ["h","a","n","n","a","H"]
