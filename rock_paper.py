import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissor): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Draw"
    elif player == "rock":
        if computer == "scissor":
            return "You win!"
        else:
            return "You lose!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif player == "scissor":
        if computer == "paper":
            return "You win!"
        else:
            return "You lose!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)