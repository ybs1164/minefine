import pygame
import pygame.gfxdraw

PRIMARY = (150,150,150)
SECONDARY = (255,255,255)
MINE = (255,100,100)
FLAG = (100,100,255)

UI = (230,230,230)

def background(screen):
    screen.fill(SECONDARY)

def drawCell(screen, x, y, r, n):
    x = x*r*2+r
    y = y*r*2+r

    pygame.draw.rect(screen, SECONDARY, [x-r, y-r, r*2, r*2])

    if n==-3: # 깃발 세움
        pygame.gfxdraw.filled_circle(screen, x, y, r, FLAG)
    elif n==-2: # 지뢰 밟음
        pygame.gfxdraw.filled_circle(screen, x, y, r, MINE)
    elif n==-1: # 공개됨
        pygame.gfxdraw.filled_circle(screen, x, y, r, PRIMARY)
    else: # 비공개됨
        pygame.gfxdraw.circle(screen, x, y, r, PRIMARY)

    font = pygame.font.SysFont(None, int(r * 2.8))

    if n>0:
        text = font.render(str(n), True, PRIMARY)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

def drawCellMap(screen, cellmap, w, h):
    for i in range(w):
        for j in range(h):
            drawCell(screen, i, j, 10, cellmap[i][j].getMineCount())
