import re

def getSize(dir):
    size = dir["size"]
    for d in dir["dirs"].values():
        size += getSize(d)
    return size

def getDir(path, cd):
    if len(path) == 0:
        return cd
    return getDir(path[1:], cd["dirs"][path[0]])
    
def calcTotalSum(dir):
    size = getSize(dir)
    if size > 100000:
        size = 0
    total = size
    for d in dir["dirs"].values():
        total += calcTotalSum(d)
    return total

with open("input.txt") as file:
    pwd = []
    root = {"size": 0, "dirs": {}}
    for line in file.readlines():
        m_cd = re.match(r'\$ cd (.+)', line)
        m_ls = re.match(r'\$ ls', line)
        m_dir = re.match(r'dir (.+)', line)
        m_file = re.match(r'(\d+) (.+)', line)

        # Update current path
        if m_cd:
            if m_cd.group(1) == "..":
                if len(pwd) > 1:
                    pwd.pop()
                else: 
                    pwd = []
            elif m_cd.group(1) == ".":
                pass
            elif m_cd.group(1) == "/":
                pwd = []
            else:
                pwd.append(m_cd.group(1))
        elif m_ls:
            pass

        # Update directory structure
        else:
            cd = getDir(pwd, root)
            if m_dir:
                if m_dir.group(1) not in cd:
                    cd["dirs"][m_dir.group(1)] = {"size": 0, "dirs": {}}
            elif m_file:
                cd["size"] += int(m_file.group(1))
    
    print(calcTotalSum(root))