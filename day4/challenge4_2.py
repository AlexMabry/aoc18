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

guard_common_minutes = {guard: max(set(naps), key=naps.count) for guard, naps in guard_naps.items()}
guard_count_minutes = {guard: naps.count(guard_common_minutes[guard]) for guard, naps in guard_naps.items()}
common_guard = max(guard_count_minutes.items(), key=lambda item: item[1])[0]

print(int(common_guard) * int(guard_common_minutes[common_guard]))
