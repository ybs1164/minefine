import pygame
import pygame_gui
import sys

# pylint: disable=no-member

mapsize = (32, 32)

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((mapsize[0] * 20, mapsize[1] * 20))
pygame.display.set_caption('Minesweep')

from objects import ui
from objects import draw
from objects import utils

mineCount = 120
cellmap = utils.getCellMap(mapsize[0], mapsize[1], mineCount)

draw.background(screen)

draw.drawCellMap(screen, cellmap, mapsize[0], mapsize[1])

clock = pygame.time.Clock()

manager = ui.GetManager(mapsize[0], mapsize[1])
gameOver = ui.GetPanel(manager, mapsize[0], mapsize[1], "Game Over", "you just activated my trap mine")
gameClear = ui.GetPanel(manager, mapsize[0], mapsize[1], "Game Clear", "You Win! Congratulation!")

showCells = 0 # 보여진 칸 개수
countFlag = 0 # 깃발 개수
enableMine = True # 칸을 공개할 수 있는지 여부
run = True
while run:
    time_delta = clock.tick(60)/1000.
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and enableMine:
            # 마우스 좌표값
            mousex = event.pos[0] // 20
            mousey = event.pos[1] // 20

            if event.button == 1: # 좌클릭
                for p in utils.clickCellMap(cellmap, mousex, mousey, mapsize[0], mapsize[1]):
                    draw.drawCell(screen, p[0], p[1], 10, cellmap[p[0]][p[1]].getMineCount())
                    showCells+=1
                
                if cellmap[mousex][mousey].isMine:
                    showCells-=1
                    enableMine = False
                    gameOver.show()
                
                if showCells == mapsize[0] * mapsize[1] - mineCount:
                    enableMine = False
                    gameClear.show()

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
                    enableMine = False
                    gameOver.show()
                    continue
                    
                if isShow:
                    for k in utils.close:
                        if utils.isBorder(mousex+k[0], mousey+k[1], mapsize[0], mapsize[1]):
                            continue
                        if not cellmap[mousex + k[0]][mousey + k[1]].isFlag:
                            for p in utils.clickCellMap(cellmap, mousex + k[0], mousey + k[1], mapsize[0], mapsize[1]):
                                draw.drawCell(screen, p[0], p[1], 10, cellmap[p[0]][p[1]].getMineCount())
                                showCells+=1
                    
                    if showCells == mapsize[0] * mapsize[1] - mineCount:
                        enableMine = False
                        gameClear.show()

            elif event.button == 3: # 우클릭
                if cellmap[mousex][mousey].isEnable:
                    continue
                cellmap[mousex][mousey].isFlag = not cellmap[mousex][mousey].isFlag
                if cellmap[mousex][mousey].isMine: # 깃발 확인
                    countFlag += 1 if cellmap[mousex][mousey].isFlag else -1
                if countFlag == mineCount: # 깃발이 모든 지뢰를 찾았다면 게임 클리어
                    enableMine = False
                    gameClear.show()

                draw.drawCell(screen, mousex, mousey, 10, cellmap[mousex][mousey].getMineCount())

        if event.type == pygame.QUIT: # 게임 종료
            run = False
        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_object_id == "panel.button": # 게임 리셋
                    cellmap = utils.getCellMap(mapsize[0], mapsize[1], mineCount)
                    enableMine = True
                    countFlag = 0
                    showCells = 0
                    draw.drawCellMap(screen, cellmap, mapsize[0], mapsize[1])
                    gameOver.hide()
                    gameClear.hide()
        
        manager.process_events(event)
    
    manager.update(time_delta)
    manager.draw_ui(screen)

    pygame.display.update()


pygame.quit()
sys.exit()