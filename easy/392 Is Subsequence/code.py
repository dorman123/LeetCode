class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        for i in range(len(t)):
            if t[i] == s[0]:
                s = s[:0] + s[0 + 1:]
            if len(s) == 0:
                return True
        return False


s = Solution()
print(s.isSubsequence(s="abc", t="ahbgdc"))  # Output: true
print(s.isSubsequence(s="axc", t="ahbgdc"))  # Output: false
