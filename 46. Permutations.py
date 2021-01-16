# time: O(N! * N)
# space: O(N! * N)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        permutation = []
        size = len(nums)

        def backtrack(pos=0):
            if pos == size:
                ans.append(permutation.copy())
                return
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack(pos + 1)
                    permutation.pop()

        backtrack()
        return ans


# time: O(N! * N)
# space: O(N! * N)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
