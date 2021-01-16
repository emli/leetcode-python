# time - O(N)
# space - O(N)
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        stack = [root]
        ans = 0
        sumOfNode = {}
        visited = {}

        while len(stack):
            top = stack[-1]
            if top is None:
                stack.pop()
                continue
            if top in visited:
                left = sumOfNode.get(top.left, 0)
                right = sumOfNode.get(top.right, 0)
                ans += abs(left - right)
                sumOfNode[top] = left + right + top.val
                stack.pop()
            else:
                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)
                visited[top] = True
        return ans
