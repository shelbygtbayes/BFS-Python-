from tkinter import *
from tkinter import messagebox 
import time
import sys
game_over  = False
class Node:
    def __init__(self,x,y,d):
        self.row = x
        self.col = y
        self.dist = d

board = [ ["gray"]*20 for val in range(20) ]
path = [[[None]*2 for i in range(20)] for k in range(20)]
dest_row = -1
dest_col = -1
source_row = -1
source_col = -1
def minDistance(window):
    global board , game_over , path , dest_col , dest_row , source_row , source_col
    vis = [[None]*20 for row in range(len(board))]
    source = Node(0,0,0)

# Initialization
    for row,x in enumerate(board):
        for col,y in enumerate(x):
            if(board[row][col] == "green"):
                vis[row][col] = False
                source.row = row 
                source_row = row
                source.col = col
                source_col = col
            elif(board[row][col] == "black"):
                vis[row][col] = True
            else:
                vis[row][col] = False
    queue = []
    queue.append(source)
    vis[source.row][source.col] = True
    path[source_row][source_col] = [-1,-1]

    # BFS
    ans = -1
    while(len(queue)!=0):
        n = queue.pop(0)
        if(board[n.row][n.col] == "red"):
            dest_row , dest_col = n.row , n.col
            messagebox.showinfo("BFS", "Destination Found At distance : "+ str(n.dist))
            ans = n.dist
            break
        board[n.row][n.col] = "yellow"
       # Moving Up 

        if(n.row - 1 >=0 and not vis[n.row-1][n.col]):
            queue.append(Node(n.row-1, n.col , n.dist+1))
            path[n.row-1][n.col] = [n.row,n.col]
            vis[n.row-1][n.col] = 1
            #print(f"Before : {n.row-1} {n.col} {path[n.row-1][n.col]}")

            # Moving Down
        if(n.row + 1 < 20 and not vis[n.row+1][n.col]):
            queue.append(Node(n.row+1, n.col , n.dist+1))
            path[n.row+1][n.col] = [n.row,n.col]
            vis[n.row+1][n.col] = 1
            #print(f"Before : {n.row+1} {n.col} {path[n.row+1][n.col]}")

            # Moving Left
        if(n.col - 1 >=0 and not vis[n.row][n.col-1]):
            queue.append(Node(n.row , n.col-1, n.dist+1))
            path[n.row][n.col-1] = [n.row,n.col]
            #print(f"Before : {temp_row} {temp_col} {path[temp_row][temp_col]}")
            vis[n.row][n.col-1] = 1

            # Moving Right
        if(n.col + 1 < 20 and not vis[n.row][n.col+1]):
            queue.append(Node(n.row , n.col+1, n.dist+1))
            path[n.row][n.col+1] = [n.row,n.col]
            #print(f"Before : {temp_row} {temp_col} {path[temp_row][temp_col]}")
            vis[n.row][n.col+1] = 1


# Final Coloring
    if(ans==-1):
        messagebox.showinfo("BFS", "No Path exists")
        return
    final()

    

source_selected = False

destination_selected = False

blocks = 0

root = Tk()

def on_click(row,col,event):
    global source_selected
    global destination_selected
    global blocks , game_over , board
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
        messagebox.showinfo("BFS", "Please Select the Destination cell")
    if(blocks == 2):
        messagebox.showinfo("BFS", "Select the Block cells and Press any key when Over")

def blocked(row,col,event):
    global blocks
    blocks+=1
    event.widget.config(bg="black")
    board[row][col] = "black"

def final():
    global board , path
    temp_row = dest_row
    temp_col = dest_col
    
    cnt = 0
    board[source_row][source_col] = "green"
    print(f"Before : {source_row} {source_col} {path[source_row][source_col]}")
    while(temp_row!=None and  temp_col!=None and (path[temp_row][temp_col][0]!=source_row or path[temp_row][temp_col][1] != source_col)):
        board[temp_row][temp_col] = "blue"
        print(f"Before : {temp_row} {temp_col} {path[temp_row][temp_col]}")
        temp_row = path[temp_row][temp_col][0]
        temp_col = path[temp_row][temp_col][1]
        print(f"After : {temp_row} {temp_col} {path[temp_row][temp_col]} {cnt}")
        cnt+=1
    board[temp_row][temp_col] = "blue"
    board[dest_row][dest_col] = "red"
    board[source_row][source_col] = "green"

def board_setup():

    def ask_quit():
        if messagebox.askokcancel("Quit", "You want to quit now? "):
            window.destroy()
            sys.exit(1)

    def key_press(event): 
        key = event.char
        show = minDistance(event)

        '''for x in board:
            for y in x:
                print(y,end=" ")
            print("")'''
        for x,row in enumerate(board):
            for y,col in enumerate(row):
                L = Canvas(window, width=80, height=80, background=board[x][y])
                L.grid(row=x,column=y)
                window.rowconfigure(x, weight=1)
                window.columnconfigure(y,weight=1)
        #ask_quit()


    global source_selected
    global destination_selected
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
    window.title("DFS")
    window.geometry('800x800')
    window.resizable(True,True)
    for x,row in enumerate(board):
        for y,column in enumerate(row):
            L = Canvas(window, width=80, height=80, background=board[x][y])
            L.grid(row=x,column=y)
            window.rowconfigure(x, weight=1)
            window.columnconfigure(y,weight=1)
            L.bind('<Button-1>',lambda e,row=x,col=y: on_click(row,col,e))

 


    window.bind('<Key>', lambda a : key_press(a))		

    window.protocol("WM_DELETE_WINDOW", ask_quit)
    
    window.mainloop()


root.withdraw()
messagebox.showinfo("Welcome W47ch3r", "Continue to BFS")
messagebox.showinfo("BFS", "Please Select the Source cell")
board_setup()
root.destroy()

