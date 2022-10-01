
def retry():

  decision = input('Would you like to retry,\ny/n?\n')

  if( decision == 'y' or decision == 'Y' ):
    print('**New Game!**')
  elif( decision == 'n' or decision == 'N' ):
    exit()
  else:
    print('\n**Unrecognized character**\n')
    retry()