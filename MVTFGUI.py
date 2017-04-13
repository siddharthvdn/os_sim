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

label[0]=Label(frame1,bg='red')
label[0].place(x=100,y=100,width=100,height=500)

label[1]=Label(frame1,bg='red')
label[1].place(x=400,y=100,width=100,height=500)

label[2]=Label(frame1,bg='red')
label[2].place(x=700,y=100,width=100,height=500)

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

memory=100

#--------------------------------------------------FIRST_FIT------------------------------------------------------------------------
occupied0=[]
border0=[]
hole0=[[0,memory]]
process0=[]
block0=[]
processindex0=[]
box0=[]
coordinateindex0=[[]]
def firstfit(processno,m,ch):
	if ch==1:
		print "process",processno,"request"
		if hole0 == []:
			print "Memory Full"
			
		else:
			print m
			flag=0
			for i in hole0:
				if i[1]>= m:
					flag=1
					occupied0.append([i[0],m])
					process0.append(processno)
					occupied0.sort()
					hole0.remove(i)
					processindex0.append([i[0],processno])
					processindex0.sort()
					print "process",processno, "added"
					box=Label(label[0],width=10,height=30,bg='green',text="Process"+str(processno),borderwidth=5,relief=RAISED)
					box0.append([processno,box])
					for j in xrange(np.shape(box0)[0]):
						if box0[j][0]==processno:
							mem=0
							for k in xrange(np.shape(processindex0)[0]):
								if processindex0[k][1]==processno:
									break
							try:
								box0[j][1].place(y=(float(occupied0[k][0])/100)*500,height=(float(occupied0[k][1])/100)*500,width=100)
							except:
								box0[j][1].place(height=(float(occupied0[k][1])/100)*500,width=100)
								
							log[0]=Label(frame1,bg="black",width=300,height=50,text="Process "+str(processno)+" added",fg="white")
							log[0].place(x=5,y=650,height=50,width=290)
					if i[1] !=m:
						hole0.append([i[0]+m,i[1]-m])
						hole0.sort()
						break
			if flag == 0:
					print " Not enough memory for continuous allocation"
	
	else:
		if occupied0!= [] :
			p=processno
			for j in xrange(np.shape(processindex0)[0]):
				if processindex0[j][1]==p:
					print "process", processindex0[j][1], "removed"
					rem=processindex0[j][1]
					break
			for k in xrange(np.shape(box0)[0]):
				if rem==box0[k][0]:
					box0[k][1].config(bg='red',text='',relief=FLAT)
					box0.pop(k)
					break
			log[0]=Label(frame1,bg="black",width=300,height=50,text="Process "+str(processno)+" removed",fg="white")
			log[0].place(x=5,y=650,height=50,width=290)
			for i in occupied0:
				if i[0]==p:
					break
			process0.remove(p)
			occupied0.remove(i)
			hole0.append(i)
			hole0.sort()
			processindex0.pop(j)
			for x in xrange(np.shape(hole0)[0]):
				if i==hole0[x]:
					if (hole0[x][0]+hole0[x][1]!=100)&(hole0[x][0]+hole0[x][1]==hole0[x+1][0]):
						hole0[x][1]+=hole0[x+1][1]
						hole0.pop(x+1)
						break
		

#--------------------------------------------------FIRST_FIT------------------------------------------------------------------------
#--------------------------------------------------BEST_FIT------------------------------------------------------------------------

occupied1=[]
hole1=[[0,memory]]
process1=[]
block1=[]
processindex1=[]
box1=[]
maxi=10000
def bestfit(processno,m,ch):
	if ch==1:
		print "process",processno,"request"
		if hole1 == []:
			print "Memory Full"
			
		else:
			print m
			flag=0
			maxi=10000
			for i in hole1:
				if (i[1]>=m)&(i[1]<maxi):
					flag=1
					pos=i;
					maxi=i[1]
			
			if flag:
				occupied1.append([pos[0],m])
				process1.append(processno)
				occupied1.sort()
				hole1.remove(pos)
				processindex1.append([pos[0],processno])
				processindex1.sort()
				print "process",processno, "added"
				box=Label(label[1],width=10,height=30,bg='green',text="Process"+str(processno),borderwidth=5,relief=RAISED)
				box1.append([processno,box])
				for j in xrange(np.shape(box0)[0]):
					if box1[j][0]==processno:
						mem=0
						for k in xrange(np.shape(processindex1)[0]):
							if processindex1[k][1]==processno:
								break
						try:
							box1[j][1].place(y=(float(occupied1[k][0])/100)*500,height=(float(occupied1[k][1])/100)*500,width=100)
						except:
							box1[j][1].place(height=(float(occupied1[k][1])/100)*500,width=100)
						log[1]=Label(frame1,bg="black",width=300,height=50,text="Process "+str(processno)+" added",fg="white")
						log[1].place(x=305,y=650,height=50,width=290)
				if i[1] !=m:
					hole1.append([i[0]+m,i[1]-m])
					hole1.sort()
			if flag == 0:
					print " Not enough memory for continuous allocation"
	
	else:
		if occupied1!= [] :
			p=processno
			for j in xrange(np.shape(processindex1)[0]):
				if processindex1[j][1]==p:
					print "process", processindex1[j][1], "removed"
					rem=processindex1[j][1]
					break
			for k in xrange(np.shape(box1)[0]):
				if rem==box1[k][0]:
					box1[k][1].config(bg='red',text='',relief=FLAT)
					box1.pop(k)
					break
			log[1]=Label(frame1,bg="black",width=300,height=50,text="Process "+str(processno)+" removed",fg="white")
			log[1].place(x=305,y=650,height=50,width=290)
			for i in occupied1:
				if i[0]==p:
					break
			process1.remove(p)
			occupied1.remove(i)
			hole1.append(i)
			hole1.sort()
			processindex1.pop(j)
			for x in xrange(np.shape(hole1)[0]):
				if i==hole1[x]:
					if (hole1[x][0]+hole1[x][1]!=100)&(hole1[x][0]+hole1[x][1]==hole1[x+1][0]):
						hole1[x][1]+=hole1[x+1][1]
						hole1.pop(x+1)
						break






#--------------------------------------------------BEST_FIT------------------------------------------------------------------------
#--------------------------------------------------WORST_FIT------------------------------------------------------------------------

occupied2=[]
hole2=[[0,memory]]
process2=[]
block2=[]
processindex2=[]
box2=[]
mini=10000
def worstfit(processno,m,ch):
	if ch==1:
		print "process",processno,"request"
		if hole2 == []:
			print "Memory Full"
			
		else:
			print m
			flag=0
			mini=10000
			for i in hole2:
				if (i[1]>=m)&(i[1]<mini):
					flag=1
					pos=i;
					mini=i[1]
			
			if flag:
				occupied2.append([pos[0],m])
				process2.append(processno)
				occupied2.sort()
				hole2.remove(pos)
				processindex2.append([pos[0],processno])
				processindex2.sort()
				print "process",processno, "added"
				box=Label(label[2],width=10,height=30,bg='green',text="Process"+str(processno),borderwidth=5,relief=RAISED)
				box2.append([processno,box])
				for j in xrange(np.shape(box0)[0]):
					if box2[j][0]==processno:
						mem=0
						for k in xrange(np.shape(processindex2)[0]):
							if processindex2[k][1]==processno:
								break
						try:
							box2[j][1].place(y=(float(occupied2[k][0])/100)*500,height=(float(occupied2[k][1])/100)*500,width=100)
						except:
							box2[j][1].place(height=(float(occupied2[k][1])/100)*500,width=100)
				log[2]=Label(frame1,bg="black",width=300,height=50,text="Process "+str(processno)+" added",fg="white")
				log[2].place(x=605,y=650,height=50,width=290)
				if i[1] !=m:
					hole2.append([i[0]+m,i[1]-m])
					hole2.sort()
			if flag == 0:
					print " Not enough memory for continuous allocation"
	
	else:
		if occupied2!= [] :
			p=processno
			for j in xrange(np.shape(processindex2)[0]):
				if processindex2[j][1]==p:
					print "process", processindex2[j][1], "removed"
					rem=processindex2[j][1]
					break
			for k in xrange(np.shape(box2)[0]):
				if rem==box2[k][0]:
					box2[k][1].config(bg='red',text='',relief=FLAT)
					box2.pop(k)
					break
			log[2]=Label(frame1,bg="black",width=300,height=50,text="Process "+str(processno)+" removed",fg="white")
			log[2].place(x=605,y=650,height=50,width=290)
			for i in occupied2:
				if i[0]==p:
					break
			process2.remove(p)
			occupied2.remove(i)
			hole2.append(i)
			hole2.sort()
			processindex2.pop(j)
			for x in xrange(np.shape(hole2)[0]):
				if i==hole2[x]:
					if (hole2[x][0]+hole2[x][1]!=100)&(hole2[x][0]+hole2[x][1]==hole2[x+1][0]):
						hole2[x][1]+=hole2[x+1][1]
						hole2.pop(x+1)
						break






#--------------------------------------------------WORST_FIT------------------------------------------------------------------------
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
		var.set(process0[0]) 
	except:
		var.set("NONE")
	option= apply(OptionMenu, (master, var) + tuple(process0))
	option.pack()
	def ok():
		firstfit(int(var.get()),0,0)
		bestfit(int(var.get()),0,0)
		worstfit(int(var.get()),0,0)
		master.destroy()
	    
	button = Button(master, text="OK", command=ok,width=25)
	button.pack()
	
	master.mainloop()
'''
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
	
	
'''	
	
button0 = Button (frame0, text = "Create Process",bg="blue",fg="white", activebackground="black",activeforeground="white",command = create_process)
button0.place(x=116,y=100,width=232,height=50)

button1 = Button (frame0, text = "Terminate Process",bg="blue",fg="white", activebackground="black",activeforeground="white",command = terminate_process)
button1.place(x=116,y=200,width=232,height=50)
'''
button3 = Button (frame0, text = "Reset",bg="blue",fg="white", activebackground="black",activeforeground="white",command = reset)
button3.place(x=116,y=400,width=232,height=50)


'''
root.mainloop()
