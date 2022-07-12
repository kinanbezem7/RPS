import random
def get_computer_choice():
    # Pick randomly between Rock, Paper and Scissors
    computer_choice = random.choice(["Rock","Paper","Scissors"])
    return computer_choice

def get_user_choice():
    # Get user input 
    user_choice = input("Enter Rock, Paper or Scissors: ")
    return user_choice

def get_winner(choice_dict):
    # Decide who won
    if "Rock" and "Paper" in choice_dict.values():
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Paper")]
    elif "Rock" and "Scissors" in choice_dict.values(): 
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Rock")]   
    elif "Paper" and "Scissors" in choice_dict.values(): 
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Scissors")]
    elif choice_dict["User"]==choice_dict["Computer"]:
        print("Draw!")
    else:
        print("Error please check letter case and try again")
        quit()
    return winner


computer_choice = get_computer_choice()
user_choice =  get_user_choice()
choice_dict = {"User": user_choice, "Computer": computer_choice}
winner = get_winner(choice_dict)
print("The computer chose: ", computer_choice,"\n The user chose: ",user_choice)
print("The winner is ", winner,"!")
