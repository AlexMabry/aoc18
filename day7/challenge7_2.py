import re
from collections import defaultdict

lines = map(lambda l: re.match('Step ([A-Z]).*([A-Z])', l).groups(), open('input.txt', 'r').readlines())
steps = defaultdict(set)
for l in lines:
    steps[l[1]].add(l[0])
    steps[l[0]] = steps[l[0]]

seconds = 0
workers = [0 for r in range(5)]
step_complete = defaultdict(set)
while len(steps) or len(step_complete):
    if seconds in step_complete:
        steps = {step: cond.difference(step_complete[seconds]) for step, cond in steps.items()}
        del step_complete[seconds]

    for next_step in [s[0] for s in sorted(filter(lambda pair: len(pair[1]) == 0, steps.items()))]:
        for ix, w in enumerate(workers):
            if w <= seconds:
                workers[ix] = seconds + 60 + ord(next_step) - 64
                step_complete[workers[ix]].add(next_step)
                del steps[next_step]
                break

    seconds += 1

print(seconds-1)
