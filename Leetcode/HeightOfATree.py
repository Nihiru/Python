class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
def diameterOfBinaryTree(self,root):
    if root == None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameterOfBinaryTree(root.left)
    rdiameter = diameterOfBinaryTree(root.right)
    
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))



