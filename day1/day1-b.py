with open('input.txt') as f:
    inputs = f.read()
inputs = inputs.splitlines()

desired = 2020
for i in range(len(inputs)):
    diffSet = set()
    for j in range(i, len(inputs)):
        x = int(inputs[i])
        y = int(inputs[j])
        diff = desired - x - y
        if diff in diffSet:
            print(x * y * diff)
            exit()
        else:
            diffSet.add(y)