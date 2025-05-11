class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def preOrder(node):
            if not node:
                return
            result.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return result