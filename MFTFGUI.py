import numpy as np
import math
import time
import tkSimpleDialog
from Tkinter import *
root=Tk()

#--------------------------------------------------FRAMES--------------------------------------------------------------------------

frame0=Frame(root,height=780,width=465,bg='lightblue')
frame0.grid(row=0,column=0)
frame1=Frame(root,height=780,width=900,bg='purple')
frame1.grid(row=0,column=1)

label=[0,0,0]
log=[0,0,0]

label[0]=Label(frame1,bg='black')
label[0].place(x=100,y=100,width=100,height=545)

label[1]=Label(frame1,bg='black')
label[1].place(x=400,y=100,width=100,height=545)

label[2]=Label(frame1,bg='black')
label[2].place(x=700,y=100,width=100,height=545)

text0=Label(frame1,text='First Fit',bg="magenta")
text0.place(x=118,y=50)

text1=Label(frame1,text='Best Fit',bg="magenta")
text1.place(x=418,y=50)

text2=Label(frame1,text='Worst Fit',bg="magenta")
text2.place(x=718,y=50)

log[0]=Label(frame1,bg="black",width=300,height=50)
log[0].place(x=5,y=650,height=50,width=290)

log[1]=Label(frame1,bg="black",width=300,height=50)
log[1].place(x=305,y=650,height=50,width=290)

log[2]=Label(frame1,bg="black",width=300,height=50)
log[2].place(x=605,y=650,height=50,width=290)

processno=0




blox=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

def close_window (): 
    root.destroy()
    
button4 = Button (frame0, text = "Exit",bg="blue",fg="white", activebackground="black",activeforeground="white",command = close_window)
button4.place(x=116,y=500,width=232,height=50)

#--------------------------------------------------FIRST_FIT------------------------------------------------------------------------

NumberOfBlocks=10

block=[{'process':-1,'mem':10,'alloc':0},{'process':-1,'mem':20,'alloc':0},{'process':-1,'mem':30,'alloc':0},{'process':-1,'mem':5,'alloc':0},{'process':-1,'mem':5,'alloc':0},{'process':-1,'mem':10,'alloc':0},
{'process':-1,'mem':7,'alloc':0},
{'process':-1,'mem':3,'alloc':0},
{'process':-1,'mem':4,'alloc':0},
{'process':-1,'mem':6,'alloc':0}]

mem=[0,0,0,0,0,0,0,0,0,0]

for i in xrange(NumberOfBlocks):
	mem[i]=block[i]['mem']
	

for i in xrange(10):
	blox[0][i]=Label(label[0],height=50,width=100,bg="red",text="EMPTY")
	blox[0][i].place(y=i*5+(float(sum(mem[0:i]))/10)*50,height=(float(block[i]['mem'])/100)*500,width=100)

for i in xrange(10):
	blox[1][i]=Label(label[1],height=50,width=100,bg="red",text="EMPTY")
	blox[1][i].place(y=i*5+(float(sum(mem[0:i]))/10)*50,height=(float(block[i]['mem'])/100)*500,width=100)
	
for i in xrange(10):
	blox[2][i]=Label(label[2],height=50,width=100,bg="red",text="EMPTY")
	blox[2][i].place(y=i*5+(float(sum(mem[0:i]))/10)*50,height=(float(block[i]['mem'])/100)*500,width=100)

a=[1,1,1,0]
process=[]


def firstfit(processno,m,flag0):

	root.update()
			
	if flag0==1:
		print "New Process"
		print m
		flag1=1
		for j in xrange(NumberOfBlocks):
			if((block[j]['process']==-1)&(block[j]['mem']>=m)):
				flag1 = 0
				process.append(processno)
				block[j]['process']=processno
				block[j]['alloc']=m
				blox[0][j].configure(text='')
				box=Label(label[0],height=50,width=100,bg="green",text="PROCESS"+str(processno))
				box.place(y=j*5+(float(sum(mem[0:j]))/10)*50,height=(float(m)/100)*500,width=100)
				log[0]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Process "+str(processno)+" Allocated" )
				log[0].place(x=5,y=650,height=50,width=290)
				break
		if flag1:
			free=0
			for j in xrange(NumberOfBlocks):
				if block[j]['process']==-1:
					free=free+block[j]['mem']
			if free>=m:
				print "External Fragmentation"
				log[0]=Label(frame1,bg="black",fg="white",width=300,height=50,text="External Fragmentation !!" )
				log[0].place(x=5,y=650,height=50,width=290)
			else:
				print "Not enough space"
				log[0]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Not enough memory in Disk !!" )
				log[0].place(x=5,y=650,height=50,width=290)
	else :
		No=processno	
		print " Remove process" , No
		process.remove(No)
		for j in xrange(NumberOfBlocks):	
			if block[j]['process']==No:		
				block[j]['process']=-1
				block[j]['alloc']=0
				blox[0][j]=Label(label[0],height=50,width=100,bg="red",text="EMPTY")
				blox[0][j].place(y=j*5+(float(sum(mem[0:j]))/10)*50,height=(float(block[j]['mem'])/100)*500,width=100)
				log[0]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Process "+str(No)+" Terminated" )
				log[0].place(x=5,y=650,height=50,width=290)
				break
	time.sleep(1)
	for j in xrange(NumberOfBlocks):
		print "-->" , block[j]['process'],block[j]['mem'],block[j]['alloc']	
		
#---------------------------------------------------------FIRST FIT-----------------------------------------------------------------


#---------------------------------------------------------BEST FIT------------------------------------------------------------------
block1=[{'process':-1,'mem':10,'alloc':0},{'process':-1,'mem':20,'alloc':0},{'process':-1,'mem':30,'alloc':0},{'process':-1,'mem':5,'alloc':0},{'process':-1,'mem':5,'alloc':0},{'process':-1,'mem':10,'alloc':0},
{'process':-1,'mem':7,'alloc':0},
{'process':-1,'mem':3,'alloc':0},
{'process':-1,'mem':4,'alloc':0},
{'process':-1,'mem':6,'alloc':0}]

process1=[]

def bestfit(processno,m,flag0):

	root.update()
			
	if flag0==1:
		print "New Process"
		print m
		flag1=1
		min=1000
		pos=-1
		for j in xrange(NumberOfBlocks):
			if((block1[j]['process']==-1)&(block1[j]['mem']>=m)&(block1[j]['mem']<min)):
				flag1 = 0
				min=block1[j]['mem']
				pos=j
			
		if flag1==0:
			process1.append(processno)
			block1[pos]['process']=processno
			block1[pos]['alloc']=m
			blox[1][pos].configure(text='')
			box=Label(label[1],height=50,width=100,bg="green",text="PROCESS"+str(processno))
			box.place(y=pos*5+(float(sum(mem[0:pos]))/10)*50,height=(float(m)/100)*500,width=100)
			log[1]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Process "+str(processno)+" Allocated" )
			log[1].place(x=305,y=650,height=50,width=290)
			

		if flag1:
			free=0
			for j in xrange(NumberOfBlocks):
				if block1[j]['process']==-1:
					free=free+block1[j]['mem']
			if free>=m:
				print "External Fragmentation"
				log[1]=Label(frame1,bg="black",fg="white",width=300,height=50,text="External Fragmentation !!" )
				log[1].place(x=305,y=650,height=50,width=290)
			else:
				print "Not enough space"
				log[1]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Not enough memory in Disk !!" )
				log[1].place(x=305,y=650,height=50,width=290)
	else :
		No=processno	
		print " Remove process" , No
		process1.remove(No)
		for j in xrange(NumberOfBlocks):	
			if block1[j]['process']==No:		
				block1[j]['process']=-1
				block1[j]['alloc']=0
				blox[1][j]=Label(label[1],height=50,width=100,bg="red",text="EMPTY")
				blox[1][j].place(y=j*5+(float(sum(mem[0:j]))/10)*50,height=(float(block1[j]['mem'])/100)*500,width=100)
				log[1]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Process "+str(No)+" Terminated" )
				log[1].place(x=305,y=650,height=50,width=290)
				break
	time.sleep(1)
	for j in xrange(NumberOfBlocks):
		print "-->" , block1[j]['process'],block1[j]['mem'],block1[j]['alloc']	
		
#---------------------------------------------------------BEST FIT------------------------------------------------------------------

#---------------------------------------------------------WORST FIT-----------------------------------------------------------------


block2=[{'process':-1,'mem':10,'alloc':0},{'process':-1,'mem':20,'alloc':0},{'process':-1,'mem':30,'alloc':0},{'process':-1,'mem':5,'alloc':0},{'process':-1,'mem':5,'alloc':0},{'process':-1,'mem':10,'alloc':0},
{'process':-1,'mem':7,'alloc':0},
{'process':-1,'mem':3,'alloc':0},
{'process':-1,'mem':4,'alloc':0},
{'process':-1,'mem':6,'alloc':0}]

process2=[]

def worstfit(processno,m,flag0):

	root.update()
			
	if flag0==1:
		print "New Process"
		print m
		flag1=1
		max=-1
		pos=-1
		for j in xrange(NumberOfBlocks):
			if((block2[j]['process']==-1)&(block2[j]['mem']>=m)&(block2[j]['mem']>max)):
				flag1 = 0
				max=block2[j]['mem']
				pos=j
			
		if flag1==0:
			process2.append(processno)
			block2[pos]['process']=processno
			block2[pos]['alloc']=m
			blox[2][pos].configure(text='')
			box=Label(label[2],height=50,width=100,bg="green",text="PROCESS"+str(processno))
			box.place(y=pos*5+(float(sum(mem[0:pos]))/10)*50,height=(float(m)/100)*500,width=100)
			log[2]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Process "+str(processno)+" Allocated" )
			log[2].place(x=605,y=650,height=50,width=290)
			

		if flag1:
			free=0
			for j in xrange(NumberOfBlocks):
				if block2[j]['process']==-1:
					free=free+block2[j]['mem']
			if free>=m:
				print "External Fragmentation"
				log[2]=Label(frame1,bg="black",fg="white",width=300,height=50,text="External Fragmentation !!" )
				log[2].place(x=605,y=650,height=50,width=290)
			else:
				print "Not enough space"
				log[2]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Not enough memory in Disk !!" )
				log[2].place(x=605,y=650,height=50,width=290)
	else :
		No=processno	
		print " Remove process" , No
		process2.remove(No)
		for j in xrange(NumberOfBlocks):	
			if block2[j]['process']==No:		
				block2[j]['process']=-1
				block2[j]['alloc']=0
				blox[2][j]=Label(label[2],height=50,width=100,bg="red",text="EMPTY")
				blox[2][j].place(y=j*5+(float(sum(mem[0:j]))/10)*50,height=(float(block2[j]['mem'])/100)*500,width=100)
				log[2]=Label(frame1,bg="black",fg="white",width=300,height=50,text="Process "+str(No)+" Terminated" )
				log[2].place(x=605,y=650,height=50,width=290)	
				break
	time.sleep(1)
	for j in xrange(NumberOfBlocks):
		print "-->" , block2[j]['process'],block2[j]['mem'],block2[j]['alloc']	
		

#---------------------------------------------------------WORST FIT-----------------------------------------------------------------

#--------------------------------------------------BUTTONS--------------------------------------------------------------------------

def create_process ():

	processno=var = tkSimpleDialog.askstring("Enter Process", "Enter Process Number")
	var = tkSimpleDialog.askstring("Process "+processno, "Enter Memory requirement`")
	firstfit(int(processno),int(var),1)
	bestfit(int(processno),int(var),1)
	worstfit(int(processno),int(var),1)

def terminate_process ():
	
	master = Tk()
	var = StringVar(master)
	try:
		var.set(process[0]) 
	except:
		var.set("NONE")
	option= apply(OptionMenu, (master, var) + tuple(process))
	option.pack()
	def ok():
		firstfit(int(var.get()),0,0)
		bestfit(int(var.get()),0,0)
		worstfit(int(var.get()),0,0)
		master.destroy()
	    
	button = Button(master, text="OK", command=ok,width=25)
	button.pack()
	
	master.mainloop()

def reset():
	for j in xrange(NumberOfBlocks):
		block[j]['alloc']=0
		block[j]['process']=-1
		block1[j]['alloc']=0
		block1[j]['process']=-1
		block2[j]['alloc']=0
		block2[j]['process']=-1
	for j in xrange(len(process)):
		try:
			del process[0]
		except:
			print "clean"
		try:
			del process1[0]
		except:
			print "clean"
		try:
			del process2[0]
		except:
			print "clean"
		
	for i in xrange(10):
		blox[0][i]=Label(label[0],height=50,width=100,bg="red",text="EMPTY")
		blox[0][i].place(y=i*5+(float(sum(mem[0:i]))/10)*50,height=(float(block[i]['mem'])/100)*500,width=100)

	for i in xrange(10):
		blox[1][i]=Label(label[1],height=50,width=100,bg="red",text="EMPTY")
		blox[1][i].place(y=i*5+(float(sum(mem[0:i]))/10)*50,height=(float(block[i]['mem'])/100)*500,width=100)
	
	for i in xrange(10):
		blox[2][i]=Label(label[2],height=50,width=100,bg="red",text="EMPTY")
		blox[2][i].place(y=i*5+(float(sum(mem[0:i]))/10)*50,height=(float(block[i]['mem'])/100)*500,width=100)
	
	log[0]=Label(frame1,bg="black",width=300,height=50)
	log[0].place(x=5,y=650,height=50,width=290)

	log[1]=Label(frame1,bg="black",width=300,height=50)
	log[1].place(x=305,y=650,height=50,width=290)

	log[2]=Label(frame1,bg="black",width=300,height=50)
	log[2].place(x=605,y=650,height=50,width=290)
	
	
	
	
button0 = Button (frame0, text = "Create Process",bg="blue",fg="white", activebackground="black",activeforeground="white",command = create_process)
button0.place(x=116,y=100,width=232,height=50)
	
button1 = Button (frame0, text = "Terminate Process",bg="blue",fg="white", activebackground="black",activeforeground="white",command = terminate_process)
button1.place(x=116,y=200,width=232,height=50)

button3 = Button (frame0, text = "Reset",bg="blue",fg="white", activebackground="black",activeforeground="white",command = reset)
button3.place(x=116,y=400,width=232,height=50)

'''
button2 = Button (frame0, text = "Display Stats",bg="blue",fg="white", activebackground="black",activeforeground="white",command = display)
button2.place(x=116,y=300,width=232,height=50)
'''
				
root.mainloop()
