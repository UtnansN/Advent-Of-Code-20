with open('input.txt') as f:
    inputs = [int(x) for x in f.read().strip().split(',')]

memory = {}
for idx, input in enumerate(inputs):
    memory[input] = idx + 1

spoken = inputs[-1]
for i in range(len(inputs), 30000000):
    try:
        prev_spoken = memory[spoken]
        memory[spoken] = i
        spoken = i - prev_spoken
    except KeyError:
        memory[spoken] = i
        spoken = 0
print(spoken)