with open('input.txt') as f:
    inputs = f.read()

sum = 0
for group in inputs.split('\n\n'):
    answer_set = None
    for row in group.splitlines():
        if answer_set is not None:
            answer_set &= set(row)
        else:
            answer_set = set(row)
    sum += len(answer_set)
print(sum)