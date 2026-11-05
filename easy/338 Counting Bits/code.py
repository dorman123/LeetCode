from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        new_arr = []

        for i in range(n + 1):
            list_in_bin = list(bin(i)[2:])
            filtered_list = [item for item in list_in_bin if item == 1 or item == '1']
            new_arr.append(len(filtered_list))

        return new_arr


s = Solution()
print(s.countBits(n=2))  # Output: [0,1,1]
print(s.countBits(n=5))  # Output: [0,1,1,2,1,2]
