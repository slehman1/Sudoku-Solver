from PuzzleClass import Puzzle
from sudoku import Sudoku

new_puzzle = Sudoku(3).difficulty(0.3)

myPuzzle = Puzzle(new_puzzle.board)
myPuzzle.initialize_puzzle()
myPuzzle.print_puzzle()
myPuzzle.three_by_three_starter()

myPuzzle.solve()
myPuzzle.print_puzzle()