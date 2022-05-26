from itertools import count
from random import sample
from signal import raise_signal
from sys import exc_info
from typing import Counter
from xmlrpc.client import Boolean
import time

snakeMovements = {'L':[-1,0],'R':[1,0],'D':[0,-1],'U':[0,1]}

VISUALIZATION = False



class snakeGame(object):

    #__init__ function defining board, snake and depth, as well as imposing constraints on variables

    def __init__(self, board: list, snake: list, depth: int, currDepth = 0):
    
        #reversing nXm table to mXn
        board.reverse()

        self.snake = snake
        self.board = board
        self.depth = depth
        self.currDepth = currDepth

        global totalValidMovements
        totalValidMovements = []


        #constraint: board.length = 2
        if len(board) != 2:
            raise IndexError(f"in board definition, {len(board)} dimensions instead of 2")

        #Board dimension constraint 1 ≤ board[i] ≤ 10
        for dimension in self.board:

            if isinstance(dimension,int):
                pass
            else:
                raise TypeError(f"in  Board definition {dimension}")

            if dimension < 1 or dimension > 10:
                raise IndexError(f"Board definition unsuccessful, {dimension} out of range")

        #Snake constraint: 3 ≤ ​snake.length​ ≤ 7,
        if len(snake)<3 or len(snake)>7:
            raise IndexError(f"snake list out of range")
        
        #Snake constraint: snake[i].length​ = 2,
        for coordinatesPath in self.snake:
            if len(coordinatesPath) != 2:
                raise TypeError(f"in Snake definition {dimension}")

        #Depth constraint: 1 ≤ depth ≤ 20
        if depth<1 or depth>20:
            raise TypeError(f"in Depth definition, Depth can not be {dimension}")
            
               
    def snakeMovementAction(self,snake,currDepth,depth):

        board = self.board        
        validMovements = []

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
            
            #Getting all possible (l,r,d,u) snake movements for iterrated first steps
            for step in possibleFirstSteps:

                tempList = []

                tempList.append(step)
                for x in range(len(snake)-1):
                    tempList.append(snake[x])

                totalSnakePossibleMovements.append(tempList)
            
            #Removing overlapping tiles
            for element in totalSnakePossibleMovements:
                unique_data = [list(x) for x in set(tuple(x) for x in element)]

                if element[0][0] > 0 and element[0][0] < board[0] + 1 and element[0][1] > 0 and element[0][1] < board[1]+1:
                    if len(unique_data) == len(snake):
                        validMovements.append(element)
                    
            #Adding elements to total valid movements lists
            for element in validMovements:
                totalValidMovements.append([element,currDepth+1])

                #Recursion in snake movement action
                self.snakeMovementAction(element,currDepth+1,depth)
                
    #Main game function, calling snakeMovementAction function and calculating available paths number 
    def numberOfAvailableDifferentPaths(self):

        validPaths = []

        board = self.board
        snake = self.snake
        depth = self.depth

        #calling snakeMovement action, generating totalValidMovements list
        self.snakeMovementAction(snake,0,depth)

        #Excluding movements with movementDepth < depth
        for movement in totalValidMovements:
            if movement[-1] == depth:
                validPaths.append(movement[0])

        #Finding unique paths, sorting valid paths and excluding same trajectory paths
        uniquePaths = []
        for element in validPaths:

            elementToAdd = sorted(element)
            if elementToAdd not in uniquePaths:
                uniquePaths.append(sorted(element))

                #Visualization
                if VISUALIZATION == True:
                    
                    print('Solution',elementToAdd)

                    for x in range(1,board[0]+1):
                        print('|', end=" ")
                        for y in range(1,board[1]+1):
                            
                            if [x,y] in element:
                                print(element.index([x,y]), end=" ")
                            else:
                                print('-', end=" ")
                        print('|\n')


        print('Depth', depth)
        print('Number of valid paths:',len(validPaths))
        print('Number of unique paths:',len(uniquePaths))

        
        return len(validPaths),len(uniquePaths)

