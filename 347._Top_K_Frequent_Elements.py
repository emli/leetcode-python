# time: O(N) on average
# space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        bucket = [[] for j in range(size + 1)]

        for key, value in frequency.items():
            bucket[value].append(key)

        ans = []

        for i in range(size, 0, -1):
            for j in range(0, len(bucket[i])):
                if len(ans) < k:
                    ans.append(bucket[i][j])
        return ans
