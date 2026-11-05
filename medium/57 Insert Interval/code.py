from typing import List

"""
not finished
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        return intervals


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

s = Solution()
print(s.insert(intervals, newInterval))
