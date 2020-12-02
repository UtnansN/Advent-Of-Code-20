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
        (low, high) = tokens[i].split('-')
        token = tokens[i+1]
        
        policies.update({token: [(int(low), int(high)), 0]})
    
    sequence = sequence.strip()
    
    over_expected = False
    for chr in sequence:
        if chr in policies:
            entry = policies.get(chr)
            entry[1] += 1
            if entry[1] > entry[0][1]:
                over_expected = True
                break

    if over_expected:
        continue
    
    valid = True
    for key in policies.keys():
        policy = policies.get(key)
        if policy[1] < policy[0][0]:
            valid = False
            break
    
    if valid:
        counter += 1

print(counter)