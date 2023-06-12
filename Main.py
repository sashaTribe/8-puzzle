import random

game_board = [[None,None,None],[None,None,None],[None,None,None]]

desired_goal = [[0,1,2],
                [3,4,5],
                [6,7,8]]
numbers = list(range(0,9))
random.shuffle(numbers)

closed_set = set()
for i in range(3):
    for j in range(3):
        game_board[i][j] = numbers.pop()
        print(numbers)
print(game_board)
open_set = set(game_board)
closed_set = set()
#can move up,down,left,right

class Node:
    def __init__(self,board,level,fval):
        self.board = board
        self.level = level
        self.fval = fval


    def create_child(current_board,x1,y1, x2,y2):
        temp_board = current_board
        if temp_board[x2][y2] == 0:
            temp_val = temp_board[x1][y1]
            temp_board[x1][y1] = temp_board[x2][y2]
            temp_board[x2][y2] = temp_val
            new_child = Node(temp_board,current_board.level+1,0)
            return new_child
        else:
            return None

    def generate_children(self,gameboard,x,y):
        possible_vals = [[x, y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for c in possible_vals:
            child = self.create_child(gameboard,x,y,c[0],c[1])
            if child != None:
                children.append(child)
        return children

            
    
                
    # function to calculate f(x) = g(x) + h(x)
    def f(current_node, goal_node):
        return h(current_node,goal_node) + current_node.level
    def h(current_node, goal_node):
        count = 0
        for i in range(3):
            for j in range(3):
                if current_node[i][j] != goal_node[i][j] and current_node[i][j] != 0:
                    count += 1
        return count

def update_gameboard(action, )
    
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



