import pygame
import sys
from objects import draw
from objects import utils

# pylint: disable=no-member

mapsize = (32, 32)
cellmap = utils.getCellMap(mapsize[0], mapsize[1])

screen = pygame.display.set_mode((mapsize[0] * 20, mapsize[1] * 20))
pygame.display.set_caption('Minesweep')

pygame.init()

draw.background(screen)

for i in range(len(cellmap)):
    for j in range(len(cellmap[i])):
        draw.drawCell(screen, i, j, 10, cellmap[i][j].getMineCount())

pygame.display.flip()

run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mousex = event.pos[0] // 20
            mousey = event.pos[1] // 20
            if event.button == 1: # 좌클릭
                celllist = [(mousex, mousey)]

                while len(celllist) > 0:
                    x = celllist[-1][0]
                    y = celllist[-1][1]
                    celllist.pop()

                    if not cellmap[x][y].isEnable:
                        cellmap[x][y].isEnable = True
                        close = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

                        if cellmap[x][y].isMine:
                            run = False
                        if cellmap[x][y].getMineCount()>0:
                            continue

                        for k in close:
                            if utils.isBorder(x+k[0], y+k[1], mapsize[0], mapsize[1]):
                                continue
                            celllist.append((x+k[0], y+k[1]))
                
                draw.background(screen)

                for i in range(len(cellmap)):
                    for j in range(len(cellmap[i])):
                        draw.drawCell(screen, i, j, 10, cellmap[i][j].getMineCount())

                pygame.display.flip()

            elif event.button == 3: # 우클릭
                print("right")

        if event.type == pygame.QUIT:
            run = False

    #clock.tick(60)

pygame.quit()
sys.exit()