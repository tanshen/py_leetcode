# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0

        if not root:
            return ret

        def get_height(root):
            if root is None:
                return 0
            return get_height(root.left) + 1

        for i in range(get_height(root)):
            ret += 2**i

        def helper(root):
            if get_height(root.left) > get_height(root.right):
                nonlocal ret
                helper(root.left)
                ret -= 2**get_height(root.left)//2
                if root.right is None:
                    return
            else:
                if root.right is None:
                    return
                helper(root.right)

        helper(root)
        return ret




