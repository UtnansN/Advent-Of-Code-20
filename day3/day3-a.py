with open('input.txt') as f:
    inputs = f.read()

counter = 0
pos = 3
for line in inputs.splitlines()[1:]:
    counter += int(line[pos] == '#')
    pos = (pos + 3) % len(line)
print(counter)