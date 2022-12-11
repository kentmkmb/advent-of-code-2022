input_file = open('./10/input.txt', 'r')

clock = 0
register = 1
command = None
progress = 0

sprite = lambda: (register - 1, register, register + 1)
screen: list[list[str]] = []

while True:
    if clock % 40 == 0:
        screen.append([])
    row = screen[-1]
    row.append('#' if (clock % 40) in sprite() else '.')

    clock += 1

    if not command:
        if not (command := input_file.readline().strip()):
            break


    if command.startswith('noop'):
        command = None
        progress = 0
    elif command.startswith('addx'):
        _, appendant = command.split(' ')
        if progress == 0:
            progress = 1
        elif progress == 1:
            command = None
            progress = 0
            register += int(appendant)

for row in screen:
    print(''.join(row))
