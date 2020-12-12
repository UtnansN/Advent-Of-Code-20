with open('input.txt') as f:
    inputs = [(row[0], int(row[1:])) for row in f.readlines()]

x, y = (0, 0)
directions = ['N', 'E', 'S', 'W']
face = 1
for cmd, arg in inputs:
    if cmd == 'F':
        cmd = directions[face]
    x += arg * ((cmd == 'E') - (cmd == 'W'))
    y += arg * ((cmd == 'N') - (cmd == 'S'))
    if cmd == 'L':
        face = int((face - (arg / 90)) % 4)
    elif cmd == 'R':
        face = int((face + (arg / 90)) % 4)
print(abs(x) + abs(y))