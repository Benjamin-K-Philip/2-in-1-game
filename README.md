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

  - **Automated Opponent:** The Rock Paper Scissors game features a randomized AI opponent(i.e. a user going against the system), making the game unpredictable.

  - **Comprehensive Scoreboard:** Tracks wins and losses in real-time during the Rock Paper Scissors sessions and declares an overall winner at the end.

  - **Input Flexibility:** The "continue" prompt accounts for various user inputs (lowercase, uppercase, or full words like "No").

--- 

## Project Structure  <br>
  - **Initialization & Main Control Loop:** The entire script is wrapped in a while True loop. This acts as the "engine" of the program, ensuring it stays active until the user explicitly chooses to exit.

  - **User Interface (Menu):** At the top of the loop, print statements act as a basic UI, presenting the available games and using an input function to capture the user’s choice.

  - **Mad Libs Generator (Branch 1):** This section is structured as a sequential input-to-output flow. It collects 13 different variables from the user and immediately processes them into a single formatted string.

  - **Rock Paper Scissors Component (Branch 2):**

    ➤ **Setup:** Initializes score counters (user_score, computer_score) and imports the random module.

    ➤ **Game Loop:** A nested while loop runs for a specific number of "chances" defined by the user.

    ➤ **Conditional Logic:** A series of if/elif/else statements compare the user's string input against the computer's random choice.

    ➤ **Final Result Logic:** After the sub-loop finishes, a final comparison determines the overall winner based on the accumulated scores.

  - **Error Handling:** A "catch-all" else statement handles cases where a user might enter a menu choice other than 1 or 2.

  - **Exit Protocol:** The final block of code evaluates a "repeat" input. It uses logical or operators to catch multiple variations of "no" to break the main loop and close the program gracefully.

---

## Output
<img width="1253" height="487" alt="image" src="https://github.com/user-attachments/assets/60069a65-7e71-45ac-8725-653238786224" />
<img width="1244" height="602" alt="image" src="https://github.com/user-attachments/assets/42a1a564-59fc-46e5-bd77-80001bdf6246" />


