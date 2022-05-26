from main import snakeGame      

sampleSnakeA = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
sampleBoardA = [4, 3]
sampleDepthA = 3

sampleSnakeB = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
sampleBoardB = [2, 3]
sampleDepthB = 10

sampleSnakeC = [[5,5], [5,4], [4,4], [4,5]]
sampleBoardC = [10, 10]
sampleDepthC = 4


sampleSnakeGame = snakeGame(sampleBoardA,sampleSnakeA,sampleDepthA)
sampleSnakeGame.numberOfAvailableDifferentPaths()
sampleSnakeGame = snakeGame(sampleBoardB,sampleSnakeB,sampleDepthB)
sampleSnakeGame.numberOfAvailableDifferentPaths()

sampleSnakeGame = snakeGame(sampleBoardC,sampleSnakeC,sampleDepthC)
sampleSnakeGame.numberOfAvailableDifferentPaths()
