f = open('input1.txt', 'r')
lines = list(map(lambda n: int(n), f.readlines()))

total = sum(lines)
print(total)


