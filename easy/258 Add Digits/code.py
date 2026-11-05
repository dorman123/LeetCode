class Solution:
    def addDigits(self, num: int) -> int:
        result, multiply = 0, 1

        while True:
            if num != 0:
                result += num % 10
                num -= ((num % 10) * multiply)
                num = num / 10
            elif num == 0 and result > 9:
                num = result
                result = 0
            else:
                return int(result)


s = Solution()
print(s.addDigits(num=38))  # Output: 2
