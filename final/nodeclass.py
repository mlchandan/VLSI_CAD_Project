class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
         
# Tree node
class Node:

	def __init__(self, operator=None. name=None, left=None, right=None):
		"""(Node, object, Node, Node) -> NoneType
		Initialize this node to store item and have children left and right.
		"""
    
		self.operator = operator
		self.left = left
		self.right = right
    self.name=name

	def depth(self):
		# Base Case : Leaf node.This acoounts for height = 0
		if self.left == None and self.right == None:
			return 0

		# If left subtree is Null, return 0
		left_depth = self.left.depth() if self.left else 0
		# If right subtree is Null , returns 0
		right_depth = self.right.depth() if self.right else 0

		return max(left_depth, right_depth) + 1
