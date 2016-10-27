from nodeclass import Node,Stack


###########################################################################
"""
Convert infix boolean expression to postfix boolean expression

"""
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
"""
Coverts postfix expression to Tree.

"""
def postfix_2_tree(postfix_list):
	nodes_list=Stack()
	fulllist=list()
	for token in postfix_list.split():
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			x= Node(token)
			fulllist.append(x)
			nodes_list.push(x)
		elif token == '~':
			left_node = nodes_list.pop()
			x= Node(token,left_node)
			fulllist.append(x)
			nodes_list.push(x)
		elif token in '&|^':
			left_node = nodes_list.pop()
			right_node = nodes_list.pop()
			x= Node(token,left_node,right_node)
			fulllist.append(x)
			nodes_list.push(x)
	fulllist.reverse() # to make root node come on top
	for i in range(len(fulllist)):
		fulllist[i].name= "n"+str(i)+"_"+fulllist[i].operator	
	return nodes_list.pop(),fulllist




###########################################################################
"""
Given a parse tree/ subtree which would be representing the LUT,
function returns the boolean expression for that subtree.

"""
def getBoolExpression(node, node_list):
	node_list_name =[x.name for x in node_list]
	if node.operator == "~":
		return "~"+"( "+getBoolExpression(node.left,node_list)+" )"
	if node.name in node_list_name:
		if node.depth() == 0:
			return node.name
		else:
			return "( "+getBoolExpression(node.left,node_list)+" "+node.operator +\
			" "+getBoolExpression(node.right,node_list)+" )"
	else:
		return node.name

###########################################################################

