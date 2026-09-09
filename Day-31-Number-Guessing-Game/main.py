#!/usr/bin/env python3
"""
Module: main.py
Description: A number guessing game where the player tries to guess a randomly
generated number between 1 and 100 with difficulty levels.
"""

import random
import sys

def get_difficulty() -> str:
    """
    Asks the user to select a difficulty level.
    
    Returns:
        str: The selected difficulty ('easy', 'medium', or 'hard').
    """
    print("\n" + "=" * 40)
    print("SELECT DIFFICULTY")
    print("=" * 40)
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")
    
    while True:
        choice = input("\nEnter 1, 2, or 3: ").strip()
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

def get_game_settings(difficulty: str) -> tuple:
    """
    Returns the game settings based on difficulty level.
    
    Args:
        difficulty (str): The selected difficulty.
        
    Returns:
        tuple: (max_number, max_attempts)
    """
    if difficulty == "easy":
        return 50, 10
    elif difficulty == "medium":
        return 100, 7
    else:  # hard
        return 200, 5

def play_game() -> None:
    """
    Main game loop. Handles guessing logic and user feedback.
    """
    print("=" * 40)
    print("🎯 NUMBER GUESSING GAME")
    print("=" * 40)
    print("\nI'm thinking of a number...")
    print("Try to guess it!")

    # Get difficulty and settings
    difficulty = get_difficulty()
    max_number, max_attempts = get_game_settings(difficulty)
    
    # Generate the secret number
    secret_number = random.randint(1, max_number)
    attempts = 0
    guessed = False

    print(f"\n🔢 I'm thinking of a number between 1 and {max_number}.")
    print(f"💡 You have {max_attempts} attempts.")

    # Main game loop
    while attempts < max_attempts and not guessed:
        try:
            # Get user's guess
            guess_input = input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: ")
            guess = int(guess_input)
            attempts += 1

            # Check the guess
            if guess < 1 or guess > max_number:
                print(f"⚠️ Please enter a number between 1 and {max_number}.")
                continue

            if guess < secret_number:
                print("📈 Too low! Try a higher number.")
            elif guess > secret_number:
                print("📉 Too high! Try a lower number.")
            else:
                guessed = True
                print("\n" + "=" * 40)
                print("🎉 CONGRATULATIONS! YOU WON! 🎉")
                print("=" * 40)
                print(f"✅ You guessed the number in {attempts} attempts!")
                
                # Bonus: Give a rating based on performance
                if attempts == 1:
                    print("🌟 Perfect score! You're a mind reader!")
                elif attempts <= 3:
                    print("👏 Amazing! You're very lucky!")
                elif attempts <= max_attempts - 2:
                    print("👍 Good job! You got it!")
                else:
                    print("😅 Close one! You barely made it!")

        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n👋 Game cancelled. Thanks for playing!")
            sys.exit()

    # If the player didn't guess correctly
    if not guessed:
        print("\n" + "=" * 40)
        print("😢 GAME OVER")
        print("=" * 40)
        print(f"💡 The number was: {secret_number}")
        print(f"📊 You used all {max_attempts} attempts.")
        print("\nBetter luck next time! 🍀")

def main() -> None:
    """
    Main function to run the game with replay option.
    """
    while True:
        play_game()
        
        # Ask to play again
        print("\n" + "-" * 40)
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\n👋 Thanks for playing! Goodbye!")
            break
        print("\n" + "🔄 Starting new game..." + "\n")

if __name__ == "__main__":
    main()