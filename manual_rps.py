import random
def get_computer_choice():
    # Pick randomly between Rock, Paper and Scissors
    computer_choice = random.choice(["Rock","Paper","Scissors"])
    return computer_choice

def get_user_choice():
    # Get user input 
    user_choice = input("Enter Rock, Paper or Scissors: ")
    print("\n")
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
        quit()
    else:
        print("Error please check letter case and try again")
        quit()
    return winner

def get_winners(choice_dict):
    # Decide who won
    if "Rock" in choice_dict.values() and "Paper" in choice_dict.values():
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Paper")]
    elif "Rock" in choice_dict.values() and "Scissors" in choice_dict.values(): 
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Rock")] 
    elif "Paper" in choice_dict.values() and "Scissors" in choice_dict.values(): 
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Scissors")]
    elif choice_dict["User"]==choice_dict["Computer"]:
        print("Draw!")
        quit()
    else:
        print("Error please check letter case and try again")
        quit()
    return winner




def play():
    computer_choice = "Scissors"   #get_computer_choice()
    user_choice =   "Paper"    # get_user_choice()
    choice_dict = {"User": user_choice, "Computer": computer_choice}
    winner = get_winners(choice_dict)
    print("The computer chose: ", computer_choice,"\n The user chose: ",user_choice)
    print("\n")
    print("The winner is: ", winner,"!")
    return

play()
