# time - O(N)
# space - O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        result = 0

        cache = {0: 1}

        stack = [(root, 0, False)]

        while stack:
            node, curSum, backtrack = stack.pop()

            if backtrack:
                cache[curSum] -= 1
                continue

            curSum += node.val

            result += cache.get(curSum - target, 0)

            cache[curSum] = cache.get(curSum, 0) + 1

            stack.append((None, curSum, True))

            if node.left:
                stack.append((node.left, curSum, False))

            if node.right:
                stack.append((node.right, curSum, False))
        return result
