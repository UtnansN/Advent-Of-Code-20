with open('input.txt') as f:
    inputs = f.read().splitlines()

memory = {}
mask = ''
X_indices = []
for line in inputs:
    left, right = line.split(' = ')
    if left == 'mask':
        mask = right
        X_indices = [idx for idx, v in enumerate(mask) if v == 'X']
    else:
        addr = list(bin(int(left[4:-1]))[2:].rjust(36,'0'))
        for i in range(len(mask)):
            if mask[i] != '0':
                addr[i] = mask[i]

        for j in range(2**mask.count('X')):
            current_binary = bin(j)[2:].rjust(len(X_indices), '0')
            for i, idx in enumerate(X_indices):
                addr[idx] = current_binary[i]
            memory[int(''.join(addr), 2)] = int(right)
print(sum(memory.values()))