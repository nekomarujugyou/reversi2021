


from collections import deque

H = [10,5,5,5,5,10,
      5,1,2,2,1,5,
      5,2,0,0,2,5,
      5,2,0,0,2,5,
      5,1,2,2,1,5,
     10,5,5,5,5,10]
       
def maxhand(board,color):
  hako = []
  for i in range(N*N):
    if put_and_reverse(board[:],i,color):
      hako.append(i)
  if len(hako) == 0:
    return 0
  else:
    d = []
    for k in hako:
      put_and_reverse(board,k,color)
      s = 0
      for j in range(N*N):
        if board[j] == color:
          s += H[j]
      d.append(s)
    p = max(d)
    return p


def yakiniku_AI(board,color):
  box = deque()
  box1 = []
  for position in range(N*N):
    if put_and_reverse(board[:],position,color):
      box.append(position)
      box1.append(position)

  if color == BLACK:
    AC = WHITE
  else:
    AC = BLACK
  enemypoint = []
  a_board = board
  if len(box) != 0:  
    while len(box) > 0:
      x = box.popleft()
      put_and_reverse(a_board,x,color)
      b_board = board[:]
      n = maxhand(b_board,AC)
      enemypoint.append(n)
    e = min(enemypoint)
    posi = box1[enemypoint.index(e)]
    return posi
  return 0
