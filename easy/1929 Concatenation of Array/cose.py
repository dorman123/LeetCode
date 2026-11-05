class Solution:
    def getConcatenation(self, nums):
        ans = []

        for i in range(2):
            for i in nums:
                ans.append(i)

        return ans


s = Solution()
print(s.getConcatenation([1, 2, 1]))
