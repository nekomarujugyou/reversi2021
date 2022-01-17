A=[5,30,0,35,3,17,2,18,12,23,32,33,13,27,22,26,16,19,8,9,4,34,31,1,11,6,24,29,10,25,28,7]
def kawauso_AI(board, color):
  for i in range(N*N):
    position =A[i]
    if put_and_reverse(board, position, color):
      return position
  return 0
