from tkinter import *
from tkinter import messagebox
import webbrowser
root = Tk()
root.geometry("430x430")
root.maxsize(430,430)
root.title("Contact App")

def github_profile():
    webbrowser.open("https://github.com/RupeshGovind")

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts_listbox.insert(END, f"{name} : {phone}")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter both name and phone number.")

def remove_contact():
    selected_contact_index = contacts_listbox.curselection()
    if selected_contact_index:
        contacts_listbox.delete(selected_contact_index)
    else:
        messagebox.showwarning("Warning", "You must select a contact to remove.")

def quit_app():
    root.destroy()


frame = Frame(root, bg="lightgrey", borderwidth=2, relief=SUNKEN, width=500, height=500)
frame.pack(side=TOP, fill="both")

Label(frame, text="Name:", bg="lightgrey",highlightthickness=1,highlightbackground="blue").pack(pady=5)
name_entry = Entry(frame, width=30, highlightcolor="blue", highlightthickness=1)
name_entry.pack(padx=20, pady=5)

Label(frame, text="Phone:", bg="lightgrey",highlightthickness=1,highlightbackground="blue").pack(pady=5)
phone_entry = Entry(frame, width=30, highlightcolor="blue", highlightthickness=1)
phone_entry.pack(padx=20, pady=5)

add_button = Button(frame, text="Add Contact", bg="blue", fg="white", command=add_contact)
add_button.pack(pady=10)

contacts_listbox = Listbox(frame, highlightcolor="blue", highlightthickness=1, width=40, height=10)
contacts_listbox.pack(pady=10)

remove_button = Button(frame, text="Remove Contact", bg="blue", fg="white", command=remove_contact)
remove_button.pack(pady=10)

github_button = Button(frame, text="Rupesh GitHub", bg="blue", fg="white", command=github_profile)
github_button.pack(side=BOTTOM, anchor=E, padx=2)

root.mainloop()