import pygame
import pygame.gfxdraw

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

def background(screen):
    screen.fill(WHITE)

def drawCell(screen, x, y, r, n):
    x = x*r*2+r
    y = y*r*2+r
    if n==-2:
        pygame.gfxdraw.filled_circle(screen, x, y, r, RED)
    elif n==-1:
        pygame.gfxdraw.filled_circle(screen, x, y, r, BLACK)
    else:
        pygame.gfxdraw.circle(screen, x, y, r, BLACK)

    font = pygame.font.SysFont(None, int(r))

    if n>0:
        text = font.render(str(n), True, BLACK)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)