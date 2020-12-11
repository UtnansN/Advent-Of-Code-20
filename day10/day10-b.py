with open('input.txt') as f:
    inputs = [int(x) for x in f.readlines()]

inputs.sort()
inputs.insert(0, 0)
inputs.append(inputs[-1] + 3)
paths = [0, 0, 1]
for i in range(1, len(inputs)):
    subtotal = 0
    for j in range(1, 4):
        if i-j >= 0 and inputs[i] - inputs[i-j] > 3:
            break
        subtotal += paths[3-j]
    paths.pop(0)
    paths.append(subtotal)
print(paths[-1])