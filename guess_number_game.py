
import random 

def guess_number_game():
    
    number_to_guess = random.randint(1,25)
    attempts = 0
    
    print ("Welcome to the 'Guess Random Number Game' ")
    print ("I am thinking of a number between 1 to 25")
    
    while True:
        try:
        
            guess = int(input("Enter a number your guess: "))
        
            attempts += 1
        
            if guess < number_to_guess:
                print("Your guessed number is lower than system guessed number")
        
            elif guess > number_to_guess:
                print("Your guessed number higher than system guessed number")
            
            else: 
                print(f"Congratulations! Your guessed number is {number_to_guess} in {attempts} attempts.")
                break 
        
        except ValueError:
            print("Please enter A valid number")
            
guess_number_game()
