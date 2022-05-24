from signal import raise_signal


snakeMovements = {'L':[-1,0],'R':[1,0],'D':[0,-1],'U':[0,1]}

"""
def board(width,height):
    
    for dimension in [width,height]:

        if isinstance(dimension,int):
            pass
        else:
            raise TypeError(f"in definition {dimension}")

        if dimension < 1 or dimension > 10:

            raise IndexError(f"Board definition unsuccessful, {dimension} out of range")

    return width,height
"""


class gameSetup(object):

    def __init__(self, board: list, snake: list, depth: int):
        self.snake = snake
        self.board = board

        for dimension in self.board:

            if isinstance(dimension,int):
                pass
            else:
                raise TypeError(f"in definition {dimension}")

            if dimension < 1 or dimension > 10:

                raise IndexError(f"Board definition unsuccessful, {dimension} out of range")

        print('Snake',snake)
        print('Board',board)

        for x in range(board[0]):
            for y in range(board[1]):
                if [x,y] in snake:
                    print('X', end=" ")
                else:
                    print('-', end=" ")
            print('\n')



"""
TEST lists

board = [4,3]

snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]

depth = 3

Result = 7


"""

game1= gameSetup([4,3],[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]],3)
