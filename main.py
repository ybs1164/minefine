import pygame
import sys
from objects import draw
from objects import cell

# pylint: disable=no-member

screen = pygame.display.set_mode((320,320))
pygame.display.set_caption('Minesweep')

pygame.init()

cellmap = []

for i in range(15):
    cellmap.append([])
    for j in range(15):
        cellmap[i].append(cell.Cell(False))

run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw.background(screen)

    for i in range(len(cellmap)):
        for j in range(len(cellmap[i])):
            draw.drawCell(screen, i, j, 10, -1)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()