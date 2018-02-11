from tkinter import *
import move as mv
from tkinter import messagebox
#window = Tk()
class ttt_gui:
    def aiMove(self,r,c):
        #print (r,c)
        if r is 0 and c is 0:
            self.squre0_0.config(image=self.aiImage, width="10", height="10")
        elif r is 0 and c is 1:
            self.squre0_1.config(image=self.aiImage, width="10", height="10")
        elif r is 0 and c is 2:
            self.squre0_2.config(image=self.aiImage, width="10", height="10")
        elif r is 1 and c is 0:
            self.squre1_0.config(image=self.aiImage, width="10", height="10")
        elif r is 1 and c is 1:
            self.squre1_1.config(image=self.aiImage, width="10", height="10")
        elif r is 1 and c is 2:
            self.squre1_2.config(image=self.aiImage, width="10", height="10")
        elif r is 2 and c is 0:
            self.squre2_0.config(image=self.aiImage, width="10", height="10")
        elif r is 2 and c is 1:
            self.squre2_1.config(image=self.aiImage, width="10", height="10")
        elif r is 2 and c is 2:
            self.squre2_2.config(image=self.aiImage, width="10", height="10")

    def aiFirstMove(self):
        next_move = mv.bestMove(self.board, True)
        self.aiMove(next_move[0], next_move[1])
        self.board[next_move[0]][next_move[1]] = self.ai

    def Win_Lose(self,board):
        if (mv.isFinalState(board) is not True) and mv.evaluate(board) is 0:
            return ' '
        else:
            score = mv.evaluate(board)
            if score == 10:
                return 'X'
            elif score == -10:
                return 'O'
            else:
                return 'D'

    def setImage(self,squre,new_image,r,c):
        if self.board[r][c] is not ' ':
            return
        squre.configure(image = new_image)
        self.board[r][c] = self.player
        self.isWin = self.Win_Lose(self.board)
        if self.isWin is not ' ':
            if self.isWin is 'O':
                messagebox.showinfo(title= "O Win",message = "You win!!!")
                return
            elif self.isWin is 'X':
                messagebox.showinfo(title= "X Win",message = "You win!!!")
                return
            elif self.isWin is 'D':
                messagebox.showinfo(title= "Draw",message = "Draw~")
                return
        if self.ai is 'X':
            self.aiFirst  = True
        else:
            self.aiFirst = False
        next_move = mv.bestMove(self.board,self.aiFirst)
        self.board[next_move[0]][next_move[1]] = self.ai
        self.aiMove(next_move[0],next_move[1])
        self.isWin = self.Win_Lose(self.board)
        if self.isWin is not ' ':
            if self.isWin is 'O':
                messagebox.showinfo(title="O Win", message="You lose!!!")
                return
            elif self.isWin is 'X':
                messagebox.showinfo(title="X Win", message="You lose!!!")
                return
            elif self.isWin is 'D':
                messagebox.showinfo(title="Draw", message="Draw~")
                return
        #print(next_move)

    def __init__(self,window,player):
        self.cross = PhotoImage(file='a.png')
        self.circle = PhotoImage(file='b.png')
        self.space = PhotoImage(file='c.png')
        self.board = [[' ',' ', ' '],[' ',' ',' '],[' ',' ',' ']]
        self.player = player
        if self.player is 'X':
            self.aiImage = self.circle
            self.playImage = self.cross
            self.ai = 'O'
        else:
            self.aiImage = self.cross
            self.playImage = self.circle
            self.ai = 'X'
        #self.play_move = [-1,-1]
        self.squre0_0 = Button(window , image = self.space , command =lambda: self.setImage(self.squre0_0,self.playImage,0,0))
        self.squre0_0.grid(column=0, row=0, sticky=N + S + E + W)
        #self.squre0_0.config(image = self.circle,width = "10",height="10")

        self.squre0_1 = Button(window, image = self.space , command =lambda: self.setImage(self.squre0_1,self.playImage,0,1))
        self.squre0_1.grid(column=1, row=0, sticky=N + S + E + W)

        self.squre0_2 = Button(window, image = self.space, command =lambda: self.setImage(self.squre0_2,self.playImage,0,2))
        self.squre0_2.grid(column=2, row=0, sticky=N + S + E + W)

        self.squre1_0 = Button(window, image = self.space, command =lambda: self.setImage(self.squre1_0,self.playImage,1,0))
        self.squre1_0.grid(column=0, row=1, sticky=N + S + E + W)

        self.squre1_1 = Button(window, image = self.space, command =lambda: self.setImage(self.squre1_1,self.playImage,1,1))
        self.squre1_1.grid(column=1, row=1, sticky=N + S + E + W)

        self.squre1_2 = Button(window, image = self.space, command =lambda: self.setImage(self.squre1_2,self.playImage,1,2))
        self.squre1_2.grid(column=2, row=1, sticky=N + S + E + W)

        self.squre2_0 = Button(window, image=self.space, command =lambda: self.setImage(self.squre2_0,self.playImage,2,0))
        self.squre2_0.grid(column=0, row=2, sticky=N + S + E + W)

        self.squre2_1 = Button(window, image=self.space, command =lambda: self.setImage(self.squre2_1,self.playImage,2,1))
        self.squre2_1.grid(column=1, row=2, sticky=N + S + E + W)

        self.squre2_2 = Button(window, image=self.space, command =lambda: self.setImage(self.squre2_2,self.playImage,2,2))
        self.squre2_2.grid(column=2, row=2, sticky=N + S + E + W)

