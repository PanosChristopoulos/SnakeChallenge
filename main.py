from itertools import count
from random import sample
from signal import raise_signal
from sys import exc_info
from typing import Counter
from xmlrpc.client import Boolean
import time

snakeMovements = {'L':[-1,0],'R':[1,0],'D':[0,-1],'U':[0,1]}

VISUALIZATION = False
totalValidMovements = []


class snakeGame(object):

    def __init__(self, board: list, snake: list, depth: int, currDepth = 0):
        self.snake = snake
        self.board = board
        self.depth = depth
        self.currDepth = currDepth
        



        #Board dimension limits check
        for dimension in self.board:

            if isinstance(dimension,int):
                pass
            else:
                raise TypeError(f"in definition {dimension}")

            if dimension < 1 or dimension > 10:

                raise IndexError(f"Board definition unsuccessful, {dimension} out of range")

         

       
    def snakeMovementAction(self,snake,board,currDepth,depth):
        
        
        invalidMovements = []
        if len(snake) > 0 and currDepth<depth:
            
            #Primary Board visualization
            if VISUALIZATION == True:
                print('Snake',snake)
                print('Board',board)
                print('Depth', currDepth)

                for x in range(board[0]):
                    for y in range(board[1]):
                        if [x,y] in snake:
                            print('X', end=" ")
                        else:
                            print('-', end=" ")
                    print('\n')

            board = self.board
            totalSnakePossibleMovements = []
            
            for key in snakeMovements:
                sampleList = []

                for element in snake:
                    sampleList.append([element[0]+snakeMovements[key][0],element[1]+snakeMovements[key][1]])

                totalSnakePossibleMovements.append(sampleList)
                
            for element in totalSnakePossibleMovements:

                for item_ in element:
                    if item_[0]<0 or item_[0]>board[0] or item_[1]<0 or item_[1]>board[1]:
                        invalidMovements.append(element)                          
                    else:
                        pass   
                        
            counter = 0
            for element in totalSnakePossibleMovements:
                if element in invalidMovements:
                    totalSnakePossibleMovements.remove(element)
            
            snakeValidMovements = totalSnakePossibleMovements

            print(len(snakeValidMovements))
            for element in snakeValidMovements:
                print(element)
                totalValidMovements.append([element,currDepth+1])
                currDepth = currDepth+1
                self.snakeMovementAction(element,board,currDepth,depth)

        

            
            
            
            

            
            
            



sampleSnake = [[5,5], [5,4], [4,4], [4,5]]
sampleBoard = [10,10]
sampleSnakeGame = snakeGame(sampleBoard,sampleSnake,4)
sampleSnakeGame.snakeMovementAction(sampleSnake,sampleBoard,0,4)

"""

listTempstime = [[[[2, 1], [3, 1], [3, 0], [3, -1], [2, -1], [1, -1], [0, -1]], 1], [[[1, 1], [2, 1], [2, 0], [2, -1], [1, -1], [0, -1], [-1, -1]], 2], [[[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-2, -1]], 3], [[[2, 1], [3, 1], [3, 0], [3, -1], [2, -1], [1, -1], [0, -1]], 4], [[[2, 1], [3, 1], [3, 0], [3, -1], [2, -1], [1, -1], [0, -1]], 5], [[[2, 1], [3, 1], [3, 0], [3, -1], [2, -1], [1, -1], [0, -1]], 6], [[[1, 0], [2, 0], [2, -1], [2, -2], [1, -2], [0, -2], [-1, -2]], 7], [[[1, 0], [2, 0], [2, -1], [2, -2], [1, -2], [0, -2], [-1, -2]], 8], [[[1, 0], [2, 0], [2, -1], [2, -2], [1, -2], [0, -2], [-1, -2]], 9], [[[1, 1], [2, 1], [2, 0], [2, -1], [1, -1], [0, -1], [-1, -1]], 3], [[[3, 1], [4, 1], [4, 0], [4, -1], [3, -1], [2, -1], [1, -1]], 4], [[[3, 1], [4, 1], [4, 0], [4, -1], [3, -1], [2, -1], [1, -1]], 5], [[[3, 1], [4, 1], [4, 0], [4, -1], [3, -1], [2, -1], [1, -1]], 6], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 7], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 8], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 9], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 10], [[[2, 1], [3, 1], [3, 0], [3, -1], [2, -1], [1, -1], [0, -1]], 2], [[[1, 1], [2, 1], [2, 0], [2, -1], [1, -1], [0, -1], [-1, -1]], 3], [[[1, 1], [2, 1], [2, 0], [2, -1], [1, -1], [0, -1], [-1, -1]], 4], [[[3, 1], [4, 1], [4, 0], [4, -1], [3, -1], [2, -1], [1, -1]], 5], [[[3, 1], [4, 1], [4, 0], [4, -1], [3, -1], [2, -1], [1, -1]], 6], [[[3, 1], [4, 1], [4, 0], [4, -1], [3, -1], [2, -1], [1, -1]], 7], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 8], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 9], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 10], [[[2, 0], [3, 0], [3, -1], [3, -2], [2, -2], [1, -2], [0, -2]], 11], [[[2, 1], [3, 1], [3, 0], [3, -1], [2, -1], [1, -1], [0, -1]], 3]]
counter = 0

for x in listTempstime:
    if x[1] == 3:
        counter += 1

print(counter)"""