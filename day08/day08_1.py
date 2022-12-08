with open("input.txt") as file:
    grid = [list(line.strip()) for line in file.readlines()]
    hiddenTrees = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    tallestTop = [-1 for _ in range(len(grid[0]))]
    tallestBottom = [-1 for _ in range(len(grid[0]))]
    tallestLeft = [-1 for _ in range(len(grid))]
    tallestRight = [-1 for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            # Top
            tree = grid[i][j]
            if int(tallestTop[j]) >= int(tree):
                hiddenTrees[i][j] += 1
            else: 
                tallestTop[j] = tree

            # Bottom
            tree = grid[len(grid) - i - 1][j]
            if int(tallestBottom[j]) >= int(tree):
                hiddenTrees[len(grid) - i - 1][j] += 1
            else:
                tallestBottom[j] = tree
            
            # Left
            tree = grid[i][j]
            if int(tallestLeft[i]) >= int(tree):
                hiddenTrees[i][j] += 1
            else:
                tallestLeft[i] = tree

            # Right
            tree = grid[i][len(grid[0]) - j - 1]
            if int(tallestRight[i]) >= int(tree):
                hiddenTrees[i][len(grid[0]) - j - 1] += 1
            else:
                tallestRight[i] = tree

    print(len([tree for row in hiddenTrees for tree in row if tree != 4]))