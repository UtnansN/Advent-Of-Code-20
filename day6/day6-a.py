with open('input.txt') as f:
    inputs = f.read()

sum = 0
for group in inputs.split('\n\n'):
    answer_set = set()
    for row in group.splitlines():
        answer_set |= set(row)
    sum += len(answer_set)
print(sum)