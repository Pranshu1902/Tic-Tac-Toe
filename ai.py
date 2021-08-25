  #AI of tic-tac-toe

initial_board = [["-", "-", "-"],["-", "-", "-"], ["-", "-", "-"]]
o = "O"
x = "X"


def player(board):
  x_count = 0
  o_count = 0
  for i in board:
    for j in i:
      if j=="X":
        x_count+=1
      elif j=="O":
        o_count+=1
  if x_count>o_count:
    return "O"
  return "X"

def terminal(boards):
  #horizontal
  for i in boards:
    if i[0]==i[1] and i[1]==i[2] and i[1]!="-":
      return True
  #vertical
  for i in range(3):
    if boards[0][i]==boards[1][i] and boards[1][i]==boards[2][i] and boards[1][i]!="-":
      return True
  #diagonals
  if boards[0][0]==boards[1][1] and boards[1][1]==boards[2][2] and boards[1][1]!="-":
    return True
  if boards[2][0]==boards[1][1] and boards[1][1]==boards[0][2] and boards[1][1]!="-":
    return True
  if actions(boards) == None:
    return True
  return False 

def actions(board):
  ans = []
  for i in range(3):
    for j in range(3):
      if board[i][j]=="-":
        poss = [i,j]
        ans.append(poss)
  return ans
    
def make_move(board, point):
  #AI is X
  board[point[0]][point[1]]="X"
  return board

def winner(board):
  if terminal(board)==True:#if game is over
    if player(board)==o:
      return 1# X wins
    else:
      return -1 # O wins
  else:
    return 0 # game isn't over yet

def moves_over(board):
  if "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
    return True
  return False

def test_move(board, x, y):
  board[x][y]="X"
  #winner(boards)
    
def result(move, boards):
  boards[move[0]][move[1]]=player(boards)
  return boards

#recheck
def find_move(board):
  max(board)
  for move in actions(board):
    if test_move(board, move[0], move[1])==1:
      return move # return the case when AI wins
    elif test_move(board, move[0], move[1])==-1:
      pass # ignore the case when O wins
    else:
      final = move
  return final

def min(boards): # O's favourite
  if terminal(boards)==True:
    return winner(boards), None
  v = float('-inf')
  move = None
  pos = actions(boards)
  for i in pos:
    a, act = max(result(i, boards))
    if a<v:
      v=a
      move = i
      if v==-1:
        return v, move
  return v, move

def max(board): # X's favourite
  if terminal(board)==True:
    return winner(board), None
  v = float('inf')
  move = None
  pos = actions(board)
  for i in pos:
    a, act = min(result(i, board))
    if a>v:
      v=a
      move = i
      if v==1:
        return v, move
  return v, move

# to be eliminated
def players_move_finder(board):
  possibilities = actions(board)
  #tries to minimize the output
  for i in possibilities:
    result = test_move(board, [i[0]], [i[1]])
    if result==1:
      pass #ignore the case when X wins
    elif result == -1:
      return i
    else:
      mayb=i
    return mayb #incase result is not equal to -1 in any case then return with value of 0
    
def print_board(board):
  for i in board:
    print(i)
    
def main(board):
  while terminal(board)==False: #while game is not over
    #make_move(find_move())
    max(board)
    v, move = max(board)
    if move !=None:
        board = make_move(board, move)
    print_board(board)
    if player(board)=="O":
      print("Enter move")
      x,y = map(int, input().split())
      if board[x][y]=="-":
        board[x][y]="O"
      else:
        print("InvalidMoveError")
        break
  if winner(board)==1:
    print("AI won")
  elif winner(board)==-1:
    print("Player won")
  else:
    print("Tie")
  print_board(board)

if __name__ == "__main__":
  main(initial_board)
