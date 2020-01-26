from tkinter import *
from tkinter import messagebox 
import time
import sys
board = [ [None]*20 for val in range(20) ]

source_selected = False
destination_selected = False
blocks = 0
root = Tk()
#root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
#root.title("DFS")
def on_click(row,col,event):
	global source_selected
	global destination_selected
	global blocks
	blocks += 1
	if not source_selected:
		color = "green"

		source_selected = 1
	
	elif not destination_selected:
		color = "red"
		destination_selected = 1
	else:
		blocked(row,col,event)
		return
	event.widget.config(bg=color)
	board[row][col] = color
	if(not destination_selected):
		messagebox.showinfo("DFS", "Please Select the Destination cell")
	if(blocks == 2):
		messagebox.showinfo("DFS", "Select the Block cells and Press any key when Over")

def blocked(row,col,event):
	global blocks
	blocks+=1
	event.widget.config(bg="black")
	board[row][col] = "black"

	
def board_setup():

	def ask_quit():
		if messagebox.askokcancel("Quit", "You want to quit now? "):
			window.destroy()
			sys.exit(1)
	
	def key_press(event): 
		key = event.char
		print(key,"is pressed")


	global source_selected
	global destination_selected
	window = Tk()
	window.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
	window.title("DFS")
	window.geometry('800x800')
	window.resizable(True,True)
	for x,row in enumerate(board):
	    for y,column in enumerate(row):
	    	L = Canvas(window, width=80, height=80, background="Gray")
	    	L.grid(row=x,column=y)
	    	window.rowconfigure(x, weight=1)
	    	window.columnconfigure(y,weight=1)
	    	L.bind('<Button-1>',lambda e,row=x,col=y: on_click(row,col,e))
	window.bind('<Key>', lambda a : key_press(a))		
	window.protocol("WM_DELETE_WINDOW", ask_quit)
	window.mainloop()

	    
root.withdraw()
messagebox.showinfo("Welcome W47ch3r", "Continue to DFS")
messagebox.showinfo("DFS", "Please Select the Source cell")
board_setup()
root.destroy()

