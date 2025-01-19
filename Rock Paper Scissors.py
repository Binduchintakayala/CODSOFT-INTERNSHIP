import random
def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors Game!")
    while True:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        comp_choice = computer_choice()
        print(f"Computer chose: {comp_choice}")
        result = determine_winner(user_choice, comp_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"Your score: {user_score} | Computer score: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Final scores:")
            print(f"Your final score: {user_score} | Computer's final score: {computer_score}")
            break
main()
