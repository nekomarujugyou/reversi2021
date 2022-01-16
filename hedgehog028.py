
#
# オセロ（リバーシ） 6x6
#

N = 6  # 大きさ

EMPTY = 0  # 空
BLACK = 1  # 黒
WHITE = 2  # 白
STONE = ['□', '●', '○']  #石の文字

#
# board = [0] * (N*N)
#

def xy(p):    # 1次元から2次元へ
  return p % N, p // N


def p(x, y):    # 2次元から1次元へ
  return x + y * N

# リバーシの初期画面を生成する

def init_board():
  board = [EMPTY] * (N*N)
  c = N//2
  board[p(c, c)] = BLACK
  board[p(c-1, c-1)] = BLACK
  board[p(c, c-1)] = WHITE
  board[p(c-1, c)] = WHITE
  return board

# リバーシの画面を表示する

def show_board(board):
  counts = [0, 0, 0]
  for y in range(N):
    for x in range(N):
      stone = board[p(x, y)]
      counts[stone] += 1
      print(STONE[stone], end='')
    print()
  print()
  for pair in zip(STONE, counts):
    print(pair, end=' ')
  print()


# (x,y) が盤面上か判定する
def on_borad(x, y):
  return 0 <= x < N and 0 <= y < N

# (x,y)から(dx,dy)方向をみて反転できるか調べる
def try_reverse(board, x, y, dx, dy, color):
  if not on_borad(x, y) or board[p(x, y)] == EMPTY:
    return False
  if board[p(x, y)] == color:
    return True
  if try_reverse(board, x+dx, y+dy, dx, dy, color):
    board[p(x, y)] = color
    return True
  return False

# 相手（反対）の色を返す
def opposite(color):
  if color == BLACK:
    return WHITE
  return BLACK

# (x,y) が相手（反対）の色かどうか判定

def is_oposite(board, x, y, color):
  return on_borad(x, y) and board[p(x, y)] == opposite(color)


DIR = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),         (1, 0),
    (-1, 1), (0, 1), (1, 1),
]

def put_and_reverse(board, position, color):
  if board[position] != EMPTY:
  	return False
  board[position] = color

  x, y = xy(position)
  turned = False
  for dx, dy in DIR:
    nx = x + dx
    ny = y + dy
    if is_oposite(board, nx, ny, color):
      if try_reverse(board, nx, ny, dx, dy, color):
        turned = True
  if not turned:
    board[position] = EMPTY
  return turned

# プレイが継続できるか？ 
# つまり、まだ石を置けるところが残っているか調べる？
def can_play(board, color):
  board = board[:] # コピーしてボードを変更しないようにする
  for position in range(0, N*N):
    if put_and_reverse(board, position, color):
      return True
  return False


def game(player1, player2):
	board = init_board()
	show_board(board)
	on_gaming = True  # 　ゲームが続行できるか？
	while on_gaming:
		on_gaming = False  # 　いったん、ゲーム終了にする
		if can_play(board, BLACK):
			# player1 に黒を置かせる
			position = player1(board[:], BLACK)
			show_board(board)
			# 黒が正しく置けたら、ゲーム続行
			on_gaming = put_and_reverse(board, position, BLACK)
		if can_play(board, WHITE):
			# player1 に白を置かせる
			position = player2(board[:], WHITE)
			show_board(board)
			# 白が置けたらゲーム続行
			on_gaming = put_and_reverse(board, position, WHITE)
	show_board(board)  # 最後の結果を表示!

# AI 用のインターフェース
  
def hedgehog028_AI(board,color):  
  S = {0:0, 5:0, 30:0, 35:0}
  A = {2:0, 3:0, 12:0, 17:0, 18:0, 23:0, 32:0, 33:0}
  B = {8:0, 9:0, 13:0, 16:0, 19:0, 22:0, 26:0, 27:0}
  C = {1:0, 4:0, 6:0, 11:0, 24:0, 29:0, 31:0, 34:0}
  D = {7:0, 10:0, 25:0, 28:0}

  for i in S.keys():
    S[i] += 5
    if i == 0:
      if board[i+1] != EMPTY:
        S[i] += 1
      if board[i+6] != EMPTY:
        S[i] += 1
      if board[i+7] != EMPTY:
        S[i] += 1
    if i == 5:
      if board[i-1] != EMPTY:
        S[i] += 1
      if board[i+5] != EMPTY:
        S[i] += 1
      if board[i+6] != EMPTY:
        S[i] += 1
    if i == 30:
      if board[i+1] != EMPTY:
        S[i] += 1
      if board[i-5] != EMPTY:
        S[i] += 1
      if board[i-6] != EMPTY:
        S[i] += 1
    if i == 35:
      if board[i-1] != EMPTY:
        S[i] += 1
      if board[i-6] != EMPTY:
        S[i] += 1
      if board[i-7] != EMPTY:
        S[i] += 1
  SS = sorted(S.items(), key=lambda x:-x[1])
  SSS = dict((x, y) for x, y in SS)
  SSS = list(SSS.keys())
  
  for i in A.keys():
    A[i] += 3
    if i == 2 or i == 3:
      if board[i-1] != EMPTY:
        A[i] += 1
      if board[i+1] != EMPTY:
        A[i] += 1
      if board[i+5] != EMPTY:
        A[i] += 1
      if board[i+6] != EMPTY:
        A[i] += 1
      if board[i+7] != EMPTY:
        A[i] += 1
    if i == 12 or i == 18:
      if board[i-6] != EMPTY:
        A[i] += 1
      if board[i-5] != EMPTY:
        A[i] += 1
      if board[i+1] != EMPTY:
        A[i] += 1
      if board[i+6] != EMPTY:
        A[i] += 1
      if board[i+7] != EMPTY:
        A[i] += 1
    if i == 17 or i == 23:
      if board[i-7] != EMPTY:
        A[i] += 1
      if board[i-6] != EMPTY:
        A[i] += 1
      if board[i-1] != EMPTY:
        A[i] += 1
      if board[i+5] != EMPTY:
        A[i] += 1
      if board[i+6] != EMPTY:
        A[i] += 1
    if i == 32 or i == 33:
      if board[i-7] != EMPTY:
        A[i] += 1
      if board[i-6] != EMPTY:
        A[i] += 1
      if board[i-5] != EMPTY:
        A[i] += 1
      if board[i-1] != EMPTY:
        A[i] += 1
      if board[i+1] != EMPTY:
        A[i] += 1
  AA = sorted(A.items(), key=lambda x:-x[1])
  AAA = dict((x, y) for x, y in AA)
  AAA = list(AAA.keys())    

  for i in B.keys():
    if board[i-1] != EMPTY:
      B[i] += 1
    if board[i+1] != EMPTY:
      B[i] += 1
    if board[i-6] != EMPTY:
      B[i] += 1
    if board[i+6] != EMPTY:
      B[i] += 1
    if board[i-5] != EMPTY:
      B[i] += 1
    if board[i+5] != EMPTY:
      B[i] += 1
    if board[i-7] != EMPTY:
      B[i] += 1
    if board[i+7] != EMPTY:
      B[i] += 1
  BB = sorted(B.items(), key=lambda x:-x[1])
  BBB = dict((x, y) for x, y in BB)
  BBB = list(BBB.keys())

  for i in C.keys():
    C[i] += 3
    if i == 1 or i == 4:
      if board[i-1] != EMPTY:
        C[i] += 1
      if board[i+1] != EMPTY:
        C[i] += 1
      if board[i+6] != EMPTY:
        C[i] += 1
      if board[i+5] != EMPTY:
        C[i] += 1
      if board[i+7] != EMPTY:
        C[i] += 1
    if i == 6 or i == 24:
      if board[i+1] != EMPTY:
        C[i] += 1
      if board[i-6] != EMPTY:
        C[i] += 1
      if board[i+6] != EMPTY:
        C[i] += 1
      if board[i-5] != EMPTY:
        C[i] += 1
      if board[i+7] != EMPTY:
        C[i] += 1
    if i == 11 or i == 29:
      if board[i-1] != EMPTY:
        C[i] += 1
      if board[i-6] != EMPTY:
        C[i] += 1
      if board[i+6] != EMPTY:
        C[i] += 1
      if board[i+5] != EMPTY:
        C[i] += 1
      if board[i-7] != EMPTY:
        C[i] += 1
    if i == 31 or i == 34:
      if board[i-1] != EMPTY:
        C[i] += 1
      if board[i+1] != EMPTY:
        C[i] += 1
      if board[i-6] != EMPTY:
        C[i] += 1
      if board[i-5] != EMPTY:
        C[i] += 1
      if board[i-7] != EMPTY:
        C[i] += 1
  CC = sorted(C.items(), key=lambda x:-x[1])
  CCC = dict((x, y) for x, y in CC)
  CCC = list(CCC.keys())

  for i in D.keys():
    if board[i-1] != EMPTY:
      D[i] += 1
    if board[i+1] != EMPTY:
      D[i] += 1
    if board[i-6] != EMPTY:
      D[i] += 1
    if board[i+6] != EMPTY:
      D[i] += 1
    if board[i-5] != EMPTY:
      D[i] += 1
    if board[i+5] != EMPTY:
      D[i] += 1
    if board[i-7] != EMPTY:
      D[i] += 1
    if board[i+7] != EMPTY:
      D[i] += 1
  DD = sorted(D.items(), key=lambda x:-x[1])
  DDD = dict((x, y) for x, y in DD)
  DDD = list(DDD.keys())

  X = SSS + AAA + BBB + CCC + DDD
  for _ in range(N*N):  
    for i in X:
      position=i
      if put_and_reverse(board,position,color):
        return position
  return 0
