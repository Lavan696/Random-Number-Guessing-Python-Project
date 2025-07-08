🎯 Random Number Guessing Game in Python

This is a fun and interactive number guessing game built using Python. The game randomly selects a number within a user-defined range, and the player has to guess it. After each guess, the game gives hints whether the number is too high or too low until the player guesses it correctly.

🕹️ Features
User inputs a custom range for the game.

Program generates a random number within that range.

Provides feedback after each guess (too high / too low).

Tracks and displays the number of attempts.

Input validation and error handling included.

💡 How It Works
The player enters a starting and ending number to define the guessing range.

The game generates a random number using Python's randrange().

The player starts guessing the number.

After each guess:

If the guess is correct → displays success message and number of attempts.

If the guess is wrong → gives a hint to try higher or lower.

The loop continues until the correct number is guessed.

Handles invalid inputs and improper ranges gracefully.

✅ Example Run

Hello. Welcome to the game of guessing Random number
Enter the range for guessing:(start,end)
Enter start: 10
Enter end: 20
Enter number: 15
Sorry. Your number is too high.
Enter again: 12
Sorry. Your number is too small.
Enter again: 14
Congratulations. You won in attempt 3.
******Thank You******
🧰 Requirements
Python 3.x (no external libraries needed)

🔒 Error Handling
If the end is less than or equal to the start, the game prompts to restart.

If the user enters a non-integer value, it catches ValueError and exits gracefully.

