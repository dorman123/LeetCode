from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(start_index, current_combination, current_sum):
            if current_sum == target:
                results.append(current_combination[:])
                return
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_combination, current_sum + candidates[i])
                current_combination.pop()

        backtrack(0, [], 0)
        return results


s = Solution()
print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))  # Output: [[2,2,3],[7]]
