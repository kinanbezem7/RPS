

with open("labels.txt", "r") as f:
    huge_list = f.read().split()
    label_key = huge_list[1::2]
    label_value = huge_list[::2]
    label_value = list(map(int, label_value))
    labels = dict(zip(label_key, label_value))
    print(labels)




# Get user input 
print("Show Rock, Paper or Scissors to the camera: ")
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


while True: 

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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
prediction_indx = prediction.argmax()
user_choice = list(labels.keys())[list(labels.values()).index(prediction_indx)]
print(user_choice)




