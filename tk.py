from tkinter import Tk, mainloop, TOP, BOTTOM    
from tkinter.ttk import Button 
import tkinter as tk
import os
import sys


root = tk.Tk() 

#Icon
tk.Tk.iconbitmap(root, default="untitled.ico")# configure icon in normal spot
status_canvas = tk.Canvas(root)
task = tk.Label(status_canvas)
task.pack(anchor=tk.E, side=tk.BOTTOM)

def run():
                os.system('league_autoaccept.py')
                



        
         
        


#Title
root.title('League Auto Accept')


#Window
root.geometry('250x115') 


#Run Button
button = Button(root, text = 'Run', command=run) 
button.pack(side = TOP, pady = 15) 
#Stop Button
button = Button(root, text = 'Stop') 
button.pack(side = BOTTOM, pady = 15) 



root.mainloop()
