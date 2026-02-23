import random

def play_game():
    """Main game logic for two players guessing one secret number."""
    dealer_number = random.randint(0, 10)
    p1_tries = 0
    p2_tries = 0
    game_over = False

    print("--- Welcome to the Dealer Guessing Game ---")
    print("The Dealer has chosen a number between 0 and 10.")

    while not game_over:
        # Player 1's Turn
        p1_guess = int(input("Player 1: "))
        p1_tries += 1
        if p1_guess < dealer_number:
            print("Try a greater number.")
        elif p1_guess > dealer_number:
            print("Try a smaller number.")
        else:
            print(f"That’s right Player 1! Number of tries: {p1_tries}")
            game_over = True
            break # Game ends immediately

        # Player 2's Turn
        p2_guess = int(input("Player 2: "))
        p2_tries += 1
        if p2_guess < dealer_number:
            print("Try a greater number.")
        elif p2_guess > dealer_number:
            print("Try a smaller number.")
        else:
            print(f"That’s right Player 2! Number of tries: {p2_tries}")
            game_over = True

    # Comparison Logic
    print("\n--- Final Results ---")
    if p1_tries < p2_tries:
        print(f"Player 1 wins! (Tries: {p1_tries} vs {p2_tries})")
    elif p2_tries < p1_tries:
        print(f"Player 2 wins! (Tries: {p2_tries} vs {p1_tries})")
    else:
        print(f"It's a tie! Both took {p1_tries} tries.")

if __name__ == "__main__":
    play_game()
