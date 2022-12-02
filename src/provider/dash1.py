import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import all_infos

# Create and configure window
root = tk.Tk()
root.title("Dashboard")
root.geometry("1680x920")
root.configure(bg='#222426')
root.resizable(0, 0)

# Configure Grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=5)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)

# get infos from machine
user = all_infos.system_info().node
system_info = all_infos.system_info().system + all_infos.system_info().version

# user and system info
tk.Label(root, text=user, font=('Arial', 18)).grid(row=0, column=1, sticky=tk.N, pady=30)
tk.Label(root, text=system_info,  font=('Arial', 12)).grid(row=0, column=1, sticky=tk.N, pady=100)

# get process and memory list
all_processes = all_infos.all_processes()
memorys = all_infos.memorys()

processes = tk.Variable(value=all_processes)
memory_info = tk.Variable(value=memorys)

list_processes = tk.Listbox(
    root,
    borderwidth=0,
    listvariable=[processes],
    width=30,
    height=50,
    selectmode=tk.EXTENDED, 
    bd=0,
).grid(sticky=tk.W, row=1, pady=(70), padx=(30, 0))

list_memory = tk.Listbox(
    root,
    listvariable=memory_info,
    borderwidth=0,
    height=3,
    width=45,
    font=('Times', 14)
).grid(sticky=tk.E, row=1, column=6, columnspan=5, pady=(70), padx=(0, 30))

root.mainloop()
