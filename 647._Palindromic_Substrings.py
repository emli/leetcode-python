# time - O(N^2)
# space - O(N ^ 2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        ans = 0

        isPalindrome = [[False for x in range(size + 1)] for y in range(size + 1)]

        for left in range(size - 1, -1, -1):
            for right in range(left, size):
                if left == right:
                    isPalindrome[left][right] = True
                elif left + 1 == right and s[left] == s[right]:
                    isPalindrome[left][right] = True
                elif s[left] == s[right]:
                    isPalindrome[left][right] = isPalindrome[left + 1][right - 1]
                ans += isPalindrome[left][right]

        return ans
