# time: O(N)
# space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        yesterday, today = 0, nums[0]

        for i in range(1, n):
            yesterday, today = today, max(today, yesterday + nums[i])

        return today
