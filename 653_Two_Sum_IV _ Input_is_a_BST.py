# time - O(N)
# space - O(N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root: TreeNode, k: int) -> bool:
    a = []

    def convertToList(node):
        if node is None:
            return
        convertToList(node.left)
        a.append(node.val)
        convertToList(node.right)

    convertToList(root)

    left = 0
    right = len(a) - 1

    while left < right:
        curSum = a[left] + a[right]
        if curSum > k:
            right -= 1
        elif curSum < k:
            left += 1
        else:
            return True
    return False


# time - O(N)
# space - O(height)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorderIter(root):
    if root:
        for node in inorderIter(root.left):
            yield node
        yield root
        for node in inorderIter(root.right):
            yield node


def reverseInOrder(root):
    if root:
        for node in reverseInOrder(root.right):
            yield node
        yield root
        for node in reverseInOrder(root.left):
            yield node


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        leftSide = inorderIter(root)
        rightSide = reverseInOrder(root)
        left = next(leftSide, None)
        right = next(rightSide, None)
        while True:
            if left == right:
                return False
            curSum = left.val + right.val
            if curSum > k:
                right = next(rightSide, None)
            elif curSum < k:
                left = next(leftSide, None)
            else:
                return True
