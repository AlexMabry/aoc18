puzzle_input = '306281'
circle = '37'
elf1 = 0
elf2 = 1

found = -1
while found < 0:
    circle += str(int(circle[elf1]) + int(circle[elf2]))
    elf1 = (elf1 + int(circle[elf1]) + 1) % len(circle)
    elf2 = (elf2 + int(circle[elf2]) + 1) % len(circle)
    found = circle.find(puzzle_input, len(circle)-len(puzzle_input)-2, len(circle))

print(found)
