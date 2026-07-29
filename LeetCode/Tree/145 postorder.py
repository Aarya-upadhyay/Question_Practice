# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post(self,root,ans):
        if root is None:
            return ans
        self.post(root.left,ans)
        self.post(root.right,ans)
        ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.post(root,ans)
        return ans
