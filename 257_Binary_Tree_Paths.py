# time - O(N)
# space - O(N)
def constructAns(self, node: TreeNode, ans: List[str], way):
    if node is None:
        return

    if node.left is None and node.right is None:
        way.append(str(node.val))
        joinedWay = '->'.join(way)
        ans.append(joinedWay)
        way.pop()
        return;

    if node.left:
        way.append(str(node.val))
        constructAns(self, node.left, ans, way)
        way.pop()

    if node.right:
        way.append(str(node.val))
        constructAns(self, node.right, ans, way)
        way.pop()


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        constructAns(self, root, ans, [])
        return ans

# time - O(N)
# space - O(N)

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        if root is None:
            return ans
        stack = [(root, [str(root.val)])]

        while len(stack) > 0:
            node, way = stack.pop()

            if node.left is None and node.right is None:
                joinedWay = '->'.join(way)
                ans.append(joinedWay)

            if node.left:
                left = way[:]
                left.append(str(node.left.val))
                stack.append((node.left, left))
            if node.right:
                right = way[:]
                right.append(str(node.right.val))
                stack.append((node.right, right))
        return ans
