import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
# to do list


frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=0, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
