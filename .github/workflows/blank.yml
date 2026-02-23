import random

# Dealer generates ONE random number for the whole game
dealer_number = random.randint(0, 10)

player1_tries = 0
player2_tries = 0
found = False

print("Dealer has chosen a number between 0 and 10!")

while not found:
    # Player 1's Turn
    p1_guess = int(input("Player 1: "))
    player1_tries += 1
    if p1_guess < dealer_number:
        print("Try a greater number.")
    elif p1_guess > dealer_number:
        print("Try a smaller number.")
    else:
        print(f"That’s right Player 1! Number of tries: {player1_tries}")
        found = True
        break # Exit the loop immediately
        
    # Player 2's Turn
    p2_guess = int(input("Player 2: "))
    player2_tries += 1
    if p2_guess < dealer_number:
        print("Try a greater number.")
    elif p2_guess > dealer_number:
        print("Try a smaller number.")
    else:
        print(f"That’s right Player 2! Number of tries: {player2_tries}")
        found = True
        break # Exit the loop immediately

# Determine the winner based on total tries
print("\n--- FINAL RESULT ---")
if player1_tries < player2_tries:
    print("Player 1 wins! (Fewer tries)")
elif player2_tries < player1_tries:
    print("Player 2 wins! (Fewer tries)")
else:
    # This happens if Player 2 guesses it on the same round number as Player 1 
    # OR if Player 1 gets it on the first try before Player 2 even goes.
    print("It's a tie or the first player found it immediately!")
