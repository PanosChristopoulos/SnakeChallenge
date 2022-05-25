from itertools import count
from random import sample
from signal import raise_signal
from sys import exc_info
from typing import Counter
from xmlrpc.client import Boolean
import time

snakeMovements = {'L':[-1,0],'R':[1,0],'D':[0,-1],'U':[0,1]}

VISUALIZATION = True
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
        
        validMovements = []
        invalidMovements = []




        #Pushing an if condition to check depth and prevent reccursion limit override
        if len(snake) > 0 and currDepth<depth:
            
            board = self.board
            possibleFirstSteps = []
            totalSnakePossibleMovements = []

            """
            On each turn, the snake's head moves to one of the horizontally or vertically adjacent cells,
the second cell of the snake moves to the cell where the head was situated, the third cell
takes the former place of the second cell, etc. All these movements happen simultaneously,
so the head could potentially take the place of the tail.
            """


            #Adding all snake's possible first steps in a list to iterrate between next steps
            for key in snakeMovements:
                possibleFirstSteps.append([snake[0][0]+snakeMovements[key[0]][0],snake[0][1]+snakeMovements[key[0]][1]])

            
            #Getting all possible (l,r,d,u) snake movements for defined snake 


            for step in possibleFirstSteps:

                tempList = []
                tempList.append(step)

                for x in range(len(snake)-1):
                    tempList.append(snake[x])
                totalSnakePossibleMovements.append(tempList)

            for element in totalSnakePossibleMovements:
                unique_data = [list(x) for x in set(tuple(x) for x in element)]
                if element[0][0] > 0 and element[0][0] < board[0] + 1 and element[0][1] > 0 and element[0][1] < board[1]+1:
                    if len(unique_data) == len(snake):
                        validMovements.append(element)
                    

            for element in validMovements:
                totalValidMovements.append([element,currDepth+1])
                self.snakeMovementAction(element,board,currDepth+1,depth)
                

    def numberOfAvailableDifferentPaths(self):

        board = self.board
        snake = self.snake
        depth = self.depth

        self.snakeMovementAction(snake,board,0,depth)

        validPathsNum = 0
        for movement in totalValidMovements:
            if movement[-1] == depth:
                print(movement)
                validPathsNum += 1

                if VISUALIZATION == True:
                    print('Depth', depth)

                    counterMovement = 0
                    for x in range(1,board[0]+1):
                        for y in range(1,board[1]+1):
                            if [x,y] in movement[0]:
                                print(movement[0].index([x,y]), end=" ")
                                counterMovement += 1
                            else:
                                print('-', end=" ")
                        print('\n')
                

        
        
        
        print('Number of valid paths:',validPathsNum)
        return validPathsNum


