from random import randint
o = ["rock", "paper", "scissorss"] #options to pick
user = False 
comp = o[randint(0,2)] #randomizer
user = input("rock, paper, scissorss?") #user input
print(user, "vs", comp) #info for user
if user == comp: #loop
        print('draw')
elif user == "rock":
    if comp == "paper":
        print("paper covers rock, you lost!")
    if comp == "scissors":
        print("rock breaks scissorss, you won!")
elif user == "paper":
    if comp == "rock":
        print("paper covers rock, you won!")
    if comp == "scissorss":
        print("scissors cuts paper, you lost!")
elif user == "scissorss":
    if comp == "rock":
        print("rock breaks scissors, you lost!")
    if comp == "paper":
        print("scissors cuts paper, you won!")
else:
    print("it's not an option!")
