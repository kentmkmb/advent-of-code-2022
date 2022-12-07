from pprint import pprint


input_file = open('./input.txt', 'r')
lines = [line.strip() for line in input_file.readlines()]

pointer = 0
pwd = []
dirs = {}

while pointer < len(lines):
    line = lines[pointer]
    if line.startswith('$ cd '):
        if line.endswith('..'):
            pwd.pop()
        elif line.endswith('/'):
            pwd = []
        else:
            _, _, name = line.split(' ')
            pwd.append(name)
    elif line == '$ ls':
        new_dir = {'files': [], 'dirs': []}
        while pointer + 1 < len(lines) and not lines[pointer + 1].startswith('$ '):
            pointer += 1
            ls_line = lines[pointer]
            size, name = ls_line.split(' ')
            full_name = '/'.join(pwd + [name])
            if size == 'dir':
                new_dir['dirs'].append(full_name)
            else:
                size = int(size)
                new_dir['files'].append({'name': full_name, 'size': size})
        dirs['/'.join(pwd)] = new_dir
    pointer += 1

pprint(dirs)

result = []

def full_size(dir_path: str) -> int:
    dir_data = dirs[dir_path]
    inner_dirs = dir_data['dirs']
    files = dir_data['files']
    files_sum = sum([file_data['size'] for file_data in files])
    inner_sum = sum([full_size(path) for path in inner_dirs])
    return files_sum + inner_sum


for dir_path, dir_data in dirs.items():
    size = full_size(dir_path)
    if size <= 100_000:
        result.append(size)

print(sum(result))
