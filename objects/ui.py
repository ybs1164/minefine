import pygame
import pygame_gui

from pygame_gui.elements import UIPanel
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIButton

# todo : receive this data from main.py's mapsize...
#        or this data send to main.py's mapsize
mapsize = (32, 32)

manager = pygame_gui.UIManager((mapsize[0] * 20, mapsize[1] * 20))

ggPanel = UIPanel(pygame.Rect(mapsize[0]*10 - 150, mapsize[1]*10 - 100, 300, 200),
                  starting_layer_height=4,
                  manager=manager)

ggPanel.hide()

retryButton = UIButton(pygame.Rect(0, 150, 294, 44), 'Retry', manager, container=ggPanel)

titleLabel = UILabel(pygame.Rect(0, 0, 294, 30),
                     text='Game Over',
                     manager=manager,
                     container=ggPanel,
                     parent_element=ggPanel)

subLabel = UILabel(pygame.Rect(0, 70, 294, 60),
                   text='you just activated my trap mine',
                   manager=manager,
                   container=ggPanel,
                   parent_element=ggPanel)

def ChangePanel(title, sub):
    titleLabel.set_text(title)
    subLabel.set_text(sub)

def ClearPanel(time):
    ChangePanel("Game Clear", "You Win / " + time)

def GameOverPanel():
    ChangePanel("Game Over", "You just activated my trap mine")