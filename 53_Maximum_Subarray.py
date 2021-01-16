#time: O(N)
#space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        minSum = min(ans,0)
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = curSum + nums[i];
            ans = max(ans,curSum - minSum);
            minSum = min(minSum,curSum);
        return ans