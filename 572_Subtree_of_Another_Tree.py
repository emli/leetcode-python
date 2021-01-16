#time : O(|tree| * |subtree|)
#space: O(|tree|)
def isSame(self, tree, subtree) -> bool:
    if tree is None and subtree is None:
        return True

    if tree is None or subtree is None:
        return False

    return (tree.val == subtree.val) and isSame(self, tree.left, subtree.left) and isSame(self, tree.right,
                                                                                          subtree.right)


def isSubtree(self, tree, subtree) -> bool:
    if tree is None:
        return False

    return isSame(self, tree, subtree) or isSubtree(self, tree.left, subtree) or isSubtree(self, tree.right, subtree)


class Solution:
    def isSubtree(self, tree: TreeNode, subtree: TreeNode) -> bool:
        return isSubtree(self, tree, subtree)

#time : O(|tree| * |subtree|)
#space: O(|tree|)
def isSame(self,p,q) -> bool:
    stack = []

    stack.append(p)
    stack.append(q)

    while len(stack) > 0:
        a = stack.pop()
        b = stack.pop()

        if a is None and b is None:
            continue

        if a is None or b is None:
            return False

        if a.val != b.val:
            return False

        stack.append(a.left)
        stack.append(b.left)
        stack.append(a.right)
        stack.append(b.right)
    return True

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = []
        stack.append(s)

        while len(stack) > 0:
            node = stack.pop();
            if node.val == t.val and isSame(self,node, t):
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False


#time : O(|tree|+|subtree|)
#space: O(max(|tree|,|subtree|))


def tree2str(self, t):
    if not t: return ''
    left = '({})'.format(tree2str(self, t.left)) if (t.left or t.right) else ''
    right = '({})'.format(tree2str(self, t.right)) if t.right else ''
    return '{}{}{}'.format(t.val, left, right)


def computeHash(self, a, h):
    for i in range(0, len(a)):
        h.append((h[i] + ord(a[i]) * self.powers[i]) % self.mod)


class Solution:
    def isSubtree(self, tree: TreeNode, subtree: TreeNode) -> bool:
        a = tree2str(self, tree)
        b = tree2str(self, subtree)

        maxLen = max(len(a), len(b))

        self.mod = 1000000007
        prime = 31

        self.powers = [1]
        for i in range(1, maxLen + 1):
            self.powers.append((self.powers[i - 1] * prime) % self.mod)

        h1 = [0]
        h2 = [0]
        computeHash(self, a, h1)
        computeHash(self, b, h2)

        for i in range(len(h2), len(h1) + 1):
            l = i - len(h2)
            hashOfFirstSegment = (h1[i - 1] - h1[l] + self.mod) % self.mod
            power = self.powers[l]

            if ((h2[-1] * power) % self.mod == hashOfFirstSegment):
                return True
        return False