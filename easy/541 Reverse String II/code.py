class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new_s = ""
        count = 1

        for i in range(0, len(s), k):
            if count % 2 != 0:
                new_s += (s[i:i + k])[::-1]
            else:
                new_s += (s[i:i + k])

            count += 1

        return new_s


s = Solution()
print(s.reverseStr(s="abcdefg", k=2))  # Output: "bacdfeg"
print(s.reverseStr(s="abcd", k=2))  # Output: "bacd"
