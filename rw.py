from Tkinter import *
import random
import time
import tkMessageBox as tm
import threading
import sys

WIDTH = 800
HEIGHT = 600

	
def writer(w):
	time.sleep(1)

	global rw_mutex, status
		
	rw_mutex.acquire()
	
	remWriter()
	
	status["Writer %d"%w] = "Writer %d"%w
	
	with open("data.txt", 'r') as f:
		content = f.readline()
	f.close()
    	    	
	tk = Tk() 
	tk.title("Writer %d"%w)
	
	frame = Frame(tk, width=200, height=100)
	frame.pack()

	#tk = Frame(master,width=200,height=100)  	
	

	entry = Entry(tk, width=20)
	entry.pack()
	
	entry.delete(0,END)	
	entry.insert(0,content)	
		
	new_content = entry.get()
	
	def callback():
		new_content = entry.get()
		
		with open("data.txt", 'w') as f:
				f.write(new_content)
		f.close()
			
		print entry.get()

	b = Button(tk, text="Save", width=10, command=callback)
	b.pack()

	tk.mainloop()	
	
	print "Writer %d finished\n"%w
	
	del status["Writer %d"%w]
	
	rw_mutex.release()

		
def reader(r):
	time.sleep(1)

	global rw_mutex, mutex, read_count, status
	
	mutex.acquire()
	
	read_count=read_count+1
	
	if read_count==1:
		rw_mutex.acquire()
							
	mutex.release()
	
	remReader()
	
	status["Reader %d"%r] = "Reader %d"%r
	
	with open("data.txt") as f:
		content = f.readline()
		f.close()
		
	tk = Tk()
	tk.title("Reader %d"%r)
	
	frame = Frame(tk, width=200, height=100)
	frame.pack()

	label = Label(frame, text=content, width=20, height=10)
	label.pack()
	
	tk.mainloop()		    		
	
	print "Reader %d finished\n"%r
	
	del status["Reader %d"%r]
	
	mutex.acquire()
	
	read_count=read_count-1
	
	if read_count==0:
		rw_mutex.release()
							
	mutex.release()	


def addWriter(w):
	global q1	
	q1.append(w)

def remWriter():
	global q1	
	q1.pop(0)
	
def addReader(r):
	global q2	
	q2.append(r)

def remReader():
	global q2	
	q2.pop(0)		
	
	
class Request:
	def __init__(self, color, size, x, y):		
		self.shape = canvas.create_rectangle(x, y, x+size, y+size/2, fill=color, tags='requests')
		self.fill = color
		
class Request_label:
	def __init__(self, x, y, label):		
		self.shape = canvas.create_text(x, y, fill='darkblue', font='Times 10 bold', text=label, tags='requests')
		

q1 = []
q2 = []

status = {}
contents = {}
	
def main():
	global tk, canvas, rw_mutex, mutex, read_count, v_lock
	
	
	
	tk = Tk()
	canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
	tk.title("Reader-Writer Problem")
	canvas.pack()
	canvas.focus_set()
	
	
	rw_mutex = threading.Lock()
	mutex = threading.Lock()
	read_count = 0	
	v_lock = threading.Lock()
	
	global y1, y2, r, w
	y1 = 400
	y2 = 400	
	
	r=0
	w=0
	
	
	def AddWriter():
		global w
		t = threading.Thread(target = writer, args = (w,))		
		addWriter(w)
		t.start()	
		w=w+1
	
	addW = Button(tk, text="Add Writer", command=lambda:AddWriter())
	addW.place(x=153, y=25)
	
	
	def AddReader():
		global r
		t = threading.Thread(target = reader, args = (r,))
		addReader(r)
		t.start()
		r=r+1
	
	addR = Button(tk, text="Add Reader", command=lambda:AddReader())
	addR.place(x=553, y=25)

	
	global q1, q2, status
	
	Label(tk, text="Active operators").pack(side=LEFT)
	activity = Label(tk, text="").pack(side=LEFT)
		
	while(True):
		canvas.delete('requests')
	
		i=0
		for q in q1:
			Request('green', 100, 150, y1-50*i)
			Request_label(200, y1-50*i+25,"Writer %d"%q)
			i=i+1
		
		i=0
		for q in q2:
			Request('yellow', 100, 550, y1-50*i)
			Request_label(600, y1-50*i+25, "Reader %d"%q)
			i=i+1
			
		
		canvas.create_text(100, 500, fill='darkred', font='Calibri 20 bold', text='Status : ', tags='requests')
		
		label = ""		
		for s in status:
			label = label + " " + status[s]
		
		
			
		canvas.create_text(300, 500, fill='darkred', font='Calibri 10 bold', text=label, tags='requests')
		
		
		
		tk.update()
	
	tk.mainloop()
	
if(__name__ == "__main__"):
	main()

			



