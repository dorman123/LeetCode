class Solution:
    def hammingWeight(self, n: int) -> int:
        in_bit = bin(n)[2:]
        num_of_one = 0

        for i in range(0, len(in_bit)):
            if in_bit[i] == '1':
                num_of_one += 1

        return num_of_one


s = Solution()
print(s.hammingWeight(n=2147483645))  # Output: 30
