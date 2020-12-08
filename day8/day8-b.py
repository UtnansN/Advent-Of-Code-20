with open('input.txt') as f:
    inputs = f.read().splitlines()

for i in range(len(inputs)):
    if inputs[i].startswith(('jmp', 'acc')):
        old_cmd, old_value = inputs[i].split(' ')
        inputs[i] = 'nop ' + old_value if old_cmd == 'jmp' else 'jmp ' + old_value

        pointer = 0
        visited = set()
        acc = 0
        fail = False
        while pointer < len(inputs):
            if pointer in visited:
                fail = True
                break
            cmd, value = inputs[pointer].split(' ')
            visited.add(pointer)

            if cmd == 'acc':
                acc += int(value)
            elif cmd == 'jmp':
                pointer += int(value)
                continue
            pointer += 1
        if not fail:
            print(acc)
            break
        inputs[i] = old_cmd + ' ' + old_value