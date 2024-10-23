# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 

1. Initialization Phase
* Prompt the user to input the total number of sticks on the table (between 10 and 100).
o Error Check: Ensure the input is a valid integer within the range.
o If the input is invalid, the user is prompted again until a valid number is entered.

2. Set Up Players
* There are 3 players:
1. Player 1 (Human)
2. Player 2 (Human)
3. Player 3 (Computer)
* Initialize a loss counter for each player: loss_player1, loss_player2, loss_computer, all set to 0.

3. Main Game Loop
* While loop runs until there is only one stick left (sticks > 1):
1. Player 1's turn:
a. Prompt Player 1 to take 1, 2, or 3 sticks.
b. Error Check: Ensure the input is valid (1-3 and less than or equal total sticks).
c. Subtract the chosen number from the total sticks.
d. Announce the current number of sticks remaining.
2. Player 2's turn:
a. Same as Player 1: prompt for 1, 2, or 3 sticks.
b. Error check and subtract sticks accordingly.
c. Announce the number of remaining sticks.
3. Computer's turn:
a. Randomly generate a number (1-3) for the computer's move.
b. Ensure the generated number does not exceed the remaining sticks.
c. Subtract the computer’s choice from the total and announce the result.
d. Output a message explaining what the computer chose and how many sticks are left.

4. Game End Condition
* If only 1 stick is left:
a. The current player (whoever's turn it is) loses the game.
b. Update the corresponding player's loss count (either Player 1, Player 2, or the computer).
c. Announce the loser of the game.

5. Play Again Loop
* After the game ends, prompt the user if they want to play again.
o If the answer is Yes:
a. Reset the total number of sticks (prompt for a new number between 10 and 100).
b. Continue the game with the same loss counters.
o If the answer is No:
a. Exit the game.
b. Display the total losses for each player, for example:
* "Player 1 has lost X games, Player 2 has lost Y games, Computer has lost Z games."

6. Error Checking
* All user inputs must be validated:
o Number of sticks input at the start (10-100).
o Sticks taken per turn (1, 2, or 3, within the remaining sticks).
o Play again input (Yes or No).
















