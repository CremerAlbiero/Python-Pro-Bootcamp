import random

def difficulty():
    while True:
        user_choice = input("Choose 'easy' or 'hard' mode: ").lower()
        if user_choice == 'easy':
            return 10
        elif user_choice == 'hard':
            return 5
        else:
            print("Invalid input. Choose 'easy' or 'hard'.")

def game():
    n_list = list(range(1, 101))  #creates a list between 1-100.
    number = random.choice(n_list) #picks random number from the list
    attempts = difficulty()
    guess = 0

    while True:
        print(f"You have {attempts} attempts left to guess.")
        guess = int(input("Make your guess: "))

        if guess < number:
            print('Too low')
        elif guess > number:
            print('Too high')
        else:
            print(f"You won! The number is {number}")
            break

        attempts -= 1
        if attempts == 0:
            print("Game over. You ran out of attempts.")
            break

def main():
    while True:
        game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()