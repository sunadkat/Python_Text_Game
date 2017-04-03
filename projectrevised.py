import random
#############################################################################################
def read_string_list_from_file(the_file):
    fileRef = open(the_file,"r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line                          
        localList.append(string)  # adds string to list
    fileRef.close()          
    return localList

def create_lists_board(listStrings, pythShnLc, playLoc):
    biomeLength = len(listStrings)
    board = ["Biome#    Diam     Sword    Enemy"]
    for i in range(biomeLength):
        x = listStrings[i]
        dashLoc = x.find("-")
        diam = x[0:dashLoc]  #finds the dash in the list
        line  = ""
        if len(diam) == 1:
            diam = str(diam) + " "
        sword = x[(dashLoc + 1)]
        enemy = x[(dashLoc + 3)]
        if pythShnLc >= 0 and pythShnLc <= 7: #creates board by converting parts of list to str
            if pythShnLc > 0:
                if pythShnLc == i:  #adds <== PythonShine to str
                    line = str(i) + "         " + diam + "      " + str(sword) + "        " + str(enemy) + "<=== PythonShine"
                else:
                    line = str(i) + "         " + diam + "      " + str(sword) + "        " + str(enemy)
            else:
                line = str(i) + "         " + diam + "      " + str(sword) + "        " + str(enemy)
            if playLoc == i:  #adds <--- Player to str
                line = line + "<--- Player"
            if len(diam) == 3:
                line = line[:13] + line[14:]
            if len(diam) == 4:
                line = line[:14] + line[15:]
        board = board + [line] #continuously concatenates lines of the board
    return board

def show_board(mssg): #prepares the board for printing
    boardstring = ""
    for i in range(len(mssg)):
        boardstring = boardstring + mssg[i] + "\n"
    message = "The board currently contains:\n" + boardstring
    return message

#Error checks the corresponding var
def pythonShineLoc_check(pythonShineLoc):
    while pythonShineLoc.isdigit() == False or int(pythonShineLoc) > 7 or int(pythonShineLoc) < 0:
            pythonShineLoc = raw_input("What position shall PythonShine be in? (1-7, 0 for no effect): ")
    return pythonShineLoc

def lifePoints_check(lifePoints):
    while lifePoints.isdigit() == False or int(lifePoints) > 50 or int(lifePoints) < 10:
            lifePoints = raw_input("Initial life points? (10-50): ")
    return lifePoints       

def turnstr_check(turnstr):
    while turnstr.isdigit() == False or int(turnstr) > 10 or int(turnstr) < 1:
        turnstr = raw_input("How many turns would you like to play? (1-10): ")
    return turnstr

def player_data(turnNum, playerName, lifePoints, swordPower, diamondsAmount, playerLoc): #prints player data
    print
    print "Showing player info for turn: " + str(turnNum)
    print
    print "The player '" + str(playerName) + "'"
    print "currently has: " + str(lifePoints) + " life points,"
    if swordPower == 0:
        print "no sword,"
    else:
        print "a sword of power " + str(swordPower) + ","
    print "has " + str(diamondsAmount) + " diamonds,"
    print "and is in the position: " + str(playerLoc)
    print
    
def movements(): #Decides how far the player should move
    forward = raw_input("Roll die, or enter position (d/u): ")
    while forward != "d" and forward != "u":
        forward = raw_input("Please enter (d/u): ")
    if forward == "d":
        movement = random.randint(1, 6)
    if forward == "u":
        movement = raw_input("Move forward how many spaces? (1-7): ")
        while movement.isdigit() == False:
            movement = raw_input("Please enter a number from 1-7: ")
        movement = int(movement)
        while movement > 7 or movement < 1:
            movement = input("Please enter a number from 1-7: ")
    return str(movement)

def fight(swordPower, enemyPower, lifePoints): #calculates life points gained/lost from fight
    if enemyPower > swordPower:
        damage = random.randint(1, lifePoints)
        print "The player has lost the fight and lost " + str(damage) + " life points."
        lifePoints = lifePoints - damage
        print "The player now has " + str(lifePoints) + " life points."
    if enemyPower == swordPower:
        if (lifePoints % 2) == 0:
            damage = random.randint(1, (lifePoints / 2))
        if (lifePoints % 2) == 1:
            damage = random.randint(1, (lifePoints / 2) + 1)
        print "The player has tied the fight and lost " + str(damage) + " life points."
        lifePoints = lifePoints - damage
        print "The player now has " + str(lifePoints) + " life points."
    if enemyPower < swordPower:
        damage = random.randint(1, lifePoints)
        print "the player has won the fight and gained " + str(damage) + " life points."
        lifePoints = lifePoints + damage
        print "The player now has " + str(lifePoints) + " life points."
    return lifePoints

def catastrophe_chance(listStrings): #calculates chance of catastrope (~1/5)
    numberBiomes = len(listStrings)
    chance = int(numberBiomes) * 5
    biomeSelection = random.randint(1, chance)
    return biomeSelection

def surprise_chance(listStrings):#calculates chance of surprise (~1/100)
    range = int(len(listStrings)) * 5
    chance = random.randint(1, range)
    return chance

def endgame_results(playerName, lifePoints, swordPower, diamondsAmount, playerLoc, won, cataCount, surpriseCount): #prints some of end of game results
    print
    print "Showing end of game player info:"
    print "The player '" + str(playerName) + "'"
    print "currently has: " + str(lifePoints) + " life points,"
    print "has a sword of sword power: " + str(swordPower) + ","
    print "has " + str(diamondsAmount) + " diamonds,"
    print "and is in the position: " + str(playerLoc)
    if won == 1 or won == 3:
        print "You are alive."
    if won == 2:
        print "You are dead."
    print str(cataCount) + " catastrophes happened and " + str(surpriseCount) + " surprises occured" 
    print
    replay = raw_input("Do you want to play again? (y/n): ")
    while replay != "y" and replay != "n":
        replay = raw_input("Do you want to play again? (y/n): ")
    return replay
    
def end_results(playerName, gameNumber, win, listStrings): #prints End of end of game results
    print "RESULTS OF ALL GAMES"
    print
    print "'" + str(playerName) + "'" + " played " + str(gameNumber) + " games in total."
    print "of those, '" + str(playerName) + "' won " + str(win)
    print "A conversion from binary -> decimal will now take place,"
    print "Using the diamonds from the last game board"
    print
    listStringLength = len(listStrings)
    diamondList = []
    for i in range(listStringLength):
        dashLocat = listStrings[i].find("-")
        diamondList = diamondList + [listStrings[i][0:dashLocat]]
    print "List with diamonds: " + str(diamondList)
    diamondListLength = len(diamondList)
    binList = diamondList[playerLoc:diamondListLength]
    integer = 0
    for i in range(len(binList)):
        integer = integer + int(binList[i])
    binInteger = str(bin(integer))
    binIntegerB = binInteger.find("b")
    binInteger = str(binInteger[binIntegerB + 1:])
    binIntegerList = []
    if diamondListLength > len(binInteger):
            binIntegerLength = len(binInteger)
            addZeroes = diamondListLength - binIntegerLength
            Zeroes = int(addZeroes) * "0"
            for i in range(addZeroes):
                binIntegerList = binIntegerList + [Zeroes[i]]
    for i in range(len(binInteger)):
        binIntegerList = binIntegerList + [binInteger[i]]
    print "Corresponding Binary: " + str(binIntegerList)
    print "Converted to decimal, this is: " + str(integer)
    print
    print
    print "Thank you for playing."

##############################################################################################
################################################################################
#Starting text - asks for information from the player mostly
play = raw_input("Would you like to play? (y/n): ")
pythonShineLoc = 0 #sets certain values to default
playerLoc = -1
gameNumber = 1
cataCount = 0
surpriseCount = 0
win = 0
replay = "y"
if play == "y":
    while replay == "y":
        showboard = raw_input("Would you like to draw the board? (y/n): ")
        while showboard != "y" and showboard != "n":
            showboard = raw_input("Would you like to draw the board? (y/n): ")
        biometext = raw_input("Type the name of the board file including '.txt' or 'd' for default: ") 
        print
        if biometext == "d":
            biometext = "biomesData1.txt"
        listStrings = read_string_list_from_file(biometext)
        biome = create_lists_board(listStrings, int(pythonShineLoc), playerLoc)
        if showboard == "y":
            board = show_board(biome)
            print board
        pythonShineLoc = raw_input("What position shall PythonShine be in? (1-7, 0 for no effect): ")
        pythonShineLoc = pythonShineLoc_check(pythonShineLoc)
        playerName = raw_input("What is your name? ")
        lifePoints = raw_input("Initial life points? (10-50): ")
        lifePoints = lifePoints_check(lifePoints)
        turnstr = raw_input("How many turns would you like to play? (1-10): ")
        turnstr = turnstr_check(turnstr)
        turn = int(turnstr)
        catas = raw_input("Allow catastrophes? (y/n): ")
        while catas != "y" and catas != "n":
            catas = raw_input("Allow catastrophes? (y/n): ")
        surprise = raw_input("Allow surprises? (y/n): ")
        while surprise != "y" and surprise != "n":
             surprise = raw_input("Allow surprises? (y/n): ")

        #Default character information
        turnNum = 1
        playerLoc = 0
        swordPower = 0
        diamondsAmount = 0
        won = 3
        
        for i in range(turn):
            #Printing player data
            print "\nCommencing turn " + str(turnNum) + ":"
            biome = create_lists_board(listStrings, int(pythonShineLoc), playerLoc)
            if showboard == "y":
                board = show_board(biome)
                print board
            playerdata = player_data(turnNum, playerName, lifePoints, swordPower, diamondsAmount, playerLoc)

            #Player movement
            movement = int(movements())
            playerLoc = playerLoc + movement
            biomeLength = len(listStrings)
            if playerLoc >= biomeLength:
                playerLoc = playerLoc % biomeLength
            print "The player is now in biome: " + str(playerLoc)

            #PythonShine win
            if playerLoc == int(pythonShineLoc) and playerLoc > 0:
                print "The player has arrived in Python Shine."
                print
                won = 1
                lifePoints = 9999
                diamondsAmount = 9999
                break
            else:
                #Diamond/sword collection, enemy fighting
                lifePoints = int(lifePoints)
                #takes listString[playerLocation], extracts the diamond number, and changes it accordingly
                dashLoc = listStrings[playerLoc].find("-")
                playerBiome = listStrings[playerLoc]
                diamondsAmount = diamondsAmount + (int(playerBiome[0:dashLoc]) / 3)
                diamondsCollected = (int(playerBiome[0:dashLoc]) / 3)
                diamondsRemaining = int(playerBiome[0:dashLoc]) - diamondsCollected
                newBiomeData = str(diamondsRemaining) + "-" + str(playerBiome[dashLoc + 1]) + "-" + str(playerBiome[dashLoc + 3])
                listStrings[playerLoc] = newBiomeData
                print "The player now has " + str(diamondsAmount) + " diamonds."
                if swordPower < int(playerBiome[(dashLoc + 1)]):
                    swordPower = int(playerBiome[(dashLoc + 1)])
                    print "The player has upgraded their sword to a sword power of " + str(swordPower)
                enemyPower = int(playerBiome[(dashLoc + 3)])
                lifePoints = fight(swordPower, enemyPower, lifePoints)
                print
                
                #Game Over
                if lifePoints == 0:
                    print "Game over"
                    won = 2
                    print
                    break
                
                #Catastrophe
                if catas == "y":
                    catasBiome = int(catastrophe_chance(listStrings))
                    if catasBiome - 1 <= (biomeLength - 1):
                        cataCount = cataCount + 1
                        if catasBiome == playerLoc:
                            print "A catastrophe has killed you."
                            print "Game over"
                            if playerLoc == len(listStrings) - 1:
                                playerLoc = playerLoc - 1
                            del listStrings[int(catasBiome)]
                            won = 2
                            print
                            break
                        else:
                            print "A catastrophe has occured in Biome " + str(catasBiome) + "."
                            del listStrings[int(catasBiome)]
                            if catasBiome < playerLoc:
                                playerLoc = playerLoc - 1
                
                #Surprises
                if surprise == "y":
                    biomeLengths = len(listStrings)
                    surpriseChance = surprise_chance(listStrings)
                    if surpriseChance <= biomeLengths:
                        surpriseCount = surpriseCount + 1
                        for i in range(1, (surpriseChance + 1)):
                            surpriseDiamonds = 0
                            dashLocation = listStrings[i].find("-")
                            sword = listStrings[i][dashLocation + 1]
                            enemy = listStrings[i][dashLocation + 3]
                            for c in range(i, (surpriseChance + 1)):
                                dashLocation = listStrings[c].find("-")
                                addDiamonds = listStrings[c][0:dashLocation]
                                surpriseDiamonds = surpriseDiamonds + int(addDiamonds)
                            listStrings[i] = str(surpriseDiamonds) + "-" + str(sword) + "-" + str(enemy)
                        print "A surprise has appeared in Biome " + str(surpriseChance) + "."
                        print
                        
                #increasing Turn # by 1
                turnNum = turnNum + 1
                print

        #End of game results
        print "RESULTS OF THE END OF THE GAME"
        print
        print "The game number " + str(gameNumber) + " just took place."
        if won == 1:
            print "The game ended because the player won."
            win = win + 1
        if won == 2:
            print "The game ended because the player died."
        if won == 3:
            print "The game ended because the game ran out of turns."
        print
        print "The board at end of game contains:"
        biome = create_lists_board(listStrings, int(pythonShineLoc), playerLoc)
        board = show_board(biome)
        print board
        replay = endgame_results(playerName, lifePoints, swordPower, diamondsAmount, playerLoc, won, cataCount, surpriseCount)
        if replay == "y":
            gameNumber = gameNumber + 1
            playerLoc = -1
            pythonShineLoc = 0
            cataCount = 0
            surpriseCount = 0
        print

    #EoG results
    printEndResults = end_results(playerName, gameNumber, win, listStrings)
    
