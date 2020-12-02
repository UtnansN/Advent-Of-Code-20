inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(int(line))

desired = 2020

for i in range(len(inputs)):
    diffSet = set()
    for j in range(i, len(inputs)):
        x = inputs[i]
        y = inputs[j]
        diff = desired - x - y
        if diff in diffSet:
            print('Answer: ' + str(x * y * diff))
            exit()
        else:
            diffSet.add(y)

print('No answer found')