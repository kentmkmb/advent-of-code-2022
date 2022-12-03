from pprint import pprint
import string

file = open('./1.txt', 'r')
lines = [line.strip() for line in file.readlines() if line.strip()]

def each_first(t: tuple[int, str]):
    return t[0] % 3 == 1

def each_second(t: tuple[int, str]):
    return t[0] % 3 == 2

def each_third(t: tuple[int, str]):
    return t[0] % 3 == 0

groups = zip(
    filter(each_first, enumerate(lines, 1)),
    filter(each_second, enumerate(lines, 1)),
    filter(each_third, enumerate(lines, 1)),
)

badges = []

for first, second, third in groups:
    first = set(first[1])
    second = set(second[1])
    third = set(third[1])
    for t in first:
        if t in second and t in third:
            badges.append(t)

abc = list(string.ascii_lowercase)
abc.extend(list(string.ascii_uppercase))

points = {abc: i for i, abc in enumerate(abc, 1)}
score = sum([points[x] for x in badges])
print(score)
