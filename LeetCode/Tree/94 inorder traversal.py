class Solution:

    def inorder(self, root, ans):

        if root is None:
            return

        self.inorder(root.left, ans)

        ans.append(root.val)

        self.inorder(root.right, ans)

    def inorderTraversal(self, root):

        ans = []

        self.inorder(root, ans)

        return ans
