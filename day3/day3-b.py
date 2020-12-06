with open('input.txt') as f:
    inputs = f.read()
inputs = inputs.splitlines()

jumpconfigs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1
for config in jumpconfigs:
    counter = 0
    pos = config[0]
    for i in range(config[1], len(inputs), config[1]):
        counter += int(inputs[i][pos] == '#')
        pos = (pos + config[0]) % len(inputs[i])
    result *= counter
print(result)