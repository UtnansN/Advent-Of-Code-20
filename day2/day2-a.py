with open('input.txt') as f:
    inputs = f.read()

counter = 0
for line in inputs.splitlines():
    encoding, sequence = line.split(': ')
    range, character = encoding.split(' ')
    low, high = range.split("-")
    appearances = sequence.count(character)
    counter += int(int(low) <= appearances <= int(high))
print(counter)