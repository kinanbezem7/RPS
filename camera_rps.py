import random
def get_computer_choice():
    # Pick randomly between Rock, Paper and Scissors
    computer_choice = random.choice(["Rock","Paper","Scissors"])
    return computer_choice

def get_user_choice():
    # Get user input 
    print("Show Rock, Paper or Scissors to the camera: ")
    import cv2
    from keras.models import load_model
    import numpy as np
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
 


    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)


            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    user_choice = max(prediction)
    print(user_choice)
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
        print("Draw!")
        quit()
    else:
        print("Error please check letter case and try again")
        quit()
    return winner



def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    choice_dict = {"User": user_choice, "Computer": computer_choice}
    winner = get_winner(choice_dict)
    print("The computer chose: ", computer_choice,"\n The user chose: ",user_choice)
    print("\n")
    print("The winner is: ", winner,"!")
    return




play()