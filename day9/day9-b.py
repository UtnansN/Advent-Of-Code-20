with open('input.txt') as f:
    inputs = [int(x) for x in f.read().splitlines()]

summable = 0
preamble = inputs[:25]
for row in inputs[25:]:
    differences = [row - val for val in preamble]
    if not set(preamble) & set(differences):
        summable = row
        break
    preamble.append(row)
    preamble.pop(0)

# Brute force solution for now
for i in range(len(inputs)):
    for chunk_size in range(2, len(inputs) - i):
        total = sum(inputs[i:i+chunk_size])
        if total > summable:
            break
        if total == summable:
            print(max(inputs[i:i+chunk_size]) + min(inputs[i:i+chunk_size]))
            quit()