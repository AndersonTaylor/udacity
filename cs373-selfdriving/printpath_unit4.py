# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]    
    counter = 0
    expand[init[0]][init[0]] = counter
    
    
    block_that_led_to_me = [[[0,0] for row in range(len(grid[0]))] for col in range(len(grid))]
    block_that_led_to_me[init[0]][init[1]] = init 
    
    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            counter += 1
                            expand[x2][y2] = counter
                            block_that_led_to_me[x2][y2] = [x,y]
    for i in range(len(expand)):
        print expand[i]
    finalpath = make_the_path(block_that_led_to_me)
    print ; 
    for i in range(len(expand)):
        print finalpath[i]
    
    return finalpath # make sure you return the shortest path.

def make_the_path(block_that_led_to_me):
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    path[goal[0]][goal[1]] = '*'
    cur_pos = goal
    while (cur_pos != init):
        prev_pos = cur_pos
        cur_pos = block_that_led_to_me[cur_pos[0]][cur_pos[1]]
        d = [prev_pos[0] - cur_pos[0], prev_pos[1] - cur_pos[1]]
        for i in range(len(delta)):
            if (d==delta[i]):
                b = block_that_led_to_me[prev_pos[0]][prev_pos[1]]
                path[b[0]][b[1]] = delta_name[i]
    return path

search()