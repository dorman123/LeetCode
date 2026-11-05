from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(open_count: int, close_count: int, current_string: str):
            if open_count == n and close_count == n:
                result.append(current_string)
                return
            if close_count > open_count:
                return
            if open_count < n:
                backtracking(open_count + 1, close_count, current_string + "(")
            if close_count < open_count:
                backtracking(open_count, close_count + 1, current_string + ")")

        backtracking(open_count=0, close_count=0, current_string="")
        return result


s = Solution()
print(s.generateParenthesis(n=3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(s.generateParenthesis(n=1))  # Output: ["()"]
