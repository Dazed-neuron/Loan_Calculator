
# Start by reading the coordinates of the king from the input.
x = int(input())
y = int(input())


def count_possible_moves(x, y):

    possible_moves = 0

    if x in range(2, 9):
        # print('left')
        possible_moves += 1

    if x in range(1, 8):
        # print('right')
        possible_moves += 1

    if y in range(2, 9):
        # print('down')
        possible_moves += 1

    if y in range(1, 8):
        # print('up')
        possible_moves += 1

    if x in range(2, 9) and y in range(1, 8):
        # print('left up')
        possible_moves += 1

    if x in range(2, 9) and y in range(2, 9):
        # print('left down')
        possible_moves += 1

    if x in range(1, 8) and y in range(1, 8):
        # print('right up')
        possible_moves += 1

    if x in range(1, 8) and y in range(2, 9):
        # print('right down')
        possible_moves += 1

    return possible_moves

print(count_possible_moves(x, y))