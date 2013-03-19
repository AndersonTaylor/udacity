# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
    
    #value contains for each place in grid   
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],    # holds x value of position that led to this spot
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],    # holds y value of positon that led to this spot
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],    # holds orientation that led to this point
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]    # holds action that led to this point
    
    print_value(value)
    
    value[0][init[0]][init[1]] = init[0]
    value[1][init[0]][init[1]] = init[1]  
    value[2][init[0]][init[1]] = init[2]
    value[3][init[0]][init[1]] = "START"
    
    openlist = [[0,init[0],init[1],init[2]]]
    print openlist
    found = False
    stuck = False 
    while not found and not openlist == []: 
        openlist.sort()
        pick = openlist.pop(0)
        if ([pick[1],pick[2]] == goal):
            found = True
            print 'found'
            print pick
        for exp in expand_pick(pick):
            openlist.append(exp)
        
        openlist.sort()
        print openlist
        print ;
        
    
    



   #return policy2D # Make sure your function returns the expected grid.
 
def expand_pick(p):
    #returns list of expanded picks (each is a list)
    #input pick is list pick = [cost to get to this point, row in grid, column in grid, orientation]  
    expanded = []
    
    #try each of the actions
    #if you're on the grid and not on a wall
    #then add updated cost and new position/orientation to expanded
    
    for i in range(len(action)):
        new_orientation = (p[3]+action[i]) % 4
        a = forward[new_orientation]
        x2 = p[1] + a[0]
        y2 = p[2] + a[1]  #gives position where the action takes us
        
        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
            if (grid[x2][y2] == 0):
                new_cost = p[0] + cost[i]
                print 'from' 
                print p[1], p[2]    
                print [new_cost, x2, y2, new_orientation]
                print
                expanded.append([new_cost, x2, y2, new_orientation])
    return expanded

def print_value(v):
    
    for i in v:
        if (i==0): print x
        for j in i:
            print j
        print ;
        
        
        
        

optimum_policy2D()


