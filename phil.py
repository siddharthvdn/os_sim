#Dining philosoher 2
from Tkinter import *
import random
import time
import tkMessageBox as tm
import thread

WIDTH = 800
HEIGHT = 600


tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Dining Philosophers")
canvas.pack()
canvas.focus_set()

class Ball:
	def __init__(self, color, size, x, y):		
		self.shape = canvas.create_oval(x, y, x+size, y+size, fill=color, tags='asf')
		self.fill = color


p = []
for i in range(5):
	p.append(0)
	
st = []
for i in range(5):
	st.append(0)	
		
ht = []
for i in range(5):
	ht.append(0)	

et = []
for i in range(5):
	et.append(0)	

		
balls = []

balls.append(Ball('yellow', 100, 400, 150))
balls.append(Ball('yellow', 100, 550, 250))
balls.append(Ball('yellow', 100, 490, 400))
balls.append(Ball('yellow', 100, 310, 400))
balls.append(Ball('yellow', 100, 250, 250))

texts = []

texts.append(canvas.create_text(400, 150, text='Philosopher 1\nThinking'))
texts.append(canvas.create_text(550, 250, text='Philosopher 2\nThinking'))
texts.append(canvas.create_text(490, 400, text='Philosopher 3\nThinking'))
texts.append(canvas.create_text(310, 400, text='Philosopher 4\nThinking'))
texts.append(canvas.create_text(250, 250, text='Philosopher 5\nThinking'))


def leftClick(event):
	x = event.x
	y = event.y
		
	for i in range(5):
		pos = canvas.coords(balls[i].shape)
	
		if (pos[0]<=x) and (pos[2]>=x) and (pos[1]<=y) and (pos[3]>=y):
						
			if balls[i].fill == 'red':
									
				if ((p[(i+1)%5] == 2) | (p[(i+4)%5] == 2)):
					tm.showinfo("DEADLOCK", "No forks free")
					break					
				
				canvas.itemconfig(balls[i].shape, fill='blue')
				canvas.itemconfig(texts[i], text="Philosopher %d\nEating"%(i+1))
				balls[i].fill = 'blue'
				p[i] = 2
				st[i] = time.time()
				break


canvas.bind("<Button-1>", leftClick)

				
def visualise():
	for i in range(5):
		if p[i] == 0:
			canvas.itemconfig(balls[i].shape, fill='yellow')
		if p[i] == 1:
			canvas.itemconfig(balls[i].shape, fill='red')
		if p[i] == 2:
			canvas.itemconfig(balls[i].shape, fill='blue')
	
	tk.update()



def display():
	for i in range(5):
		if p[i] == 0:
			print 'Philosopher %d is thinking'%(i+1)
		if p[i] == 1:
			print 'Philosopher %d is hungry'%(i+1)
		if p[i] == 2:
			print 'Philosopher %d is eating'%(i+1)
	print '\n'


def loop():	
	while True:	

		for i in range(5):
			if p[i] == 0:
				st[i] = time.time()
			if p[i] == 1:
				ht[i] = time.time()-st[i]
			
				if (ht[i]>6) & (ht[i]<=12):
					canvas.itemconfig(texts[i], text="Philosopher %d\nStarving"%(i+1))
				if ht[i]>12 :
					canvas.itemconfig(texts[i], text="Philosopher %d\nDead"%(i+1))
					tm.showerror("YOU LOOSE!", "Philosopher %d is Dead.\nYou are a bad waiter!"%(i+1))
					tk.destroy()
			if p[i] == 2:
				et[i] = time.time() - st[i]
				canvas.itemconfig(texts[i], text="Philosopher %d\nEating"%(i+1))
				
				if (et[i]>4) :
					canvas.itemconfig(balls[i].shape, fill='yellow')
					canvas.itemconfig(texts[i], text="Philosopher %d\nThinking"%(i+1))
					balls[i].fill = 'yellow'
					p[i] = 0

					
	
		visualise()
		#display()
		time.sleep(2)

		
def assign():
	while True:
	
		time.sleep(1)
	
		i = random.randrange(0,5)
		if (p[i] == 0) :
			canvas.itemconfig(balls[i].shape, fill='red')
			canvas.itemconfig(texts[i], text="Philosopher %d\nHungry"%(i+1))
			balls[i].fill = 'red'
			p[i] = 1
			st[i] = time.time()

		

thread.start_new_thread (loop, ())
thread.start_new_thread (assign, ())
		

	
tk.mainloop()
	
			



