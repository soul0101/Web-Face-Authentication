import face_recognition
import imutils
import pickle
import time
import cv2
import os
import base64
import io
from PIL import Image
import json
import numpy as np
from django.shortcuts import render, HttpResponse, redirect
# from register.models import SignUp, Face
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from .forms import SignupForm, FaceForm
from register.models import UserProfile

def index(request):
    messages.success(request, 'Please Sign-up')
    return render(request, 'sign_up.html')
    
def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('name')
        # username = request.POST.get('email')
        password1 = request.POST.get('psw')
        password2 = request.POST.get('psw-repeat')

        face_input = request.POST.get('input_face')
        encodings = json.dumps(get_face_encoding_from_base64(face_input))
        
        user = User.objects.create_user(username = username, password = password1)
        user_profile = UserProfile.objects.create(user = user, face_data = encodings)
        # messages.success(request, 'Signup succesful!')
        return redirect("/")
    
    return render(request, 'sign_up.html')


def loginUser(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('psw')

        # print(username, password)
        user = authenticate(username = username, password = password)

        if user is not None:
            # A backend authenticated the credentials
            raw_face = user.user_profile.face_data
            # raw_face = request.user.user_profile.face_data
            raw_face = np.array(json.loads(raw_face))
            # face_detect(raw_face)
            # print(raw_face)
            # login(request, user)
            if(face_detect(raw_face)):
                login(request, user)
                return redirect("welcome")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def welcome(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, 'welcome.html')


def logoutUser(request):
    logout(request)
    return redirect("login")


# Create your views here.

def get_face_encoding_from_base64(base64String):
    
    buf = io.BytesIO(base64.b64decode(base64String))
    process = face_recognition.load_image_file(buf)
    image_encoding = face_recognition.face_encodings(process)

    # print(np.shape(image_encoding[0]))

    return image_encoding[0].tolist()



def face_detect(data):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt2.xml')
    # data = pickle.loads(open("face_enc","rb").read())

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    hieght = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret,frame = cap.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face = faceCascade.detectMultiScale(gray,1.1,5,minSize=(60, 60),flags=cv2.CASCADE_SCALE_IMAGE)
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb)
        names = []

        for encoding in encodings:
            matches = face_recognition.compare_faces([data],encoding)     

            name = "Unknown"
            if True in matches:
                print("Match Found")
                cap.release()
                cv2.destroyAllWindows()
                return True    
        
        # cv2.imshow("live capture",frame)
        
        key=cv2.waitKey(1)

        if(key==ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()




# def sign_up(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         face_form = FaceForm(request.POST)
#         print(face_form)
#         if(form.is_valid() and face_form.is_valid()):
#             # form.save()
#             # messages.success(request, 'Signup succesful!')
#             user = form.save()
#             face = face_form.save(commit=False)
#             face.user = user
#             face.save()
#             return redirect("login")
#         else:
#             for msg in form.error_messages:
#                 print(form.error_messages[msg])

#             return render(request, 'sign_up.html', {'form' : form})
    
#     form = SignupForm()
#     face_form = FaceForm(request.POST)
#     return render(request, 'sign_up.html', {'form' : form, 'face_form' : face_form})