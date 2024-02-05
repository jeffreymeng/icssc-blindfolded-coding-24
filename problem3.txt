## Problem 3. The Mysterious Maze

Your team has been trapped in a mysterious maze! The only way out is to solve a series of coding challenges that will unlock the exit. The challenge is to write a function that can navigate through the maze.

The maze is a 2D grid represented as a list of lists in Python. Each cell in the grid can be either 0 (open path), 1 (wall), or 9 (exit). The function should return a list of moves to reach the exit. The moves are represented as strings: "UP", "DOWN", "LEFT", "RIGHT".

Here's an example of what the maze might look like:

 [ [0, 0, 1, 0], 
   [1, 0, 0, 0], 
   [0, 1, 9, 1], 
   [1, 0, 0, 0] ]

In this maze the exit is at (2,2) [It is based on index values and not direct coordinates]

For this problem you will have to solve 2 mazes.

Maze 1: Starting Coordinates (1,2) [Index Values]

[ [0, 0, 1, 1, 9],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 0] ]

Maze 2: Starting Coordinates (4,4) [Index Values]

[ [0, 0, 0, 1, 9],
  [0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1],
  [1, 0, 0, 0, 0] ]