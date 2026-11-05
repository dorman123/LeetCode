class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0

        split_word_by_space = s.split()
        return len(split_word_by_space[len(split_word_by_space)-1])


word = "amit the cool"
s = Solution()
print(s.lengthOfLastWord(word))