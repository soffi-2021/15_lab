#   This is a game Rock, Paper, Scissors 

import random     # (module) random

ACTIONS = {0: "Rock", 1: "Paper", 2: "Scissors"} # (constant) ACTIONS: dict[int, str]
VICTORIES = {         # (constant) VICTORIES: dict[str, str]
    "Rock": "Scissors",  # Rock beats scissors
    "Paper": "Rock",  # Paper beats rock
    "Scissors": "Paper",  # Scissors beats paper
}

# Function where user chooses Rock, Paper or Scissors
def get_user_selection(actions):     # (function) def get_user_selection(actions: Any) -> Any
    choices = [f"{actions[action]}[{action}]" for action in actions]    # (variable) choices: list[str]
    choices_str = ", ".join(choices)           # (variable) choices_str: str
    selection = int(input(f"Enter a choice ({choices_str}): "))    # (variable) selection: int
    action = actions[selection]   # (variable) action: Any
    return action             # (variable) action: Any

# Function where computer chooses using a random method 
def get_computer_selection(actions):          # (function) def get_computer_selection(actions: Any) -> Any
    selection = random.randint(0, len(actions) - 1)   # (variable) selection: int
    action = actions[selection]   #  (variable) action: Any
    return action

# Function that determines the winner
def get_determine_winner(victories, user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!"
    elif computer_action in defeats:
        result = f"{user_action} beats {computer_action}! You win!"
    else:
        result = f"{computer_action} beats {user_action}! You lose."
    return result

if __name__ == "__main__":
    while True:
        try:
            user_selection = get_user_selection(ACTIONS)
            print(user_selection)
            computer_selection = get_computer_selection(ACTIONS)
            print(computer_selection)
            determine_winner = get_determine_winner(
                VICTORIES, user_selection, computer_selection
            )
            print(determine_winner)
        except:
            range_str = f"[0, {len(ACTIONS) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
