class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer limits
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        # Handle edge case: overflow when dividing MIN_INT by -1
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Use repeated subtraction but speed it up by multiplying the divisor
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Instead of bitwise shift, use multiplication to increase `temp`
            while dividend >= temp + temp:  # Same as temp <<= 1
                temp += temp
                multiple += multiple  # Same as multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply the correct sign
        return -quotient if negative else quotient


# Testing the solution
s = Solution()
print(s.divide(-2147483648, -1))  # Expected output: 2147483647 (not overflow)
print(s.divide(10, 3))  # Expected output: 3
print(s.divide(7, -3))  # Expected output: -2
print(s.divide(100, 5))  # Expected output: 20
