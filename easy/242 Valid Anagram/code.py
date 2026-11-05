class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and sorted(s) == sorted(t):
            return True
        return False


s = Solution()
print(s.isAnagram(s="anagram", t="nagaram"))  # Output: true
print(s.isAnagram(s="rat", t="car"))  # Output: false
