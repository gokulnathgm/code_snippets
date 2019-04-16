N = 5
queens = []
solved = False
current_position = [-1] * N

for i in range(N):
    rows = []
    for j in range(N):
        rows.append(0)
    queens.append(rows)

def print_queens():
    print 'Queens:' 
    for i in range(N):
        print queens[i]
    print '\nQueen positions in each column: \n', current_position

def is_position_safe(row, column):
    pos_sum = row + column
    pos_diff = row - column

    for i in range(N):
        for j in range(column):
            if i == row:
                if queens[i][j] == 1:
                    return False
            if i + j == pos_sum:
                if queens[i][j] == 1:
                    return False
            if i - j == pos_diff:
                if queens[i][j] == 1:
                    return False
    return True

def safe_position(index, column):
    for pos in range(index+1, N):
        if column == 0:
            current_position[column] = pos
            queens[pos][column] = 1
            return pos

        is_safe = is_position_safe(pos, column)
        if is_safe:
            current_position[column] = pos
            queens[pos][column] = 1
            return pos

    remove_pos = current_position[column-1]
    queens[remove_pos][column-1] = 0
    current_position[column] = -1
    return -1

column = 0
while True:
    for i in range(column, N):
        index_position = safe_position(current_position[column], column)
        if index_position != -1:
            column += 1
        else:
            column -= 1
            break
        if column == N:
            solved = True
            break
    if solved:
        break
    if column < 0:
        print 'No possible solution!'
        break
print_queens()