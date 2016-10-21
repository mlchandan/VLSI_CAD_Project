from nodeclass import Node,Stack

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
  for i in range(len(nodes_list)):
      nodelist[i].name= "n"+str(i)+"_"+nodelist[i].operator

	return nodes_list.pop(),nodes_list




###########################################################################