import random
def main():
    tries = 10
    rand_number = random.randint(1,100)
    past_guesses = set()
    while(tries>0):
        try:
            guess = int(input("enter your guess: "))
            if(guess in past_guesses):
                print("HINT: you already guessed this number")
                continue
            if guess >100 or guess <1:
                print("HINT: please enter a valid number between 1 and 100")
                continue
            
            past_guesses.add(guess)
            if guess>rand_number:
                print("HINT: number is lower than your guess")
            elif guess<rand_number:
                print("HINT: number is higher than your guess")
            else:
                print("""congratulations, you won
guess another number if you have more tries""")
                rand_number = random.randint(1,100)
                past_guesses = set()                
            tries -= 1
            print("you have " + str(tries) + " tries left")

        except ValueError:
            print("please enter a valid number")
            print("you have " + str(tries) + " tries left")
    print("""Do you want to play again?
1. yes
2. no
        """)
    return input()

while(True):
    if main() == "1":
        continue
    else:
        break
    