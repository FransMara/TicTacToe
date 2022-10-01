#this function checks if a player has won or if we reach a tie condition

def didWin(theBoard , turn , count):

  if (count >= 5):  #only necessary to check after the count is greater than this value

    if (theBoard['q'] == theBoard['w'] == theBoard['e'] != ' '):  #top line - across
      return 1 #win
    elif (theBoard['a'] == theBoard['s'] == theBoard['d'] != ' '):  #middle line - across
      return 1
    elif (theBoard['z'] == theBoard['x'] == theBoard['c'] != ' '):  #bottom line - across
      return 1
    elif (theBoard['q'] == theBoard['a'] == theBoard['z'] != ' '):  #left line - down
      return 1
    elif (theBoard['w'] == theBoard['s'] == theBoard['x'] != ' '):  #middle line - down
      return 1
    elif (theBoard['e'] == theBoard['d'] == theBoard['c'] != ' '):  #right line - down
      return 1
    elif (theBoard['q'] == theBoard['s'] == theBoard['c'] != ' '):  #diag 1
      return 1
    elif (theBoard['e'] == theBoard['s'] == theBoard['z'] != ' '):  #diag 2
      return 1

  #if board fills and neither player has won we declare a tie
  if (count == 9):
    return 0 #tie
  
  #if non of the above are verified that means that we are still playing the game and we swap players
  if turn == 'X' : 
     turn = 'O'
  else:
    turn = 'X'
  return turn
