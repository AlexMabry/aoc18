import re

f = open('input.txt', 'r')
result = re.match('.* ([.#]+)', f.readline().strip())[1]
f.readline()
conditions = {g[0]: g[1] for g in [re.match('([.#]+) => ([.#])', l).groups() for l in f.readlines()]}


def generation(pots):
    return [conditions[pots[i:i + 5]] for i in range(len(pots) - 4)]


rounds = 4000
for gen in range(1, rounds+1, 1):
    result = result.join(['....', '....'])
    result = ''.join(generation(result))


answer = 0
for ix, char in enumerate(result):
    if char == '#':
        answer += ix - gen * 2
print(answer-rounds*91)
