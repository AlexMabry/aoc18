rounds = 306281
circle = [3, 7]
elf1 = 0
elf2 = 1

while len(circle) < rounds + 10:
    circle.extend([int(c) for c in str(circle[elf1] + circle[elf2])])
    elf1 = (elf1 + circle[elf1] + 1) % len(circle)
    elf2 = (elf2 + circle[elf2] + 1) % len(circle)

print(''.join([str(c) for c in list(circle)[rounds:rounds+10]]))
