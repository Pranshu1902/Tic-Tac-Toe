#tic tac toe

class tic_tac_toe:
    def __init__(self):
        self.board = [["-", "-", "-"],["-", "-", "-"], ["-", "-", "-"]]
        self.x = "X"
        self.o = "O"
    def get(self):
        return self.board
    def print_game(self):
        for i in self.board:
            print(i)
    def move_checker(self, x, y):
        if self.board[x][y]=="-":
            return True
        return False
    def make_move(self, x, y):
        if self.move_checker(x, y):
            self.board[x][y]=self.player()
        else:
            raise "NotValidError"
    def player(self):
        x_count = 0
        o_count = 0
        for i in self.board:
            for j in i:
                if j==self.x:
                    x_count+=1
                elif j==self.o:
                    o_count+=1
        #assuming X goes first
        if x_count>o_count:
            return self.o
        else:
            return self.x
    def moves_over(self):
        if "-" not in self.board[0] and "-" not in self.board[1] and "-" not in self.board[2]:
            return True
        return False
    def terminate(self):
        #horizontal
        for i in self.board:
            if i[0]==i[1] and i[1]==i[2] and i[1]!="-":
                return True
        #vertical
        for i in range(3):
            if self.board[0][i]==self.board[1][i] and self.board[1][i]==self.board[2][i] and self.board[1][i]!="-":
                return True
        #diagonals
        if self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2] and self.board[1][1]!="-":
            return True
        if self.board[2][0]==self.board[1][1] and self.board[1][1]==self.board[0][2] and self.board[1][1]!="-":
            return True
        return False
    def winner(self):
        if self.player()==self.o:
            return self.x
        else:
            return self.o
    def main(self):
        while self.moves_over()==False or self.terminate()==False:
            self.print_game()
            print(self.player()+"'s move")
            x,y = map(int, input().split())
            self.make_move(x,y)
            if self.moves_over()==True and self.terminate()==False:
                return "Tie"
        self.print_game()
        return self.winner()+" won!"

check = tic_tac_toe()
print(check.main())
