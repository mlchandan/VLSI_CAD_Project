from nodeclass import Node,Stack,LUT
from pyeda.inter import *


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
	input_list=[]
	for token in postfix_list.split():
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			x= Node(token)
			if token not in [each.operator for each in input_list]:
				input_list.append(x)  ###
			#fulllist.append(x)
			nodes_list.push(x)

		elif token in '~!':
			left_node = nodes_list.pop()
			if left_node.operator in [each.operator for each in input_list]:
				left_node=next((x for x in input_list if x.operator == left_node.operator), None)
			x= Node(token,left_node)
			fulllist.append(x)
			nodes_list.push(x)

		elif token in '&|^':
			left_node = nodes_list.pop()

			if left_node.operator in [each.operator for each in input_list]:
				left_node = next((x for x in input_list if x.operator == left_node.operator), None)
			right_node = nodes_list.pop()
			if right_node.operator in [each.operator for each in input_list]:
				right_node=next((x for x in input_list if x.operator == right_node.operator), None)
				
			x= Node(token,left_node,right_node)
			fulllist.append(x)
			nodes_list.push(x)			
	fulllist.reverse() # to make root node come on top
	for i in range(len(fulllist)):
		fulllist[i].name= "n"+str(i)+"_"+fulllist[i].operator	
	for i in input_list:
			i.name=i.operator
	return nodes_list.pop(),fulllist+input_list

###########################################################################
"""
Given a parse tree/ subtree which would be representing the LUT,
function returns the boolean expression for that subtree.

"""
def getBoolExpression(node, node_list):
	node_list_name =[x.name for x in node_list]
	if node.name in node_list_name:
		if node.operator == "~":
			return "~"+" ( "+getBoolExpression(node.left,node_list)+" )"
		if node.depth() == 0:
			return node.name
		else:
			return "( "+getBoolExpression(node.left,node_list)+" "+node.operator +\
			" "+getBoolExpression(node.right,node_list)+" )"
	else:
		return node.name

###########################################################################

def VerifyLUTset(Expression, lut_list , tree_list ):
	#Actual Boolean expression
	pyeda_exp =expr(Expression)
	print(str(pyeda_exp))
	a = expr2truthtable(pyeda_exp)

	#Derived Boolean expression and truth table
	intial_inputs={}
	listalp=sorted([x.name for x in tree_list if x.depth()==0])
	for i in range(len(listalp)):
		intial_inputs[listalp[i]]=0
	out=''

	for i in range(2**len(listalp)):
		in1 =bin(i)[2:].zfill(len(listalp)) 
		in1=in1[::-1]
		for l in range(len(listalp)):
			intial_inputs[listalp[l]]= int(in1[l])
		out+= str( lut_list[0].getOutput(intial_inputs,lut_list) )

	ab ="".join(listalp)
	f = truthtable( map(exprvar,ab),out)


	print('\n\n')
	#print derived truth table
	print('TRUTH TABLE OF THE LUT :')
	print(f )

	#Compare TRuth Table
	print("Result of Logic Verification : " , str(f) == str(a))
