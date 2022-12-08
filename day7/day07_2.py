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
 

# TODO: Fix this function
def getSizeList(dir):
    sizeList = [getSize(dir)]
    for d in dir["dirs"].values():
        sizeList += getSizeList(d)
    return sizeList

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
    

    free_space = 70000000 - getSize(root)
    needed_space = 30000000 - free_space

    deleteCandidates = sorted([dir for dir in getSizeList(root) if dir >= needed_space])
    print(deleteCandidates[0])