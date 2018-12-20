import re
from collections import namedtuple

from day16.operations import *

Operation = namedtuple('Operation', ['code', 'a', 'b', 'output'])

operations = []
lines = open('input.txt', 'r').readlines()
ir = int(re.match('#ip ([0-9])', lines[0].strip()).groups()[0])
for op in [re.match('([a-z]+) ([0-9]+) ([0-9]+) ([0-9])', line.strip()).groups() for line in lines[1:]]:
    operations.append(Operation(op[0], int(op[1]), int(op[2]), int(op[3])))

count = 0
registers = [1, 0,  0, 0, 0, 0]
while registers[ir] < len(operations) and count < 17:
    op = operations[registers[ir]]
    eval(op.code)(registers, op.a, op.b, op.output)
    registers[ir] += 1
    count += 1

number = registers[3]
factors = [i for i in range(1, number + 1) if number % i == 0]

print(sum(factors))

