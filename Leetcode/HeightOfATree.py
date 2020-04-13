class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def diameterOfBinaryTree(self,root):
        if root == None:
            return 0
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        lef_max = max(left.right, left.right)
        right_max = max(right.right, right.right)
        diam = max(lef_max, right_max)
        return diam+1



