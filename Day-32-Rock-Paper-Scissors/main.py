#!/usr/bin/env python3
"""
Module: main.py
Description: A simple Rock Paper Scissors game against the computer.
The player chooses rock, paper, or scissors and plays against a random computer choice.
"""

import random
import sys

def get_winner(player: str, computer: str) -> str:
    """
    Determines the winner of a Rock Paper Scissors game.
    
    Args:
        player (str): The player's choice ('rock', 'paper', or 'scissors')
        computer (str): The computer's choice
        
    Returns:
        str: 'player' if player wins, 'computer' if computer wins, 'tie' if tie
    """
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def main():
    """
    Main game loop for Rock Paper Scissors.
    """
    choices = ["rock", "paper", "scissors"]
    score_player = 0
    score_computer = 0
    
    print("=" * 40)
    print("🎮 ROCK PAPER SCISSORS")
    print("=" * 40)
    print("\nRules:")
    print("- Rock crushes Scissors")
    print("- Scissors cuts Paper")
    print("- Paper covers Rock")
    print("\nType 'quit' to exit the game.")
    
    while True:
        print("\n" + "-" * 40)
        print(f"📊 Score: You {score_player} - {score_computer} Computer")
        print("-" * 40)
        
        # Get player's choice
        player_input = input("\nChoose rock, paper, or scissors: ").strip().lower()
        
        # Check if player wants to quit
        if player_input == "quit":
            print("\n👋 Thanks for playing!")
            print(f"Final Score: You {score_player} - {score_computer} Computer")
            break
        
        # Validate input
        if player_input not in choices:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Computer chooses randomly
        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")
        
        # Determine winner
        result = get_winner(player_input, computer_choice)
        
        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "player":
            print("🎉 You win this round!")
            score_player += 1
        else:
            print("😢 Computer wins this round!")
            score_computer += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game cancelled. Thanks for playing!")
        sys.exit()