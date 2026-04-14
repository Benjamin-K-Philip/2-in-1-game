# 2-in-1-game

## Description
The project is a console-based application designed for entertainment and logic practice. It utilizes a looping menu system that allows the user to play multiple rounds or switch between games without restarting the program. It demonstrates fundamental programming concepts like user input handling, conditional logic, and random number generation.

---

## How the Code Works <br>
The script operates through a centralized while True loop, following these logic steps: <br>

  - **Menu Selection:** The program starts by displaying a menu. It captures the user's choice (1 or 2) using the input() function.

  - **Game Logic Execution:**

    ➤ **Mad Libs Generator:** If choice "1" is picked, the code prompts for a series of strings (verbs, nouns, etc.). It then uses string concatenation to plug those variables into a pre-written story template and prints the result.

    ➤ **Rock Paper Scissors:** If choice "2" is picked, the code enters a secondary while loop. It uses the random.choice() method to let the computer pick from a list (["R", "P", "S"]). It compares the computer's choice against the user's input to determine a winner based on standard game rules.

  - **Scoring & Iteration:** In the Rock Paper Scissors game, a counter i tracks the number of rounds played, and score variables track wins for both the player and the computer.

  - **The Exit Condition:** After the game ends, the program asks the user if they want to continue. If the user enters "n" (or variations like "No"), the break statement is triggered, terminating the main loop and ending the program.

---

## Features <br>
  - **Persistent Gameplay:** The use of while True ensures the user isn't kicked out after just one round.

  - **Dynamic Storytelling:** The Mad Libs generator creates unique (and often nonsensical) stories based entirely on user-provided vocabulary.

  - **Automated Opponent:** The Rock Paper Scissors game features a randomized AI opponent, making the game unpredictable.

  - **Comprehensive Scoreboard:** Tracks wins and losses in real-time during the Rock Paper Scissors sessions and declares an overall winner at the end.

  - **Input Flexibility:** The "continue" prompt accounts for various user inputs (lowercase, uppercase, or full words like "No").

--- 

## Project Structure  <br>
  - **Main Engine:** A while True loop that keeps the program running until the user chooses to quit.

  - **Menu System:** Displays game options and captures the user's choice via input().

  - **Game 1 (Mad Libs):**

➤ Sequential flow that gathers 13 unique inputs.

➤ Combines inputs into a single story string using concatenation.

Game 2 (Rock Paper Scissors):

Setup: Sets up score tracking and imports the random module.

Internal Loop: Runs a user-defined number of rounds.

Logic: Uses if/elif/else to compare moves and update scores.

Results: Compares final scores to declare an overall winner or tie.

Input Validation: An else block to catch invalid menu selections.

Exit Logic: A flexible check for "No" (handling various formats) to break the loop and end the session.
