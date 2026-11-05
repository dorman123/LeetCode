class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        right_to_left = list(x)
        left_to_right = []
        pos = len(x) - 1

        while pos >= 0:
            left_to_right.append(x[pos])
            pos-=1

        print(f"right_to_left={right_to_left}\nleft_to_right={left_to_right}")

        if right_to_left == left_to_right:
            return True
        return False

s = Solution()
print(s.isPalindrome(x=121))


