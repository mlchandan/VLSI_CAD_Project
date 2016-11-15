from nodeclass import *


###########################################################################
""" 
Returns the list of tuples of size 2, such that it's sum = input value provided
"""
def get_list_of_tuples(value):
	sets=[]
	for i in range(value+1):
		for j in range(value+1):
			if (i+j) == value:
				sets.append((i,j))
	return sets


###########################################################################		
"""
There is possibility that, in a list of trees, A tree can be a part of another 
tree in the list. Such tree is redundant.
This function removes such trees.So that computation  recurence is minimized
"""
def refine_List_of_Lists(alist):
	alist.sort(key=len)
	alll=[]
	for j in range(len(alist)):
		smallindexlist= [x for x in range(j,len(alist))if x != j]
		smallindexlist.reverse()
		if not any((all(any(n.name == o.name for o in alist[x]) for n in alist[j]) )for x in smallindexlist) :
			alll.append(alist[j])
	#remove extra nodes from each list if present
	ref=[]
	for list1 in alll:
		list2 = []    
		for i in list1: 
			names=[]
			for k in list2:
				names.append(k.name)
			if not i.name in names:
				list2.append(i)
		ref.append(list2)
	return ref
	
	
	
###########################################################################		
"""
Returns all possible set of subtrees having root_node.
Inverter node is not considered while counting Number of Nodes to be present
in a subtree.

"""
def getsubTree_lists(noOfNodes, root):
	if root.depth() == 0 or noOfNodes == 0:
		return [[]]
		
	if root.depth() == 1:
		return [[root]]
	
	if noOfNodes == 1:
		if not ( root.left != None and root.right == None):#if not inverter
			return [[root]]
		else:
			return [[root,root.left]]

	if 	not ( root.left != None and root.right == None):#if not inverter
		noOfNodes = noOfNodes -1

	list1=[]
	for i in get_list_of_tuples(noOfNodes):
		left_list_of_lists = getsubTree_lists( i[0], root.left)
		if 	not ( root.left != None and root.right == None):#if not inverter
			right_list_of_lists = getsubTree_lists(i[1] , root.right)
		else:
			right_list_of_lists = [[]]		
		list1.extend ([l + r for l in left_list_of_lists for r in right_list_of_lists ])
	[A.append(root) for A in list1]
	return refine_List_of_Lists(list1)


###########################################################################		
"""
Below print functions are used to display the objects in terms of their attribute "name"
for easy understandability.

"""
def print_list_of_lists_of_lists_nodes(allist):
	for index,sub in enumerate(allist):
		#print "index = ",index
		print("Length = " ,len(sub))
		for a in sub:
			print("[", end=" ")
			for k in a:
				print( k.name, ",", end=" ")
			print("] ", end=" ")
		print()

###########################################################################		

def print_lists_of_lists_of_nodes(alllist):
	for a in alllist:
		for k in a:
			print(k.name, " ", end=" ")
		print()

###########################################################################		

def print_list_of_nodes(a):
	for k in a:
		print(k.name, " ", end=" ")
	print()
###########################################################################		

"""
Since we are comparing nodes which are objects.
Comparision is used considering the name, to be on safer side

Not necessary!!!
"""
def getremainingNodes_list(allNodes_list,removeNodes_list ):
	if all(isinstance(elem, list) for elem in removeNodes_list):
		removeNodes_list = sum( removeNodes_list , []) 
	otherNodes_list=[]
	otherNodes_list = list(filter(lambda x: x not in removeNodes_list and x.depth()!=0,allNodes_list))
	otherNodes_list.sort(key=lambda x: x.depth(), reverse=True)
	return otherNodes_list

###########################################################################		
"""
This function provides all possible "list of subtrees" which represent the
boolean expression given.
  
"""
def  all_possible_LUT_cuts(combinations,final_list,tree_list, Number_of_Nodes):	
	if combinations == []:
		combinations=getsubTree_lists( Number_of_Nodes, tree_list[0])
		combinations = [[x] for x in combinations]
	for comb in combinations:
		remainigNodes =[]
		remainigNodes =  getremainingNodes_list(tree_list , comb)
		
		if  remainigNodes == []:
			final_list.append(comb)
		else:
			subtree1 = getsubTree_lists (Number_of_Nodes,remainigNodes[0])
			combinations2 =[]
			for i in subtree1:
				a=comb+[i]
				combinations2.append(a)
			all_possible_LUT_cuts(combinations2,final_list,tree_list, Number_of_Nodes)
