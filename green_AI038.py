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
