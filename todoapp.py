from tkinter import *
from tkinter import messagebox
import webbrowser
root = Tk()
root.geometry("300x320")
root.maxsize(300,320)
root.title("To Do App")
def open_linkedin_profile():
    webbrowser.open("https://www.linkedin.com/in/rupesh-kumar-a680a7301")

def addtask():
    task = e1.get()
    if task:
        lstbox.insert(END, task)
        e1.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
def removetask():
    selected_task_index = lstbox.curselection()
    if selected_task_index:
        lstbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "You must select a task to remove.")
def quit_app():
    root.destroy()
f1 = Frame(root,bg="lightgrey",borderwidth=2,relief=SUNKEN,width=500,height=500)
f1.pack(side=TOP,fill="both")
e1 = Entry(f1,width=20,highlightcolor="blue",highlightthickness=1)
e1.pack(padx=20,pady=2)

b1 = Button(f1, text="Add Task",bg="blue",fg="white",command=addtask)
b1.pack(pady=3)

lstbox= Listbox(f1,highlightcolor="blue",highlightthickness=1)
lstbox.pack()
lstbox.insert(END)

b2 = Button(f1, text="Remove Task",bg="blue",fg="white",command=removetask)
b2.pack(pady=5)
b3 = Button(f1, text="Quit",bg="blue",fg="white",command=quit_app)
b3.pack(pady=3)
b4=Button(f1,text="Rupesh linkedin",bg="blue",fg="white",command=open_linkedin_profile)
b4.pack(side=BOTTOM,anchor=E)
root.mainloop()