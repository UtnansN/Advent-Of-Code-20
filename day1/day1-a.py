with open('input.txt') as f:
    inputs = f.read()

desired = 2020
diffSet = set()
for intStr in inputs.splitlines():
    num = int(intStr)
    diff = desired - num
    if diff in diffSet:
        print(num*diff)
        break
    else:
        diffSet.add(num)