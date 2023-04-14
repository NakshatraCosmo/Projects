def hangman(word):
    wrong=0
    stages=["",
            "____________       ",
            "
    
             ]
    remaining letters=list(word)
    board[""]*len(word)
    win=False
    print("Welcome to Hangman")
    while wrong<len(stages)-1:
    print("\n")
    msg="Guessaletter"
    char=input(msg)
    if char in remaining_letters:
        cind=remaining_letters.index(char)
        board[cind]=char
        remaining letters[cind]='$'
    else:
        wrong+=1
    print(("".join(board)))
    e=wrong+1
    print("\n".join(stages[0:e]))
    if"not in board:
        print("You win!")
        print("".join(board))
        win=True
        break
         