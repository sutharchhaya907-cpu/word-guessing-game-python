# immport random module
import random

#create file
guess_file = "guess.txt"

# create functions
def show_guess_words():
    f = open(guess_file , "r")
    lines = f.readlines()
    for line in reversed(lines) :
       print(line)
    f.close()   

def file_history(Guess):
    f = open(guess_file , "a")
    f.write(f" your guessing word : {Guess}\n")
    f.close()

def clear_history():
    f = open(guess_file , "w")
    f.close()

# welcome massege
print("Welcome in WORD GUESSING GAME ! ")
print("Choose  difficulty according to your level(easy , modrate , hard)")

# take input
level = input("Enter your difficulty level :").lower().strip()

#lists
easy_words = [
     "cat", "dog", "sun", "bat", "pen",
    "cup", "hat", "ball", "book", "tree",
    "fish", "milk", "star", "rain", "car"
]

medium_words = [
     "python", "orange", "garden", "laptop", "school",
    "window", "mobile", "planet", "doctor", "friend",
    "coffee", "music", "travel", "market", "river"
]

hard_words = [
    "algorithm", "developer", "artificial", "university",
    "microscope", "psychology", "astronomy", "blockchain",
    "cybersecurity", "architecture",
    "biotechnology", "cryptography"
]

if level == "easy":
   secret = random.choice(easy_words)
elif level == "modrate":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid level . TRY AGAIN !")
    exit()
   

print("GUESS A SECRET WORD . YOU HAVE ONLY 3 ATTEMPTS TO GAUESS THE SECRET WORD.") 

attempt = 0

while True :
    Guess = input("Enter your guess word here :").lower()
    file_history(Guess)
    attempt += 1
    if Guess == secret :
        print(f"Congratulations ! Your guessing word is perfectly match with our secret word . you complete this in {attempt} attempt.") 
        break
    elif attempt > 2 :
        print("GAME OVER !")
        print("SECRET WORD IS " , secret)
    
        break

    hint = " "

    for i in range(len(secret)) :
        if i < len(Guess) and Guess[i] == secret[i] :
           hint += Guess[i]
        else :
           hint += "_"
    print("Hint = " , hint)  

a = input("Enter command (history , clear) :").lower().strip()

if a == "history" :
    show_guess_words()
else:
    clear_history() 
    print("History cleared !")   
    
# END GAME!    
      










