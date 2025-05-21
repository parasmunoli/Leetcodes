# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def getHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)