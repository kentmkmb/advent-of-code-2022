input_file = open('./09/input.txt', 'r')
lines = [line.strip().split(' ') for line in input_file.readlines() if line.strip()]

moves = [(d, int(n)) for d, n in lines]

directions = {
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
    'UR': (1, 1),
    'UL': (-1, 1),
    'DR': (1, -1),
    'DL': (-1, -1),
}
def move(point: tuple[int, int], direction: str) -> tuple[int, int]:
    mv = directions[direction]
    return point[0] + mv[0], point[1] + mv[1]

def near_cells(point: tuple[int, int]) -> list[tuple[int, int]]:
    result = [move(point, direction) for direction in directions]
    result.append(point)
    return result

def get_direction(head: tuple[int, int], tail: tuple[int, int]) -> str:
    if head[0] == tail[0] and head[1] > tail[1]:
        return 'U'
    if head[0] == tail[0] and head[1] < tail[1]:
        return 'D'
    if head[0] > tail[0] and head[1] == tail[1]:
        return 'R'
    if head[0] < tail[0] and head[1] == tail[1]:
        return 'L'
    if head[0] > tail[0] and head[1] > tail[1]:
        return 'UR'
    if head[0] < tail[0] and head[1] > tail[1]:
        return 'UL'
    if head[0] > tail[0] and head[1] < tail[1]:
        return 'DR'
    if head[0] < tail[0] and head[1] < tail[1]:
        return 'DL'
    raise Exception(f'Wrong direction! {head} {tail}')

head = (0, 0)
tail = (0, 0)
tail_visited = {tail}

for head_direction, count in moves:
    for i in range(count):
        head = move(head, head_direction)
        if not head in near_cells(tail):
            tail_direction = get_direction(head, tail)
            tail = move(tail, tail_direction)
        tail_visited.add(tail)

print(len(tail_visited))
