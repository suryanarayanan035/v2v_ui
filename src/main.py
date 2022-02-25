import sys
sys.path.append("../")
from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import threading
from board.index import Board
win=Tk()
board=Board.getBoard()
win.geometry("900x700")
#Text shown in the header
Label(win, text= "V2V",fg='#b45', font= ('Aerial 17 bold italic')).pack(pady= 30)
#button
ttk.Button(win, text= "start streaming", command=threading.Thread(target=board.start_streaming).start()).pack(pady= 40)
win.mainloop()

