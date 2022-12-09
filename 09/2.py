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

def get_direction(front: tuple[int, int], back: tuple[int, int]) -> str:
    if front[0] == back[0] and front[1] > back[1]:
        return 'U'
    if front[0] == back[0] and front[1] < back[1]:
        return 'D'
    if front[0] > back[0] and front[1] == back[1]:
        return 'R'
    if front[0] < back[0] and front[1] == back[1]:
        return 'L'
    if front[0] > back[0] and front[1] > back[1]:
        return 'UR'
    if front[0] < back[0] and front[1] > back[1]:
        return 'UL'
    if front[0] > back[0] and front[1] < back[1]:
        return 'DR'
    if front[0] < back[0] and front[1] < back[1]:
        return 'DL'
    raise Exception(f'Wrong direction! {front} {back}')

def follow(front: tuple[int, int], back: tuple[int, int]) -> tuple[int, int]:
    return back if front in near_cells(back) else move(back, get_direction(front, back))

rope = [(0, 0) for _ in range(10)]
tail_visited = {(0, 0)}

for head_direction, count in moves:
    for _ in range(count):
        rope[0] = move(rope[0], head_direction)
        for i in range(1, len(rope)):
            front = rope[i - 1]
            back = rope[i]
            rope[i] = follow(front, back)
        tail_visited.add(rope[-1])

print(len(tail_visited))
