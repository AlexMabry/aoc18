f = open('input1.txt', 'r')
lines = list(map(lambda n: int(n), f.readlines()))

total = 0
results = set()
while True:
    for num in lines:
        total += num

        if total in results:
            print(total)
            exit()
        else:
            results.add(total)
