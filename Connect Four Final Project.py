playerOne = input("what do you want to name player one?")
playerTwo = input("what do you want to name player two?") #input for both players names
turnsTaken = 0 #initial set up so that I could distinquish whose turn it was later on
win = False #setting win to false so that the program can start and function with a loop that goes if win is false
starterboard = ["*", "*", "*", "*","*", "*","*", "\n", "*", "*", "*", "*","*", "*","*", "\n", "*", "*", "*", "*","*", "*","*", "\n", "*", "*", "*", "*","*", "*","*", "\n", "*", "*", "*", "*","*", "*","*", "\n", "*", "*", "*", "*","*", "*","*","\n"]# last slash n so program wont quit for bad index value, this is board that will be edited for the cool effect
board = ["•", "•", "•", "•","•", "•","•", "\n", "•", "•", "•", "•","•", "•","•", "\n", "•", "•", "•", "•","•", "•","•", "\n", "•", "•", "•", "•","•", "•","•", "\n", "•", "•", "•", "•","•", "•","•", "\n", "•", "•", "•", "•","•", "•","•","\n"] #board that will be contatnly edited and printed
def turn(column, player): #arguments of column and player
    '''turn(column, player) --> boolean
    given column and player number it 'drops' a checker piece and tells you if you have gotten four in a row, and does a neat animation where you did'''
    
    print ("Column  = ", column+1,"|---| Player  = ", player) #a quick informational text
    if board[40+column] == "•":
        if player == playerOne:
            board[40+column] = "X"
        else: 
            board[40+column] = "O" #xs and os depend on which player the argument is of
    elif board[32+column] == "•":
        if player == playerOne:
            board[32+column] = "X"
        else:
            board[32+column] = "O"
    elif board[24+column] == "•":
        if player == playerOne:
            board[24+column] = "X"
        else:
            board[24+column] = "O"
    elif board[16+column] == "•":
        if player == playerOne:
            board[16+column] = "X"
        else:
            board[16+column] = "O"
    elif board[8+column] == "•":
        if player == playerOne:
            board[8+column] = "X"
        else:
            board[8+column] = "O"
    elif board[column] == "•":
        if player == playerOne:
            board[column] = "X"
        else:
            board[column] = "O"#lines 13 to 41 basically all find where to put the checker by seeing if it has space in one row and if not moving up a row.
    elif "•" not in board:
        print("game over, it is a tie!") #if the board fills up it prints that its a tie
    else:
        print("sorry, that is not in range of the game, you lost a turn") #if there is no where that the checker can be placed in that column it says its not in range and causes the player to lose a turn by moving on to the next person
    print(''.join(board)) #joins the board list to make it look like an actual board with the \n

    for i in range(0, 42, 8): #narrows row
        for j in range(4): #narrows which indexes in that row, this choses which squares can have a horizontal win (going right) leading from it
            if board[i+j] == board[i+j+1] == board[i+j+2] == board[i+j+3] and board[i+j] in "XO": #if the chosen square and three after it are all one of either x or o
                starterboard[i+j] = starterboard[i+j+1] = starterboard[i+j+2] = starterboard[i+j+3] = "-" #if they are it edits a blank list and puts slashes for those four
                print("Congratulations, "+playerOne+" you won on the horizontal!")
                print("".join(starterboard))
                return(True) #joins board and returns true for the function so that win can be set equal to it
    for i in range(0,21,8):
        for j in range(4): #choses all squares that can have a diagonal right win leading from it (all of these use simple math and thinking about what index of the list to use)
            if board[i+j] == board[i+j+9] == board[i+j+18] == board[i+j+27] and board[i+j] in "XO": #if the chosen square and three diagonally to the right are all either x or o (same thing) goes through win protocol
                starterboard[i+j] = starterboard[i+j+9] = starterboard[i+j+18] = starterboard[i+j+27] = "\\"
                print("Congratulations, "+playerOne+" you won on the diagonal!")
                print("".join(starterboard))
                return(True)
    for i in range(3,23,7):
        for j in range(4): #finds all squares that can have a diagonal left win leading from it
            if board[i+j] == board[i+j+7] == board[i+j+14] == board[i+j+21] and board[i+j] in "XO": #if the chosen square and three diagonally to the left are all either x or o (same thing) goes through win protocol
                starterboard[i+j] = starterboard[i+j+7] = starterboard[i+j+14] = starterboard[i+j+21] = "/"
                print("Congratulations, "+playerOne+" you won on the diagonal!")
                print("".join(starterboard))
                return(True)
    for i in range(0,24): #narrows function down to all squares that can lead to vertical win (down)
        if board[i] == board[i+8] == board[i+16] == board[i+24] and board[i] in "XO": #if the chosen square and directly under are all either x or o (same thing) goes through win protocol
            starterboard[i] = starterboard[i+8] = starterboard[i+16] = starterboard[i+24] = "|"
            win = True
            print("Congratulations, "+playerOne+" you won on the verical!")
            print("".join(starterboard))
            return(True)

while not win: #while win is still false
    if turnsTaken%2 == 0: #if it has been an even amount do it for player one
        win = turn(int(input("What column would you like to play to "+ playerOne+", from 1-7? "))-1, playerOne) #call the function using the arguments of the input of which column, and player one. Then, set win equal to the return value so that if it returns true aka a win happens the program will stop
    else: #otherwise (if odd) do it for player two
        win = turn(int(input("What column would you like to play to "+ playerTwo+", from 1-7? "))-1, playerTwo) #call the function using the arguments of the input of which column, and player two. Also sets win equal to the output.
    turnsTaken += 1 #adds one to the total turns taken to distinquish which player to use

