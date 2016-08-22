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

def path_to_word(grid, path):
    return ''.join([grid[p] for p in path])

def is_a_real_word(word, dictionary):
    return word in dictionary

def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary

    def do_search(path):
        word = path_to_word(grid, path)
        if is_a_real_word(word, full_words):
            paths.append(path)
            # print path
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]: # neighbours of last position in path

            if next_pos not in path:
                do_search(path + [next_pos])

    for position in grid:
        # print 'next position in grid'
        do_search([position])

    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)

def get_dictionary(dictionary_file):
    full_words, stems = set(), set()

    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)

            for i in range(1, len(word)):
                stems.add(word[:i])

    return full_words, stems

def words_display(words):
    for word in words:
        print word
    print "Found {0} words".format((len(words)))

def main(grid_size):
    grid = make_grid(grid_size, grid_size)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    words_display(words)

main(100)




# print all_grid_neighbours(make_grid(2, 2))
# grid = make_grid(2, 2)
# print grid
# neighbours = all_grid_neighbours(grid)
# print neighbours
# print path_to_word(grid, [(0, 0), (1, 1), (1, 0), (0, 1)])

