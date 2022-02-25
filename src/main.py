from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import threading
win=Tk()
win.geometry("900x700")
#Text shown in the header
Label(win, text= "V2V",fg='#b45', font= ('Aerial 17 bold italic')).pack(pady= 30)
#button
ttk.Button(win, text= "connect to cyton board", command=threading.Thread(print("u have clicked the button")).start()).pack(pady= 40)
win.mainloop()