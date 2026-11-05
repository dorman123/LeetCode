from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        arr = [[1]]
        temp = []
        pos = 0

        if numRows == 1:
            return arr

        for i in range(1, numRows):
            print(i)
            if i == 1:
                temp = [1, 1]
            if i > 1:
                temp.append(arr[i - 1][0])
                for j in range(0, len(arr[i - 1]) - 1):
                    temp.append(arr[i - 1][j] + arr[i - 1][j + 1])
                temp.append(arr[i - 1][len(arr[i - 1]) - 1])

            arr.append(temp)
            temp = []

        return arr


s = Solution()
print(s.generate(5))  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
