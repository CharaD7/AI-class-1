from copy import deepcopy

Grid = [['.', '.', '2', '3'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['3', '4', '.', '.']]

square_indx = [[(0,2),(0,2)],
               [(0,2),(2,4)],
               [(2,4),(0,2)],
               [(2,4),(2,4)]]

elements = ['1','2','3','4']

def get_squares(new_Grid):
    squares = []
    for i in range(0,4):
        square = {}
        for x in range(square_indx[i][0][0],square_indx[i][0][1]):
            for y in range(square_indx[i][1][0],square_indx[i][1][1]):
                square[(x,y)] = new_Grid[x][y]
        squares.append(square)
    return squares

def get_rows(new_Grid):
    rows = []
    for i in range(0,4):
        row = {}
        for y in range(0,4):
            row[(i,y)] = new_Grid[i][y]
        rows.append(row)
    return rows

def get_cols(new_Grid):
    cols = []
    for i in range(0,4):
        col = {}
        for x in range(0,4):
            col[(x,i)] = new_Grid[x][i]
        cols.append(col)
    return cols
    
def get_all_related_cells(new_Grid):
    squares = get_squares(new_Grid)
    rows = get_rows(new_Grid)
    cols = get_cols(new_Grid)
    all_vec = squares + rows + cols
    return all_vec
    
def get_legal_for_cell(cell_r, cell_c, new_Grid):
    if new_Grid[cell_r][cell_c]!='.':
        return [None]

    map = {}
    all_vec = get_all_related_cells(new_Grid)
    for a in all_vec:
        if (cell_r, cell_c) in a.keys():
            map.update(a)          # no duplicates      # print a

    exist = []
    for m in map:                  # get key from keys
        if not map[m]=='.':
            exist.append(map[m])

    rest = list(set(elements) - set(exist))
    return rest

def get_new_r_c(r, c):
    if c==3:
        if r==3:
            new_r = r
            new_c = c
        else:
            new_c = 0
            new_r = r+1
    else:
        new_r = r
        new_c = c+1
    return new_r, new_c

def is_complete(new_Grid):
    grid_complete = True
    for r in new_Grid:
        grid_complete = grid_complete and not ('.' in r)
    return grid_complete

def print_grid(new_Grid):
    for item in new_Grid:
        print item
    print

def solve_step_in_sudoko(last_Grid, r, c):
    if is_complete(last_Grid):
        print 'Complete:'
        print_grid(last_Grid)
        return 0
##    print_grid(last_Grid)
    legal_for_cell = get_legal_for_cell(r, c, last_Grid)

    for item in legal_for_cell:
        new_Grid = deepcopy(last_Grid)
        if last_Grid[r][c]=='.':
            new_Grid[r][c] = item
        new_r, new_c = get_new_r_c(r, c)

        solve_step_in_sudoko(new_Grid, new_r, new_c)

solve_step_in_sudoko(Grid, 0, 0)
