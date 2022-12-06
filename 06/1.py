file = open('./input.txt', 'r')
line = file.readline().strip()

SEQ_LENGTH = 4

for i in range(len(line) - (SEQ_LENGTH - 1)):
    if len(set(line[i: i + SEQ_LENGTH])) == SEQ_LENGTH:
        print(i + SEQ_LENGTH)
        break
