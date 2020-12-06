with open('input.txt') as f:
    inputs = f.read()

counter = 0
for line in inputs.splitlines():
    encoding, sequence = line.split(': ')
    positions, character = encoding.split(' ')
    pos1, pos2 = positions.split("-")
    counter += int((sequence[int(pos1)-1] == character) ^ ((sequence[int(pos2)-1] == character)))
print(counter)