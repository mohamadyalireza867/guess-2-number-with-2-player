import random

# Dealer generates a random number between 0 and 10
dealer_number = random.randint(0, 10)
tries = 0
player_guess = -1  # Initialize with a number that won't match 0-10

while player_guess != dealer_number:
    # Get input from the player
    player_guess = int(input("Player: "))
    tries += 1  # Increment the number of tries
    
    # Check the guess and provide advice
    if player_guess < dealer_number:
        print("Try a greater number.")
    elif player_guess > dealer_number:
        print("Try a smaller number.")
    else:
        print(f"That’s right! Number of tries: {tries}")
