import pygame
import pygame_gui

from pygame_gui.elements import UIPanel
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIButton

def GetManager(w, h):
    return pygame_gui.UIManager((w * 20, h * 20))

def GetPanel(manager, w, h, title, sub):
    panel = UIPanel(pygame.Rect(w * 10 - 150, h * 10 - 100, 300, 200),
                   starting_layer_height=4,
                   manager=manager)
    panel.hide()

    UIButton(pygame.Rect(0, 150, 294, 44), 'Retry', manager, container=panel)

    UILabel(pygame.Rect(0, 0, 294, 30),
            text=title,
            manager=manager,
            container=panel,
            parent_element=panel)
    
    UILabel(pygame.Rect(0, 70, 294, 60),
            text=sub,
            manager=manager,
            container=panel,
            parent_element=panel)

    return panel