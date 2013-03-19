# Write two functions, the first, validity_check which takes a potential
# cover and the adjacency matrix of a graph as its inputs and returns True
# if the potential cover is a cover of the graph and False otherwise.
# The second, vertex_cover_naive, takes the adjacency matrix of a graph
# as its input, checks all potential covers, and returns the size of a
# minimum vertex cover. You should assume there are no loops in the graph.

from itertools import *


def validity_check(cover, graph):
    # Your code should go here.
    for row in range(len(graph)):
        for entry in range(row, len(graph[0])):
            if graph[row][entry] == 1:
                if not (cover[row]==1 or cover[entry] == 1):
                    return False
    return True


def number_of_ones_in(tup):
    count = 0
    for t in tup:
        if t == 1:
            count+=1    
    return count

def vertex_cover_naive(input_graph):
    n = len(input_graph)
    minimum_vertex_cover = n
    # loops through all strings of 0s and 1s of length n
    for assignment in product([0,1], repeat=n):
        # Your code should go here.
        # Based on the assignment (a list of 0s and 1s)
        # - Check the assignment is valid
        # - Calculate the size of assignment
        # - Update the minimum_vertex_cover variable if appropriate
        
        if (validity_check(assignment, input_graph)):
            possible_new_min = number_of_ones_in(assignment)
            
            if (possible_new_min<minimum_vertex_cover):
                minimum_vertex_cover = possible_new_min
            
    # End of your code
    return minimum_vertex_cover

def test():
    graph = [[0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0]]

    assert vertex_cover_naive(graph)==3 

# If you've not seen testing like this before, all you need to do is
# to call test(). If the tests pass, you'll get no output. If they don't
# you'll get an assertion error. Don't forget to remove the call to the
# test before submitting your code.

#test()
