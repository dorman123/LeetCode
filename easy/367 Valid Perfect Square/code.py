class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        side = 1

        while True:
            if side * side == num:
                return True
            elif side * side < num:
                side += 1
            else:
                return False


s = Solution()
print(s.isPerfectSquare(num=16))  # Output: true
print(s.isPerfectSquare(num=14))  # Output = false
