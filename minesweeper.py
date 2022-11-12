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

def showSpace(r,c,grid):
  grid[r][c][1]["text"]=grid[r][c][0]
  grid[r][c][1]["relief"]="sunken"

def showSpaces(r,c,grid):
  if grid[r][c][0]==-1:
    visited=set()
    queue=[(r,c)]
    while len(queue)>0:
      cu=queue.pop(0)
      if grid[cu[0]][cu[1]][0]==0:
        for roff in range(-1,2):
          for coff in range(-1,2):
            if 0<=r+roff<len(grid) and 0<=c+coff<len(grid[0]) and not((r+roff,c+coff) in visited):
              queue.append((r+roff,c+coff))
      showSpace(cu[0],cu[1],grid)
      visited.add ((cu[0],cu[1]))

