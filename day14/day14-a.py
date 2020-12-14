with open('input.txt') as f:
    inputs = f.read().splitlines()

memory = {}
mask = {}
for line in inputs:
    left, right = line.split(' = ')
    if left == 'mask':
        mask = {idx:ch for idx, ch in enumerate(right) if ch != 'X'}
    else:
        binary = list(bin(int(right))[2:].rjust(36,'0'))
        for key in mask:
            binary[key] = mask[key]
        memory[int(left[4:-1])] = int(''.join(binary), 2)
print(sum(memory.values()))