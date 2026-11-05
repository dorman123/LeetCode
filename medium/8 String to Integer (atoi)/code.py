class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        is_positive = True
        number = 0
        start_point = 0

        if s[0] == "-":
            is_positive = False
            start_point = 1
        elif s[0] == "+":
            start_point = 1

        for i in range(start_point, len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            else:
                break

        if number > 2147483647 and is_positive:
            return 2147483647
        elif number > 2147483648 and not is_positive:
            return -2147483648

        if is_positive:
            return number
        else:
            return -number


num = "-91283472332"
s = Solution()
print(s.myAtoi(num))
