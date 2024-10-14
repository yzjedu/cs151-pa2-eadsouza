# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md] (README.md) File carefully

1. Initialization Phase
* Prompt the user to input the total number of sticks on the table (between 10 and 100).
o Error Check: Ensure the input is a valid integer within the range.
o If the input is invalid, prompt the user again until a valid number is entered.
2. Set Up Players
* There are 3 players:
1. Player 1 (Human)
2. Player 2 (Human)
3. Player 3 (Computer)
Initialize a loss counter for each player: loss_player1, loss_player2, loss_computer, all set to 0.
3. Main Game Loop
* While loop runs until there is only one stick left (sticks > 1):
1. Player 1's turn:
- Prompt Player 1 to take 1, 2, or 3 sticks.
- Error Check: Ensure the input is valid (1-3 and <= total sticks).
- Subtract the chosen number from the total sticks.
- Announce the current number of sticks remaining.
2. Player 2's turn:
- Same as Player 1, prompt for 1, 2, or 3 sticks.
- Perform error checking and subtract sticks accordingly.
- Announce the number of remaining sticks.
3. Computer's turn:
- Randomly generate a number (1-3) for the computer's move.
- Ensure the generated number does not exceed the number of remaining sticks.
- Subtract the computer’s choice from the total and announce the result.
- Output a message explaining what the computer chose and how many sticks are left.


4. Game End Condition
* If only 1 stick is left:
- The current player (whoever's turn it is) loses the game.
- Update the corresponding player's loss count (either Player 1, Player 2, or the computer).
- Announce the loser of the game.
5. Play Again Loop
* Prompt the users if they want to play again.
o If the answer is Yes:
* Reset the total number of sticks (prompt for a new number between 10 and 100).
* Continue the game with the same loss counters.
o If the answer is No:
* Exit the game.
* Display the total losses for each player.
6. Error Checking
* All user inputs must be validated:
o Number of sticks input at the start (10-100).
o Sticks taken per turn (1, 2, or 3, within the remaining sticks).
o Play again input (Yes or No).
7. Optional: Smarter Computer Player (Advanced)
* If implementing the smarter computer player:
o Instead of randomly picking 1-3 sticks, the computer will try to leave the human players with a disadvantage.
o The computer could aim to leave a multiple of 4 sticks after its turn, forcing humans to take the last stick.


