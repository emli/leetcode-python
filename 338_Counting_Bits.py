# time - O(N)
# space - O(N)
class Solution:
    def countBits(self, num: int) -> List[int]:
        numOfBits = [0] * (num + 1)

        for i in range(1, num + 1):
            if i % 2 == 0:
                numOfBits[i] = numOfBits[i // 2]
            else:
                numOfBits[i] = numOfBits[i - 1] + 1
        return numOfBits
