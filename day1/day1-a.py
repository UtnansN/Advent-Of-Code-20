inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

desired = 2020
diffSet = set()

for intStr in inputs:
    num = int(intStr)
    diff = desired - num
    if diff in diffSet:
        print('Answer: ' + str(num*diff))
        break
    else:
        diffSet.add(num)