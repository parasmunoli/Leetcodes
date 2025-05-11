class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def postOrder(node):
            if not node:
                return
            postOrder(node.left)
            postOrder(node.right)
            result.append(node.val)

        postOrder(root)
        return result