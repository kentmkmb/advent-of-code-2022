import string

file = open('./1.txt', 'r')
lines = [line.strip() for line in file.readlines() if line.strip()]

wrong = []

for line in lines:
    line = list(line)
    left = set(line[:int(len(line) / 2)])
    right = set(line[int(len(line) / 2):])
    for t in left:
        if t in right:
            wrong.append(t)

abc = list(string.ascii_lowercase)
abc.extend(list(string.ascii_uppercase))

points = {abc: i for i, abc in enumerate(abc, 1)}
score = sum([points[x] for x in wrong])
print(score)
