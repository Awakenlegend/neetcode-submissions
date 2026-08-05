# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0,True
            leftheight,leftbalanced=dfs(root.left)
            rightheight,rightbalanced=dfs(root.right)
            height=max(leftheight,rightheight)+1
            balanced=(
                leftbalanced and rightbalanced and abs(leftheight-rightheight)<=1
            )
            return height,balanced
        _,balanced=dfs(root)
        return balanced
        