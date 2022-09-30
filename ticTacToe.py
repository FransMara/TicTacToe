
from board import printBoard

theBoard = { 'q' : '' , 'w' : '' , 'e' : '' ,
             'a' : '' , 's' : '' , 'd' : '' , 
             'z' : '' , 'x' : '' , 'c' : '' }



def game():

  turn = 'X'
  count = 0


  #we want to check if the chosen move is correct for the player

  for i in range(10):          #there are 9 possible moves a player can make

    if( i  == 0):
      printBoard(theBoard)

    print('It is ' + turn + 's turn. Move where?')

    move = input()

    if(theBoard[move] == ''):
      theBoard[move] = turn
      printBoard(theBoard)
      count = count + 1
    else:
      print('This spot is already occupied , please retry')
      i = i -1
    


game()
