
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
      # 黒が正しく置けたら、ゲーム続行
      on_gaming = put_and_reverse(board, position, BLACK) 
      position = player1(board[:], BLACK)
      show_board(board)
    if can_play(board, WHITE):
      # player1 に白を置かせる
      position = player2(board[:], WHITE)
      show_board(board)
      # 白が置けたらゲーム続行
      on_gaming = put_and_reverse(board, position, WHITE)
  show_board(board)  # 最後の結果を表示!

# AI 用のインターフェース
  
def my_AI(board, color): #おチビちゃんAI
  for position in range(N*N):
    if put_and_reverse(board, position, color):
      return position
  return 0
#ここを編集しましょうね^^

import random

def Pine_AI(board,color):
  CanPutlist=[]
  for position in range(N*N):
    if put_and_reverse(board, position, color):
      CanPutlist.append(position)

  #優先度最高
  list1 = []
  if 0 or 5 or 30 or 35 in CanPutlist:
    if 0 in oklist:list1.append(0)
    if 5 in oklist:list1.append(5)
    if 30 in oklist:list1.append(30)
    if 35 in oklist:list1.append(35)
    return(random.choice(list1))

  #優先度2番目
  elif 2 or 3 or 12 or 17 or 18 or 23 or 32 or 33 in CanPutlist:
    if 2 in oklist:list1.append(2)
    if 3 in oklist:list1.append(3)
    if 12 in oklist:list1.append(12)
    if 17 in oklist:list1.append(17)
    if 18 in oklist:list1.append(18)
    if 23 in oklist:list1.append(23)
    if 32 in oklist:list1.append(32)
    if 33 in oklist:list1.append(33)
    return(random.choice(list1))

  #優先度3番目
  elif 8 or 9 or 13 or 16 or 19 or 22 or 26 or 27 in CanPutlist:
    if 8 in oklist:list1.append(8)
    if 9 in oklist:list1.append(9)
    if 13 in oklist:list1.append(13)
    if 16 in oklist:list1.append(16)
    if 19 in oklist:list1.append(19)
    if 22 in oklist:list1.append(22)
    if 26 in oklist:list1.append(26)
    if 27 in oklist:list1.append(27)
    return(random.choice(list1))

  #優先度4番目
  elif 1 or 4 or 6 or 11 or 24 or 29 or 31 or 34 in CanPutlist:
    if 1 in oklist:list1.append(1)
    if 4 in oklist:list1.append(4)
    if 6 in oklist:list1.append(6)
    if 11 in oklist:list1.append(11)
    if 24 in oklist:list1.append(24)
    if 29 in oklist:list1.append(29)
    if 31 in oklist:list1.append(31)
    if 34 in oklist:list1.append(34)
    return(random.choice(list1))

  #優先度最高
  else:
    if 7 in oklist:list1.append(7)
    if 10 in oklist:list1.append(10)
    if 25 in oklist:list1.append(25)
    if 28 in oklist:list1.append(28)
    return(random.choice(list1))
  
  return 0

#まあfor文で繰り返し書いたほうが楽だなあとは思ったのですが...
