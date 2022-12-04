file = open('./input.txt', 'r')
lines = [line.strip().split(',') for line in file.readlines() if line.strip()]
pairs = [(list(map(int, first.split('-'))), list(map(int, second.split('-')))) for first, second in lines]

count = 0

for first, second in pairs:
    if not ((first[0] < second[0] and first[1] < second[0]) or (first[0] > second[1] and first[1] > second[1])):
        count += 1

print(count)
