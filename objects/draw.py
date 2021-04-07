import pygame
import pygame.gfxdraw

BLACK = (0,0,0)
WHITE = (255,255,255)

def background(screen):
    screen.fill(WHITE)

def drawCell(screen, x, y, r, n):
    if n<0:
        pygame.gfxdraw.filled_circle(screen, x*r*2+r, y*r*2+r, r, BLACK)
    else:
        pygame.gfxdraw.circle(screen, x*r*2+r, y*r*2+r, r, BLACK)

    font = pygame.font.SysFont(None, int(r * 0.6))

    if n>0:
        text = font.render(str(n), True, BLACK)
        text_rect = text.get_rect(center=(x*r, y*r))
        screen.blit(text, text_rect)