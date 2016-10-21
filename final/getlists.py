import copy
from nodeclass import *


###########################################################################

def get_list_of_tuples(value):
	sets=[]
	for i in range(value+1):
		for j in range(value+1):
			if (i+j) == value:
				sets.append((i,j))
	return sets

###########################################################################		
#This function gives lists of subtrees each formed by straight path,
#i.e., no branching in the subtrees

def get_lists_of_StraightNodesList_recurr(remainingsize ,slist , root,bigBucket):
		
	if root == None or root.depth() == 0 or remainingsize == 0:
		return

	slist.append(root)

	#To check if node is  an inverter
	if root.left != None and root.right == None:
		get_lists_of_StraightNodesList_recurr(remainingsize ,slist, root.left,bigBucket)	


	if remainingsize != 1 :
		slist_copy=[]
		slist_copy=copy.deepcopy( slist )

		get_lists_of_StraightNodesList_recurr(remainingsize-1 ,slist, root.left,bigBucket)
		get_lists_of_StraightNodesList_recurr(remainingsize-1 ,slist_copy , root.right,bigBucket)

	if remainingsize == 1 or root.depth() == 1 :
		bigBucket.append(slist)
		return refine_List_of_Lists(bigBucket)

###########################################################################		

def refine_List_of_Lists(alist):
	alist.sort(key=len)
	alll=[]
	for j in range(len(alist)):
		smallindexlist= [x for x in range(j,len(alist))if x != j]
		smallindexlist.reverse()
		if not any((all(any(n.name == o.name for o in alist[x]) for n in alist[j]) )for x in smallindexlist) :
			alll.append(alist[j])


	#remove extra nodes from each list
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
def getsubTree(noOfNodes,root):
	alllist=[]

	if noOfNodes == 1 or root.depth() == 1:
		return [[root]]
	else:
		if not ( root.left != None and root.right == None):
			noOfNodes = noOfNodes - 1
		
	for i in get_list_of_tuples(noOfNodes):	
		bigBucket=list()
		if root.left!=None:
			get_lists_of_StraightNodesList_recurr(i[0],[],root.left,bigBucket)
			leftlist=bigBucket
		else:
			leftlist=[]
		
		bigBucket=list()
		if root.right!=None:
			get_lists_of_StraightNodesList_recurr(i[1],[],root.right,bigBucket)
			rightlist=bigBucket
		else:
			rightlist=[]
		
		if leftlist == [] and rightlist != []:
			for j in rightlist:
				alllist.append(list(set( [root] + j)))

		elif leftlist != [] and rightlist == []:
			for j in leftlist:
				alllist.append(list(set( j + [root])))

		else:
			for j in leftlist:
				for k in rightlist:
					alllist.append(list(set(j + [root] + k )))
	return alllist


###########################################################################		

def getsubTree_lists(noOfNodes_in_LUT , root):
	alllist=[]

	if noOfNodes_in_LUT == 1 :
		if  ( root.left != None and root.right == None):#if inverter
			return [[root,root.left]]
		else:
			return [[root]]


	if root.depth()== 1:
		return [[root]]
	
	noOfNodes_in_LUT = noOfNodes_in_LUT -1	
	
	for i in get_list_of_tuples(noOfNodes_in_LUT):	
		if root.left!=None:
			left_list_of_list=getsubTree(i[0],root.left)
		else:
			left_list_of_list=[[]]
		
		if root.right!=None:
			right_list_of_list=getsubTree(i[1],root.right)
		else:
			right_list_of_list=[[]]

		if left_list_of_list == [] and right_list_of_list != []:
			for j in right_list_of_list:
				alllist.append(list(set( [root] + j )))
		
		elif left_list_of_list != [] and right_list_of_list == []:
			for j in left_list_of_list:
				alllist.append(list(set( j + [root] )))
		
		else:
			for j in left_list_of_list:
				for k in right_list_of_list:
					alllist.append(list(set(j + [root] + k )))
	

	return refine_List_of_Lists(alllist)

###########################################################################		


def print_lists_of_lists_of_nodes(alllist):
	for a in alllist:
		for k in a:
			print k.name, " " ,
		print ""

###########################################################################		

def print_list_of_nodes(a):
	for k in a:
		print k.name, " " ,
	print ""

###########################################################################		


