import random 

print("Welcome to this game board")

game_word = ["Love", "ship", "Happy", "Life", "Miracle", "Goal", "Unique", "Style", "Mine", "Real"]

user_wins = 0

while True:
    mach_choice = (random.choice(game_word))
    print("Guess a word from this list:", game_word)

    for _ in range(3):  
       userInp = input("Enter your choice: ")
       if userInp == mach_choice:
           print("You won the match")
           user_wins += 1
           break
 
       else:
           print("Incorrect guess. Try again.")
    print ("Game Over")       
    break