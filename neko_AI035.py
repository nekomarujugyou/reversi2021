def neko_AI(board, color):
  a = [0,5,30,35,2,3,12,17,18,23,32,33,8,9,13,16,19,22,26,27,1,4,6,11,24,29,31,34,7,10,25,28]
  for i in range(len(a)):
    position =a[i]
    if put_and_reverse(board, position, color):
      return position
  return 0
