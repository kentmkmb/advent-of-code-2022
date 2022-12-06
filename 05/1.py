from pprint import pprint
import re


file = open('./input.txt', 'r')
STACKS_COUNT = 9

rows = []

while line := file.readline().replace('\n', ''):
    if re.match(r'.*\d.*', line):
        continue
    line += ' ' * (STACKS_COUNT * 4 - len(line))
    line = re.sub(r'\[(\w)\] ', r'\1', line)
    line = re.sub(' ' * 4, '-', line)
    rows.append(line)

rows.reverse()
stacks = {}

def filtration(s: str) -> bool:
    return s != '-'

for i, crates in enumerate(list(zip(*rows)), 1):
    stacks[i] = list(filter(filtration, crates))


for line in file.readlines():
    line = line.strip()
    line = re.sub(r'^move (\d+) from (\d+) to (\d+)$', r'\1,\2,\3', line)
    count, frm, to = map(int, line.split(','))
    for i in range(count):
        stacks[to].append(stacks[frm].pop())

result = []
for stack in stacks.values():
    result.append(stack[-1])
print(''.join(result))
