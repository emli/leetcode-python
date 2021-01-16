#time: O(N * log(logN))
#space: O(N)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        i = 2
        while i * i < n:
            if isPrime[i]:
                    for j in range(i * i, n, i):
                        isPrime[j] = False
            i += 1
        return isPrime.count(True)
