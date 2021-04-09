import pygame
import sys
from objects import draw
from objects import utils

# pylint: disable=no-member

mapsize = (32, 32)
cellmap = utils.getCellMap(mapsize[0], mapsize[1], 120)

screen = pygame.display.set_mode((mapsize[0] * 20, mapsize[1] * 20))
pygame.display.set_caption('Minesweep')

pygame.init()

draw.background(screen)

for i in range(mapsize[0]):
    for j in range(mapsize[1]):
        draw.drawCell(screen, i, j, 10, cellmap[i][j].getMineCount())

pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mousex = event.pos[0] // 20
            mousey = event.pos[1] // 20

            if event.button == 1: # 좌클릭
                isGameover = True
                for p in utils.clickCellMap(cellmap, mousex, mousey, mapsize[0], mapsize[1]):
                    isGameover = False
                    draw.drawCell(screen, p[0], p[1], 10, cellmap[p[0]][p[1]].getMineCount())
                if isGameover:
                    run = False
            elif event.button == 3: # 우클릭
                if cellmap[mousex][mousey].isEnable:
                    continue
                cellmap[mousex][mousey].isFlag = not cellmap[mousex][mousey].isFlag

                draw.drawCell(screen, mousex, mousey, 10, cellmap[mousex][mousey].getMineCount())

            pygame.display.flip()

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
sys.exit()