# time - O(N)
# space - O(N)
class Solution:
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            if node.val < L:
                return trim(node.right)
            if node.val > R:
                return trim(node.left)

            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

        return trim(root)
