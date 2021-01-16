# time: O(H + k)
# space: O(H)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

# time: O(H)
# space: O(H)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans = 0
        self.k = k
        def helper(node):
            if node is None:
                return
            if node.left:
                helper(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
            helper(node.right)

        helper(root)
        return self.ans
