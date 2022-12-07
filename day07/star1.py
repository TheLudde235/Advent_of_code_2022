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

inp = open('input.txt').read().split('\n')
class File:
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Dir(File):
    directories: dict = dict()
    files: list[File] = list()

    def __init__(self, name: str, size: int, parent):
        super().__init__(name, size)
        self.parent = parent

    def add_dir(self, child: File):
        self.directories[child.name] = child
        self.size += child.size

    def add_file(self, child: File):
        self.files.append(child)
        self.size += child.size

    def update_size(self):
        self.size = 0
        for child in self.files:
            self.size += child.size
        for child in self.directories:
            self.directories[child].update_size()
            self.size += self.directories[child].size
        return self.size

dirs: dict = {
    '/': Dir('/', 0, None)
}

current_dir: Dir = dirs['/']

for line in inp:
    split_arr = line.split()

    if split_arr[0] == '$':
        if split_arr[1] == 'cd':
            if split_arr[2] == '..':
                current_dir.parent.update_size()
                current_dir = current_dir.parent
            elif split_arr[2] == '/':
                current_dir = dirs['/']
            else:
                current_dir = current_dir.directories[split_arr[2]]
    else:
        if split_arr[0] == 'dir':
            d = Dir(split_arr[1], 0, current_dir)
            d.directories = dict()
            d.files = []
            current_dir.add_dir(d)
            if split_arr[1] in dirs:
                dirs[split_arr[1] + d.__str__()] = d
            else:
                dirs[split_arr[1]] = d
        else:
            f = File(split_arr[1], int(split_arr[0]))
            current_dir.add_file(f)

s = 0

dirs['/'].update_size()
for d in dirs:
    se = dirs[d].update_size()
    if se <= 100000:
        s += se
print(s)
