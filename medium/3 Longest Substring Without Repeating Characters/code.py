class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_word_array, biggest_array = [], []

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            sub_word_array.append(s[0])

        for i in range(1, len(s)):
            if s[i] not in sub_word_array:
                sub_word_array.append(s[i])
            else:
                if len(biggest_array) > len(sub_word_array):
                    dup_index = sub_word_array.index(s[i])
                    sub_word_array = sub_word_array[dup_index + 1:]
                    sub_word_array.append(s[i])
                else:
                    biggest_array = sub_word_array
                    dup_index = sub_word_array.index(s[i])
                    sub_word_array = sub_word_array[dup_index + 1:]
                    sub_word_array.append(s[i])

            print(f"sub_word_array={sub_word_array}")

        if len(sub_word_array) > len(biggest_array):
            biggest_array = sub_word_array

        return len(biggest_array)


s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))
