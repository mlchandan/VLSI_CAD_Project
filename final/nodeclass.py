from pyeda.inter import *

#################################################################################
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
         
#################################################################################
         
# Tree node
class Node:

	def __init__(self, operator=None, left=None, right=None , name=None):
		"""(Node, object, Node, Node) -> NoneType
		Initialize this node to store item and have children left and right.
		"""
    
		self.operator = operator
		self.left = left
		self.right = right
		self.name=name

	def depth(self):
		# Base Case : Leaf node.This accounts for height = 0
		if self.left == None and self.right == None:
			return 0

		# If left subtree is Null, return 0
		left_depth = self.left.depth() if self.left!=None else 0
		# If right subtree is Null , returns 0
		right_depth = self.right.depth() if self.right!=None else 0

		return max(left_depth, right_depth) + 1

#################################################################################
         
# Tree node
class LUT:

	def __init__(self, expression ,output, input_size):
		self.input_size =input_size
		self.output=output
		self.inputs=[]
		self.input_renamed={}
		self.mem_array = self.Fill_Array(expression,input_size)
	
	def Fill_Array(self,expression,input_size):
		expr_list=expression.split()
		self.inputs = list(filter(lambda z: z not in "~!&^|()",expr_list))
		lists="abcdefghijklmnopqrstuvwxyz"

		#Replace the variables
		#store which variable is replaced by what
		for indx in range(input_size):
			if indx < len(self.inputs):
				expression = expression.replace(self.inputs[indx], lists[indx] )
				self.input_renamed[indx]= self.inputs[indx]
			else:
				self.input_renamed[indx]=	'-'
			
		pyeda_expr = expr(expression) #Pyeda expression
		pyeda_tt = expr2truthtable(pyeda_expr) # Pyeda Truth table
		y = list(pyeda_tt.satisfy_all()) # get list od dictionaries which has output=1
		
		indexes_with_ouput1=[]
		for each in y:
			e=sorted(each.items())#Arrange sequence with MSB='A' followed by 'BCDEF'
			v=list(a[1] for a in e) # Get the Dictionary values
			i= "".join(map(str, v)) # Get Binary String from dictionary values
			#Initialise 
			if len(v) < input_size:
				remaining_bit_size = input_size - len(v)
				list_of_binarys = [bin(x)[2:].rjust(remaining_bit_size, '0') for x in range(2**remaining_bit_size)]
				a = [i+x for x in list_of_binarys]
				for l in a:
					integer_value= int(l, 2) # Convert binary string(base 2) to Integer(base 10)
					indexes_with_ouput1.append(integer_value)
			else:
				integer_value= int(i, 2) # Convert binary string(base 2) to Integer(base 10)
				indexes_with_ouput1.append(integer_value)		
		mem_array=[]
		for i in range(2**input_size):
			if i in indexes_with_ouput1:
				mem_array.append('1')
			else:
				mem_array.append('0')
		return mem_array
	
	
	
	def getOutput(self,binary_input_dictionary,lut_list):
		all_inputs = binary_input_dictionary.keys()
		input_str=''
		
		for indx in range(self.input_size):
			if self.input_renamed[indx] == '-':
				input_str+='0'
			else:
				Ainput_name = self.input_renamed[indx]
				if Ainput_name in all_inputs:
					input_str+= str(binary_input_dictionary[Ainput_name])
				else:
					child_lut = next((eac_lut for eac_lut in lut_list if eac_lut.output.name == Ainput_name), None)
					input_str+= child_lut.getOutput(binary_input_dictionary,lut_list)
		return self.performLogic(input_str)
	
	def performLogic(self,binary_input_srting):
		integer_value= int(binary_input_srting, 2) # Convert binary string(base 2) to Integer(base 10)
		return self.mem_array[integer_value]
		
		
#################################################################################

