class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n

        one_stair, two_stair, result = 1, 2, 3

        for i in range(2, n):
            result = one_stair + two_stair
            one_stair = two_stair
            two_stair = result

        return result


s = Solution()
print(s.climbStairs(n=2))  # Output: 2
print(s.climbStairs(n=3))  # Output: 3
