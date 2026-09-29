import time
def countdown_timer(seconds):
    """Counts down from a specified number of seconds."""
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\rTime Remaining: {timer}", end="")
        time.sleep(1)
        seconds -=1
    print("\n⏰ Time's up!")
if __name__ == "__main__":
    try:
        user_input = int(input("Enter countdown time in seconds: "))
        if user_input > 0:
            countdown_timer(user_input)
        else:
            print("Please enter a positive number of seconds.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
