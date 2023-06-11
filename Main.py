import random

game_board = [[None,None,None],[None,None,None],[None,None,None]]

desired_goal = [[0,1,2],
                [3,4,5],
                [6,7,8]]
numbers = list(range(0,9))
random.shuffle(numbers)

for i in range(3):
    for j in range(3):
        game_board[i][j] = numbers.pop()
        print(numbers)
print(game_board)
#can move up,down,left,right

def create_child(current_board):
    x,y = 
    actions = [[x, y-1],[]]
    
def find_empty_space(current_board):
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            if current_board[i][j] == 0:
                x = i
                y = j
    return x,y
def a_star(start_node, end_node):
    open_set = set(start_node)
    closed_set = set()
    start_node = game_board
    end_node = desired_goal
    g = {} #distance from start node
    parents = {} #adjacency map of all nodes for each parent
    g[start_node] == 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n==None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v
        
        if n == end_node or g[n] == None:
            pass
        else:
            #for (m, action) in get_neighbours(n):



