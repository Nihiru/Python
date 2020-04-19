import math
def minimum_path_sum(grid):
    height = len(grid)
    weight = len(grid[0])
    dp = [[0] * weight] * height
    for row in range(len(height)):
        for col in range(len(weight)):
            if row == 0 and col == 0:
                dp[row][col] = grid[row][col]
            else:
                dp[row][col] = grid[row][col] + min((math.inf  if row == 0  else dp[row-1][col]), (math.inf if col == 0 else dp[row][col-1]))

    return dp[height -1][weight-1]
