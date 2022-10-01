from printBoard import printBoard
from winCheck import didWin 
from retry import retry
from theBoardDef import board
from keyCheck import key

def game():

  theBoard = board()            #initialize the board
  turn = 'X'                    # first player X goes
  count = 0                     # game counter

  for i in range(10):           #there are 9 possible moves a player can make

    if( i  == 0):               #print starting board
      printBoard(theBoard)

    move = key(turn)              #player must input position where they want to place X or O.

    if(theBoard[move] == ' '):  #if valid position
      theBoard[move] = turn
      printBoard(theBoard)
      count = count + 1         #the game goes forward
    else:
      print('This spot is already occupied , please retry')
      continue                  #reject remaining statements in loop and restart

    if( didWin(theBoard , turn , count) == 1 ):        #did a player win?
      print('**Player ' + turn + ' has won**')
      return 'gameOver'
    elif(  didWin(theBoard , turn , count) == 0):      #or was there a tie?
      print('Tie -- game over')
      return 'gameOver'
    else:                                             #else proceed with the game 
      turn =  didWin(theBoard , turn , count)
      



# "MAIN":
print('Welcome to my TicTacToe game!')
print('Please use the following keys to play:\n')
print('q|w|e')
print('-+-+-')
print('a|s|d')
print('-+-+-')
print('z|x|c\n\n')
print('This is the layout of the board:')

while(1):
  if( game() == 'gameOver' ):
    retry()




