def key(turn):
  inputKey = input('It is ' + turn + 's turn. Move where?\n')
  if(inputKey == 'q' or inputKey == 'w' or inputKey == 'e' or inputKey == 'a' or inputKey == 's' or inputKey == 'd' or inputKey == 'z' or inputKey == 'x' or inputKey == 'c'):
    return inputKey
  else:
    print('**Unrecognized character, please retry**')
    inputKey = key(turn)
    return inputKey

