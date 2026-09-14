#!/usr/bin/env python3
"""
Module: main.py
Description: A simple dice roller that simulates rolling one or more dice.
The user can choose how many dice to roll and see the results with a visual representation.
"""

import random
import sys

def roll_dice(num_dice: int) -> list:
    """
    Rolls a specified number of dice and returns the results.
    
    Args:
        num_dice (int): The number of dice to roll (1-6)
        
    Returns:
        list: A list of random numbers between 1 and 6
    """
    return [random.randint(1, 6) for _ in range(num_dice)]

def display_dice(value: int) -> str:
    """
    Returns a visual representation of a dice face.
    
    Args:
        value (int): The dice value (1-6)
        
    Returns:
        str: A string showing the dice face
    """
    dice_faces = {
        1: "[     ]\n[  ●  ]\n[     ]",
        2: "[●    ]\n[     ]\n[    ●]",
        3: "[●    ]\n[  ●  ]\n[    ●]",
        4: "[●   ●]\n[     ]\n[●   ●]",
        5: "[●   ●]\n[  ●  ]\n[●   ●]",
        6: "[●   ●]\n[●   ●]\n[●   ●]"
    }
    return dice_faces.get(value, "[     ]\n[  ?  ]\n[     ]")

def main():
    """
    Main game loop for the Dice Roller.
    """
    print("=" * 40)
    print("🎲 DICE ROLLER")
    print("=" * 40)
    print("\nRoll 1 to 6 dice at once!")
    print("Type 'quit' to exit.")
    
    while True:
        print("\n" + "-" * 40)
        
        # Get number of dice
        user_input = input("\nHow many dice? (1-6): ").strip().lower()
        
        if user_input == "quit":
            print("\n👋 Thanks for rolling! Goodbye!")
            break
        
        # Validate input
        try:
            num_dice = int(user_input)
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        if num_dice < 1 or num_dice > 6:
            print("❌ Please enter a number between 1 and 6.")
            continue
        
        # Roll the dice
        results = roll_dice(num_dice)
        
        # Display results
        print("\n" + "=" * 40)
        print("🎲 RESULTS")
        print("=" * 40)
        
        # Show each dice face
        for i, value in enumerate(results, 1):
            print(f"\nDice {i}: {value}")
            print(display_dice(value))
        
        # Show total
        total = sum(results)
        print("\n" + "-" * 40)
        print(f"📊 Total: {total}")
        
        # Bonus messages
        if num_dice > 1:
            if len(set(results)) == 1:
                print("🎉 All dice show the same number! Lucky!")
            elif total == num_dice * 6:
                print("🔥 Maximum roll! Incredible!")
            elif total == num_dice:
                print("😅 Minimum roll! Better luck next time!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game cancelled. Thanks for playing!")
        sys.exit()