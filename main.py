import tkinter as tk
from minesweeper import *
ROWCOUNT=10
COLLUMCOUNT=10
MINECOUNT=10
grid=buildAGrid(ROWCOUNT,COLLUMCOUNT)
layMines(grid,MINECOUNT)
window=tk.Tk()


for y in range(ROWCOUNT):
  for x in range(COLLUMCOUNT):
    grid[y][x] = funnyGround(y,x,grid)
  print()


for r in range(ROWCOUNT):
  for c in range(COLLUMCOUNT):
    button=tk.Button(
      text=" ",
      width=6,
      height=3,
      command=lambda row=r,collum=c,g=grid:showSpaces(row,collum,g)
      )
    button.grid(row=r,column=c)
    grid[r][c] = [grid[r][c],button]

tk.mainloop()