# Bingo
## How to play:
1. Enter the number of players or boards to be generated. 
2. Enter a name for each player
3. Press enter to generate a random letter-number combination. 
4. Continue clicking enter and generating a letter-number combination until someone gets BINGO.

## Bingo Explained:
BINGO is an old-fashioned game of chance. Each player is given a randomly generated BINGO board which contains 5 rows and 5 columns where the index of each column is B I N G O. Each square has a number that is randomly generated with certain constraints depending on which column it is located in. A host then calls out a code that is randomly generated which contains a letter (B, I, N, G, or O), which indicates the column followed by a number (example: B13). The players search their BINGO board for the number that has been called out and marks down the code that has been called if they have the code on their board. The first person to get 5 in a row either vertically, horizontally or diagonally must shout out "BINGO!" and they win the game!

Here is a link to a video on how BINGO works:
https://www.google.com/search?q=how+to+play+bingo&oq=how+to+play+bingo&aqs=chrome..69i57j0l7.1932j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_l1CcX8bsIOehytMP2NKYqAM21


Bingo needs to meet the conditions.

1. A board must contain 5 rows and 5 columns.
2. Players must have 5 points that form a straight line.
3. Players must use a newly generated BINGO board per game.
4. Each column letter can only have certain intervals of numbers. For example:
    Column B: Can only contain random numbers between 1-15.
    Column I: Can only contain random numbers between 16-30.
    Column N: Can only contain random numbers between 31-45.
    Column G: Can only contain random numbers between 46-60.
    Column O: Can only contain random numbers between 60-75.
5. There can be no repeating numbers on a BINGO board.



Bingo originated in Italy in the 16th century and spread to North America in the late 20th century. A toy salesman in New York officially named it Bingo (BINGO). This is a very old-fashioned gameplay, which is very common in lottery sales stores abroad. But in the era of big data, bingo games have gradually disappeared in casinos.



## Our Program:
First we needed to import numpy, pandas and random. 

### Creating BINGO boards:
We first created a function that created a dictionary where each key is a letter of BINGO (the diction() function). The diction() function calls the numbers() function to iterate through each key. The numbers() function generates 5 random numbers for each column whilst adhering to the constraints of each column using the numpy module. 'B' can only contain random numbers between 1-15, and 'I' can only be random numbers between 16-30, 'N' 31-45, 'G' 46-60, and 'O' is 61-75. Initially, the numbers() function would sometimes have repeating values in the column so we had to re-do the function. Intead of using random.randint(1,16) to choose a number for column 'B' we did default=random.sample(range(1,16),5) where default becomes a list of 5 values that have random integers chosen between the numbers of 1 and 15.
 
 ### numbers_check()
 Created another version of the numbers() function that would check to see if there were any duplicates in each column using the collections library. In order for this code to run you must replace it with the numbers() function and for every column on each BINGO board, it will print whether or not it had repeating values.
 
 ### Creating players:
 The players() function asks for input about how many players you would like to have and then asks for the name of each player, the names of each player is stored in a list. Based on the number of players, the players() function will then call the diction() function to create a new BINGO board for each player and convert these BINGO boards from dictionaries into dataframes using the pandas module. The boards and names of the players in a dictionary where the names of the players are the keys and the BINGO board dataframes are the values. The function then prints each player's name followed by their BINGO board.
 
 ### Creating the code generator:
 The generator() function is responsible for creating a unique code whilst following the constraints of each letter ('B' can only contain random numbers between 1-15, and 'I' can only be random numbers between 16-30, 'N' 31-45, 'G' 46-60, and 'O' is 61-75). The generator() function chooses a random letter (B, I, N, G, O) and based on what letter is chosen, must choose a random number that fits within the aforementioned constraints. The generator() function then calls the tracker() function which adds each code to a list in order to keep track of the codes that have already been called (we don't want any repeats) and then prints the code. The tracker() function checks to see if the code has already been called and if it has it will call the generator() function again until a code that has not already been called gets produced. The tracks() function also prints how many codes have been called so far (there will be 75 total).
 
Then there is a for loop that iterates over 75 times calling the generator function because that is how many codes there are (usually someone calls BINGO before all 75 are read).


### Bringing all functions together:
Adjustments and final touches had to be made because each function was independent of one another and had to be integrated with the rest of the program so that it could operate seamlessly. Each function had to call upon other ‘helper’ functions that needed to be connected properly so that the proper values were returned. The numbers() function had to be re-done because we had been returning repeating values in columns which is why we used the random.sample() function.
