import operator
import re
from collections import defaultdict
from dateutil import parser

f = open('input.txt', 'r')
lines = f.readlines()


def key_with_max_value(d):
    return max(d.items(), key=operator.itemgetter(1))[0]


def most_freq_element(lst):
    return max(set(lst), key=lst.count)


def process_lines(line):
    m = re.match('\[(?P<time>.*)\] (?P<event>.*)', line)
    return parser.parse(m['time']), m['event']


processed = list(map(process_lines, lines))
processed.sort()

guards = defaultdict(list)
for time, event in processed:
    if event.startswith('Guard'):
        guard = re.match('Guard #([0-9]+).*', event)[1]
    elif event == 'falls asleep':
        start = time.minute
    elif event == 'wakes up':
        end = time.minute
        guards[guard].extend([x for x in range(start, end, 1)])

guard_max_min = {guard: naps.count(most_freq_element(naps)) for guard, naps in guards.items()}
common_guard = key_with_max_value(guard_max_min)
common_minute = most_freq_element(guards[common_guard])

print(int(common_guard) * int(common_minute))
