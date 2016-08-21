from string import ascii_uppercase
from random import choice

def check():
    return 1

def make_grid(width, height):
    return {(row, col): choice(ascii_uppercase)
                for row in range(height)
                for col in range(width)}

def neighbours_of_position((row, col)):
    return [ (row - 1, col - 1), (row - 1, col), (row - 1, col +1),
             (row, col - 1),                     (row, col + 1),
             (row + 1, col - 1), (row + 1, col), (row +1, col +1)]

def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

def path_to_word(selfgrid, path):
    return ''.join([grid[p] for p in path])

#grid = make_grid(2, 2)
#print path_to_word(grid, [(0, 0), (1, 1), (1, 0), (0, 1)])

# print all_grid_neighbours(make_grid(2, 2))
