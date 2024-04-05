def playerWon(board):
    
    spaceOccupied = 0

    # Player 0
    # Diagonal Check
    if (board[2][0] == '0' and board[1][1] == '0' and board[0][2] == '0'):
        print('diagonal')
        return '0'
    # Reverse Diagonal Check
    if (board[2][2] == '0' and board[1][1] == '0' and board[0][0] == '0'):
       # print('reverse diagonal')
        return '0'

    #Player *
    # Diagonal Check
    if (board[2][0] == '*' and board[1][1] == '*' and board[0][2] == '*'):
       # print('diagonal')
        return '*'
    # Reverse Diagonal Check
    if (board[2][2] == '*' and board[1][1] == '*' and board[0][0] == '*'):
       # print('reverse diagonal')
        return '*'


    for i in range(0, 3):
        # Player '0'
        # Horizontal Check
        if (board[i][0] == '0' and board[i][1] == '0' and board[i][2] == '0'):
           # print('horizontal')
            return '0'
        # Vertical Check
        if (board[0][i] == '0' and board[1][i] == '0' and board[2][i] == '0'):
           # print('vertical')
            return '0'


        # Player '*'
        # Horizontal Check
        if (board[i][0] == '*' and board[i][1] == '*' and board[i][2] == '*'):
           # print("horizontal")        
            return '*'
        # Vertical Check
        if (board[0][i] == '*' and board[1][i] == '*' and board[2][i] == '*'):
           # print("vertical")
            return '*'
        
        for j in range(0,3):
            if (board[i][j] != ''):
                spaceOccupied += 1
    

    if (spaceOccupied == 9):
        return 'OutOfSpace'

    
    return ''


players = {
    'player1': '0',
    'player1Scores': 0,

    'player2': '*',
    'player2Scores': 0
}
currentPlayer = players['player1']
running = True
spaceOccupied = 0

board = [
    # 0   1   2
    ['', '', ''], # 0
    ['', '', ''], # 1
    ['', '', '']  # 2
]

while running:
    print ("    0   1   2")
    for i in range(0, 3):
        print(i, end=' ')
        print(board[i])
    
    if (currentPlayer == players['player1']):
        currentPlayer = players['player2']
    else:
        currentPlayer = players['player1']


    while True:
        coordinate = str(input(f"Current player[{currentPlayer}]: ")).split(',')

        try:
            if (board[int(coordinate[0])][int(coordinate[1])] == ''):
                board[int(coordinate[0])][int(coordinate[1])] = currentPlayer
                break
            else:
                print("Invalid Input")
        except:
            print("Out of bound")


    result = playerWon(board)
    # print(result)
    if (result != ''):
        for i in range(0, 3):
            print(board[i])

        if (result == players['player1']):
            players['player1Scores'] = players['player1Scores'] + 5
            print("Player 1 (0) won")
            print(players['player1Scores'])
        else:
            players['player2Scores'] = players['player2Scores'] + 5
            print("Player 2 (*) won")
            print(players['player2Scores'])

        playMore = input("Would you like to continue? (Yes, No): ")
        if (playMore.lower() == 'no' or playMore.lower() == 'n'):
            print(f"Player 1 scores {players['player1Scores']}")
            print(f"Player 2 scores {players['player2Scores']}")

            if (players['player1Scores'] > players['player2Scores']):
                print("Player 1 won")
            else:
                print("Player 2 won")

            running = False

        board = [['', '', ''],['', '', ''], ['', '', '']]
        
    elif (result == "OutOfSpace"):
        playMore = input("Would you like to continue? (Yes, No): ")
        if (playMore.lower() == 'no' or playMore.lower() == 'n'):
            print(f"Player 1 scores {players['player1Scores']}")
            print(f"Player 2 scores {players['player2Scores']}")

            if (players['player1Scores'] > players['player2Scores']):
                print("Player 1 won")
            else:
                print("Player 2 won")

            running = False
    
    