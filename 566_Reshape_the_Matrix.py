# time : O(r * c)
# space: O(r * c)
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])

        if n * m != r * c:
            return nums

        ans = []

        x = 0
        y = 0

        row = []

        for i in range(0, n):
            for j in range(0, m):
                row.append(nums[i][j])
                y += 1
                if y == c:
                    y = 0
                    x += 1
                    ans.append(row)
                    row = []
        return ans

# time : O(r * c)
# space: O(r * c)
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])

        if n * m != r * c:
            return nums

        ans = [[0 for x in range(c)] for y in range(r)]

        for i in range(0, r * c):
            x = i // c
            y = i % c
            ans[x][y] = nums[i // m][i % m]

        return ans
