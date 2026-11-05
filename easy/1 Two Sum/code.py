from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        args = []
        i = 0

        for num_pos in range(0, len(nums)):
            for j in range(num_pos+1, len(nums)):
                print(f"nums[num_pos] + nums[j] == target\n{nums[num_pos]} + {nums[j]} == {target}\n--------")
                if nums[num_pos] + nums[j] == target:
                    args.append(num_pos)
                    args.append(j)
                    return args

s = Solution()
print(s.twoSum(nums = [3,2,3], target = 6))