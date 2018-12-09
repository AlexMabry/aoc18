import re
from llist import dllist
import time
start_time = time.time()

players, last_marble = re.match('([0-9]+).* ([0-9]+)', open('input.txt', 'r').read()).groups()
score = [0 for _ in range(int(players))]
current_player = 0
circle = dllist([0])

for marble in range(1, int(last_marble)):
    if marble % 23 == 0:
        circle.rotate(7)
        score[current_player] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        print(circle)
        circle.append(marble)
        print(circle)

    current_player = (current_player + 1) % len(score)


print(max(score))
print("--- %s seconds ---" % (time.time() - start_time))