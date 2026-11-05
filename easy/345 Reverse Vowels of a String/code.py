class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        list_of_vowels = []

        for char in s:
            if char.lower() in vowels:
                list_of_vowels.append(char)

        list_of_vowels.reverse()

        result = []
        pos = 0
        for char in s:
            if char.lower() in vowels:
                result.append(list_of_vowels[pos])
                pos += 1
            else:
                result.append(char)

        return ''.join(result)


s = Solution()
print(s.reverseVowels(s="IceCreAm"))  # Output: "AceCreIm"
print(s.reverseVowels(s="leetcode"))  # Output: "leotcede"
