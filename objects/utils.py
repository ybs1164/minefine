import random
from . import cell

close = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

def isBorder(x, y, w, h):
    return x < 0 or y < 0 or x > w-1 or y > h-1

def getCellMap(w, h, count):
    cellmap = []
    cells = w * h
    for i in range(w):
        cellmap.append([])
        for _ in range(h):
            isMine = random.random() < count / cells
            if isMine:
                count-=1
            cellmap[i].append(cell.Cell(isMine))
            cells-=1
    
    for i in range(w):
        for j in range(h):
            if not cellmap[i][j].isMine:
                continue
            for k in close:
                if isBorder(i+k[0], j+k[1], w, h):
                    continue
                cellmap[i+k[0]][j+k[1]].mineCount+=1

    return cellmap


def clickCellMap(cellmap, x, y, w, h):
    celllist = [(x, y)]

    returnlist = []

    if cellmap[x][y].isEnable:
        return []
    cellmap[x][y].isEnable = True

    while len(celllist) > 0:
        x = celllist[-1][0]
        y = celllist[-1][1]

        returnlist.append(celllist[-1])
        celllist.pop()

        if cellmap[x][y].isMine:
            return [(x, y)]
        if cellmap[x][y].getMineCount()>0:
            continue

        for k in close:
            if isBorder(x+k[0], y+k[1], w, h):
                continue
            if cellmap[x+k[0]][y+k[1]].isEnable:
                continue
            cellmap[x+k[0]][y+k[1]].isEnable = True
            celllist.append((x+k[0], y+k[1]))
    
    return returnlist