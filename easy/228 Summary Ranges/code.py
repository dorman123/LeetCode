from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        new_list = []
        start, end = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] - end == 1:
                end = nums[i]
            else:
                if start == end:
                    new_list.append(str(start))
                else:
                    new_list.append(f"{start}->{end}")
                if len(nums) > i:
                    start, end = nums[i], nums[i]

        if start == end:
            new_list.append(str(start))
        else:
            new_list.append(f"{start}->{end}")

        return new_list


s = Solution()
print(s.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))  # Output: ["0->2","4->5","7"]
print(s.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))  # Output: ["0","2->4","6","8->9"]
