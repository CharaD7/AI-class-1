# Sudoko a-star example
from copy import deepcopy

Grid = [['4', '.', '7',     '3', '.', '9',      '8', '.', '5'],
        ['.', '3', '.',     '.', '.', '.',      '.', '.', '.'],
        ['.', '.', '.',     '7', '.', '.',      '.', '.', '.'],
        
        ['.', '2', '.',     '.', '.', '.',      '.', '6', '.'],
        ['.', '.', '.',     '.', '8', '.',      '4', '.', '.'],
        ['.', '.', '.',     '.', '1', '.',      '.', '.', '.'],

        ['.', '.', '.',     '6', '.', '3',      '.', '7', '.'],
        ['5', '.', '.',     '2', '.', '.',      '.', '.', '.'],
        ['1', '.', '4',     '.', '.', '.',      '.', '.', '.']]

square_indx = [[(0,3),(0,3)],
               [(0,3),(3,6)],
               [(0,3),(6,9)],
               
               [(3,6),(0,3)],
               [(3,6),(3,6)],
               [(3,6),(6,9)],
               
               [(6,9),(0,3)],
               [(6,9),(3,6)],
               [(6,9),(6,9)]]

elements = ['1','2','3','4','5','6','7','8','9']

def get_squares(new_Grid):
    squares = []
    for i in range(0,9):
        square = {}
        for x in range(square_indx[i][0][0],square_indx[i][0][1]):
            for y in range(square_indx[i][1][0],square_indx[i][1][1]):
                square[(x,y)] = new_Grid[x][y]
        squares.append(square)
    return squares

def get_rows(new_Grid):
    rows = []
    ##    Put Your Code Here
        row = {}
        ##    Put Your Code Here
            ##    Put Your Code Here
        ##    Put Your Code Here
    return rows

def get_cols(new_Grid):
    cols = []
    for i in range(0,9):
        col = {}
        for x in range(0,9):
            col[(x,i)] = new_Grid[x][i]
        cols.append(col)
    return cols
    
def get_all_related_cells(new_Grid):
    ##    Put Your Code Here
    ##    Put Your Code Here
    ##    Put Your Code Here
    all_vec = squares + rows + cols
    return all_vec

def get_legal_for_cell(cell_r, cell_c, new_Grid):
    map = {}
    all_vec = get_all_related_cells(new_Grid)
    for a in all_vec:
        if (cell_r, cell_c) in a.keys():
            map.update(a)

    ##    Put Your Code Here
    ##    Put Your Code Here
        ##    Put Your Code Here
            ##    Put Your Code Here

    rest = list(set(elements) - set(exist))
    return rest

def get_legal_for_all(new_Grid):
    legal_for_all = {}
    for r in range(0,9):
        for c in range(0,9):
            if new_Grid[r][c]=='.':
                ##    Put Your Code Here
    return legal_for_all

def get_next_cell(new_Grid):
    ##    Put Your Code Here
    if len(legal_for_all)>0:
        ##    Put Your Code Here
    else:
        key=(None,None)     # only when grid completed
    return key

def is_complete(new_Grid):
    grid_complete = True
    for r in new_Grid:
        grid_complete = grid_complete and not ('.' in r)
    return grid_complete

def print_grid(new_Grid):
    for item in new_Grid:
        print item
    print

def solve_step_in_sudoko(last_Grid):
    if is_complete(last_Grid):
        print 'Complete:'
        print_grid(last_Grid)
        return 0
    ##    Put Your Code Here
    ##    Put Your Code Here

    for item in legal_for_cell:
        new_Grid = deepcopy(last_Grid)
        ##    Put Your Code Here
        ##    Put Your Code Here

solve_step_in_sudoko(Grid)
