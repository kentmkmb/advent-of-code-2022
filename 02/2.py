file = open('./input1.txt', 'r')
lines = [line.strip().split(' ') for line in file.readlines() if line.strip()]
score = 0

opponent_map = {
    'A': 'r',
    'B': 'p',
    'C': 's',
}

my_map = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

winner_map = {
    'r': 'p',
    'p': 's',
    's': 'r',
}

choice_bonus = {
    'r': 1,
    'p': 2,
    's': 3,
}

win_table = {}
for opponent in winner_map.keys():
    for my in winner_map.keys():
        if opponent == my:
            key = opponent + str(3)
        elif my == winner_map[opponent]:
            key = opponent + str(6)
        else:
            key = opponent + str(0)
        win_table[key] = my

for opponent, my in lines:
    opponent = opponent_map[opponent]
    my_choice = win_table[opponent + str(my_map[my])]
    score += my_map[my] + choice_bonus[my_choice]

print(score)
