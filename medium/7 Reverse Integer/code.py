class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1

        reversed_str = str(abs(x))[::-1]
        sign = -1 if x < 0 else 1
        reversed_num = sign * int(reversed_str)

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num


s = Solution()
print(s.reverse(123))
