# time - O(n * m)
# space - O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        n = len(grid)
        m = len(grid[0])

        total = 0

        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    for k in range(0, 4):
                        x = i + dx[k]
                        y = j + dy[k]

                        if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0:
                            total += 1
        return total
