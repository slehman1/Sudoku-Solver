from PuzzleClass import Puzzle
from sudoku import Sudoku

new_puzzle = Sudoku(3).difficulty(0.4)

myPuzzle = Puzzle(new_puzzle.board)
myPuzzle.initialize_puzzle()
myPuzzle.print_puzzle()
myPuzzle.three_by_three_starter()
myPuzzle.print_puzzle()

myPuzzle.solve()
myPuzzle.print_puzzle()
# myPuzzle.three_by_three_starter()
# counter = 0
# while True:
#     myPuzzle.random_solution()
#     done = myPuzzle.check_done()
#     counter += 1
#     print(counter)
#     if done:
#         break
# print(f"It took {counter} iterations")
# myPuzzle.print_puzzle()