with open('input.txt') as f:
    inputs = [int(x) for x in f.read().splitlines()]

preamble = inputs[:25]
for row in inputs[25:]:
    differences = [row - val for val in preamble]
    if not set(preamble) & set(differences):
        print(row)
        break
    preamble.append(row)
    preamble.pop(0)