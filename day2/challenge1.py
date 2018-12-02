f = open('input.txt', 'r')
lines = f.readlines()

counts = list(map(lambda line: dict((letter, line.count(letter)) for letter in set(line)), lines))
twos = len(list(filter(lambda count: 2 in count.values(), counts)))
threes = len(list(filter(lambda count: 3 in count.values(), counts)))
print(twos * threes)
