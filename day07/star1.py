# directories are dicts and files ints

inp = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split('\n')
def find(x):
    return dict()

root: dict = {'/': {}}
parent_dirs: list[dict] = [root]
current_dir: dict = root


for line in inp:
    line_arr = line.split()
    if line[0] == '$':
        if line_arr[1] == 'cd':
            if line_arr[2] == '..':
                current_dir = parent_dirs.pop()
            else:
                if current_dir not in parent_dirs[-1]:
                    parent_dirs[-1].setdefault(line_arr[2], dict())
                parent_dirs.append(current_dir)
                current_dir = find(line_arr[2])
    else:
        print(line_arr)

print(root)