# Programmer: Ethan D'Souza
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/23/2024
# Programming Assignment: 02
# Problem Statement: Create a three-player game of the Game of Sticks where players alternate taking 1-3 sticks from a pile, and the player forced to take the last stick loses.
# Purpose: Provide practice with handling user input validation, implementing decision-making, using loops, and fostering creativity in game design.


import random

def get_stick():
    sticks = input("Enter the total number of sticks (between 10 and 100): ")
    while not sticks.isdigit() or int(sticks) < 10 or int(sticks) > 100:
        print("Error: Please enter a valid number between 10 and 100.")
        sticks = input("Enter the total number of sticks (between 10 and 100): ")
    return int(sticks)

def get_move(sticks_left):
    move = input("Enter the number of sticks to take (1, 2, or 3, but no more than " + str(sticks_left) + "): ")
    while not move.isdigit() or int(move) < 1 or int(move) > 3 or int(move) > sticks_left:
        print("Error: You must choose between 1, 2, or 3 sticks, and it cannot be more than the sticks left (" + str(
            sticks_left) + ").")
        move = input("Enter the number of sticks to take (1, 2, or 3, but no more than " + str(sticks_left) + "): ")
    return int(move)

def computer_move(sticks_left):
    return random.randint(1, min(3, sticks_left))

def play_game():
    loss_player1, loss_player2, loss_computer = 0, 0, 0
    play_again = "yes"

    while play_again.lower() == "yes":
        sticks = get_stick()  # Using the renamed function here
        game_over = False

        while not game_over and sticks > 1:
            # Player 1's turn
            print("Player 1's turn. Sticks left: " + str(sticks))
            move = get_move(sticks)  # Using the renamed function here
            sticks -= move
            if sticks == 1:
                print("Player 1 loses!")
                loss_player1 += 1
                game_over = True
                continue

            # Player 2's turn
            print("Player 2's turn. Sticks left: " + str(sticks))
            move = get_move(sticks)  # Using the renamed function here
            sticks -= move
            if sticks == 1:
                print("Player 2 loses!")
                loss_player2 += 1
                game_over = True
                continue

            # Computer's turn
            print("Computer's turn. Sticks left: " + str(sticks))
            move = computer_move(sticks)
            print("Computer takes " + str(move) + " sticks.")
            sticks -= move
            if sticks == 1:
                print("Computer loses!")
                loss_computer += 1
                game_over = True

        # Game ends, ask to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    print("Game over! Here are the total losses:")
    print("Player 1 losses: " + str(loss_player1))
    print("Player 2 losses: " + str(loss_player2))
    print("Computer losses: " + str(loss_computer))

# Start the game
play_game()

