import os

def get_input(fp):
    with open(fp) as f:
        return f.read().splitlines()    



def right_substring(inputString, prefixToRemove):
    if inputString.startswith(prefixToRemove):
        return inputString[len(prefixToRemove):]
    else:
        return inputString


# Create struct name and value


# Create an object tree
class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = {} #[]

    def ensure_file(self, name, size):
        if name not in self.files:
            self.files[name] = int(size)
        else:
            if self.files[name] != int(size):
                print(f"ERROR: different size found for file '{name}': orig ({self.files[name]}), new ({size})")
                ValueError("ERROR: different size found for file '{name}': orig ({self.files[name]}), new ({size})")
        

    def sum_file_sizes(self):
        #return sum(self.files)
        sum = 0
        for value in self.files.values():
            sum += value
        return sum

    def sum_descendant_file_sizes(self):
        x = 0
        for child in self.children:
            x = child.sum_file_sizes()
            x += child.sum_descendant_file_sizes()
        return x

    def total(self):
        return self.sum_file_sizes() + self.sum_descendant_file_sizes()

    def ensure_child(self, childName):
        #self.children.append(child)
        if childName not in self.children:
            newChild = Directory(childName, self)
            self.children.append(newChild)
            return newChild
        else:
            print(f"Child '{child.name}' already exists.")
            return self.children[child]

    def get_path(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.get_path() + '/' + self.name

    def __repr__(self):
        #return self.get_path()
        return self.name

    def __str__(self):
        #return self.get_path()
        return self.name

    def __eq__(self, other):
        #return self.get_path() == other.get_path()
        return self.name == other

    def __hash__(self):
        return hash(self.get_path())


# add a child to a directory
# def add_child(parent, child):
    
#     if child not in parent.children:
#         newChild = Directory(child, parent)
#         parent.children.append(newChild)
#         return newChild
#     else:
#         print(f"Child '{child.name}' already exists.")
#         return parent.children[child]
    


def recurse_flatten_dirs(parent):
    descendants = []
    descendants.append(parent)
    for child in parent.children:
        if isinstance(child, Directory):
            temp = recurse_flatten_dirs(child)
            for t in temp:
                descendants.append(t)
        else:
            TypeError("Invalid type found in recurse_flatten_dirs()")
    return descendants

def print_recursive_hierarchy(parent, indent=0):

    print('  ' * indent + str(parent.name))
    for child in parent.children:
        #print('  ' * (indent) + str(child.name))
        print_recursive_hierarchy(child, indent + 1)
    
    for f in parent.files:
        print('  ' * (indent) + str(f))
        



# ================================================
 
#fp = os.path.join("day-7", "example-input.txt")
fp = os.path.join("day-7", "input.txt")

inputLines = get_input(fp)
print("Input read complete")


# Create the root directory
root = Directory('/', None)


# Create tree
# This puzzle only allows either going up or down, or jumping right to the root. 
# Assume can only ever get to a new child via a 'cd' command, so can ignore 'dir' outputs

cwd = {}


for line in inputLines:
    if line.startswith('$ '):
        
        if line.startswith('$ ls'):    
            pass

        elif line.startswith('$ cd /'):
            cwd =  root #'/'

        elif line.startswith('$ cd ..'):
            cwd = cwd.parent

        elif line.startswith('$ cd '):
            # This condition should only represent a change to a child directory
            childName = right_substring(line, '$ cd ')
            child = cwd.ensure_child(childName)
            cwd = child

    else:
        # Output line
        if not line.startswith('dir'):
            parts = line.split(' ')
            if len(parts) == 2:
                cwd.ensure_file(parts[1], parts[0])
            else:
                print(f"Unexpected line: {line}")


# Print recurse
print_recursive_hierarchy(root)


flatDirs = recurse_flatten_dirs(root)
print(flatDirs)

filter = 100000
filteredDirs = []
for dir in flatDirs:
    total = dir.total()
    if (total <= filter):
        print(f"{dir.name}: {total} *")
        filteredDirs.append(dir)
    else:
        print(f"{dir.name}: {total}")
        


answer = sum(dir.total() for dir in filteredDirs)
print(f"The answer is: {answer}")
x = 0
for f in filteredDirs:
    x += f.total()
print(x)

# Example
#   Expected: 95437
#     Answer: 95437 (correct)
#
# Puzzle
#   Expected: ?
#     Actual: 1583249 (WRONG - says answer is too high. I give up.)