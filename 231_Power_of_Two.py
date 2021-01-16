# time: O(number of digits of N)
# space: O(number of digits of N)
class Solution:
    def isPowerOfTwo(self, n) -> bool:
        return n > 0 and (n & (n - 1)) == 0

# time: O(number of bits)
# space: O(number of bits)
class Solution:
    def isPowerOfTwo(self, n) -> bool:
        return n > 0 and bin(n).count("1") == 1

# time: O(logN)
# space: O(1)
class Solution:
    def isPowerOfTwo(self, n) -> bool:
        while n > 0 and n & 1 == 0:
            n = n >> 1
        return n == 1