numbers = [36, 48, 50, 68, 34, 78, 45, 90, 21, 32, 67, 73, 74]
while True:
    answer= input("Guess a number or type q to exit:")
    if answer == 'q':
        break
    try:
        answer=int(answer)
    except ValueError:
        print("Type a number or q to exit")
    if answer in numbers:
        print("You guessed right!")
    else:
        print("Sorry you guessed wrong try again.")    


    
