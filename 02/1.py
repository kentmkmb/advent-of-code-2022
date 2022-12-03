file = open('./input1.txt', 'r')
lines = [line.strip().split(' ') for line in file.readlines() if line.strip()]
score = 0

opponent_map = {
    'A': 'r',
    'B': 'p',
    'C': 's',
}

my_map = {
    'X': 'r',
    'Y': 'p',
    'Z': 's',
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
        key = opponent + my
        if opponent == my:
            win_table[key] = 3
        elif my == winner_map[opponent]:
            win_table[key] = 6
        else:
            win_table[key] = 0

for opponent, my in lines:
    opponent = opponent_map[opponent]
    my = my_map[my]
    score += win_table[opponent+my] + choice_bonus[my]

print(score)
