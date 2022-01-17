# reversi2021
強化学習を使ったAIオセロの開発に挑戦しましょう
!git clone https://github.com/kkuramitsu/reversi2021.git
from reversi2021.reversi import *
STONE = ['🟩', '⚫', '⚪']
board = init_board()
show_board(board)
game(my_AI, my_AI)
game(my_AI, random_AI)
