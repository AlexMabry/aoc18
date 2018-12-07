import re

answer = ''
lines = list(map(lambda l: re.match('Step ([A-Z]).*([A-Z])', l).groups(), open('input.txt', 'r').readlines()))
preconditions = {step: {p[0] for p in lines if p[1] == step} for step in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
while preconditions:
    answer += sorted(filter(lambda pair: len(pair[1]) == 0, preconditions.items()))[0][0]
    preconditions = {step: cond.difference(answer[-1]) for step, cond in preconditions.items() if step != answer[-1]}

print(answer)
