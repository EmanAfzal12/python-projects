import random

def get_level():
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    
    while True:
        choice = input("Enter the level (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def get_range(level):
    if level == 1:
        return 10
    elif level == 2:
        return 50
    elif level == 3:
        return 100

def play_game(level):
    max_number = get_range(level)
    secret_number = random.randint(1, max_number)
    attempts = 0
    max_attempts = 5

    print(f"\nGuess the number between 1 and {max_number}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            return

    print(f"Sorry! You've used all your attempts. The correct number was {secret_number}.")

def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        level = get_level()
        play_game(level)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()


 
