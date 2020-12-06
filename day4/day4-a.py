with open('input.txt') as f:
    inputs = f.read()

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0

for pass_inputs in inputs.split('\n\n'):
    curr_passport = []
    for row in pass_inputs.splitlines():
        curr_passport.extend([y[0] for y in [x.split(':') for x in row.split(' ')]])
    valid += int(all([req in curr_passport for req in required]))
print(valid)