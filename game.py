from main import snakeGame      
import time



def calculateSnakeMoves(board,snake,depth):

    snakeGame_ = snakeGame(board,snake,depth)
    funcReturn = snakeGame_.numberOfAvailableDifferentPaths()

    return funcReturn[1]


start_time = time.time()


sampleSnakeA = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
sampleBoardA = [4, 3]
sampleDepthA = 3

sampleSnakeB = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
sampleBoardB = [2, 3]
sampleDepthB = 10

sampleSnakeC = [[5,5], [5,4], [4,4], [4,5]]
sampleBoardC = [10, 10]
sampleDepthC = 4

calculateSnakeMoves(sampleBoardA,sampleSnakeA,sampleDepthA)
calculateSnakeMoves(sampleBoardB,sampleSnakeB,sampleDepthB)
calculateSnakeMoves(sampleBoardC,sampleSnakeC,sampleDepthC)


#Detailed usage of caluclateSnakeMoves
"""
sampleSnakeGame = snakeGame(sampleBoardA,sampleSnakeA,sampleDepthA)
sampleSnakeGame.numberOfAvailableDifferentPaths()

sampleSnakeGame = snakeGame(sampleBoardB,sampleSnakeB,sampleDepthB)
sampleSnakeGame.numberOfAvailableDifferentPaths()

sampleSnakeGame = snakeGame(sampleBoardC,sampleSnakeC,sampleDepthC)
sampleSnakeGame.numberOfAvailableDifferentPaths()

"""


stop_time = time.time()
totalTime = stop_time - start_time

print("Calculated sample snakes' paths in",round(totalTime, 5),'seconds')


#calculateSnakeMoves(,,,)
