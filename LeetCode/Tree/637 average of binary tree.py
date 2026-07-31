# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        if root is None:
            return []
        qu=deque([root])
        while qu:
            size=len(qu)
            lsum=0
            for i in range(size):
                t=qu.popleft()
                lsum+=t.val
                if t.left:
                    qu.append(t.left)
                if t.right:
                    qu.append(t.right)
                
            ans.append(lsum/size)
        return ans

        
