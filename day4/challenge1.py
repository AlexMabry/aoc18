import operator
import re
from collections import defaultdict
from dateutil import parser

f = open('input.txt', 'r')
lines = f.readlines()


def key_with_max_value(d):
    return max(d.items(), key=operator.itemgetter(1))[0]


def process_lines(line):
    m = re.match('\[(?P<time>.*)\] (?P<event>.*)', line)
    return parser.parse(m['time']), m['event']


processed = list(map(process_lines, lines))
processed.sort()

guard_naps = defaultdict(list)
for time, event in processed:
    if event.startswith('Guard'):
        guard = re.match('Guard #([0-9]+).*', event)[1]
    elif event == 'falls asleep':
        start = time.minute
    elif event == 'wakes up':
        end = time.minute
        guard_naps[guard].extend([x for x in range(start, end, 1)])

nap_lengths = {guard: len(naps) for guard, naps in guard_naps.items()}
sleepiest = key_with_max_value(nap_lengths)
minute_freq = dict((minute, guard_naps[sleepiest].count(minute)) for minute in set(guard_naps[sleepiest]))
most_minute = key_with_max_value(minute_freq)

print(int(sleepiest) * int(most_minute))
