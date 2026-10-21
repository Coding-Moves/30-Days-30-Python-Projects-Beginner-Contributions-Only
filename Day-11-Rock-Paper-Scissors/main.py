import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    print("🎮 Welcome to Rock, Paper, Scissors!\n")

    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").strip().lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        return

    if user_choice not in choices:
        print("❌ Invalid input! Please enter rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

if __name__ == "__main__":
    play_game()
  
