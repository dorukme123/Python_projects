# Rock, Paper, Scissors Game
from random import choice
from time import sleep


choices = ["rock","paper","scissors"];

print("please choose: 1- Rock , 2- Paper , 3- Scissors ");

players_choice = input("Enter Choice:");

def get_comp_choices():
    return choice(choices);

computers_choice = get_comp_choices();
players_final_c = choices[int(players_choice) - 1];

print("Player Choosed: " + players_final_c + " Computer Choosed: " + computers_choice);
sleep(2);

if computers_choice == players_final_c:
    print("its a tie!");
elif computers_choice == "rock" and players_final_c == "scissors" or computers_choice == "paper" and players_final_c == "rock" or computers_choice == "scissors" and players_final_c == "paper":
    print("Computer wins");
elif players_final_c == "rock" and computers_choice == "scissors" or players_final_c == "paper" and computers_choice == "rock" or players_final_c == "scissors" and computers_choice == "paper":
    print("Player wins!");
else:
    print("Error");

#hi