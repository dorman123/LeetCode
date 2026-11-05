class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pos_a, pos_b = len(a) - 1, len(b) - 1
        rest = 0
        result = ""

        while pos_a >= 0 or pos_b >= 0 or rest:
            sum = rest
            if pos_a >= 0:
                sum += int(a[pos_a])
                pos_a -= 1
            if pos_b >= 0:
                sum += int(b[pos_b])
                pos_b -= 1

            rest = sum // 2
            sum = sum % 2

            result = str(sum) + result

        return result


s = Solution()
print(s.addBinary(a="11", b="1"))  # Output: "100"
print(s.addBinary(a="1010", b="1011"))  # Output: "10101"
