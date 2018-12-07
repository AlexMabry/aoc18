import re
from collections import defaultdict

lines = map(lambda l: re.match('Step ([A-Z]).*([A-Z])', l).groups(), open('input.txt', 'r').readlines())
steps = defaultdict(set)
for l in lines:
    steps[l[1]].add(l[0])
    steps[l[0]] = steps[l[0]]

answer = ''
while len(steps):
    next_step = sorted(filter(lambda pair: len(pair[1]) == 0, steps.items()))[0][0]
    steps = {step: cond.difference(next_step) for step, cond in steps.items() if step != next_step}
    answer += next_step

print(answer)
