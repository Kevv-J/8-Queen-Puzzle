import tkinter as tk
import tkinter.messagebox as messagebox

""" 
Grey Blocks indicate valid blocks to place a Queen
Green Blocks indicate blocks on which a Queen is placed.
Red Blocks indicate blocks which become invalid for a Queen to be placed due to placement of another Queen

Instructions:
Place Queens in Grey Blocks and try to place 8 Queens on the board to win.

"""



board = [ [None]*8 for _ in range(8) ]

counter = 0
root = tk.Tk()

def check_board():
    freespaces = 0
    redspaces = 0
    greenspaces = 0
    for i,row in enumerate(board):
        for j,column in enumerate(row):
            if board[i][j] == "red":
                redspaces += 1
            elif board[i][j] == "green":
                greenspaces += 1
            elif board[i][j] == None:
                freespaces += 1

    if freespaces == 0:
        if counter == 8:
            messagebox.showinfo("Victory","Congratulations you have solved the 8 Queen problem")
        else:
            messagebox.showinfo("Defeat","You failed to solve the problem")





def on_click(i,j,event):
    global counter
    if counter < 8:
        color = "green"
        invalid = "red"
        if board[i][j] == None:
            board[i][j] = color
            
            
            for x in range(len(board)):
                if x != j:
                    board[i][x] = invalid
                if x != i:
                    board[x][j] = invalid
            for x in range(1,len(board)):  
                if  (i+x) < 8 and (j+x) < 8: 
                    board[(i+x)][(j+x)] = invalid
                if  (i-x) >= 0 and (j-x) >= 0: 
                    board[(i-x)][(j-x)] = invalid
                if  (i+x) < 8 and (j-x) >= 0: 
                    board[(i+x)][(j-x)] = invalid
                if  (i-x) >= 0 and (j+x) < 8: 
                    board[(i-x)][(j+x)] = invalid


                    
                    
            counter += 1
            global gameframe
            gameframe.destroy()
            redraw()
            root.wm_title("Pick an Empty Spot to put Queen "+str(counter+1))
        else:
            if board[i][j] == color:
                messagebox.showinfo("Alert","This space is occupied by a Queen")
            else:
                messagebox.showinfo("Alert","This space is invlaid")
        check_board()


def redraw():
    global gameframe
    gameframe = tk.Frame(root)
    gameframe.pack()

    for i,row in enumerate(board):

        for j,column in enumerate(row):
            name = str(i)+str(j)
            L = tk.Label(gameframe,text='    ',bg= "grey" if board[i][j] == None else board[i][j])
            L.grid(row=i,column=j,padx='3',pady='3')
            L.bind('<Button-1>',lambda e,i=i,j=j:on_click(i,j,e))


redraw()
root.mainloop()