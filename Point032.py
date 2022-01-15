def point_AI(board, color):

  point = [20,-10,0,0,-10,20,
         -10,-5,-2,-2,-5,-10,
         0,-2,0,0,-2,0,
         0,-2,0,0,-2,0,
         -10,-5,-2,-2,-5,-10,
         20,-10,0,0,-10,20]

  arr=[]
  for pos, val in enumerate(point):
    arr.append([val,pos])
  arr.sort(reverse=True)
  for i in range(len(arr)):
    position = arr[i][1]
    if put_and_reverse(board, position, color):
      return position
  return 0
