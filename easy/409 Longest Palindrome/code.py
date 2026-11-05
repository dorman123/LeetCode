class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_of_chars = {}
        len_of_palindrome = 0
        odd_found = False

        if len(s) == 1:
            return 1

        for i in s:
            if i in dict_of_chars:
                dict_of_chars[i] += 1
            else:
                dict_of_chars[i] = 1

        for count in dict_of_chars.values():
            if count % 2 == 0:
                len_of_palindrome += count
            else:
                len_of_palindrome += count - 1
                odd_found = True

        if odd_found:
            len_of_palindrome += 1

        return len_of_palindrome


s = Solution()
print(s.longestPalindrome(s="abccccdd"))  # Output: 7
print(s.longestPalindrome(s="a"))  # Output: 1
