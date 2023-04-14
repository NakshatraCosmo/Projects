qs = ["What is your name?", "What is your age?" , 
"What is your height?" , 
"What is your gender?"]
n=0
while True:
    print("Type q to quit")
    a=input(qs[n])
    if a == "q":
        break
    n = (n+1) % 3 #This expression here works a bit different. 1. When n=0 it will give 0 cause (n+1) is less than 3.
#mathematically i know the answer should be different but this is programming think in terms of 0 and 1.
#2. When n=1, n+1=2, it is still less than 3 so we will get 2. 
#3. When n=2, n+1=3, so we finally get 0. and the loop runs again.

# You can change the value of n as you need.