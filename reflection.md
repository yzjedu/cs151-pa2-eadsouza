# Reflection Document

* Full Name:  Ethan D’Souza
* Student ID: 1735988

 

Objective:
The overall purpose of this PA was to create a three-player Game of Sticks using loops, input validation, decision-making, and basic game logic, while ensuring proper error handling and allowing users to play multiple rounds. The goal was to apply these concepts in Python while practicing programming fundamentals.

Procedure:
The steps followed involved:
1. Initializing the game with input validation to ensure the correct number of sticks (between 10 and 100).
2.  Setting up the players (Player 1, Player 2, and the computer) and keeping track of their losses.
3. Creating a main game loop that alternated between the players and computer, prompting for valid inputs and reducing the number of sticks accordingly.
4. Ensuring the game ends when 1 stick remains, with the losing player being announced.
5. Implementing a play-again loop that resets the game if the user chooses to continue.

Key Concepts Explored:
* Input validation using loops.
* Alternating player turns and tracking game states.
* Basic logic for random decision-making by the computer.

Results:
The results matched what I expected. The game worked as intended, allowing two players and a computer to take turns, while tracking who lost when there was only one stick left. I also tested the game with extreme cases, such as starting with the minimum number of sticks (10) and maximum (100), and the game handled both well.

Challenges Encountered:
I encountered challenges in managing input validation and ensuring that the game loop continued properly without breaking. Error checking for invalid inputs was tricky to get right initially, as I had to ensure all possible incorrect inputs were caught. I also needed to revise my algorithm, in order for my program to actually work.
First 3 Rules of Programming:
1. Identify the problem: I started by understanding the requirements for the Game of Sticks and defining the expected behaviors, including input validation, player turns, and the game’s end condition. 
2. Design: I created an algorithm that outlined the structure of the game, including how players take turns, how to handle invalid inputs, and how to track the game state and losses. 
3. Implement and test: After writing the code, I tested it with various cases, including normal and extreme inputs, to ensure the game worked as expected. I refined the input validation and game loop logic to make sure the game ran smoothly. 
I overcame these challenges by using loops to continuously prompt for valid inputs and testing edge cases, like entering invalid moves or taking too many sticks. I simplified the logic for alternating turns by structuring the game flow clearly, ensuring no unnecessary breaks in the game loop.

Key Takeaways:
* Ensuring input validation is essential for a good user experience and to avoid crashes.
* Implementing a loop to restart the game with new input is a useful structure when creating interactive programs.
* I learned that managing game flow and user interaction in Python requires careful planning, especially when dealing with multiple players.
* I learned how to manage a game with multiple players, handle input errors, and apply looping logic effectively. This lab reinforced the importance of structure and validation in game programming.

What was it like working by yourself:
Working by myself was challenging, as I had to troubleshoot issues without immediate help. However, it pushed me to think critically and test thoroughly. It was a valuable experience for learning problem-solving and independently.

