inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0

curr_passport = []
for row in inputs:
    if row == '':
        if all([req in curr_passport for req in required]):
            valid += 1
        curr_passport.clear()
    else:
        curr_passport.extend([y[0] for y in [x.split(':') for x in row.split(' ')]])

# Just for the last row
if len(curr_passport > 0):
    if all([req in curr_passport for req in required]):
        valid += 1

print(valid)