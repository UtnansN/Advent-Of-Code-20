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
        groups.update([c for c in row])

if len(groups) > 0:
    sum += len(groups)
print(sum)