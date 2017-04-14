from Tkinter import *
root=Tk()
frame=Frame(root,height=768,width=1366,bg="#f1f1f2")
frame.grid()
def close_window ():
        root.destroy()
button0=Button(frame,text="Continuous Memory Allocation",bg="#a1d6e2",activebackground="#1995ad",activeforeground="white",font=("Helvetica",16))#command=close_window())
button0.place(x=80,y=50,width=400,height=200)
button1=Button(frame,text="CPU Scheduling",bg="#a1d6e2",activebackground="#1995ad",activeforeground="white",font=("Helvetica",16))#command=close_window())
button1.place(x=480,y=50,width=400,height=200)
button2=Button(frame,text="Semaphores",bg="#a1d6e2",activebackground="#1995ad",activeforeground="white",font=("Helvetica",16))#command=close_window())
button2.place(x=880,y=50,width=400,height=200)
button3=Button(frame,text="Banker's Algorithm",bg="#a1d6e2",activebackground="#1995ad",activeforeground="white",font=("Helvetica",16))#command=close_window())
button3.place(x=80,y=250,width=400,height=200)
button4=Button(frame,text="Page Replacement",bg="#a1d6e2",activebackground="#1995ad",activeforeground="white",font=("Helvetica",16))#command=close_window())
button4.place(x=480,y=250,width=400,height=200)
button5=Button(frame,text="Disk Scheduling",bg="#a1d6e2",activebackground="#1995ad",activeforeground="white",font=("Helvetica",16))#command=close_window())
button5.place(x=880,y=250,width=400,height=200)
button6=Button(frame,text="Socket Programming",bg="#a1d6e2",activebackground="#1995ad",activeforeground="white",font=("Helvetica",16))#command=close_window())
button6.place(x=480,y=450,width=400,height=200)





root.mainloop()


