def react(poly):
    unit = 0
    while unit <= len(poly) - 2:
        if abs(ord(poly[unit]) - ord(poly[unit + 1])) == 32:
            poly = poly[:unit] + poly[unit+2:]
            unit = unit if unit == 0 else unit-1
        else:
            unit += 1
    return poly


polymer = open('input.txt', 'r').readline()
print(len(react(polymer)))
