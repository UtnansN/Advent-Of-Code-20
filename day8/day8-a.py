with open('input.txt') as f:
    inputs = f.read().splitlines()

pointer = 0
visited = set()
acc = 0
while True:
    if pointer in visited:
        break
    cmd, value = inputs[pointer].split(' ')
    visited.add(pointer)

    if cmd == 'acc':
        acc += int(value)
    elif cmd == 'jmp':
        pointer += int(value)
        continue
    pointer += 1
print(acc)