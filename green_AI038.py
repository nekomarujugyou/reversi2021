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

board = [
  0, 0, 0, 0, 0, 0,           
  0, 0, 0, 0, 0, 0,           
  0, 0, 1, 2, 0, 0,           
  0, 0, 2, 1, 0, 0,           
  0, 0, 0, 0, 0, 0,           
  0, 0, 0, 0, 0, 0,           
]

def green_AI(board,color):
  #リスト
  A=[0, 5, 30, 35, 
     2, 3, 12, 17, 18, 23, 32, 33,
     8, 9, 13, 16, 19, 22, 26, 27,
     7, 10, 25, 28,
     1, 4, 6, 11, 24, 29, 31, 34]

  for _ in range(100):
    for i in A:
      position=i
      #確認
      if put_and_reverse(board,position,color):
        #置けるときは位置を返す
        return position
  return 0


def run_reversi(ai):
  display(IPython.display.HTML(HTML))
  
  def accept(x, y):
    global count
    count+=1
    position=y*6+x
    if count%2==0:
      color=2
      ai(board,color)
      return IPython.display.JSON({'result': board})

    else:
      color=1
      put_and_reverse(board, position, color)
      print(count,":",x, y, y*6+x)
      return IPython.display.JSON({'result': board})
  

  output.register_callback('notebook.accept', accept)
  
count=0
run_reversi(green_AI)
