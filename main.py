import numpy as np
import pandas as pd
import random
import collections

"""
def numbers_check(l:str):
    # This function is a copy of the other numbers() function that was used to test if there were any duplicates
    # within each column.
    default=[]
    if l=='B':
        default=random.sample(range(1,16),5)  
        a = [item for item, count in collections.Counter(default).items() if count > 1]
        if not a:
            print("There is no duplicate element under 'B'.")

        return default
    if l=='I':
        default=random.sample(range(16,31),5)
        a = [item for item, count in collections.Counter(default).items() if count > 1]
        if not a:
            print("There is no duplicate element under 'I'.")
        return default
    if l=='N': 
        default=random.sample(range(31,46),5)
        a = [item for item, count in collections.Counter(default).items() if count > 1]
        if not a:
            print("There is no duplicate element under 'N'.")
        return default
    if l=='G':
        default=random.sample(range(46,61),5)
        a = [item for item, count in collections.Counter(default).items() if count > 1]
        if not a:
            print("There is no duplicate element under 'G'.")
        return default
    if l=='O':
        default=random.sample(range(61,76),5)
        a = [item for item, count in collections.Counter(default).items() if count > 1]
        if not a:
            print("There is no duplicate element under 'O'.")
        return default
"""


def numbers(l: str):
    # This function checks to see what letter l is. For example, 'B' can only contain numbers between
    # 1-15, and 'I' can only be numbers 16-30, 'N' 31-45, 'G' 46-60, and 'O' is 61-75
    # Also makes the numbers for the bingo board random and the for loop is to create 5 random numbers
    # random.sample(range(1,16),5) will create a list of 5 random numbers between 1 and 15 and will not repeat
    default = []
    if l == 'B':
        default = random.sample(range(1, 16), 5)
        return default
    if l == 'I':
        default = random.sample(range(16, 31), 5)
        return default
    if l == 'N':
        default = random.sample(range(31, 46), 5)
        return default
    if l == 'G':
        default = random.sample(range(46, 61), 5)
        return default
    if l == 'O':
        default = random.sample(range(61, 76), 5)
        return default


def diction():
    # Generate the dictionary and does so by setting each board index (each letter)
    # equal to the 5 randomly chosen numbers from the previous function^
    board = {'B':
                 [],
             'I':
                 [],
             'N':
                 [],
             'G':
                 [],
             'O':
                 []}
    letters = list(board.keys())
    for i in board.keys():
        # board[i]=numbers(i)
        board[i] = numbers(i)
    return board


def players():
    # This function will ask for user input of how many players and each players name, and store their names in a
    # temporary list. The function will then call the previous function to create new randomly generated bingo board
    # for each player. The function then converts the bingoboard generated from the diction() function and
    # turns it into a DataFrame. Then it stores the new board and name in a dictionary where the name is the key and
    # the board is the value.
    users = []
    boards = {}
    num_of_players = eval(input("How many players do you want? "))
    for i in range(0, num_of_players):
        name = input("Enter your name: ")
        users.append(name + ':')
    for i in users:
        # iterates based on number of users^. Below it creates the new board by calling the diction function
        # and plugs it into the DataFrame module.
        df = pd.DataFrame(diction(), columns=['B', 'I', 'N', 'G', 'O'], index=['1', '2', '3', '4', '5'])
        boards[i] = df
    for i in boards:
        print(i)
        print(boards[i])
    return boards


tracks = []


def tracker(code: str):
    # Gets called and gets passed a code. The code is then added to a list and printed for the host person to call out
    # the function also checks to see if the code has already been called (sees if it is in the list) and if it is in
    # this list, it will call a new code via the generator() function.
    # This function also prints how many codes have been called so far so you know how far in a game you are
    if code in tracks:
        generator()
    else:
        tracks.append(code)
        print(code)
        print(str(len(tracks)) + " codes have been called so far!")


def generator():
    # This function generates a random number based on the contraints already explained above for each column.
    # It chooses a random number from BINGO and based on the letter chooses a random numbers based on the contraints
    # of the letter. (i.e. Column B can only contain random numbers between 1-15, column C 16-30 etc.)
    chooser = ['B', 'I', 'N', 'G', 'O']
    instance = chooser[random.randint(0, 4)]

    if instance == 'B':
        number = random.randint(1, 15)
    elif instance == 'I':
        number = random.randint(16, 30)
    elif instance == 'N':
        number = random.randint(31, 45)
    elif instance == 'G':
        number = random.randint(46, 60)
    elif instance == 'O':
        number = random.randint(61, 75)
    code = (instance + str(number))
    tracker(code)


players()

for i in range(75):
    # for loop generates 75 numbers because that is how many options there are.
    input("Press enter to call new code!")
    generator()