import re

inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)


def validate(passport):
    rules = [
    ('byr', lambda x: 1920 <= int(x) <= 2002), 
    ('iyr', lambda x: 2010 <= int(x) <= 2020), 
    ('eyr', lambda x: 2020 <= int(x) <= 2030), 
    ('hgt', lambda x: 150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' else 59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else False), 
    ('hcl', lambda x: re.match(r'^#[0-9a-f]{6}$', x)), 
    ('ecl', lambda x: x in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])), 
    ('pid', lambda x: re.match(r'^[0-9]{9}$', x))]

    try:
        for param, check in rules:
            param_value = passport[param]
            if not check(param_value):
                return False
    except:
        return False
    return True

valid = 0
curr_passport = {}
for row in inputs:
    if row == '':
        if validate(curr_passport):
            valid += 1
        curr_passport.clear()
    else:
        params = [(y[0], y[1]) for y in [x.split(':') for x in row.split(' ')]]
        curr_passport.update(params)

# Just for the last row
if len(curr_passport.keys()) > 0:
    if validate(curr_passport):
        valid += 1

print(valid)