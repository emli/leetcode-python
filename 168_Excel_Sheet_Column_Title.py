# time: O(logN)
# space: O(1)
class Solution:
    def convertToTitle(self, num: int) -> str:
        result = []
        while num > 0:
            result.append(chr(ord('A') + (num - 1) % 26))
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)
