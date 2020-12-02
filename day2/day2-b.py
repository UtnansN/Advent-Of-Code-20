inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

# Works for arbitrary amount of policies in front of the colon
counter = 0
for line in inputs:
    (encoding, sequence) = line.split(':')

    policies = {}
    tokens = encoding.split(' ')
    
    for i in range(0, len(tokens), 2):
        (x, y) = tokens[i].split('-')
        token = tokens[i+1]
        
        policies.update({token: (int(x), int(y))})
    
    sequence = sequence.strip()
    
    validPolicy = [(sequence[policies[key][0]-1] == key) ^ (sequence[policies[key][1]-1] == key) for key in policies.keys()]

    if (all(validPolicy)):
        counter += 1

print(counter)