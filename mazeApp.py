# MazeApp is an application that creates, solves, and prints a maze.
# Code based upon the example by Lewis & Chase.
#
# Note: See the documentation for the the toString() method of
#       the Maze class for the display format for a maze.
#
# author S. Sigman
# version 1.0 3/3/2023

from maze import Maze

if __name__ == "__main__":
    maze = Maze()  # make a new maze obj

    print("The original maze:")
    print(maze)

    maze.traverse()
    print("The solved maze:")
    print(maze)

