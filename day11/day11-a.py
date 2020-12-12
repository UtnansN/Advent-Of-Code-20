from copy import deepcopy
with open('input.txt') as f:
    inputs = f.read().splitlines()

prox = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def count_proximity(i, j):
    return sum((0 <= i+a < len(seats)) and (0 <= j+b < len(seats[i+a])) and (seats[i+a][j+b] == '#') for a, b in prox)

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
                elif seats[row][col] == '#' and neighbors >= 4:
                    new_seats[row][col] = 'L'
                    changes = True
    seats = new_seats
print(sum(sum(seat == '#' for seat in row) for row in seats))