from itertools import count
from pprint import pprint


input_file = open('./08/input.txt', 'r')
lines = [line.strip() for line in input_file.readlines() if line.strip()]

trees: list[list[dict]] = []
for line in lines:
    trees.append([{'level': int(tree), 'visible': False} for tree in line])

def look(trees: list[list[dict]]) -> None:
    for line in trees:
        current_level = -1
        for tree in line:
            if tree['level'] > current_level:
                current_level = tree['level']
                tree['visible'] = True

look(trees)
for line in trees:
    line.reverse()
look(trees)
trees = [list(line) for line in zip(*trees)]
look(trees)
for line in trees:
    line.reverse()
look(trees)

counts = [len(list(filter(lambda tree: tree['visible'], line))) for line in trees]
visible_count = sum(counts)
print(visible_count)
