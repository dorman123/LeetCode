class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:  # בדיקה אם המחסנית ריקה או אם הסוגר לא מתאים
                    return False
                stack.pop()

        return not stack


s = Solution()
print(s.isValid("([])"))
