import random

class Puzzle:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.puzzle = [[None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None]]
        self.solved = False

    def initialize_puzzle(self):
        for i in range(9):
            for j in range(9):
                self.puzzle[i][j] = self.puzzle_input[i][j]

    def print_puzzle(self):
        for i in range(9):
            for j in range(9):
                if j == 3 or j == 6:
                    print("|", end="")
                    print(f" {self.puzzle[i][j]} ", end="")
                else:
                    print(f" {self.puzzle[i][j]} ", end="")
            print("")
            if i == 2 or i == 5:
                for i in range(29):
                    print("-", end="")
                print("")

    def print_initial_puzzle(self):
        for i in range(9):
            for j in range(9):
                if j == 3 or j == 6:
                    print("|", end="")
                    if self.puzzle[i][j] == None:
                        print(f"  ", end="")
                    else:
                        print(f" {self.puzzle[i][j]} ", end="")
                else:
                    if self.puzzle[i][j] == None:
                        print(f"   ", end="")
                    else:
                        print(f" {self.puzzle[i][j]} ", end="")
            print("")
            if i == 2 or i == 5:
                for i in range(29):
                    print("-", end="")
                print("")

    def three_by_three_starter(self):
        '''Input top left coordinate of 3x3 and it will fill in possible'''
        possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        top_lefts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        # First find all the used numbers

        for top_left_tup in top_lefts:
            used_nums = []
            for rowz in range(3):
                for colz in range(3):
                    row_index = top_left_tup[0] + rowz
                    col_index = top_left_tup[1] + colz
                    if self.puzzle[row_index][col_index] != None and isinstance(self.puzzle[row_index][col_index],
                                                                                 list) != True:
                        used_nums.append(self.puzzle[row_index][col_index])
            # calculate openings
            openings = []
            for num in possible:
                if num not in used_nums:
                    openings.append(num)
            # fill none values with openings
            for rowz in range(3):
                for colz in range(3):
                    row_index = top_left_tup[0] + rowz
                    col_index = top_left_tup[1] + colz
                    if self.puzzle[row_index][col_index] == None:
                        self.puzzle[row_index][col_index] = openings

    def list_to_int(self):
        for i in range(9):
            for j in range(9):
                if isinstance(self.puzzle[i][j], list) and len(self.puzzle[i][j]) == 1:
                    self.puzzle[i][j] = self.puzzle[i][j][0]

    def row_solver(self):
        #for each row in the puzzle
        for i in range(9):
            new_row = []
            used_nums = []
            #for each column in the row append to used nums if an int
            for j in range(9):
                if isinstance(self.puzzle[i][j], int):
                    used_nums.append(self.puzzle[i][j])

            #go through each column and if its a list, removed used_nums from it
            for k in range(9):
                if isinstance(self.puzzle[i][k], int):
                    new_row.append(self.puzzle[i][k])
                else:
                    new_list = [num for num in self.puzzle[i][k] if num not in used_nums]
                    new_row.append(new_list)
            self.puzzle[i] = new_row
        self.list_to_int()

    def col_solver(self):
        #for each col in the puzzle
        for i in range(9):
            new_col = []
            used_nums = []
            #for each row in the col append to used nums if an int
            for j in range(9):
                if isinstance(self.puzzle[j][i], int):
                    used_nums.append(self.puzzle[j][i])

            #go through each row and if its a list, removed used_nums from it
            for k in range(9):
                if isinstance(self.puzzle[k][i], int):
                    new_col.append(self.puzzle[k][i])
                else:
                    new_list = [num for num in self.puzzle[k][i] if num not in used_nums]
                    new_col.append(new_list)
            for z in range(9):
                self.puzzle[z][i] = new_col[z]
        self.list_to_int()

    def three_by_three_solver(self):
        '''Input top left coordinate of 3x3 and it will fill in possible'''
        top_lefts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        # First find all the used numbers
        for top_left_tup in top_lefts:
            used_nums = []
            new_3x3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for rowz in range(3):
                for colz in range(3):
                    row_index = top_left_tup[0] + rowz
                    col_index = top_left_tup[1] + colz
                    if isinstance(self.puzzle[row_index][col_index], int):
                        used_nums.append(self.puzzle[row_index][col_index])

            # fill in our 3x3 values with openings
            for rowz in range(3):
                for colz in range(3):
                    row_index = top_left_tup[0] + rowz
                    col_index = top_left_tup[1] + colz
                    if isinstance(self.puzzle[row_index][col_index], int):
                        new_3x3[rowz][colz] = self.puzzle[row_index][col_index]
                    else:
                        new_list = [num for num in self.puzzle[row_index][col_index] if num not in used_nums]
                        new_3x3[rowz][colz] = new_list

            #copy over our 3x3
            for rowz in range(3):
                for colz in range(3):
                    row_index = top_left_tup[0] + rowz
                    col_index = top_left_tup[1] + colz
                    self.puzzle[row_index][col_index] = new_3x3[rowz][colz]
        self.list_to_int()

    def row_list_one_instance(self):
        '''The goal of this function is to go through the puzzle by row,
        checking the lists and counting the values in the lists, if any value has a single count then it must be
        placed in the spot where the list is. V1 flaw was that '''
        #for each row
        for i in range(9):
            #initialize a map
            myMap = {}
            #go through each column
            for j in range(9):
                if isinstance(self.puzzle[i][j], list):
                    for num in self.puzzle[i][j]:
                        if num in myMap:
                            myMap[num] += 1
                        else:
                            myMap[num] = 1
            #loop through map and see if any values are 1
            nums_to_replace = []
            for k,v in myMap.items():
                if v == 1:
                    nums_to_replace.append(k)
            #loop through column again and replace any lists that have the item with it
            for k in range(9):
                if isinstance(self.puzzle[i][k], list):
                    for num in nums_to_replace:
                        if num in self.puzzle[i][k]:
                            self.puzzle[i][k] = num
                            #need to update all list to show range so that in downstream iterations they account for the
                            #new value else you can get double
                            self.row_solver()
                            self.col_solver()
                            break

    def col_list_one_instance(self):
        # for each col
        for i in range(9):
            # initialize a map
            myMap = {}
            # go through each row
            for j in range(9):
                if isinstance(self.puzzle[j][i], list):
                    for num in self.puzzle[j][i]:
                        if num in myMap:
                            myMap[num] += 1
                        else:
                            myMap[num] = 1
            # loop through map and see if any values are 1
            nums_to_replace = []
            for k, v in myMap.items():
                if v == 1:
                    nums_to_replace.append(k)
            # loop through row again and replace any lists that have the item with it
            for k in range(9):
                if isinstance(self.puzzle[k][i], list):
                    for num in nums_to_replace:
                        if num in self.puzzle[k][i]:
                            self.puzzle[k][i] = num
                            self.row_solver()
                            self.col_solver()
                            break





    def check_done(self):
        for i in range(9):
            for j in range(9):
                if isinstance(self.puzzle[i][j], list):
                    return False
        for i in range(9):
            row_sum = sum(self.puzzle[i])
            if row_sum != 45:
                return False

        for i in range(9):
            col_sum = 0
            for j in range(9):
                col_sum += self.puzzle[j][i]
            if col_sum != 45:
                return False
        return True

    def solve(self):
        counter = 0
        while counter < 40:
            self.row_solver()
            self.col_solver()
            self.three_by_three_solver()
            self.row_solver()
            self.col_solver()
            self.three_by_three_solver()
            self.row_solver()
            self.col_solver()
            self.three_by_three_solver()
            self.print_puzzle()
            self.row_list_one_instance()
            self.print_puzzle()
            self.row_solver()
            self.col_solver()
            self.three_by_three_solver()
            self.col_list_one_instance()
            self.print_puzzle()
            self.solved = self.check_done()
            if self.solved:
                print(f"You win! It took {counter} iterations!")
                break
            counter += 1
            print(counter)
            self.print_puzzle()
            if counter % 50 == 0:
                self.print_puzzle()
                self.stuck()
            if counter > 100:
                break

    def stuck(self):
        '''Run this method if you get stuck in a loop where multiple end options work to win, just have to choose one'''
        #randomly pick one option from list
        for i in range(9):
            for j in range(9):
                if isinstance(self.puzzle[i][j], list):
                    self.puzzle[i][j] = self.puzzle[i][j][0]
                    return

    def random_solution(self):
        for i in range(9):
            for j in range(9):
                if isinstance(self.puzzle[i][j], list):
                    self.puzzle[i][j] = random.choice(self.puzzle[i][j])

    def random_possibilities_solution(self):
        '''For each row randomly put a number 1-9, but remove that from the list as you go thru'''
        for i in range(9):
            possibilites = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                if self.puzzle[i][j] == None:
                    random_num = random.choice(possibilites)
                    self.puzzle[i][j] = random_num
                    possibilites.remove(random_num)



