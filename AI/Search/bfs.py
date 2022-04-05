from maps import *
import colorama

map = map1

# function to display the map
def displaymap(maptoprint):
    for row in maptoprint:
        for cell in row:
            print(cell, end='')
        print()

#displaymap(map)

# find the starting cell
for row in map:
    for cell in row:
        if cell == 'AA':
            rowindex = map.index(row)
            cellindex = row.index(cell)
            start = (rowindex, cellindex)
            state = start
            print('start: ', state)

# 0, 0 is the top left corner
# state is in the form: (row, cell)

moves = []
previous = []
# define the frontier
frontier = []
explored = [start]

def getfrontier(state):
    # look at all surrounding cells
    for row in range(state[0]-1, state[0]+2):
        for cell in range(state[1]-1, state[1]+2):
            # if the cell is not the current cell
            if (row, cell) != state:
                # if the cell is not a diagonal
                if abs(row - state[0]) + abs(cell - state[1]) == 1:
                    # if the cell is not in explored
                    if (row, cell) not in explored:
                        # if the cell is not a wall
                        if map[row][cell] != '██':
                            # if the cell is not already in the frontier
                            if (row, cell) not in frontier:
                                # add the cell to the frontier
                                frontier.append((row, cell))

                                # everytime i add a cell to the frontier
                                # i add it to the previous list containing a
                                # tuples of that cell and its previous cell
                                previous.append(((row, cell), state))
    return frontier

# getfrontier returns a list of the frontier of the state


# breadth first search is FIFO
# depth first search is LIFO

# steps

# start in start cell
# add all surrounding cells to the frontier
# explore the frontier from front to back
# remove the cell from the frontier when explored
# repeat until the goal is found

# state is the start cell
getfrontier(state)

while frontier:
    cell = frontier[0] # bfs is index 0 and dfs is index -1
    explored.append(cell)
    frontier.remove(cell)
    if map[cell[0]][cell[1]] == 'BB':
        print('goal: ', cell)
        goalcell = cell
        break
    else:
        # add all surrounding cells to the frontier
        getfrontier(cell)



# print(explored)
#print(previous)
# previous is in the form (a)'s previous is (b)    ((a),(b))

# now we trace back to the start using the previous list

#print(goalcell)

shortestpath = [goalcell]
previouscell = goalcell
while previouscell != start:
    for cell in previous:
        if cell[0] == previouscell:
            previouscell = cell[1]
            shortestpath.append(previouscell)
            break

shortestpath.reverse()
print('shortestpath: ', shortestpath)

# colour the shortest path
for row in range(len(map)):
    for cell in range(len(map[row])):
        if (row, cell) in shortestpath:
            map[row][cell] = colorama.Back.GREEN + map[row][cell]
        else:
            map[row][cell] = colorama.Style.RESET_ALL + map[row][cell]

for cell in shortestpath:
    map[cell[0]][cell[1]] = colorama.Back.GREEN + map[cell[0]][cell[1]]
    colorama.Style.RESET_ALL

displaymap(map)

