# space - O(N)
class NumArray:

    # time - O(N)
    def __init__(self, nums: List[int]):
        self.prefixSum = nums
        for i in range(1, len(nums)):
            self.prefixSum[i] += nums[i - 1]

    # time - O(1)
    def sumRange(self, l: int, r: int) -> int:
        return self.prefixSum[r] - (self.prefixSum[l - 1] if l - 1 >= 0 else 0)
