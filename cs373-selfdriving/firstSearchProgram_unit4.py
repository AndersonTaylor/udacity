# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------

    initial_open_list = [0, init[0], init[1]]
    
    open_list = []
    open_list.append(initial_open_list)
    
    visited =[]
    
    
    while(open_list != []):
        open_list.sort()  #sorts open_list by the "g value" 
        popped = open_list.pop(0)  #pops off one with lowest "g value"
        
        if ([popped[1],popped[2]] == goal):
            return popped
        
        nodes = expand_node([popped[1],popped[2]])
        visited.append([popped[1],popped[2]])
        
        for node in nodes:
            #only add the node to open_list only if it's not in there somewhere
            if not any( x[1] == node[0] and x[2] == node[1] for x in open_list):
                #and make sure isn't in visted
                if not any(node == v for v in visited):
                    open_list.append([popped[0]+1,node[0],node[1]]) #increment "g value" as we add node to open_list
                    
        print "New Open List" ;
        print "-------------" ;
        for x in open_list:
            print x ;
        
    
    return 'fail' # you should RETURN your result


def expand_node(node):
    expandednodes = []
    for direction in delta:
        new_coordinate = map(sum, zip(node, direction)) 
        # check to see if new_coordinate is on the board, if so add it to list of expanded nodes
        if (new_coordinate[0] >= 0 and new_coordinate[0] < len(grid) and new_coordinate[1] >= 0 and new_coordinate[1] < len(grid[0]) ):
            #check to see that new_coordinate isn't a wall  
            if (grid[new_coordinate[0]][new_coordinate[1]] == 0):
                expandednodes.append(new_coordinate)
    return expandednodes
print search()