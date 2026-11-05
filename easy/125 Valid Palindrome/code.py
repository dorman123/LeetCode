import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)

        print(f"{cleaned[::1]} == {cleaned[::-1]}")
        if cleaned[::1] == cleaned[::-1]:
            return True
        return False

s = Solution()
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))  # Output: true
print(s.isPalindrome(s="race a car"))  # Output: false
