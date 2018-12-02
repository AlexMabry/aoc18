f = open('input.txt', 'r')
lines = f.readlines()

for first in lines:
    for second in lines:
        result = [f if f == s else '' for f, s in zip(first, second)]
        if abs(len(result) - len(first)) == 1:
            print(''.join(result))
            exit()
