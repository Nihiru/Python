# Python3 program to check if a given tree is BST. 

''' A binary tree node has data, pointer to 
left child and a pointer to right child '''
class newNode: 

	# Constructor to create a newNode 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Utility function to check if Binary Tree is BST 
def isBSTUtil(root, prev): 
	
	# traverse the tree in inorder fashion and 
	# keep track of prev node 
	if (root): 
		if (not isBSTUtil(root.left, prev)): 
			return False
			
		# Allows only distinct valued nodes 
		if (root.data <= prev): 
			return False
			
		# Initialize prev to current 
		prev = root.data 
		
		return isBSTUtil(root.right, prev) 
	
	return True

# Function to check if Binary Tree is BST 
def isBST(root): 
	
	prev = -(2**32) 
	return isBSTUtil(root, prev) 

# Driver code 
root = newNode(5) 
root.left = newNode(2) 
root.right = newNode(15) 
root.left.left = newNode(1) 
root.left.right = newNode(4) 

if (isBST(root)): 
	print("Is BST") 
else: 
	print("Not a BST") 

# This code is contributed by shubhamsingh10 
