from pprint import pprint


input_file = open('./08/input.txt', 'r')
lines = [line.strip() for line in input_file.readlines() if line.strip()]

trees: list[list[int]] = []
for line in lines:
    trees.append([int(tree) for tree in line])

def look(spot: int, trees: list[int]) -> int:
    count = 0
    for tree in trees:
        count += 1
        if tree >= spot:
            break
    return count

def right(x: int, y: int):
    result = trees[y][x + 1:]
    return result

def left(x: int, y: int):
    result = trees[y][:x]
    result.reverse()
    return result

def up(x: int, y: int):
    result = [line[x] for line in trees[:y]]
    result.reverse()
    return result

def down(x: int, y: int):
    result = [line[x] for line in trees[y + 1:]]
    return result

max_score = 0

for y, line in enumerate(trees):
    for x, tree in enumerate(line):
        up_line, right_line, down_line, left_line = up(x, y), right(x, y), down(x, y), left(x, y)
        look_up, look_right, look_down, look_left = look(tree, up_line), look(tree, right_line), look(tree, down_line), look(tree, left_line)
        score = look_up * look_right * look_down * look_left
        max_score = max(max_score, score)

print(max_score)
