class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        excel_columns = {chr(i + 65): i + 1 for i in range(26)}
        result = ""

        while columnNumber != 0:
            rest = (columnNumber - 1) % 26

            for key, value in excel_columns.items():
                if value == rest + 1:
                    result = result + key
                    break

            columnNumber = int((columnNumber - 1) / 26)

            print(f"columnNumber={columnNumber} rest={rest}")

        return result[::-1]


s = Solution()
print(s.convertToTitle(columnNumber=1))  # Output: "A"
print(s.convertToTitle(columnNumber=28))  # Output: "AB"
print(s.convertToTitle(columnNumber=701))  # Output: "ZY"
