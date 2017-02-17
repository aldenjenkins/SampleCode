import random

"""
    Author: Alden Jenkins
    Title: Airline Flight Scheduling Documentation
    Creation Date: 6/25/16
"""

def randomizeColors(colors, amtColors):
    randomColors = []
    for i in range(amtColors):
        randomColors.append(colors[random.randint(0, len(colors)-1)])
    print(randomColors)
    return randomColors
        
# Returns a valid, non-string integer
def getValidInt(strng):
    correctInt = False
    while not correctInt:
        try:
            intgr = int(input(strng))
            correctInt = True
        except ValueError:
            print("Please enter a valid integer\n")
    return intgr

# Gets the guesses of the colors for the amount of guesses specified by the user
def queryGuesses(numGuesses):
    # The guesses list should hold each of the user's guesses in the order in 
    # which they were guessed and should not contain any numbers which do not
    # correspond to a shown color
    guesses  = []
    errorMsg = "Please enter one of the integers shown.\n" 
    # Library used to link guesses to actual strings of the respective color
    querySelections = {0: "red"   ,
                       1: "orange",
                       2: "yellow",
                       3: "green" ,
                       4: "blue"  ,
                       5: "purple"}
    for i in range(numGuesses):
        # Try Catch block to make sure the user enters a number for a valid color
        validGuess = False
        while not validGuess:
            selection = getValidInt("Make a guess of four colors:     \n" \
                                    "0 - red                          \n" \
                                    "1 - orange                       \n" \
                                    "2 - yellow                       \n" \
                                    "3 - green                        \n" \
                                    "4 - blue                         \n" \
                                    "5 - purple                       \n" \
                                    "----------------------------     \n" )
            # If the selection corresponds to a correct color...
            if selection in querySelections.keys():
                # append the color (not the integer) to the list of guesses
                guesses.append(querySelections.get(selection))
                validGuess = True
            else:
                print(errorMsg)
    print("Your guess is:\n", guesses)
    return guesses
    
def calculateClue(guesses, colors):
    clue                 = [] 
    leftOverColors       = colors[:]
    correctColCorrectPos = False
    correctColWrongPos   = False
    AllCorrect           = True
    for i in range(len(guesses)):
        if guesses[i] == colors[i]:
            correctColCorrectPos = True
            leftOverColors[i] = ""
        if guesses[i] != colors[i]:
                AllCorrect = False
    for i in range(len(guesses)):
        for k in range(len(leftOverColors)):
            if guesses[i] == leftOverColors[k]:
                correctColWrongPos = True
            
    if correctColWrongPos == True:
        clue += [1]
    if correctColCorrectPos == True:
        clue += [2]
    if AllCorrect:
        clue = [0]
    print(clue)
    return clue
    
def main():
    ALL_COLORS    = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    amtColors     = getValidInt("Select the difficulty (amount of pegs): (Eg. 4): ")
    randomColors  = randomizeColors(ALL_COLORS, amtColors)
    correct       = False
    while not correct:
        guessedColors = queryGuesses(amtColors)
        clue = calculateClue(guessedColors, randomColors)
        if clue == [0]:
            correct = True
    print("Great job! You guessed correctly!")
    
main()