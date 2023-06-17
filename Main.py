import random



desired_goal = [[0,1,2],
                [3,4,5],
                [6,7,8]]



def generate_start_node(game_board):
    numbers = list(range(0,9))
    random.shuffle(numbers)
    for i in range(3):
        for j in range(3):
            game_board[i][j] = numbers.pop()
    return game_board

#can move up,down,left,right

class Node:
    def __init__(self,board,level,fval):
        self.board = board
        self.level = level
        self.fval = fval
    
    def __lt__(self, other):
        return self.fval < other.fval


    def create_child(self,x1,y1, x2,y2):
        temp_board = self.board
        k = range(0,3)
        if x2 in k and y2 in k:
            temp_val = temp_board[x1][y1]
            temp_board[x1][y1] = temp_board[x2][y2]
            temp_board[x2][y2] = temp_val
            new_child = Node(temp_board,self.level+1,0)
            #print(new_child)
            return new_child
        else:
            return None

    def generate_children(self,x,y):
        gameboard = self.board
        possible_vals = [[x, y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for c in possible_vals:
            child = self.create_child(x,y,c[0],c[1])
            if child != None:
                
                children.append(child)
        return children
    
    def find_empty_space(self):
        current_board = self.board
        x = 0
        y = 0
        for i in range(3):
            for j in range(3):
                if current_board[i][j] == 0:
                    x = i
                    y = j
        return x,y

            
    
class Puzzle:

    def __init__(self, open=[],close=[]):
        self.open = open
        self.close = close

    # approximation heuristic
    def h(self, current_node, goal_node):
        count = 0
        for i in range(3):
            for j in range(3):
                if current_node[i][j] != goal_node[i][j] and current_node[i][j] != 0:
                    count += 1
        return count


    # function to calculate f(x) = g(x) + h(x)
    def f(self,current_node, goal_node):
        return self.h(current_node[0].get_board(),goal_node) + current_node[0].get_level()


    def a_star(self):
        game_board = [[None,None,None],
                      [None,None,None],
                      [None,None,None]]
        start_board = generate_start_node(game_board)

        start_node = Node(start_board,0,0)
        end_node = desired_goal
        print(desired_goal)
        
        start_node.fval = self.f(start_node,end_node)

        self.open.append(start_node)
        
        print("The starting board: ")
        for i in start_node.board:
            for j in i:
                print(j,end=" ")
            print("")
        while True:
            
            current_status = self.open[0]
            print("Current Status: ")
            print("\n")
            for i in current_status.board:
                for j in i:
                    print(j,end=" ")
                print("")
            if self.h(current_status.board,end_node) == 0:
                break
            x,y = current_status.find_empty_space()
            for i in current_status.generate_children(x,y):
                i.fval = self.f(i,end_node)
                self.open.append(i)
            self.close.append(current_status)
            del self.open[0]

            self.open.sort(key = lambda x:x.fval, reverse=False)
            #print("Length of open array: ", len(self.open))
        print("Success!")

puzzle = Puzzle()
puzzle.a_star()


        
            


