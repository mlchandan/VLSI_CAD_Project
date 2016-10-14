
# Tree node
class Node:

	def __init__(self, item, left=None, right=None):
		"""(Node, object, Node, Node) -> NoneType
		Initialize this node to store item and have children left and right.
		"""
    
		self.item = item
		self.left = left
		self.right = right

	def depth(self):
		# Base Case : Leaf node.This acoounts for height = 0
		if self.left == None and self.right == None:
			return 0

		# If left subtree is Null, return 0
		left_depth = self.left.depth() if self.left else 0
		# If right subtree is Null , returns 0
		right_depth = self.right.depth() if self.right else 0

		return max(left_depth, right_depth) + 1


############### TESTING THE NODE CLASS DEPTH FUNCTION  #####################

## Driver Program 
node1 = Node("x1")
node2 = Node("x0")
node3 = Node("OR", node1,node2)
node4 =Node("AND",node3)

print "node1 depth = ",node1.depth()
print "node3 depth = ",node3.depth()
print "node4 depth = ",node4.depth()


#Using "setattr()" and "getattr()" for a class
print getattr(node1, 'left')
print getattr(node4, 'right')
setattr(node4,'right',node1)

############# END OF TESTING THE NODE CLASS DEPTH FUNCTION ###################
