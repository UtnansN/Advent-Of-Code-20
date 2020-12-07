with open('input.txt') as f:
    inputs = f.read()

def count_bags(mappings):
    return sum(mappings[key] * (count_bags(bagdict[key]) + 1) for key in mappings)

bagdict = {}
for row in inputs.splitlines():
    key, values = row.split(' bags contain ')
    value_dict = {}
    if values != 'no other bags.':
        for value in values.split(', '):
            amount, colour = value.split(' ', 1)
            value_dict.update({colour.rpartition(' ')[0]: int(amount)})
    bagdict[key] = value_dict
print(count_bags(bagdict['shiny gold']))