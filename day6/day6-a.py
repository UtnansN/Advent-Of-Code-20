inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

sum = 0
groups = set()
for row in inputs:
    if row == '':
        sum += len(groups)
        groups.clear()
    else:
        for c in row:
            groups.add(c)

if len(groups) > 0:
    sum += len(groups)
print(sum)