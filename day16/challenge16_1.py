import re
from collections import namedtuple, defaultdict

from day16.operations import *

Operation = namedtuple('Operation', ['opcode', 'a', 'b', 'output'])
Example = namedtuple('Example', ['before', 'after', 'operation'])

before, after, operation = None, None, None
examples = []
for line in [line.strip() for line in open('input.txt', 'r').readlines()]:
    if line.startswith('Before:'):
        before = [int(n) for n in re.match('.*\[([0-9]), ([0-9]), ([0-9]), ([0-9])\]', line).groups()]
    elif line.startswith('After:'):
        after = [int(n) for n in re.match('.*\[([0-9]), ([0-9]), ([0-9]), ([0-9])\]', line).groups()]
    elif line == '':
        examples.append(Example(before, after, operation))
    else:
        operation = Operation(*[int(n) for n in line.split(' ')])

funcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
scores = defaultdict(int)
for i, ex in enumerate(examples):
    for f in funcs:
        before = list(ex.before)
        if f(before, ex.operation.a, ex.operation.b, ex.operation.output) == ex.after:
            scores[i] += 1

print(len(list(filter(lambda s: s >= 3, scores.values()))))


