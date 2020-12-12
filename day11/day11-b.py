from copy import deepcopy
with open('input.txt') as f:
    inputs = f.read().splitlines()

prox = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def rangenerator(x_start, y_start, x_stop, y_stop, x_step, y_step):
    x = x_start
    y = y_start
    while (0 <= x < x_stop) and (0 <= y < y_stop):
        pos = seats[x][y]
        if pos == '.':
            yield False
        elif pos == '#':
            yield True
        else:
            yield False
            break
        x += x_step
        y += y_step

def count_proximity(i, j):
    return sum(any(x for x in rangenerator(i+a, j+b, len(seats), len(seats[i]), a, b)) for a, b in prox)

seats = [list(row) for row in inputs]
changes = True
while changes:
    new_seats = deepcopy(seats)
    changes = False
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] != '.':
                neighbors = count_proximity(row, col)
                if seats[row][col] == 'L' and neighbors == 0:
                    new_seats[row][col] = '#'
                    changes = True
                elif seats[row][col] == '#' and neighbors >= 5:
                    new_seats[row][col] = 'L'
                    changes = True
    seats = new_seats
print(sum(sum(seat == '#' for seat in row) for row in seats))