# time - O(N)
# space - O(height)
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return 0, 0
            leftCount, left = dfs(root.left)
            rightCount, right = dfs(root.right)

            left = left + 1 if root.left and root.left.val == root.val else 0
            right = right + 1 if root.right and root.right.val == root.val else 0

            return max(leftCount, rightCount, left + right), max(left, right)

        ans, _ = dfs(root)
        return ans

