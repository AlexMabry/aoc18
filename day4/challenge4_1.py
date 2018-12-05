import re
from collections import defaultdict
from dateutil import parser

f = open('input.txt', 'r')
lines = f.readlines()
lines.sort()


def process_lines(line):
    m = re.match('\[(?P<time>.*)\] (?P<event>.*)', line)
    return parser.parse(m['time']), m['event']


guard_naps = defaultdict(list)
for time, event in map(process_lines, lines):
    if event.startswith('Guard'):
        guard = re.match('Guard #([0-9]+)', event)[1]
    elif event == 'falls asleep':
        start = time.minute
    elif event == 'wakes up':
        end = time.minute
        guard_naps[guard].extend([x for x in range(start, end, 1)])

sleepiest = max(guard_naps.items(), key=lambda item: len(item[1]))[0]
minute_freq = {minute: guard_naps[sleepiest].count(minute) for minute in set(guard_naps[sleepiest])}
most_minute = max(minute_freq.items(), key=lambda item: item[1])[0]

print(int(sleepiest) * int(most_minute))
