#Module for tree and  classes
from nodeclass import *
from BoolExprFunc import *
from getlists import *


###########################################################################		

#Initilisations
Expression= "  ~ ( A  | ( B   &  C ) ) ^  ( D | E )  & ( F   &  G )  "
LUT_input_size=6

###########################################################################		

"""STAGE 1 progress
For a given boolean expression, Convert it to binary tree
Obtain which is the root node
"""


print("Boolean Expression = ",Expression)
print("LUT input size = ",LUT_input_size) 
print("So maximum nodes that can be fitted into  a LUT = ",str(LUT_input_size -1))

Number_of_Nodes_in_LUT = LUT_input_size -1
postfix_list = infixToPostfix(Expression)

print("\n POSTFIX Expression = ",postfix_list)


Tree,tree_list = postfix_2_tree (postfix_list)

print("\nNumber of  Nodes in the tree obtained from Boolean expression = ",str(len(tree_list)))


print("\nThe Binary nodes of the tree are :\n")
print("Node left_child Right_child")
for i in tree_list:
	print(i.name , " ", end=" ")
	if i.left != None:
		print(i.left.name ," ", end=" ")
	else:
		print(None, end=" ")
	if i.right != None:
		print(i.right.name ," ")
	else:
		print(None)
	

###########################################################################

"""
#Stage 1 completed
#Stage 2 progress :
#Aim to get all possible sets of LUT splits(parse trees combinations).
"""

print("\n Primary Node= ",Tree.name)


#x=getremainingNodes_list(tree_list , [[tree_list[0],tree_list[1]]])
#print_list_of_nodes(x)

possible_LUT_cuts = []
all_possible_LUT_cuts([],possible_LUT_cuts,tree_list,Number_of_Nodes_in_LUT)

print("\n\nTotal number of possibility of LUT cuts =",len(possible_LUT_cuts))
print("\n\nAll possible LUT  cuts =")
print_list_of_lists_of_lists_nodes(possible_LUT_cuts)



#print possible_LUT_cuts.index(final_cutset)
result = list(filter(lambda x: len(x) == min(map(len, possible_LUT_cuts)), possible_LUT_cuts))
print("\n\nLUT cuts with minimum size =")
print_list_of_lists_of_lists_nodes(result)

print("\n\nSelected LUT cut = ")
set1 = result[0]
print_lists_of_lists_of_nodes(set1)


###########################################################################

"""
#Stage 2 completed
#Stage 3 progress :
#Get boolean expressions of the LUT splits.
#Define LUT class and fill the memory array using Pyeda

"""

print("\n\nThe boolean expression for each parse tree =")
for parse_tree in set1:
	parse_tree.sort(key=lambda x: x.depth(), reverse=True)
	print("parse tree=", end=" ")
	print_list_of_nodes(parse_tree)
	print("Expression=", getBoolExpression(parse_tree[0],parse_tree))
	print()





###########################################################################

"""
#Stage 4 :
Connect the LUTS to act as Event driven logic.
Make test.py to test the LUT logic with boolean expression logic.
Represent the boolean tree in GUI form.
"""

###########################################################################

"""
#Stage 5 :
Above approach is a brute force method.
Optimise the approach of partitioning.
"""

