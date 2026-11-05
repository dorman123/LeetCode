class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        excel_columns = {chr(i + 65): i + 1 for i in range(26)}
        result = 0
        length = len(columnTitle)

        for i in range(length):
            char = columnTitle[i]
            value = excel_columns[char]
            power = length - i - 1
            result += value * pow(26, power)

        return result


s = Solution()
print(s.titleToNumber(columnTitle="A"))  # Output: 1
print(s.titleToNumber(columnTitle="AB"))  # Output: 28
print(s.titleToNumber(columnTitle="ZY"))  # Output: 701
