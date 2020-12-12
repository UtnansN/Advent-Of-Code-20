import math

with open('input.txt') as f:
    inputs = [(row[0], int(row[1:])) for row in f.readlines()]

x, y = (0, 0)
wp_x, wp_y = (10, 1)
for cmd, arg in inputs:
    if cmd == 'F':
        x, y = (x + arg * wp_x, y + arg * wp_y)
    elif cmd in {'L', 'R'}:
        rads = math.radians(arg)
        wp_x, wp_y = (
            round(math.cos(rads) * wp_x + (1 if cmd == 'R' else -1) * math.sin(rads) * wp_y), 
            round((-1 if cmd == 'R' else 1) * math.sin(rads) * wp_x + math.cos(rads) * wp_y))
    else:
        wp_x += arg * ((cmd == 'E') - (cmd == 'W'))
        wp_y += arg * ((cmd == 'N') - (cmd == 'S'))
print(abs(x) + abs(y))