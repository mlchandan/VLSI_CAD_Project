import matplotlib.pyplot as plt
import numpy as np

import operator

#initialization
key={}	# node name : index
values=list()


def str2bool(v):
	return map(lambda x: True if x== "1" else False,v)

def bool2str(v):
	return "1" if v==True else "0"

def addkey(v):
	for i in v:
		if i not in key.keys():
			key[i]=len(key)
			values.append('0')

def SquareWave(plot_values):
	ymin=-0.5
	ymax=1.5
	xmin=0
	xmax=tmax
	Nx=xmax*30
	offset=0
	num_of_signal=len(plot_values)
	plt.figure(1).suptitle('WAVEFORM', fontsize=14, fontweight='bold')
	plt.ylabel('some numbers')
	colors = ['b','g','r','c','m','y','k','w']
	
	for key,num in zip(plot_values.keys(),range(num_of_signal)):
		x=np.linspace(xmin, xmax, Nx)
		y=np.sign(x)
		for i in range(xmax):
			y[(x>i)]=plot_values[key][i]
		ax=plt.subplot((num_of_signal*100)+ 11 + num)
		plt.plot(x, y,colors[num % 7])
		plt.axis([xmin, xmax, ymin, ymax])
		plt.grid(True)
		ax.annotate(key, xy=(0.5, 0.9), xycoords='axes fraction',fontsize=14,fontweight='bold',color=colors[num % 7],va="top", ha="left")
		#ax.margins(0.3,0.3)
		#ax.axis('tight')	
			
		plt.xticks(np.arange(min(x), max(x)+1, 1.0))
		plt.yticks(np.arange(min(y), max(y)+1, 1.0))
	plt.subplots_adjust(wspace=0, hspace=0)
	plt.show()


class black_box(object):

	def __init__(self,in_nodes,out_nodes,func,delay):
		if type(in_nodes) != list:
			self.in_nodes=[in_nodes]
		else:
			self.in_nodes=in_nodes
		self.out_nodes=out_nodes
		self.delay=delay
		self.function=func
		self.stored_vlaue=['0' for j in range(delay-1)]
		addkey(self.in_nodes+ [self.out_nodes])

		
	def execute(self):
		values[key[self.out_nodes]]=self.stored_vlaue.pop(0)
		temp=str2bool([values[key[i]] for i in self.in_nodes])
		if self.function == "not":
			self.stored_vlaue.append(bool2str(not temp[0]))
		elif self.function == "or":
			self.stored_vlaue.append(bool2str(any(temp)))
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




####################################################################################
current_time=0
tmax=50
input_seq={0:"0",10:"1",20:"0"} #in1 sequence

block1=black_box(['in1','b'],'out1',"xor",8)		#(inputs,output,function,delay)

block2=black_box('in1','b',"not",6)

#block4=black_box('out1','out2',"not",6)
####################################################################################

plot_values=dict()
for i in key:
	plot_values[i]=[]

while current_time <= tmax:
	for i in key:
		plot_values[i].append(int(values[key[i]]))
	print str(current_time)," ","input=",values[key['in1']]," ","output=",values[key['out1']]
	block1.execute()
	block2.execute()
	current_time+=1
	if current_time in input_seq.keys():
		values[key['in1']]=input_seq[current_time]


SquareWave(plot_values)
