input_file = open('./10/input.txt', 'r')

clock = 0
register = 1
command = None
progress = 0

wanted = (20, 60, 100, 140, 180, 220)
result = 0

while True:
    clock += 1

    if clock in wanted:
        result += register * clock

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

print(result)
