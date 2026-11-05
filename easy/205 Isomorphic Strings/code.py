class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_of_mapping = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in dict_of_mapping:
                if t[i] in dict_of_mapping.values():
                    return False
                dict_of_mapping[s[i]] = t[i]
            else:
                if dict_of_mapping[s[i]] != t[i]:
                    return False

        return True


s = Solution()
print(s.isIsomorphic(s="egg", t="add"))  # Output: true
print(s.isIsomorphic(s="badc", t="babc"))  # Output: false
