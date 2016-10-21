#Module for tree and  classes
from nodeclass import *
from BoolExprFunc import *
from getlists import *



###########################################################################		

#Initilisations
Expression= "  ~ ( A  | ( B   &  C ) ) ^ ( D | E ) ^ ( D | E )  "
LUT_input_size=6

###########################################################################		

"""STAGE 1 progress
For a given boolean expression, Convert it to binary tree
Obtain which is the root node
and Get set of cuts based on the LUT expression
"""


print "Boolean Expression = ",Expression,"\n" 
print "LUT input size = ",LUT_input_size,"\n" 
print "So maximum nodes that can be fitted into  a LUT = ",str(LUT_input_size -1)

Number_of_Nodes_in_LUT = LUT_input_size -1
postfix_list = infixToPostfix(Expression)

print "\n POSTFIX Expression = ",postfix_list

Tree,tree_list = postfix_2_tree (postfix_list)

print "\nNumber of  Nodes in the tree obtained from Boolean expression = ",str(len(tree_list))

print "\nThe Binary nodes of the tree are :"
for i in tree_list:
	print i.name , " ", 
	if i.left != None:
		print i.left.name ," ",
	else:
		print None,
	if i.right != None:
		print i.right.name ," "
	else:
		print None
	
#print "\n Primary SETs= "
x=getsubTree_lists(Number_of_Nodes_in_LUT,Tree)
print_lists_of_lists_of_nodes((x))


###########################################################################

"""
Stage 1 completed
Stage 2 progress :
Aim to get all possible sets of LUT splits.
"""

set1=x[0]
print_list_of_nodes(set1)

























