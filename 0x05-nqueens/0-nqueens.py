#!/usr/bin/python3
""" module docs """
from sys import argv, exit

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    queens = argv[1]

    try:
        queens = int(queens)
    except ValueError:
        print("N must be a number")
        exit(1)

    if queens < 4:
        print("N must be at least 4")
        exit(1)

    solution = []

    def nqueens(row, queens, solution):
        """ method docs """
        if (row == queens):
            print(solution)
        else:
            for col in range(queens):
                pos = [row, col]
                if validposition(solution, pos):
                    solution.append(pos)
                    nqueens(row + 1, queens, solution)
                    solution.remove(pos)

    def validposition(solution, position):
        """ method docs """
        for queen in solution:
            if queen[1] == position[1] or \
                (queen[0] - queen[1]) == (position[0] - position[1]) or \
                    (queen[0] + queen[1]) == (position[0] + position[1]):
                return False
        return True

    nqueens(0, queens, solution)
