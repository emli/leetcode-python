# time : O(N)
# space : O(height)
def collectSum(self, node: TreeNode, L: int, R: int):
    if node is None:
        return
    if L <= node.val <= R:
        self.sum += node.val
    if L < node.val:
        collectSum(self, node.left, L, R)
    if node.val < R:
        collectSum(self, node.right, L, R)


class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        collectSum(self, root, L, R)
        return self.sum

# time : O(N)
# space : O(height)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    sum += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return sum
