from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        fruits.sort(reverse=True)  # מיון פירות מהגדול לקטן
        baskets.sort(reverse=True)  # מיון סלים מהגדול לקטן

        print(f"---------------\nfruits={fruits}\nbaskets={baskets}\n---------------")

        for fruit in fruits:
            for basket in baskets:
                if fruit <= basket:
                    baskets.remove(basket)

        return len(baskets)



# בדיקות
sol = Solution()
print(sol.numOfUnplacedFruits([4, 2, 5], [3, 5, 4]))  # פלט נכון: 1
print(sol.numOfUnplacedFruits([3, 6, 1], [6, 4, 7]))  # פלט נכון: 0
print(sol.numOfUnplacedFruits([5, 5, 5], [1, 2, 3]))  # פלט נכון: 3
print(sol.numOfUnplacedFruits([1, 2, 3], [10, 10, 10]))  # פלט נכון: 0

