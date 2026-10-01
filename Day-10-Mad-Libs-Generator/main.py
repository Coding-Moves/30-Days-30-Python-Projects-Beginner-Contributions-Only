def mad_libs():
    print("Welcome to the Mad Libs Word Game!\n")
    print("Please provide the following words:\n")

    adjective1 = input("Enter an adjective (e.g., funny, scary): ").strip()
    noun1 = input("Enter a noun (e.g., dog, laptop): ").strip()
    verb_past = input("Enter a verb in past tense (e.g., jumped, coded): ").strip()
    place = input("Enter a place (e.g., park, office): ").strip()
    adjective2 = input("Enter an adjective: ").strip()

    story = f"""
    ---Here is your Mad Libs Story ---
    Today was a very {adjective1} day.
    I decided to visit the local {place} with my trusty {noun1}.
    Suddenly, everyone around us {verb_past} because it looked so {adjective2}!
    It was a day to remember!
    """
  
    print(story)

if __name__ == "__main__":
    mad_libs()
