
#A Binary Tree node
class Node:

	def __init__(self, item, left=None, right=None):
		"""(Node, object, Node, Node) -> NoneType
		Initialize this node to store item and have children left and right.
		"""
		self.item = item
		self.left = left
		self.right = right

	def depth(self):
		if self.left == None and self.right == None:
			return 0
		left_depth = self.left.depth() if self.left else 0
		right_depth = self.right.depth() if self.right else 0
		return max(left_depth, right_depth) + 1
	
	#def __str__(self):
		#print  self.item," "
		#if self.right == None and self.left == None:
			#print "0"
		#elif self.right != None and self.left != None:
			#print self.right
			#print self.left
		#else:
			#print self.left


###########################################################################

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

###########################################################################

def infixToPostfix(infixexpr):
	opStack = Stack()
	postfixList = []
	tokenList = infixexpr.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
				if  not opStack.isEmpty() :
					if opStack.peek()== "~" :
						postfixList.append(opStack.pop())
		else:
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())
	
	return " ".join(postfixList)

###########################################################################

def postfix_2_tree(postfix_list):
	nodes_list=Stack()
	for token in postfix_list.split():
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			nodes_list.push(Node(token))
		elif token == '~':
			left_node = nodes_list.pop()
			nodes_list.push(Node(token,left_node))
		elif token in '&|^':
			left_node = nodes_list.pop()
			right_node = nodes_list.pop()		
			nodes_list.push(Node(token,left_node,right_node))
	return nodes_list.pop()


###########################################################################

postfix_list = infixToPostfix("  ~  ( A  | ( B   &  C ) ) ^ D  ")
print "postfix_list = ",postfix_list
Tree = postfix_2_tree (postfix_list)


