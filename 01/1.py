file = open('./input-1.txt', 'r')
lines = [line.strip() for line in file.readlines()]
elfs = []
elf = None

for line in lines:
    elf = elf if elf != None else 0
    if not line:
        elfs.append(elf)
        elf = None
    else:
        elf += int(line)

elfs.sort()
print(elfs[-1])
