#time - O(N)
#space - O(N)
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.result = 0
        cache = {0: 1}

        self.dfs(root, target, 0, cache)

        return self.result

    def dfs(self, root, target, curSum, cache):
        if root is None:
            return

        curSum += root.val

        self.result += cache.get(curSum - target, 0)

        cache[curSum] = cache.get(curSum, 0) + 1

        self.dfs(root.left, target, curSum, cache)
        self.dfs(root.right, target, curSum, cache)

        cache[curSum] -= 1
