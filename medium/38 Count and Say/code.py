class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        return self.sub_count_and_say(prev)

    def sub_count_and_say(self, s: str) -> str:
        num = s[0]
        new_s = ""
        count = 1

        for i in range(1, len(s)):
            if s[i] != num:
                new_s += str(count) + num
                count = 1
                num = s[i]
            else:
                count += 1
        new_s += str(count) + num

        return new_s


s = Solution()
print(s.countAndSay(5))  # פלט: "111221"
