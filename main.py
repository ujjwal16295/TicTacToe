t=0
num=3
game_is_on="true"
sum=0
game_board=["_","_","_",
           "_","_","_",
           "_","_","_"]

def display_game_board():
  print("\n")
  print(game_board[0] + " | " + game_board[1] + " | " + game_board[2] + "     1 | 2 | 3")
  print("---------")
  print(game_board[3] + " | " + game_board[4] + " | " + game_board[5] + "     4 | 5 | 6")
  print("---------")
  print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "     7 | 8 | 9")
  print("\n")


display_game_board()




def gamecheck():
    global t
    if game_board[0]=="X":
        if game_board[1]=="X":
            if game_board[2]=="X":
                t = 1
                return "false"


    if game_board[3]=="X":
        if game_board[4]=="X":
            if game_board[5]=="X":
                t = 1
                return "false"


    if game_board[6]=="X":
        if game_board[7]=="X":
            if game_board[8]=="X":
                t = 1
                return "false"


    if game_board[0]=="O":
        if game_board[1]=="O":
            if game_board[2]=="O":
                t = 1
                return "false"

    if game_board[3]=="O":
        if game_board[4]=="O":
            if game_board[5]=="O":
                t = 1
                return "false"

    if game_board[6]=="O":
        if game_board[7]=="O":
            if game_board[8]=="O":
                t = 1
                return "false"



    if game_board[0]=="X":
        if game_board[3]=="X":
            if game_board[6]=="X":
                t = 1
                return "false"

    if game_board[1]=="X":
        if game_board[4]=="X":
            if game_board[7]=="X":
                t = 1
                return "false"


    if game_board[2]=="X":
        if game_board[5]=="X":
            if game_board[8]=="X":
                t = 1
                return "false"


    if game_board[0]=="O":
        if game_board[3]=="O":
            if game_board[6]=="O":
                t = 1
                return "false"

    if game_board[1]=="O":
        if game_board[4]=="O":
            if game_board[7]=="O":
                t = 1
                return "false"


    if game_board[2]=="O":
        if game_board[5]=="O":
            if game_board[8]=="O":
                t = 1
                return "false"




    if game_board[0]=="X":
        if game_board[4]=="X":
            if game_board[8]=="X":
                t = 1
                return "false"


    if game_board[2]=="X":
        if game_board[4]=="X":
            if game_board[6]=="X":
                t = 1
                return "false"


    if game_board[0]=="O":
        if game_board[4]=="O":
            if game_board[8]=="O":
                t = 1
                return "false"


    if game_board[2]=="O":
        if game_board[4]=="O":
            if game_board[6]=="O":
                t = 1
                return "false"

    if t==0:
        return "true"










while game_is_on=="true":
    a=gamecheck()
    if a=="false":
        game_is_on="false"
        if num%2==0:
            print("player 1 won")
        else:
            print("player 2 won")
        break
    for i in game_board:
        if i != "_":
            sum=sum+1

    if sum==45:
        print("tie")
        break

    i = int(input("give position"))
    if i > 9 or i<1:
        print("wrong input")
        display_game_board()
    else:
        if num % 2!=0:
            game_board[i-1]="X"
            num=num+1
            display_game_board()
        else:
            game_board[i-1]="O"
            num=num+1
            display_game_board()


