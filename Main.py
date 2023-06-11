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

def a_star(game_board)