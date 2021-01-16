# time - O(N)
# space - O(N)
def dfs(self, node):
    if node:
        self.a.append(node.val)
        dfs(self, node.left)
        dfs(self, node.right)


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.a = []
        dfs(self, root)

        min1, ans = root.val, float('inf')
        for v in self.a:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1

# time - O(N)
# space - O(N)

def findSecondMinimumValue(self, root):
    self.ans = float('inf')
    min1 = root.val

    def dfs(node):
        if node:
            if min1 < node.val < self.ans:
                self.ans = node.val
            elif node.val == min1:
                dfs(node.left)
                dfs(node.right)

    dfs(root)
    return self.ans if self.ans < float('inf') else -1