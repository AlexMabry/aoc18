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
possible_opcodes = defaultdict(set)
for i, ex in enumerate(examples):
    for f in funcs:
        before = list(ex.before)
        if f(before, ex.operation.a, ex.operation.b, ex.operation.output) == ex.after:
            possible_opcodes[f.__name__].add(ex.operation.opcode)

opcodes = {}
known = [oc for oc, pos in possible_opcodes.items() if len(pos) == 1]
while known:
    func = known.pop()
    code = possible_opcodes[func].pop()
    opcodes[code] = func
    del possible_opcodes[func]
    possible_opcodes = {oc: st.difference([code]) for oc, st in possible_opcodes.items()}
    known = [oc for oc, pos in possible_opcodes.items() if len(pos) == 1]

lines = [line.strip() for line in open('sample.txt', 'r').readlines()]
code = [Operation(*[int(n) for n in line.split(' ')]) for line in lines]

before = [0, 0, 0, 0]
for loc in code:
    eval(opcodes[loc.opcode])(before, loc.a, loc.b, loc.output)

print(before[0])
