with open('input.txt') as f:
    inputs = f.read()

def has_shiny_gold(coll):
    return 'shiny gold' in coll or any(has_shiny_gold(bagdict[key]) for key in coll)

bagdict = {}
for row in inputs.splitlines():
    key, values = row.split(' bags contain ')
    value_set = set()
    if values != 'no other bags.':
        for value in values.split(', '):
            _, colour = value.split(' ', 1)
            value_set.add(colour.rpartition(' ')[0])
    bagdict[key] = value_set
print(sum(has_shiny_gold(bagdict[key]) for key in bagdict))