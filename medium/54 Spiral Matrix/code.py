from typing import List


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        while matrix:
            # שורה עליונה
            result += matrix.pop(0)

            # עמודה ימנית
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # שורה תחתונה
            if matrix:
                result += matrix.pop()[::-1]

            # עמודה שמאלית
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    result.append(row.pop(0))

        return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
s = Solution()
print(s.spiralOrder(matrix))
