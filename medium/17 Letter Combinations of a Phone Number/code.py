from typing import List


class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        phone_keys = [
            ["a", "b", "c"],  # 2
            ["d", "e", "f"],  # 3
            ["g", "h", "i"],  # 4
            ["j", "k", "l"],  # 5
            ["m", "n", "o"],  # 6
            ["p", "q", "r", "s"],  # 7
            ["t", "u", "v"],  # 8
            ["w", "x", "y", "z"]  # 9
        ]

        if not s:
            return []

        combinations = [""]
        for digit in s:
            new_combinations = []
            for combo in combinations:
                for letter in phone_keys[int(digit) - 2]:
                    new_combinations.append(combo + letter)
            combinations = new_combinations

        return combinations


s = Solution()
print(s.letterCombinations(s="23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(s.letterCombinations(s="2"))  # Output: ["a","b","c"]
