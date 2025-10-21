import random
import sys
import time

def slow_print(text, delay=0.03):
    # Typewriter effect >:D
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def choose_difficulty():
    # Difficulty selection
    while True:
        slow_print("\n[!] Choose the difficulty level:")
        print("[1] Easy (1–10, 5 lives)")
        print("[2] Medium (1–50, 7 lives)")
        print("[3] Hard (1–100, 10 lives)")
        choice = input(">>> ").strip()

        if choice == '1':
            return 10, 5
        elif choice == '2':
            return 50, 7
        elif choice == '3':
            return 100, 10
        else:
            print("[!] Are you a fucking retard? Pick 1, 2, or 3!")

def get_user_guess(max_num):
    # Anti-Stupidity
    while True:
        try:
            guess = int(input(f"[!] Enter your guess (1–{max_num}): "))
            if 1 <= guess <= max_num:
                return guess
            else:
                print(f"Hey retard, pick only between 1 and {max_num}.")
        except ValueError:
            print("That's not a number, you absolute retarded shit. TRY AGAIN")

def play_game():
    # Magic happens here
    slow_print("\n[!] Welcome to the Number Guessing Game 🎯")
    max_num, lives = choose_difficulty()
    secret = random.randint(1, max_num)
    attempts = 0

    slow_print(f"\n[!] I’m thinking of a number between 1 and {max_num}...")
    slow_print(f"[!] You have {lives} lives. Start guessing.\n")

    while lives > 0:
        guess = get_user_guess(max_num)
        attempts += 1

        if guess == secret:
            slow_print(f"\n🎉 Correct! You guessed it in {attempts} tries!")
            break
        elif guess < secret:
            print("Too LOW, my dude!")
        else:
            print("Too HIGH, lolz!")

        lives -= 1
        print(f"Lives left: {lives}\n")

        if lives == 0:
            slow_print(f"[!] You’re out of lives! The number was {secret}. 💀")
            break

    # Replay option
    again = input("\n[!] Do you want to play again? (y/n): ").lower().strip()
    if again == 'y':
        print("\n[!] Restarting...\n")
        play_game()
    else:
        slow_print("\n[!] Goodbye, retard! Go drink some kvass and rest that brain.\n")
        sys.exit()

# Start the game
if __name__ == "__main__":
    play_game()
