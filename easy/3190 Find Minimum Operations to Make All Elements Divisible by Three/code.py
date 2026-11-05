class Solution:
    def minimumOperations(self, nums) -> int: # nums: List[int]
        actions = 0

        for num in nums:
            print(f"{num}(num) % 3 = {num % 3}")
            if num % 3 != 0:
                actions+=1

        return actions

s = Solution()
print(s.minimumOperations([3,6,9]))
