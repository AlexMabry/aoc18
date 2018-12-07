import re
from collections import defaultdict

lines = list(map(lambda l: re.match('Step ([A-Z]).*([A-Z])', l).groups(), open('input.txt', 'r').readlines()))
steps = {letter: {p[0] for p in lines if p[1] == letter} for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

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
