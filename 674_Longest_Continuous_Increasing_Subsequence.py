# time - O(N)
# space - O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        length = 1
        ans = float('-inf')

        for i in range(0, n + 1):
            if i + 1 < n and nums[i] < nums[i + 1]:
                length += 1
            else:
                ans = max(ans, length)
                length = 1

        return ans
