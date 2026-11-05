class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_of_pattern = {}
        list_of_s = s.split(" ")
        list_of_pattern = list(pattern)

        if len(list_of_pattern) != len(list_of_s):
            return False

        for i in range(len(list_of_pattern)):
            if list_of_pattern[i] in dict_of_pattern:
                if dict_of_pattern[list_of_pattern[i]] != list_of_s[i]:
                    return False
            else:
                dict_of_pattern[list_of_pattern[i]] = list_of_s[i]

            found_keys = []
            for key, value in dict_of_pattern.items():
                if value == list_of_s[i]:
                    found_keys.append(key)
            if len(found_keys) >= 2:
                return False

        return True


s = Solution()
print(s.wordPattern(pattern="abc", s="dog cat dog"))  # Output: false
print(s.wordPattern(pattern="abba", s="dog cat cat dog"))  # Output: true
print(s.wordPattern(pattern="abba", s="dog dog dog dog"))  # Output: false
