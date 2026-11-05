class Solution:
    def mySqrt(self, x: int) -> int:
        sqr_number = 0

        if sqr_number * sqr_number == x:
            return sqr_number

        while True:
            sqr_number += 1

            if (x - sqr_number * sqr_number) < 0:
                return sqr_number - 1
            if (x - sqr_number * sqr_number) == 0:
                return sqr_number

            print(f"sqr_number={sqr_number}")


s = Solution()
result = s.mySqrt(15)
print(result)
