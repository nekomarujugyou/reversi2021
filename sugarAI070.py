## ソースコード ##

N = 6
EMPTY = 0
BLACK = 1
WHITE = 2

# 1次元から2次元へ
def xy(p):
    return p%N, p//N

# 2次元から1次元へ
def p(x, y):
    return x + y*N

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

# (x, y)が盤面上か判定する
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
 

## UI ##

import IPython
from google.colab import output

HTML = '''
<style>
#canvas {
  background: lightgreen;
}
</style>
<canvas id="canvas" width="320" height="320"></canvas>
<script>
var canvas = document.getElementById("canvas");
var wsize = 320;
var N=6;
var dsize = (wsize / N);
var r = (dsize/2);

var board = [
  0, 0, 0, 0, 0, 0, //           
  0, 0, 0, 0, 0, 0, //           
  0, 0, 1, 2, 0, 0, //           
  0, 0, 2, 1, 0, 0, //           
  0, 0, 0, 0, 0, 0, //           
  0, 0, 0, 0, 0, 0, //           
];

function drawBoard(board) {
  var context = canvas.getContext('2d');
  for (var yi = 0; yi < N; yi += 1) {
    for (var xi = 0; xi < N; xi += 1) {
      if ((xi+yi) % 2 == 0) {
        context.fillStyle = "darkgreen";
        context.fillRect(xi*dsize, yi*dsize, dsize-1, dsize-1);       
      }
      if(board[yi*N+xi] != 0) {
          context.beginPath () ;
          var cx = xi*dsize + r;
          var cy = yi*dsize + r;
          context.arc( cx, cy, r, 0 * Math.PI / 180, 360 * Math.PI / 180, false ) ;
          if(board[yi*N+xi] == 1) {
            context.fillStyle = "rgba(0,0,0,1.0)" ;
          }
          else {
            context.fillStyle = "rgba(255,255,255,1.0)" ;
          }
          context.fill() ;
      }
    }    
  }    
}

drawBoard(board);


function drawRect(x, y, width, height) {
  var context = canvas.getContext('2d');
  context.fillRect(x, y, width, height);
}

function onClick(e) {
  console.log("click");
  var x = e.clientX - canvas.offsetLeft;
  var y = e.clientY - canvas.offsetTop;
  //console.log("x:", x, "y:", y);
  // 非同期でPython 側に送る
  (async function() {
    const result = await google.colab.kernel.invokeFunction('notebook.accept', [(x / dsize)|0, (y / dsize)|0], {});
    const data = result.data['application/json'];
    drawBoard(data.result);
  })();
  //drawRect(x, y, 10, 10);
}

canvas.addEventListener('click', onClick, false);


</script>
'''


## AI ##
import random

def sugar_AI(board, color): #sugarAI
    C = 0
    while C==0 :
        for kado in [0, 5, 30, 35]:
            position = kado
            if put_and_reverse(board, position, color):
                C = 1
                break
        position = random.randint(0, N*N-1)
        if put_and_reverse(board, position, color):
            C = 1
            break
    return position
  
 
board = [
  0, 0, 0, 0, 0, 0,           
  0, 0, 0, 0, 0, 0,           
  0, 0, 1, 2, 0, 0,           
  0, 0, 2, 1, 0, 0,           
  0, 0, 0, 0, 0, 0,           
  0, 0, 0, 0, 0, 0,           
]

def accept(x, y):
    global switch
    if switch == 'B':           # 黒：人
        position = p(x, y)
        color = BLACK
        if put_and_reverse(board, position, color):
            print("黒：", board.count(1), "　　白：", board.count(2))
        if can_play(board, WHITE):
            switch = 'W'
        return IPython.display.JSON({'result': board})
    
    else:                       # 白：AI
        color = WHITE
        position = sugar_AI(board, color)
        if put_and_reverse(board, position, color):
            print("黒：", board.count(1), "　　白：", board.count(2))
        if can_play(board, BLACK):
            switch = 'B'
        return IPython.display.JSON({'result': board})

def run_reversi(accept):
    display(IPython.display.HTML(HTML))
    output.register_callback('notebook.accept', accept)
    
    
switch = 'B'
run_reversi(accept)
#AIを動かすのにどこかのマスをクリックする必要がある
