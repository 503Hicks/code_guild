
# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

# The Player class has the following properties:

# name = player name
# token = 'X' or 'O'
# The Game class has the following properties:

# board = your representation of the board
# You can represent the board however you like, such as a 2D list, tuples, or dictionary.

# The Game class has the following methods:

# __repr__() Returns a pretty string representation of the game board
# >>> print(board)
# X| | 
# O|X|O
#  | | 
# move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
# >>> board.move(2, 1, player_1)
#  | | 
#  | |X
#  | | 
# calc_winner() What token character string has won or None if no one has.
# X| | 
# O|X|O
#  | |X
# >>> board.calc_winner()
# X
# is_full() Returns true if the game board is full.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_full()
# True
# is_game_over() Returns true if the game board is full or a player has won.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_game_over()
# True

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False

# The Player class has the following properties:
# name = player name
# token = 'X' or 'O'


# CLASS SOLUTION 

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

# The Game class has the following properties:

# board = your representation of the board
class Game:
    def __init__(self,):
        self.win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8))
        self.board =  [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # __repr__() Returns a pretty string representation of the game board
    def __repr__(self):
        print('')
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print('')

        # 0 1 2
        # 3 4 5
        # 6 7 8

    # move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
    def move(self, player):
        player_pick = int(input(f'{player.name}, Make your move: '))
        
        if self.board[player_pick] != 'X' or self.board[player_pick] != 'O':
            self.board[player_pick] = player.token
            return player_pick
        else:
            print('Spot is taken, Try another!')
            self.move(player)
    
    # calc_winner() What token character string has won or None if no one has.
    def calc_winner(self,):
    #    self.win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8))
        for a in self.win_conditions:
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == "X":
                print("PLAYER X WINS")
                return True

            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == "O":
                print("PLAYER O WINS")
                return True
    
    # is_full() Returns true if the game board is full.
    def is_full(self):
        for i in self.board:
            if i in [0,1,2,3,4,5,6,7,8]:
                return False
        return True

    # is_game_over() Returns true if the game board is full or a player has won.
    def is_game_over(self):
        pass

def main():
    player1 = Player('Bob', "X")
    player2 = Player('Jill', 'O')
    board = Game()
  
    while True:
        board.__repr__()
        board.move(player1)
        if board.calc_winner():
            board.__repr__()
            break
        if board.is_full():
            print("board is full tie-game")
            break
        board.__repr__()
        board.move(player2)
        if board.calc_winner():
            board.__repr__()
            break
        if board.is_full():
            print("board is full tie-game")
            break
        board.__repr__()
main()









# JON + VAN's SOLUTION
#! python3

class Player:
   def __init__(self, name, token):
      self.name = name
      self.token = token

class Game:
   def __init__(self):
      self.board = [['1','2','3'],['4','5','6'],['7','8','9']]
   
   def __repr__(self):
      #drawing a board 
      for i in self.board:
         result = " | ".join(i)
         print(result)     

   def calc_winner(self, player, ls):
      ls.sort()
      if ls.__contains__(1) and ls.__contains__(2) and ls.__contains__(3): # Across top
         return True, player.name
      elif ls.__contains__(4) and ls.__contains__(5) and ls.__contains__(6): # Across middle
         return True, player.name
      elif ls.__contains__(7) and ls.__contains__(8) and ls.__contains__(9): # Across Bottom
         return True, player.name
      elif ls.__contains__(1) and ls.__contains__(4) and ls.__contains__(7): # Vert left
         return True, player.name         
      elif ls.__contains__(2) and ls.__contains__(5) and ls.__contains__(8): # Vert middle
         return True, player.name
      elif ls.__contains__(3) and ls.__contains__(6) and ls.__contains__(9): # Vert Right
         return True, player.name
      elif ls.__contains__(1) and ls.__contains__(5) and ls.__contains__(9): # Top left lower right
         return True, player.name
      elif ls.__contains__(3) and ls.__contains__(5) and ls.__contains__(7): # Top right to bottom left
         return True, player.name
      else:
         return False, player.name
   
   def move(self, player):
      number_dict = {
                  1: [0, 0],
                  2: [0, 1],
                  3: [0, 2],
                  4: [1, 0],
                  5: [1, 1],
                  6: [1, 2],
                  7: [2, 0],
                  8: [2, 1],
                  9: [2, 2],
                     }
                     
      player_pick = int(input(f"{player.name}, Make your move: "))
      numb = number_dict.get(player_pick)

      if self.board[numb[0]][numb[1]] != '👻' or self.board[numb[0]][numb[1]] != '☠️':
         self.board[numb[0]][numb[1]] = player.token
         return player_pick
      else:
         print("This box is taken. Try another one!")
         self.move(player)

def game_begin(board, p1, p2):
   winning_undetermined = True
   player1_numb_ls = []
   player2_numb_ls = []

   print("To place \'👻\' or \'☠️\' on the grid, enter an integer from 1-9 as a designated box on the grid.")
   #drawing a board for sample
   board.__repr__()
   while winning_undetermined:
      #player 1 move
      player_pick = board.move(p1)
      player1_numb_ls.append(player_pick)
      is_Winning, winner_name = board.calc_winner(p1, player1_numb_ls)

      if is_Winning == True:
         board.__repr__()
         print(f"{winner_name}, you won!!!")
         exit()

      #print the game board
      board.__repr__()
      # Check for tie
      if len(player1_numb_ls) + len(player2_numb_ls) == 9:
            print("Tie! Board is full!")
            exit()

      #player 2 move
      player_pick = board.move(p2)
      player2_numb_ls.append(player_pick)
      is_Winning, winner_name = board.calc_winner(p2, player2_numb_ls)

      if is_Winning == True:
         board.__repr__()
         print(f"{winner_name}, you won!!!")
         exit()
      
      board.__repr__()
      # Check for tie
      if len(player1_numb_ls) + len(player2_numb_ls) == 9:
         print("Tie! Board is full!")
         exit()

def main():
   print("Welcome to tic-tac-toe!\nThis is a two-player game.\n")
   player1_name = input("Player 1, type in your name: ")
   player2_name = input("Player 2, type in your name: ")
   print(f"{player1_name}, you are '👻'. {player2_name}, you are '☠️'.")
   p1= Player(player1_name, '👻') # instantiate player 1
   p2 = Player(player2_name, '☠️') # instantiate player 2
   board = Game()
   game_begin(board, p1, p2)
# board = Game()
# board.__repr__()
# main()

## FAILS WHEN RUNS INTO DOUBLE INT

win_check = [[2,3],[3,4],[8,7],[4,5],[5,6]]
win_check.sort()
horizontal_list = []
for i in win_check:
   horizontal_list.append(i[0])
count = horizontal_list.count(win_check[0][0])
if count == 4:
   print("you win horizontally")


vertical_list = []
for i in win_check:
   vertical_list.append(i[1])
count = vertical_list.count(win_check[1][1])
if count == 4:
   print("You win vertically!")


#Van version for diagonal check
win_check.sort()
count = 0
previous_ls = []

for i in (win_check):
   if previous_ls == []:
      previous_ls = i
      count += 1
      print(previous_ls)
   else:
      if previous_ls[0] + 1 == i[0] and previous_ls[1] + 1 == i[1]:
         count += 1
         previous_ls = i

print(count)
if count >= 4:
   print("You won!")
else:
   print("You have not won!")