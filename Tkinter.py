#import tkinter
#window = tkinter.Tk()
#window.title("GUI")
#label = tkinter.Label(window,text = "Hello World!").pack()
#window.mainloop()

#Can also right it like this to reduce typing tkinter

#from tkinter import * #This like indicates that from the tkinter module, we want everything
#window = Tk() #window is an object and of class ktinter
#window.title("GUI")
#label = Label(window,text = "Hello World!").pack() #message shown through method called label, whuch has 2 parameters (tkinter object, string)
#window.mainloop()

#labels are created to view text
#from module_name import (what you want from the module) - if you want to import a part of the module



## this is a button
#from tkinter import *
#window = Tk()
#window.title("GUI")
#BT = Button(window,text='Enter',fg='red',bg='black')
#BT.place(x=250,y=250)
#window.mainloop()

##when the button get clicked, it will execute a code
#from tkinter import *
#window = Tk()
#window.title("GUI")
#window.geometry("500x500")
#def clicked():
#    L1.configure(text = "Button was clicked!!")
#L1 = Label()
#L1.place(x=230,y=200)
#BT = Button(window,text='Enter',command=clicked,)#fg='red',bg='black'
#BT.place(x=250,y=250)
#window.mainloop()

##Entry class
from tkinter import *
window = Tk()
window.title("GUI")
window.geometry("300x300")
def clicked():
    L1.configure(text = e.get())
e = Entry(window,width=10)
L1 = Label(text="Text will pop up here")
L1.place(x=127,y=170)
e.place(x=130,y=140)
BT = Button(window,text='Enter',command=clicked,)#fg='red',bg='black'
BT.place(x=130,y=100)
window.mainloop()


##Spinbox
from tkinter import *
window = Tk()
window.title("GUI")
window.geometry("300x300")
Spin = Spinbox(window,from_=0,to=10,width=5)
Spin.place(x=130,y=130)
window.mainloop()

##Messagebox  syntax is messagebox.function_name(title,message, [options])
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
messagebox.showinfo("info","Warning!!")
top.mainloop()

    ##Listbox
from Tkinter import *
import Tkinter
top = Tk()
Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Rust")
Lb1.insert(3, "C++")
Lb1.insert(4, "PHP")
Lb1.insert(5, "C#")
Lb1.insert(6, "Ruby")
Lb1.pack()
top.mainloop()

##scrollbar
from Tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y ) #side tells where to place the bar and fill so it can fill the space in both directions
mylist = Listbox(root, yscrollcommand = scrollbar.set ) # can on scroll vertilcle and set it to scroll bar
for line in range(100):
    mylist.insert(END, "This is line number " + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
mainloop()

##Photoimage - used to view photos - syntax: Icon = PhotoImage(file='path_of_the_filr)
import tkinter
window = tkinter.Tk()
window.title("Welcome")
icon = tkinter.PhotoImage(file = "location of the photo")
label = tkinter.Label(window ,image = icon)
label.pack()
window.mainloop()

#Events
from tkinter import *
window = Tk()
window.title("Welcome")
window.geometry("200x200")
label = Label(text='Learning Python 101!')
label.place(x=70 ,y=20)
btn = Button(width=7 ,height=3)
def leftclick(event):
    label.configure(text="leftclick")
def middleclick(event):
    label.configure(text="middleclick")
def rightclick(event):
    label.configure(text="rightclick")

btn.bind("<Button-1>" ,leftclick)
btn.bind("<Button-2>" ,middleclick)
btn.bind("<Button-3>" ,rightclick)
btn.place(x=80 ,y=70)
window.mainloop()

##Task
from tkinter import *
from tkinter import messagebox

my_entry = Entry
lb = Listbox
def newTask():
    task = my_entry.get() # is use to pull vale provided by use in the entry box.
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
def deleteTask():
    lb.delete(ANCHOR)