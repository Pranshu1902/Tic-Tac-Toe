# tic tac toe gui
import tkinter
from tkinter import *

#initialization
start = tkinter.Tk()

start.title("Tic Tac Toe")
start.resizable(0,0)
start.geometry("500x500")
start.configure(bg="white")

green = [0,255,0]
red = [255,0,0]
white = [255,255,255]
blue = [0,0,255]

class game:
    def __init__(self):
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.x = "X"
        self.o = "O"
        self.mouse_x = 0
        self.mouse_y = 0

    def get(self):
        return self.board

    def player(self):
        x_count = 0
        o_count = 0
        for i in self.board:
            for j in i:
                if j==self.x:
                    x_count+=1
                elif j==self.o:
                    o_count+=1
        if x_count>o_count:
            return self.o
        return self.x

    def move_checker(self, x, y):
        if self.board[x][y]=="-":
            return True
        return False
    
    def make_move(self, x, y):
        if self.move_checker(x, y):
            self.board[x][y]=self.player()
        else:
            raise "NotValidError"

    def moves_over(self):
        if "-" not in self.board[0] and "-" not in self.board[1] and "-" not in self.board[2]:
            return True
        return False

    def terminate(self):
        
        global winner
        winner = ""
        #horizontal
        for i in self.board:
            if i[0]==i[1] and i[1]==i[2] and i[1]!="-":
                winner = i[1]
                return True
        #vertical
        for i in range(3):
            if self.board[0][i]==self.board[1][i] and self.board[1][i]==self.board[2][i] and self.board[1][i]!="-":
                winner = self.board[1][i]
                return True
        #diagonals
        if self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2] and self.board[1][1]!="-":
            winner = self.board[1][1]
            return True
        if self.board[2][0]==self.board[1][1] and self.board[1][1]==self.board[0][2] and self.board[1][1]!="-":
            winner = self.board[2][0]
            return True
        return False

    def display_move(self, x, y, move):
        global canvas
        #move = self.player()
        if x==0:
            b=110
        elif x==1:
            b=250
        elif x==2:
            b=390
        else:
            a=225
            b=250
        if y==0:
            a=90    
        elif y==1:
            a=225
        elif y==2:
            a=360

        text1 = canvas.create_text(a,b,anchor=W,font=("Purisa",60),text=move)

    def mouse(self, event):
        x,y = event.x, event.y
        global canvas
        # locating the box
        if x>=60 and y>=57 and x<=170 and y<=170:
            x=0
            y=0
        elif x>=170 and y>=50 and x<=325 and y<=170:
            x=0
            y=1
        elif x>325 and y>50 and x<=450 and y<=170:
            x=0
            y=2
        elif x>=50 and y>=170 and x<=170 and y<=325:
            x=1
            y=0
        elif x>=170 and y>=170 and x<=325 and y<=325:
            x=1
            y=1
        elif x>=325 and y>=170 and x<=450 and y<=325:
            x=1
            y=2
        elif x>=50 and y>=325 and x<=170 and y<=450:
            x=2
            y=0
        elif x>=170 and y>=325 and x<=325 and y<=450:
            x=2
            y=1
        elif x>=325 and y>=325 and x<=450 and y<=450:
            x=2
            y=2
        Tie = False
        while self.moves_over()==False and self.terminate()==False:
            turn = self.player()
            print(turn+"'s move")
            self.make_move(x,y)
            self.display_move(x,y,turn)
            if self.moves_over()==True and self.terminate()==False:
                Tie=True
                break
        if Tie:
            print("Tie")
            canvas.destroy()
            l1.configure(text="Tie")
        else:
            print(winner+" won!")
            canvas.destroy()
            l1.configure(text=winner+" won")
        bt.configure(text="Play Again")

# GUI

def gui():
    global canvas
    canvas = Canvas(start)
    canvas.pack()
    canvas.config(width=500,height=500)
    line0=canvas.create_line(175,50,175,450,fill='black',width=5)
    line2=canvas.create_line(325,50,325,450,fill='black',width=5)
    line3=canvas.create_line(50,175,450,175,fill='black',width=5)
    line4=canvas.create_line(50,325,450,325,fill='black',width=5)
    play = game()
    start.bind("<Button-1>", play.mouse)


# Tkinter display

l1 = tkinter.Label(start, text = "Tic Tac Toe", font = ("Arial Bold",50))
l1.place(x=70,y=0)

bt = tkinter.Button(start, text="Play", height=2, width=50, bg="yellow", command=gui)
bt.place(x=80,y=300)

start.mainloop()
