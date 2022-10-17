import tkinter as tk
from tkinter import * 

root = Tk()

root.geometry("500x500")
listSample = Listbox(root , width=15,height=30 , fg="red" , font=(" Arial", 28))
listSample.insert(1, "Margerita")
listSample.insert(2,"Thin Crust")
listSample.insert(3,"Cheese Burst")

listSample.pack()
root.mainloop()