from optparse import OptionValueError
from struct import pack
from tkinter import *
root = Tk()
root.geometry("300x200")

W = Label(root,text='Gujarat UNiversity',font="50"),pack()

Checkbutton1 = tk.intVar()
Checkbutton2 = tk.intVar()
Checkbutton3 = tk.intVar()

Button1 = Checkbutton(root,text="Tutorial",variable=Checkbutton1,onvalue = 1, offvalue=0,height=2,width=10)
Button2 = Checkbutton(root,text="Student",variable=Checkbutton2,onvalue = 1, offvalue=0,height=2,width=10)
Button3 = Checkbutton(root,text="Courses",variable=Checkbutton1,onvalue = 1, offvalue=0,height=2,width=10)

Button1.pack()
Button2.pack()
Button3.pack()

