class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while p1 >= 0 or p2 >= 0 or carry:
            digit1 = int(num1[p1]) if p1 >= 0 else 0
            digit2 = int(num2[p2]) if p2 >= 0 else 0

            temp = digit1 + digit2 + carry
            carry = temp // 10
            result.append(str(temp % 10))

            p1 -= 1
            p2 -= 1

        return ''.join(result[::-1])


s = Solution()
print(s.addStrings(num1="11", num2="123"))  # Output: "134"
print(s.addStrings(num1="456", num2="77"))  # Output: "533"
print(s.addStrings(num1="0", num2="0"))  # Output: "0"
