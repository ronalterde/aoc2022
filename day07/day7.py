
"""
Goal: Find all of the directories with a total size of at most 100000.
What is the sum of the total sizes of those directories?

- parse example into a dict (to represent the tree)
- traverse the tree
    - find directories with total size of <= 100k
"""

import json

if __name__ == "__main__":

    # with open('example.txt') as f:
    with open('input.txt') as f:
        lines = f.readlines()

    tree = {}
    cwd = []

    for line in lines:
        line = line.strip()
        if line.startswith('$ cd'):
            dir = line.split('cd')[-1].strip()
            if dir == '..':
                cwd.pop()
            else:
                cwd.append(dir)
        elif line.startswith('$ ls'):
            pass
        else: # dir listing follows

            # Traverse tree, starting from / 
            # every time(!)
            node = tree
            for level in cwd:
                if level not in node:
                    node[level] = {}
                node = node[level]

            if not line.startswith('dir'):
                size = line.split()[0]
                filename = line.split()[-1]
                node[filename] = { 'size': size }

    print(json.dumps(tree, indent=4))

    # for all nodes that have children, sum the size of all children, recursively.

    total = 0

    def foo(node):
        global total

        if 'size' in node:
            return int(node['size'])
        else:
            total_size = 0
            for child in node.keys():
                total_size = total_size + foo(node[child])
            if total_size <= 100000:
                total = total + total_size
            return total_size

    foo(tree)
    print("total:", total)

    # Part 2: Find the smallest directory that, if deleted, would free up enough
    # space on the filesystem to run the update. What is the total size of that directory?
    """
    - get total size of outermost dir
    - calculate how much needs to be deleted
    - find directory of smallest size that's greater than that value
    """

    totals = {}

    def foo2(node, name):
        if 'size' in node:
            return int(node['size'])
        else:
            total_size = 0
            for child in node.keys():
                total_size = total_size + foo2(node[child], child)
            global totals
            totals[name] = total_size
            return total_size

    foo2(tree, 'n/a')
    unused_space = 70000000 - totals['/']
    needed_space = 30000000 - unused_space

    del totals['n/a']
    all = [(i, k) for i, k in totals.items() if k >= needed_space]
    all.sort(key=lambda item: item[1])
    smallest = all[0]
    print(f"Directory to remove: {smallest[0]}, size: {smallest[1]}")