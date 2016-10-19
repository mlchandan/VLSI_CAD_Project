import copy
import itertools  

class Node:

	def __init__(self, operator, left=None, right=None,name=None):
		"""(Node, object, Node, Node) -> NoneType
		Initialize this node to store item and have children left and right.
		"""
		self.operator = operator
		self.left = left
		self.right = right
		self.name = name
		
		
	def depth(self):
		if self.left == None and self.right == None:
			return 0
		left_depth = self.left.depth() if self.left else 0
		right_depth = self.right.depth() if self.right else 0
		return max(left_depth, right_depth) + 1

	

	
	def execute(self):
		if self.operator == "~":
			self.output = bool2str(not (str2bool(self.left.inputs)))
		elif self.function == "|":
			self.output = bool2str(any (str2bool(self.left.inputs)))
		elif self.function == "nor":
			self.stored_vlaue.append(bool2str(not any(temp)))
		elif self.function == "nand":
			self.stored_vlaue.append(bool2str(not all(temp)))
		elif self.function == "and":
			self.stored_vlaue.append(bool2str(all(temp)))
		elif self.function == "xor":
			self.stored_vlaue.append(bool2str(reduce(lambda i, j: i ^ j, temp)))
		elif self.function == "xnor":
			self.stored_vlaue.append(bool2str(reduce(lambda i, j: not(i ^ j), temp)))
		else:
			print "Error: Invalid function"
			quit()
	
		return  self.item

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
	slist.append(root)
	
	if remainingsize <= 0:
		return []
		
	if remainingsize == 1 or (root.left == None and root.right == None) :
		for aNode in bigBucket:
			if slist in aNode:
				return
		bigBucket.append(slist)
		return bigBucket

	if remainingsize != 1 :
		slist_copy=[]
		slist_copy=copy.deepcopy( slist ) 
		get_lists_of_StraightNodesList_recurr(remainingsize-1 ,slist, root.left,bigBucket)		
		get_lists_of_StraightNodesList_recurr(remainingsize-1 ,slist_copy , root.right,bigBucket)

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

	if noOfNodes == 1 or root.depth() == 0:
		return [[root]]
	else:
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
				alllist.append(list(set(j + [root])))

		elif leftlist != [] and rightlist == []:
			for j in leftlist:
				alllist.append(list(set( j + [root])))

		else:
			for j in leftlist:
				for k in rightlist:
					alllist.append(list(set(j + k + [root])))
	return alllist


###########################################################################		

def getTree(noOfNodes_in_LUT , root):
	alllist=[]
	if noOfNodes_in_LUT == 1 or root.depth()==0:
		return [[root]]
	else:
		noOfNodes_in_LUT = noOfNodes_in_LUT -1
	
	for i in get_list_of_tuples(noOfNodes_in_LUT):	
		if root.left!=None:
			left_list_of_list=getsubTree(i[0],root.left)
		else:
			left_list_of_list=[[]]
		
		if root.right!=None:
			right_list_of_list=getsubTree(i[1],root.right)
		else:
			rightlist=[[]]

		if left_list_of_list == [] and right_list_of_list != []:
			for j in right_list_of_list:
				alllist.append(list(set(j + [root])))
		
		elif left_list_of_list != [] and right_list_of_list == []:
			for j in left_list_of_list:
				alllist.append(list(set( j + [root])))
		
		else:
			for j in left_list_of_list:
				for k in right_list_of_list:
					alllist.append(list(set(j + k + [root])))
		
	return refine_List_of_Lists(alllist)

###########################################################################		


def printnode(alllist):
	for a in alllist:
		for k in a:
			print k.name, " " ,
		print ""

###########################################################################		

def printlist(a):
	for k in a:
		print k.name, " " ,
	print ""


###########################################################################		
#Example of the
#Nodes constituting binary tree 
#to test the list

n6=Node(0,None,None,'n6')
n4=Node(0,None,None,'n4')
n5=Node(0,None,None,'n5')
n3=Node(0,None,None,'n3')
n2=Node(0,n5,n6,'n2')
n1=Node(0,n3,n4,'n1')
n0=Node(0,n1,n2,'n0')

noOfNodes_in_LUT=4
print "noOfNodes_in_LUT =",noOfNodes_in_LUT
x=getTree(noOfNodes_in_LUT,n0)

printnode(x)
