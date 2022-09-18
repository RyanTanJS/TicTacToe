

board=[" "," "," ",
       " "," "," ",
       " "," "," "]
counter=0
def win1():
    global play 
    print("Player 1 is the winner")
    play=False
def draw():
    global play
    print("DRAW")
    play=False
def win2():
    global play
    print("Player 2 is the winner")
    play=False
def rules():
    if board[0]==board[1]==board[2]:
        if board[0]=="X":
            win1()
        if board[0]=="O":
            win2()
    if board[3]==board[4]==board[5]:
        if board[3]=="X":
            win1()
        if board[3]=="O":
            win2()
    if board[6]==board[7]==board[8]:
        if board[6]=="X":
            win1()
        if board[6]=="O":
            win2()
    if board[0]==board[4]==board[8]:
        if board[0]=="X":
            win1()
        if board[0]=="O":
            win2()
    if board[2]==board[4]==board[6]:
        if board[2]=="X":
            win1()
        if board[2]=="O":
            win2()
    if board[0]==board[3]==board[6]:
        if board[0]=="X":
            win1()
        if board[0]=="O":
            win2()
    if board[1]==board[4]==board[7]:
        if board[1]=="X":
            win1()
        if board[1]=="O":
            win2()
    if board[2]==board[5]==board[8]:
        if board[2]=="X":
            win1()
        if board[2]=="O":
            win2()
    if counter==9:
        draw()
def move1():
    global counter
    x=int(input("Which box do you want to move to(1-9):"))
    while board[x-1]!=" ":
        x=int(input("Which box do you want to move to(1-9)"))
    board[x-1]="X"
    counter=counter+1
def move2():
    global counter
    x=int(input("Which box do you want to move to(1-9)"))
    while board[x-1]!=" ":
        x=int(input("Which box do you want to move to(1-9)"))
    board[x-1]="O"
    counter=counter+1
def display_board():
    print("|",board[0],"|",board[1],"|",board[2],"|\n|",
          board[3],"|",board[4],"|",board[5],"|\n|",
          board[6],"|",board[7],"|",board[8],"|\n")     
display_board()
play=True
while play==True:
    move1()
    rules()
    display_board()
    if play==False:
        break
    move2()
    rules()
    display_board()
    if play==False:
        break