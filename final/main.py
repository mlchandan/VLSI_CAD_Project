#Module for tree and  classes
from nodeclass import *
from BoolExprFunc import *
from getlists import *


import matplotlib.ticker as plticker
import networkx as nx
import matplotlib.pyplot as plt

###########################################################################		

#Initilisations
Expression= "  ~ ( A  | ( B   &  C ) ) ^  ( D | E ) ^  ( D | E ) &  ( A  | ( B   &  C ) ) ^  ( D | E ) ^  ( D | E ) "
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
print("Node left_child Right_child depth")
for i in tree_list:
	print(i.name , " ", end=" ")
	if i.left != None:
		print(i.left.name ," ", end=" ")
	else:
		print(None, end=" ")
	if i.right != None:
		print(i.right.name)
	else:
		print(None)

###########################################################################	
nodes_list =[]
for i in tree_list:
	print(i.name , " ", end=" ")
	if i.left != None:
		nodes_list.append((i.name , i.left.name ) )
	if i.right != None:
		nodes_list.append((i.name , i.right.name ) )

def  hierarchy_pos(tree_list, root,width=1., vert_gap = 0.2, vert_loc = 0,pos= None, xcenter = 0.5):
	top_depth = tree_list[0].depth( )
	if pos == None:
		pos = {tree_list[0].name:(xcenter,vert_loc)}
	
	for a in range(top_depth):
		neighbors=[x for x in tree_list if x.depth() == a]
		print_list_of_nodes(neighbors)
		vert_loc = ( a - top_depth )*vert_gap
		for  indx, neighbor in  enumerate( neighbors ):
				hor_gap =   width / (len( neighbors ) + 1 )
				hor_loc =   hor_gap * (indx+1)
				pos[neighbor.name] = (hor_loc, vert_loc)
	return pos

edge_colors =range(len(nodes_list))
pos = hierarchy_pos( tree_list, tree_list[0] )
G=nx.MultiGraph()
G.add_edges_from(nodes_list)#rgbwcmy
nx.draw(G,node_size=1500,pos = pos, with_labels=True ,node_color='c',\
        edge_color=edge_colors,width=2,edge_cmap=plt.cm.Blues)
#plt.show()
plt.savefig("img/Tree_diagram.png") # save as png





###########################################################################


	

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


#nx.draw(G,node_size=1000,pos = pos, with_labels=True ,node_color='b',edge_color='r',width=3)
#plt.axis('off')
#plt.show()

colors='rgbwcmy' 
shapes ='ho'  #shov^

G=nx.Graph()
G.add_edges_from(nodes_list)
input_node_names = [x.name for x in tree_list if x.depth()==0]
nx.draw(G,pos, nodelist=input_node_names, node_size=1500,\
  node_color=colors[4], with_labels=True,node_shape='s',edge_color=edge_colors,width=4,edge_cmap=plt.cm.Blues)
for indx,each_set in enumerate(set1):
	nx.draw(G,pos, nodelist=[x.name for x in each_set], node_size=1500,\
	node_color=colors[indx % len(colors)], with_labels=True,node_shape=shapes[indx % len(shapes)],\
	edge_color=edge_colors,width=3,edge_cmap=plt.cm.Blues)
#plt.show()
plt.savefig("img/After_partitioning.png") # save as png



###########################################################################

"""
#Stage 2 completed
#Stage 3 progress :
#Get boolean expressions of the LUT splits.
#Define LUT class and fill the memory array using Pyeda
"""

boolExp=[]
lut_list=[]
print("\n\nThe boolean expression for each parse tree =")
for parse_tree in set1:
	parse_tree.sort(key=lambda x: x.depth(), reverse=True)
	print("parse tree=", end=" ")
	print_list_of_nodes(parse_tree)
	print("Expression:",parse_tree[0].name +"="+ getBoolExpression(parse_tree[0],parse_tree))
	eq =getBoolExpression(parse_tree[0],parse_tree)
	boolExp.append(eq)
	lut_list.append(LUT(eq,parse_tree[0],LUT_input_size))
	print('\n')

###########################################################################

"""
#stage 3 : Completed
#Stage 4 : In progress
Connect the LUTS to act as Event driven logic.
Make test.py to test the LUT logic with boolean expression logic.
Represent the boolean tree in GUI form.
"""
#intial_inputs={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
#print(lut_list[0].getOutput(intial_inputs,lut_list))


VerifyLUTset(Expression, lut_list , tree_list )

###########################################################################

"""
#Stage 5 :
Above approach is a brute force method.
Optimise the approach of partitioning.
"""

