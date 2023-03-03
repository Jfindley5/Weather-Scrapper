from tkinter import *
ws = Tk()
ws.title("PythonGuides")
ws.geometry("500x500")

frame = Frame(ws)#used to hold other widgets, They help in keeping and maintaining use interfcae UI & user experience UI
frame.pack(pady=10) #pady is adding extra frame from outside

Lb1 = Listbox(  #lb is variable namee for storing listbox
    frame, #editing the frame
    width=25, #horizontal space
    height=8, #vertical space
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0, #should not show any movement
    selectbackground='#a6a6a6', #color of the backgroud of list since its in list
    activestyle="none", #removes underline that appears when the item is selected or focused
)
Lb1.pack(side = LEFT, fill = BOTH)

#adding the listbox
task_list = []

for item in task_list:
    Lb1.insert(END, item)#insert is a built in method of listbox to insert the data, END is so new item can be added at the end at zero then the new item will be added at the top.

#adding Scrollbars
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH) #pack is the geometry method,

Lb1.config(yscrollcommand=sb.set)#assign a purpose to the scroll bar define listbox w a scroll bar
sb.config(command=Lb1.yview)#yview means scroll bar will work in veritical direction

#entry so it can take input from the users
my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.pack(pady=20)

#Adding buttons
button_frame = Frame(ws)
button_frame.pack(pady=20)


addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask

)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

messagebox = Message

def newTask():
    task = my_entry.get()
    if task != "":
        Lb1.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
def deleteTask():
    Lb1.delete(ANCHOR) #to delete the selected item from the list box

ws.mainloop()


#scrollbar not showing
#no action is happening after I click add or delete