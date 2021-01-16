# time : O(len|a|))
# space : O(1)
class Solution:
    def addToArrayForm(self, a: List[int], k: int) -> List[int]:
        a.reverse()

        for i in range(len(a)):
            a[i] += (k % 10)
            k //= 10
            k += a[i] // 10
            a[i] %= 10

        while k != 0:
            a.append(k % 10)
            k //= 10
        a.reverse()
        return a