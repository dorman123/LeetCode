from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        row = 2
        temp, result = [], [1, 1]

        while row <= rowIndex:
            temp.append(1)

            for i in range(len(result) - 1):
                temp.append(result[i] + result[i + 1])

            temp.append(1)
            result = temp
            temp = []
            row += 1

        return result


s = Solution()
print(s.getRow(rowIndex=3))  # Output: [1,3,3,1]
# print(s.getRow(rowIndex=0))  # Output: [1]
# print(s.getRow(rowIndex=1))  # Output: [1,1]
