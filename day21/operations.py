# addr (add register) stores into register C the result of adding register A and register B.
def addr(regs, a, b, out):
    regs[out] = regs[a] + regs[b]
    return regs


# addi (add immediate) stores into register C the result of adding register A and value B.
def addi(regs, a, b, out):
    regs[out] = regs[a] + b
    return regs


# mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(regs, a, b, out):
    regs[out] = regs[a] * regs[b]
    return regs


# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(regs, a, b, out):
    regs[out] = regs[a] * b
    return regs


# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(regs, a, b, out):
    regs[out] = regs[a] & regs[b]
    return regs


# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(regs, a, b, out):
    regs[out] = regs[a] & b
    return regs


# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(regs, a, b, out):
    regs[out] = regs[a] | regs[b]
    return regs


# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(regs, a, b, out):
    regs[out] = regs[a] | b
    return regs


# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(regs, a, _, out):
    regs[out] = regs[a]
    return regs


# seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(regs, a, _, out):
    regs[out] = a
    return regs


# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B.
# Otherwise, register C is set to 0.
def gtir(regs, a, b, out):
    regs[out] = 1 if a > regs[b] else 0
    return regs


# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B.
# Otherwise, register C is set to 0.
def gtri(regs, a, b, out):
    regs[out] = 1 if regs[a] > b else 0
    return regs


# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B.
# Otherwise, register C is set to 0.
def gtrr(regs, a, b, out):
    regs[out] = 1 if regs[a] > regs[b] else 0
    return regs


# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B.
# Otherwise, register C is set to 0.
def eqir(regs, a, b, out):
    regs[out] = 1 if a == regs[b] else 0
    return regs


# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B.
# Otherwise, register C is set to 0.
def eqri(regs, a, b, out):
    regs[out] = 1 if regs[a] == b else 0
    return regs


# eqrr (equal register/register) sets register C to 1 if register A is equal to register B.
# Otherwise, register C is set to 0.
def eqrr(regs, a, b, out):
    regs[out] = 1 if regs[a] == regs[b] else 0
    return regs
