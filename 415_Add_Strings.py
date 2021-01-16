# time : O(max(len(a), len(b)))
# space: O(max(len(a), len(b)))
class Solution:
    def addStrings(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)

        a.reverse()
        b.reverse()

        while len(a) < len(b):
            a.append('0')
        while len(b) < len(a):
            b.append('0')

        carry = 0
        ans = []

        for i in range(0, max(len(a), len(b))):
            total = ord(a[i]) - ord('0') + ord(b[i]) - ord('0') + carry
            carry = total // 10
            ans.append(chr(total % 10 + ord('0')))

        if carry > 0:
            ans.append('1')

        ans.reverse()

        return ''.join(ans)
