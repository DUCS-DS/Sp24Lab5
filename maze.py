# Adapted from Lewis and Chase, Java Software
# Structures: Designing and Using Data Structures.
#
# Author:  S. Sigman
# version: 1.0 (3/3/2023)
#
# Modifications:
# 3/19/2023 Changed the name of toString to __str__.
#           S. Sigman
# 3/24/2024 Refactored by Simmons

from stack import Stack

class Maze:
    """Traverse and print a solved maze.

    Upon instantiation of this class, the following grid of zeros
    and ones is created:

                   0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                   0 1 1 1 0 1 0 0 0 1 1 1 1 1 1 1 0
                   0 1 0 0 0 1 0 1 1 1 0 0 0 1 0 1 0
                   0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0
                   0 0 0 0 0 1 1 1 0 1 0 1 0 1 0 1 0
                   0 1 1 1 0 1 1 1 0 1 0 1 1 1 0 1 0
                   0 1 0 1 0 0 0 0 0 1 0 0 0 1 0 1 0
                   0 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0
                   0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
                   0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
                   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0

    The grid represents a maze as follows:

           0 indicates a wall.
           1 indicates a valid next position during traversal.

    The starting position for a traversal of the maze is (0,1)
    near the upper left corner.  The maze is solved when a tra-
    versal reaches the exit position near the lower right corn-
    er.  A valid traversal cannot go through walls, of course.

    The traverse method below finds a path through the maze. It
    modifies the grid:

           2 indicates a position has been visited
           3 indicates a position is part of the solution path
    """

    def __init__(self):
        """Set up the grid for the maze and set some constants."""

        self.WALL = 0
        self.UNVISITED = 1
        self.VISITED = 2
        self.PATH = 3

        self.grid = \
            [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
             [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

        self.ENTRY = (0, 1)
        self.ROWS = len(self.grid)
        self.COLS = len(self.grid[0])
        self.EXIT = (self.ROWS - 1, self.COLS - 2)

        # Mark the initial position as visited
        self.grid[self.ENTRY[0]][self.ENTRY[1]] = self.VISITED

    def traverse(self):
        """Traverse the maze.

        This method modifies self.grid by first marking the positions of
        a successful traversal with self.VISITED, and then re-marking the
        positions (with self.PATH) of the same traversal but without any
        retracements.
        """
        stack = Stack()
        stack.push(self.ENTRY)
        while stack.peek() != self.EXIT:
            break # delete this line

            # your code goes here that finds a successful traversal
            # and marks each position along it with self.VISITED.

        #  Your code goes here that re-marks the traversal above
        #  with self.PATH indicating the positions of the final
        #  path (without retracements).

    def isMoveValid(self, nextPos):
        """Return True if nextPos is a valid move; otherwise, return False.

        The argument to nextPos is a valid move if
            - it is not a wall, and
            - it has not been visited previously, and
            - is within the maze.
        """
        valid = 0 <= nextPos[0]
        if valid:
            value = self.grid[nextPos[0]][nextPos[1]]
        return valid and value != self.WALL and value != self.VISITED

    def nextMove(self, curPos):
        """Return a valid move or None.

        This method first checks the validity of the position to the east
        of curPos, then it looks south, then west, then north.
        """
        if self.isMoveValid((curPos[0], curPos[1]+1)):
            return (curPos[0], curPos[1]+1)
        if self.isMoveValid((curPos[0]+1, curPos[1])):
            return (curPos[0]+1, curPos[1])
        if self.isMoveValid((curPos[0], curPos[1]-1)):
            return (curPos[0], curPos[1]-1)
        if self.isMoveValid((curPos[0]-1, curPos[1])):
            return (curPos[0]-1, curPos[1])
        return None

    def __str__(self):
        """Return a string representation of the maze.

        The solved maze is rendered to a string as follows:
            - Walls are represented with periods.
            - Unvisited positions are represented with spaces.
            - The solution path is represented with *s.
            - Paths that had to be retraced are represented with +s.
        """
        d = {self.WALL:'.', self.UNVISITED:' ', self.VISITED:'+', self.PATH:'*'}
        mazeStr = "\n"
        for row in self.grid:
            for colVal in row:
                mazeStr += d[colVal] + " "
            mazeStr += "\n"
        return mazeStr
