# ============================================================
# TASK 1: Hangman Game
# Intern   : Isra Asif  |  ID: CA/DF1/54477
# Internship: CodeAlpha — Python Programming (May 2026)
# ============================================================

import random

# ---------- 1. Word bank (5 predefined words) ---------------
WORDS = ["python", "hangman", "keyboard", "science", "program"]

# ---------- 2. Hangman ASCII art (0 wrong → 6 wrong) --------
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

MAX_WRONG = 6  # matches len(HANGMAN_STAGES) - 1


# ---------- 3. Helper: display current word state -----------
def display_word(word: str, guessed: set) -> str:
    """Return the word with unguessed letters replaced by '_'."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


# ---------- 4. Helper: display game status ------------------
def show_status(word: str, guessed: set, wrong: int) -> None:
    print(HANGMAN_STAGES[wrong])
    print(f"\n  Word  : {display_word(word, guessed)}")
    print(f"  Wrong guesses ({wrong}/{MAX_WRONG}): {', '.join(sorted(guessed - set(word))) or '—'}")
    print(f"  Used letters : {', '.join(sorted(guessed)) or '—'}\n")


# ---------- 5. Main game loop -------------------------------
def play_hangman() -> None:
    word = random.choice(WORDS)
    guessed: set = set()
    wrong_count = 0

    print("\n" + "=" * 45)
    print("       W E L C O M E   T O   H A N G M A N")
    print("=" * 45)
    print(f"  Guess the {len(word)}-letter word before you run out!")
    print(f"  You have {MAX_WRONG} incorrect guesses allowed.\n")

    while wrong_count < MAX_WRONG:
        show_status(word, guessed, wrong_count)

        # --- Check win condition ---
        if all(letter in guessed for letter in word):
            print(f"  🎉  You won!  The word was: '{word.upper()}'\n")
            return

        # --- Get valid input ---
        guess = input("  Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.\n")
            continue
        if guess in guessed:
            print(f"  ⚠  You already guessed '{guess}'. Try another.\n")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"  ✅  '{guess}' is in the word!\n")
        else:
            wrong_count += 1
            print(f"  ❌  '{guess}' is NOT in the word.\n")

    # --- Out of guesses ---
    show_status(word, guessed, wrong_count)
    print(f"  💀  Game over!  The word was: '{word.upper()}'\n")


# ---------- 6. Play-again loop ------------------------------
def main() -> None:
    while True:
        play_hangman()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()