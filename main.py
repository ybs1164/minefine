import pygame
import pygame_gui
import sys
from objects import draw
from objects import utils

# pylint: disable=no-member

mapsize = (32, 32)

pygame.init()

screen = pygame.display.set_mode((mapsize[0] * 20, mapsize[1] * 20))
pygame.display.set_caption('Minesweep')

from objects import ui

mineCount = 50
cellmap = utils.getCellMap(mapsize[0], mapsize[1], mineCount)

draw.background(screen)

draw.drawCellMap(screen, cellmap, mapsize[0], mapsize[1])

clock = pygame.time.Clock()

showCells = 0
countFlag = 0
enableMine = True
run = True
while run:
    time_delta = clock.tick(60)/1000.
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and enableMine:
            mousex = event.pos[0] // 20
            mousey = event.pos[1] // 20

            if event.button == 1: # 좌클릭
                for p in utils.clickCellMap(cellmap, mousex, mousey, mapsize[0], mapsize[1]):
                    draw.drawCell(screen, p[0], p[1], 10, cellmap[p[0]][p[1]].getMineCount())
                    showCells+=1
                
                if cellmap[mousex][mousey].isMine:
                    showCells-=1
                    ui.GameOverPanel()
                    enableMine = False
                    ui.ggPanel.show()
                
                if showCells == mapsize[0] * mapsize[1] - mineCount:
                    ui.ClearPanel("")
                    enableMine = False
                    ui.ggPanel.show()

            elif event.button == 2:
                if not cellmap[mousex][mousey].isEnable:
                    continue
                
                isShow = True
                isBomb = False

                for k in utils.close:
                    if utils.isBorder(mousex+k[0], mousey+k[1], mapsize[0], mapsize[1]):
                        continue
                    cell = cellmap[mousex+k[0]][mousey+k[1]]
                    if cell.isMine and not cell.isFlag:
                        isShow = False
                    if cell.isFlag and not cell.isMine:
                        isBomb = True
                
                if isBomb:
                    ui.GameOverPanel()
                    enableMine = False
                    ui.ggPanel.show()
                    continue
                    
                if isShow:
                    for k in utils.close:
                        if utils.isBorder(mousex+k[0], mousey+k[1], mapsize[0], mapsize[1]):
                            continue
                        if not cellmap[mousex + k[0]][mousey + k[1]].isFlag:
                            for p in utils.clickCellMap(cellmap, mousex + k[0], mousey + k[1], mapsize[0], mapsize[1]):
                                draw.drawCell(screen, p[0], p[1], 10, cellmap[p[0]][p[1]].getMineCount())
                                showCells+=1
                    
                    print(showCells)
                    if showCells == mapsize[0] * mapsize[1] - mineCount:
                        ui.ClearPanel("")
                        enableMine = False
                        ui.ggPanel.show()

            elif event.button == 3: # 우클릭
                if cellmap[mousex][mousey].isEnable:
                    continue
                cellmap[mousex][mousey].isFlag = not cellmap[mousex][mousey].isFlag
                if cellmap[mousex][mousey].isMine:
                    countFlag = 1 if cellmap[mousex][mousey].isFlag else -1
                if countFlag == mineCount:
                    ui.ClearPanel("")
                    enableMine = False
                    ui.ggPanel.show()

                draw.drawCell(screen, mousex, mousey, 10, cellmap[mousex][mousey].getMineCount())

        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == ui.retryButton:
                    cellmap = utils.getCellMap(mapsize[0], mapsize[1], mineCount)
                    enableMine = True
                    countFlag = 0
                    showCells = 0
                    draw.drawCellMap(screen, cellmap, mapsize[0], mapsize[1])
                    ui.ggPanel.hide()
        
        ui.manager.process_events(event)
    
    ui.manager.update(time_delta)
    ui.manager.draw_ui(screen)

    pygame.display.update()


pygame.quit()
sys.exit()