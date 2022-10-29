from random import randint as rand
def buildAGrid(row,col):
  board=[]
  for r in range(row):
    r=[]
    for c in range(col):
      r.append(0)
    board.append(r)
  return board

def layMines(board,meinen):
  count=0
  while count<meinen:
    row=rand(0,len(board)-1)
    col=rand(0,len(board[0])-1)
    if board[row][col]!=-1:
      board[row][col]=-1
      count+=1

def funnyGround(r,c,grid):
  if grid[r][c]!=-1:
    count=0
    for roff in range(-1,2):
      for coff in range(-1,2):
        if 0<=r+roff<len(grid) and 0<=c+coff<len(grid[0]) and grid[r+roff][c+coff]==-1:
          count=count+1
    return count      
  return-1