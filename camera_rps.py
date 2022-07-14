from contextlib import contextmanager
import sys, os
import math
import cv2
from keras.models import load_model
import numpy as np
import time

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout







import random
def get_computer_choice():
    # Pick randomly between Rock, Paper and Scissors
    computer_choice = random.choice(["Rock","Paper","Scissors"])
    return computer_choice

def get_user_choice():
    # Get user input 
    with open("labels.txt", "r") as f:
        huge_list = f.read().split()
        label_key = huge_list[1::2]
        label_value = huge_list[::2]
        label_value = list(map(int, label_value))
        labels = dict(zip(label_key, label_value))


    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    t_end = 0


    print("Show Rock, Paper or Scissors to the camera: ")
    t_start = time.time()
    while t_end-t_start < 5:
    
        with suppress_stdout():

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
        
        prediction_indx = prediction.argmax()
        user_choice = list(labels.keys())[list(labels.values()).index(prediction_indx)]

        print(user_choice)
        t_end = time.time()
        t_countdown = t_end-t_start
        print(math.floor(6-t_countdown))
        cv2.waitKey(1)
            
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return user_choice

def get_winner(choice_dict):
    # Decide who won
    if "Rock" in choice_dict.values() and "Paper" in choice_dict.values():
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Paper")]
    elif "Rock" in choice_dict.values() and "Scissors" in choice_dict.values(): 
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Rock")] 
    elif "Paper" in choice_dict.values() and "Scissors" in choice_dict.values(): 
        winner = list(choice_dict.keys())[list(choice_dict.values()).index("Scissors")]
    elif choice_dict["User"]==choice_dict["Computer"]:
        winner = "Draw!"
    else:
        print("Error no choice detected")
        winner = "Noone!"
        #quit()
    return winner



def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    choice_dict = {"User": user_choice, "Computer": computer_choice}
    winner = get_winner(choice_dict)
    print("The computer chose: ", computer_choice,"\n The user chose: ",user_choice)
    print("\n")
    print("The winner is: ", winner,"!")
    return winner



computer_wins = 0
user_wins = 0

while computer_wins < 3 and user_wins < 3:
    winner = play()
    if winner == "Computer":
        computer_wins += 1
    elif winner == "User":
        user_wins += 1
    else:
        print("null round")

    print("Computer: ", computer_wins, "User: ", user_wins)
    

