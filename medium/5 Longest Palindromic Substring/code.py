class Solution:
    def longestPalindrome(self, s: str) -> str:
        lst = []

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                lst.append(s[i:j])

        sorted_list = sorted(lst, key=len, reverse=True)

        for value in sorted_list:
            if value == value[::-1]:
                return value




s = Solution()
print(s.longestPalindrome(s="babad"))  # Output = bab
