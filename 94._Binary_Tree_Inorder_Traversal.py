# time - O(N)
# space - O(Height)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans

# time - O(N)
# space - O(Height)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []

        while len(stack) > 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        return ans
