import random
from . import cell

def isBorder(x, y, w, h):
    return x < 0 or y < 0 or x > w-1 or y > h-1

def getCellMap(w, h):
    cellmap = []
    for i in range(w):
        cellmap.append([])
        for _ in range(h):
            cellmap[i].append(cell.Cell(random.random() > 0.9))
    
    close = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

    for i in range(w):
        for j in range(h):
            l = []
            for k in close:
                if isBorder(i+k[0], j+k[1], w, h):
                    continue
                l.append(cellmap[i+k[0]][j+k[1]])
            cellmap[i][j].setCloseCells(l)


    return cellmap