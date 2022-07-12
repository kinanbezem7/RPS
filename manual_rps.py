import random
def get_computer_choice():
    # Pick randomly between Rock, Paper and Scissors
    computer_choice = random.choice(["Rock","Paper","Scissors"])
    return computer_choice

def get_user_choice():
    # Get user input 
    user_choice = input("Enter Rock, Paper or Scissors: ")
    return user_choice




computer_choice = get_computer_choice()
user_choice =  get_user_choice()

print(computer_choice,user_choice)