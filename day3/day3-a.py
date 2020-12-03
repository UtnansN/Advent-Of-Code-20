inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

counter = 0
pos = 3
for i in range(1, len(inputs)):
    if inputs[i][pos] == '#':
        counter += 1
    pos = (pos + 3) % len(inputs[i])

print(counter)