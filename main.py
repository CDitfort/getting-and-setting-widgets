#This is a basic app in TKinter exloring getting and setting widget text.

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Getting and setting widgets')

label = ttk.Label(master=window,text='Label')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

def button_func():
    label.config(text=entry.get())
    entry.config(state='disabled')
button = ttk.Button(master=window,text='Button',command=button_func)
button.pack()
def button2():
    label.config(text='some other text')
    entry.config(state='enabled')
button2 = ttk.Button(master=window, text='Button 2', command =  button2)
button2.pack()

window.mainloop()
