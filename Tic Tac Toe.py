"""[Documentazione]

  Returns:
      [Autore]: [Mino Bibawy]
      
      [Esame]: [Programmazione avanzata Python e Arduino]
      
      [Descrizione Progetto]: [
                              Tic Tac Toe, 
                              matrice di 5x5,
                              UserX contro UserO  
                               ]
      
      [Regolamento]: [1 Turno a User
                      Vince chi arriva prima a 50
                       ]
"""

board = [
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]

user = True
turns = 0
pointuser1 = 0
pointuser2 = 0

def print_board(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()

def quit(user_input):
  if user_input.lower() == "q": 
    print("Grazie per aver giocato")
    return True
  else: return False


def check_input(user_input):
  if not isnum(user_input): return False
  user_input = int(user_input)
  if not bounds(user_input): return False

  return True

def isnum(user_input):
  if not user_input.isnumeric(): 
    print("Inserisci un n umero valido")
    return False
  else: return True

def bounds(user_input):
  if user_input > 25 or user_input < 1: 
    print("Insertisci un numero compreso tra 1 e 25")
    return False
  else: return True

def istaken(coords, board):
  row = coords[0]
  col = coords[1]
  if board[row][col] != "-":
    print("Questo numero è gia preso, Ritenta")
    return True
  else: return False

def coordinates(user_input):
  row = int(user_input / 5)
  col = user_input
  if col > 4: col = int(col % 5)
  return (row,col)

def add_to_board(coords, board, active_user):
  row = coords[0]
  col = coords[1]
  board[row][col] = active_user

def current_user(user):
  if user: return "x"
  else: return "o"

def iswin(user, board):
  global pointuser1
  global pointuser2
  n = check_row(user, board) + check_col(user, board) + check_diag(user, board)
  if user == "x":
    pointuser1 = n
    print("Punteggio:")
    print(pointuser1)
    if pointuser1 >= 50:
	    return True
    else:
        return False
  else:
     pointuser2 = n
     print("Punteggio:")
     print(pointuser2)
     if pointuser2 >= 50:
        return True
     else:
        return False
		
def check_row(user, board):
  rowpoints = 0
  for row in board:
    maxl = 0
    l = 0
    for slot in row:
      if slot == user:
         l = l+1
         if l > maxl:
            maxl = l
      else:
         l = 0
    if maxl == 3:
      rowpoints = rowpoints + 2
    if maxl == 4:
      rowpoints = rowpoints + 10
    if maxl == 5:
      rowpoints = rowpoints + 50
  return rowpoints 

def check_col(user, board):
  colpoints = 0
  for col in range(5):
    maxl = 0
    l = 0
    for row in range(5):
      if board[row][col] == user:
        l = l+1
        if l > maxl:
            maxl = l
        else:
         l = 0
    if maxl == 3:
      colpoints = colpoints + 2
    if maxl == 4:
      colpoints = colpoints + 10
    if maxl == 5:
      colpoints = colpoints + 50
  return colpoints 

def check_diag(user, board):
  diagpoints = 0
  # 2 punti
  if board[0][0] == user and board[1][1] == user and board[2][2] == user:
    diagpoints = 2
  if board[0][2] == user and board[1][3] == user and board[2][4] == user:
    diagpoints = 2
  if board[2][0] == user and board[3][1] == user and board[4][2] == user:
    diagpoints = 2
  if board[4][2] == user and board[3][3] == user and board[1][4] == user:
    diagpoints = 2
  if board[0][2] == user and board[1][1] == user and board[2][0] == user:
    diagpoints = 2
  if board[0][4] == user and board[1][3] == user and board[2][2] == user:
    diagpoints = 2
  if board[1][2] == user and board[2][3] == user and board[3][4] == user:
    diagpoints = 2
  if board[2][2] == user and board[3][3] == user and board[4][4] == user:
    diagpoints = 2
  if board[1][0] == user and board[2][1] == user and board[3][2] == user:
    diagpoints = 2
  if board[1][4] == user and board[2][3] == user and board[3][2] == user:
    diagpoints = 2
  if board[0][3] == user and board[1][2] == user and board[2][1] == user:
    diagpoints = 2
  if board[2][3] == user and board[3][2] == user and board[4][1] == user:
    diagpoints = 2
  if board[1][2] == user and board[2][1] == user and board[3][0] == user:
    diagpoints = 2
  if board[0][2] == user and board[1][1] == user and board[2][0] == user:
    diagpoints = 2
  # 10 punti
  if board[0][0] == user and board[1][1] == user and board[2][2] == user and board[3][3]== user:
    diagpoints = 10
  if board[0][1] == user and board[1][2] == user and board[2][3] == user and board[3][4]== user:
    diagpoints = 10
  if board[1][0] == user and board[2][1] == user and board[3][2] == user and board[4][3]== user:
    diagpoints = 10
  if board[0][4] == user and board[1][3] == user and board[2][2] == user and board[3][1]== user:
    diagpoints = 10
  if board[1][4] == user and board[2][3] == user and board[3][2] == user and board[4][1]== user:
    diagpoints = 10
  if board[0][3] == user and board[1][2] == user and board[2][1] == user and board[3][0]== user:
    diagpoints = 10
#50 punti
  if board[0][0] == user and board[1][1] == user and board[2][2] == user and board[3][3] == user and board[4][4] == user:
    diagpoints = 50
  if board[0][4] == user and board[1][3] == user and board[2][2] == user and board[3][1] == user and board[4][0] == user:
    diagpoints = 50
  return diagpoints

while turns < 25:
  print("Punteggio:")
  print("Giocatore x: ", pointuser1)
  print("Giocatore o: ", pointuser2)
  active_user = current_user(user)
  print_board(board)
  user_input = input("Inserisci un numero tra 1 e 25 per scegliere la posizione oppure premi \"q\" per uscire: ")
  if quit(user_input): break
  if not check_input(user_input):
    print("Ritenta")
    continue
  user_input = int(user_input) - 1
  coords = coordinates(user_input)
  if istaken(coords, board):
    print("Ritenta")
    continue
  add_to_board(coords, board, active_user)
  if iswin(active_user, board): 
    print(f"{active_user.upper()} ha vinto!")
    break
  
  turns += 1
  if turns == 25: print("Patta")
  user = not user