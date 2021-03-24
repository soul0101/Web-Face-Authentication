import face_recognition
import imutils
import pickle
import time
import cv2
import base64
import io
import numpy as np
from PIL import Image


def face_detect(reference, to_check):

    print(reference, to_check)
    matches = face_recognition.compare_faces(np.array(reference),[np.array(to_check)])    
    # print(np.array(reference))
    # print([np.array(to_check)])
    name = "Unknown"
    if True in matches:
        # print("Match Found")
        return True    
    else:
        return False

def get_FE(base64String):

    buf = io.BytesIO(base64.b64decode(base64String))
    process = face_recognition.load_image_file(buf)
    image_encoding = face_recognition.face_encodings(process)

    # print(np.shape(image_encoding[0]))

    if(len(image_encoding) != 0):
        return(True, image_encoding[0])
    else:
        return (False, 0)

