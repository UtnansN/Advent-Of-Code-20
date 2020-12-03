inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

jumpconfigs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1

for config in jumpconfigs:
    counter = 0
    pos = config[0]
    for i in range(config[1], len(inputs), config[1]):
        if inputs[i][pos] == '#':
            counter += 1
        pos = (pos + config[0]) % len(inputs[i])
    result *= counter

print(result)