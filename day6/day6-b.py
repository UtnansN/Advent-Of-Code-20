inputs = []
print('Paste inputs, Ctrl-Z or Ctrl-D to proceed')
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

sum = 0
answer_set = set()
initial_values_set = False
for row in inputs:
    if row == '':
        sum += len(answer_set)
        answer_set.clear()
        initial_values_set = False
    else:
        member_answers = set([c for c in row])

        if initial_values_set:
            answer_set.intersection_update(member_answers)
        else:
            answer_set.update(member_answers)
            initial_values_set = True

if len(answer_set) > 0:
    sum += len(answer_set)
print(sum)